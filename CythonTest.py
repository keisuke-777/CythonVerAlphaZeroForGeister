# cythonの速度を確認(だいぶ雑)

import game
import time
import py_game as pygame
import cProfile


def PythonTime():
    # Python
    state = pygame.State()
    start = time.time()
    for _ in range(10):
        while True:
            # ゲーム終了時
            if state.is_done():
                print(state.depth)
                break
            # 次の状態の取得
            # state = state.next(random_action(state))
            state = state.next(pygame.mcts_action(state))

    # 時間計測
    elapsed_time = time.time() - start
    print("Python:elapsed_time:{0}".format(elapsed_time) + "[sec]")


def CythonTime():
    # Cython
    state = game.State()
    start = time.time()
    for _ in range(10):
        while True:
            if state.is_done():
                print(state.depth)
                break
            state = state.next(game.mcts_action(state))
    elapsed_time = time.time() - start
    print("Cython:elapsed_time:{0}".format(elapsed_time) + "[sec]")


if __name__ == "__main__":
    # cProfile.run("PythonTime()")
    # cProfile.run("self_play()")
    CythonTime()
    # PythonTime()

