import random
import datetime

# 0～1億のランダムな整数要素を持つ100万個のリストを内包表記で作成
a = [random.randint(0, 100000000) for _ in range(1000000)]

# 0～1億のランダムな整数要素を持つ100個のリストの要素
checked_list = [random.randint(0, 100000000) for _ in range(100)]

# リストでのチェックの開始時間
start_time = datetime.datetime.now()

# リストの中に要素が存在するかチェック
for temp in checked_list:
    if temp in a:
        # 必要に応じて出力可能
        # print(f'temp:{temp} in a')
        pass

# リストでのチェックにかかった時間を表示
print("List check time:", datetime.datetime.now() - start_time)

# 100万個のリストをセットに変換
a_set = set(a)

# セットでのチェックの開始時間
start_time_set = datetime.datetime.now()

# セットの中に要素が存在するかチェック
for temp in checked_list:
    if temp in a_set:
        # 必要に応じて出力可能
        # print(f'temp:{temp} in a_set')
        pass

# セットでのチェックにかかった時間を表示
print("Set check time:", datetime.datetime.now() - start_time_set)
