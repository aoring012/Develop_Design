import sys
from enum import Enum


# Enumで信号機の色を定義
class Signal(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3


# ジェネレータを使って、信号機の色を生成
def signal_generator():
    for signal in Signal:
        yield signal


# ラムダ式で信号の色に応じたアクションを決定
signal_action = lambda signal: {
    Signal.RED: "Stop",
    Signal.GREEN: "Go",
    Signal.YELLOW: "Caution",
}.get(signal, "Unknown")


def main():
    # コマンドライン引数で指定された色を処理
    if len(sys.argv) != 2:
        print("Usage: python exercise.py <color>")
        sys.exit(1)

    try:
        # コマンドライン引数の色を取得
        color = int(sys.argv[1])

        # 指定された色が信号機に対応しているか確認
        signal = Signal(color)
        print(f"The action for {signal.name} is: {signal_action(signal)}")

        # ジェネレータを使って全ての信号機の色を出力
        print("\nAll signal actions:")
        for signal in signal_generator():
            print(f"{signal.name}: {signal_action(signal)}")

    except ValueError:
        print(
            "Invalid signal color. Please use 1 for RED, 2 for GREEN, or 3 for YELLOW."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
