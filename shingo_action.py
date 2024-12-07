import sys
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


# コマンドライン引数を取得し、処理を行う
if __name__ == "__main__":
    try:
        # コマンドライン引数から色を取得（第1引数が色の値）
        color_value = int(sys.argv[1])

        # act_shingou を呼び出し
        act_shingou(color_value)

    except IndexError:
        print(
            "引数が不足しています。コマンドライン引数で信号機の色の値を指定してください。"
        )
    except ValueError as e:
        print(e)
