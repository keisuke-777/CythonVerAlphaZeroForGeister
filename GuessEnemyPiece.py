# 相手の駒配置を予測
# これは不完全情報ゲームにおいて動作するようにする
# 正体が不明な相手の駒をとりあえず-1としておく

# board→14R24R34R44R15B25B35B45B41u31u21u11u40u30u20u10u
# move

import numpy as np
from game import State
from pv_mcts import predict

# おそらく不完全情報ガイスター(のstateのみ？)を定義してそれを更新して管理した方がよさげ
# 不完全情報ガイスターの盤面情報
class II_State:
    # 初期化
    def __init__(self, all_piece=None):

        #
        # 全ての駒(hgfedcbaABCDEFGHの順になっている)

        if all_piece == None:
            # numpyは基本的に型指定しない方が早い(指定すると多分裏で余計な処理をする)
            self.all_piece = np.zeros(16)
            # 初期配置を代入
            self.all_piece[0] = 1
            self.all_piece[1] = 2
            self.all_piece[2] = 3
            self.all_piece[3] = 4
            self.all_piece[4] = 7
            self.all_piece[5] = 8
            self.all_piece[6] = 9
            self.all_piece[7] = 10
            self.all_piece[8] = 25
            self.all_piece[9] = 26
            self.all_piece[10] = 27
            self.all_piece[11] = 28
            self.all_piece[12] = 31
            self.all_piece[13] = 32
            self.all_piece[14] = 33
            self.all_piece[15] = 34

        else:
            self.all_piece = all_piece

    #   ボードの初期配置はこんな感じ(小文字が敵の駒で大文字が自分の駒)
    #     0 1 2 3 4 5
    #   0   h g f e
    #   1   d c b a
    #   2
    #   3
    #   4   A B C D
    #   5   E F G H


# プロトコルから相手の行動は送られず、更新されたボードが送られてくるそうなので、行動した駒の座標を求める(これ駒が食われた時検知不可能)
def coordinate_checker(before_board, now_board):
    for i in range(len(before_board)):
        if before_board[i] != now_board[i]:
            break
    # iではなく(i//3)*3とすることで、座標と駒色(例:14R)の先頭インデックスが取れる(これしないと2文字目からとってくる恐れがある)
    beginningOfTheChanged = (i // 3) * 3

    # 列番号+行番号*6でgame.pyで使ってる表現に直せる
    before_coordinate = (
        int(before_board[beginningOfTheChanged])
        + int(before_board[beginningOfTheChanged + 1]) * 6
    )
    now_coordinate = (
        int(now_board[beginningOfTheChanged])
        + int(now_board[beginningOfTheChanged + 1]) * 6
    )

    # 行動前と行動後の座標を返す
    return before_coordinate, now_coordinate


# 移動前と移動後の座標から行動を算出(エラー未修正)
def find_move_number_from_coordinate(before_coordinate, now_coordinate):
    difference = now_coordinate - before_coordinate
    if difference == 6:  # 下
        return State.position_to_action(self, before_coordinate, 0)
    elif difference == -1:  # 左
        return State.position_to_action(self, before_coordinate, 1)
    elif difference == 6:  # 上
        return State.position_to_action(self, before_coordinate, 2)
    elif difference == -1:  # 右
        return State.position_to_action(self, before_coordinate, 3)
    else:
        print("ERROR:find_move_number_from_coordinate(illegal move)")
        return -1


# 行動を相手視点に変更
def swap_viewpoints():
    pass


# 相手の行動を受けて、ガイスターの盤面を更新
def update_II_state(ii_state, before_coordinate, now_coordinate):
    # 行動前の座標を行動後の座標に変更する
    ii_state.all_piece[
        np.where(ii_state.all_piece == before_coordinate)[0][0]
    ] = now_coordinate


# 自分の行動を決定し、ガイスターの盤面を更新&TCPで送信
def action_decision():
    pass


# predictここで定義し直した方が良さそう(わざわざ完全情報のstateに直すのは時間がかかる)
def II_predict():
    pass


def predict_all():
    pass


# 行動価値を算出
# ニューラルネットからデータとってくる
def get_policie_and_value_from_NN(II_state):
    # 不完全情報の盤面を完全情報に変換

    # ニューラルネットワークの推論で方策と価値を取得
    policies, value = predict(model, self.state)
    print(policies)
    print(value)


# 動作確認
if __name__ == "__main__":
    # GetDataFromNN()
    print(coordinate_checker("14R24R55R78B", "14R24R42R78B"))
    # coordinate_checker("14R24R55R78B", "14R24R52R78B")
    a = coordinate_checker("14R24R55R78B", "14R24R56R78B")
    # print(find_move_number_from_coordinate(a[0], a[1]))

    ii_state = II_State()
    print(ii_state.all_piece)
    print(ii_state.all_piece[4])
    print(np.where(ii_state.all_piece == 27)[0][0])
