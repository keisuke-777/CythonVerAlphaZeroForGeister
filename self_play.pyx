from joblib import Parallel, delayed
from time import time

# パッケージのインポート
from game import State
from pv_mcts import pv_mcts_scores
from dual_network import DN_OUTPUT_SIZE
from datetime import datetime
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from pathlib import Path
import numpy as np
import pickle
import os

# パラメータの準備
SP_GAME_COUNT = 500  # セルフプレイを行うゲーム数（本家は25000）
SP_TEMPERATURE = 1.0  # ボルツマン分布の温度パラメータ

# ガイスター特有の要素
# PLACEMENT_PIECE_NUM = 9800  # 配置の数(8C4*8C4)*2(先手と後手)

# 先手プレイヤーの価値
def first_player_value(ended_state):
    # 1:先手勝利, -1:先手敗北, 0:引き分け
    if ended_state.is_lose():
        return -1 if ended_state.is_first_player() else 1
    return 0


# 学習データの保存
def write_data(history):
    now = datetime.now()
    os.makedirs("./data/", exist_ok=True)  # フォルダがない時は生成
    path = "./data/{:04}{:02}{:02}{:02}{:02}{:02}.history".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )
    with open(path, mode="wb") as f:
        pickle.dump(history, f)


# 1ゲームの実行
def play(model):
    # 学習データ
    history = []

    # 状態の生成
    state = State()

    while True:
        # ゲーム終了時
        if state.is_done():
            break

        # 合法手の確率分布の取得
        scores = pv_mcts_scores(model, state, SP_TEMPERATURE)

        # 学習データに状態と方策を追加
        policies = [0] * DN_OUTPUT_SIZE
        for action, policy in zip(state.legal_actions(), scores):
            policies[action] = policy
        history.append([state.pieces_array(), policies, None])

        # 行動の取得
        action = np.random.choice(state.legal_actions(), p=scores)

        # 次の状態の取得
        state = state.next(action)

    # 学習データに価値を追加
    value = first_player_value(state)
    for i in range(len(history)):
        history[i][2] = value
        value = -value
    return history


# マルチプロセスでplayを実行
def multi_play(process_id):
    # ベストプレイヤーモデルの読み込み
    # 並列jobの引数にはpickle化できる奴しか渡せないので内側でloadする
    # (modelをpickle化する方法はわからなかったので保留)
    model = load_model("./model/best.h5")

    history = []

    # 1ゲームの実行
    h = play(model)
    history.extend(h)

    # 出力
    print("\rSelfPlay {}/{}".format(process_id + 1, SP_GAME_COUNT))

    # モデルの破棄
    K.clear_session()
    del model

    return history


# セルフプレイ
def self_play():
    # n_jobsで使用コア数を指定(-1で勝手に最大値をとる)
    all_history = Parallel(n_jobs=-1)(
        [delayed(multi_play)(i) for i in range(SP_GAME_COUNT)]
    )

    # 返り値の結合
    history = []
    for his in all_history:
        history.extend(his)

    # 学習データの保存
    write_data(history)


# 動作確認
if __name__ == "__main__":
    self_play()
