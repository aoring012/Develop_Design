def test_closure(check_value):
    data = []

    def add_data(checked_value):
        if checked_value >= check_value:
            data.append(checked_value)

    def get_data():
        return data

    return add_data, get_data


if __name__ == "__main__":
    add_data, get_data = test_closure(3)

    add_data(2)
    add_data(3)

    data = get_data()
    print(data)
