from enum import Enum


# 列挙型 Shingou を定義
class Shingou(Enum):
    RED = 1  # 赤
    BLUE = 2  # 青
    YELLOW = 3  # 黄色


# 関数 act_shingou の定義
def act_shingou(color: int) -> Shingou:
    try:
        # color に対応する列挙型を取得
        shingou = Shingou(color)

        # color に対応する処理を実行
        if shingou == Shingou.RED:
            print("とまれ")
        elif shingou == Shingou.BLUE:
            print("すすめ")
        elif shingou == Shingou.YELLOW:
            print("ちゅうい")

        return shingou
    except ValueError:
        # 無効な color が渡された場合、例外を発生させる
        raise ValueError("信号機の色に対応していません")
