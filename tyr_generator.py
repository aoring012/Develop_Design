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
