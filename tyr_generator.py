def try_generator():
    for data in (1, 2, 3, 4, 5):
        yield data


def main():
    for data in try_generator():
        print(data)
        if data > 2:
            break


if __name__ == "__main__":
    main()


# try_generator関数のジェネレータ式を使用した実装
def try_generator():
    # ジェネレータ式で 1 から 5 の値を生成
    return (data for data in (1, 2, 3, 4, 5))


# main関数
def main():
    # ジェネレータ式を直接 for ループに渡す
    for data in try_generator():
        print(data)
        if data > 2:
            break


# main関数を実行
if __name__ == "__main__":
    main()
