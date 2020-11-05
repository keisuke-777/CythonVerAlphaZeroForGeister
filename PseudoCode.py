# 疑似コード

# パターンリスト
EnPatternList = []
MyPatternList = []

# パターン格納
EnPattern = int[70]
MyPattern = int[70]

gamma = 0.9


def fight():

    # 相手の行動を受け取る(相手の行動は自分の駒配置をある程度予測するはず)

    # 相手の盤面を推定する
    suiteiValue = banmenSuitei()

    # 一番価値の高い行動を選択

    pass


# 相手の盤面を推定する(引数：盤面+行動、ニューラルネット、過去の盤面推定値)
def banmenSuitei():
    for EnPatternList in e:
        EnNuraruValue = 0
        for MyPatternList in m:
            # ニューラルネットを使って価値を算出
            EnNuraruValue += nuraruValue
            # ここ全部足すのではなく、相手の読みも想定して重みづけする？？
            # (ここの処理で相手の行動から、相手の信じるこっちの盤面もおんなじ流れで足しとく？？)
            MyPattern[i] += MyPattern[i] * gamma + nuraruValue
        # 相手の盤面推定値を更新
        EnPattern[i] += EnPattern[i] * gamma + EnNuraruValue

    pass
    return null


# 実際に敵駒を食ってみて、ありえなかった駒配置を削除


# 盤面推定値を使って行動決定
def KoudouKettei():
    EnPattern  # 70の値
    RealMyPattern  # 1通り
    moveMargeList
    for EnPattern in i:
        # ニューラルネットを使って価値を算出
        moveValueList = nuraruValue(EnPattern[i], RealMyPattern)
        # 書き方間違ってそうだけど、合併(全要素を足し合わせる)
        moveMargeList += moveValueList

    pass


# ニューラルネットで価値のリストを返す
def nuraruValue():
    pass


# 動作確認
if __name__ == "__main__":
    fight()
