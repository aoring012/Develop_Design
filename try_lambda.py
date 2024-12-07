# 関数 execute_param_fn を定義
def execute_param_fn(args, hosei, fn):
    # 引数argsの最大または最小値と補正値hoseiを使用して処理を行い、結果を返却
    return fn(max(args), hosei)


# 例としてラムダ関数を2つ定義
lambda1 = lambda a, b: a + b  # 最大値に補正値を加える
lambda2 = lambda a, b: a - b  # 最小値から補正値を引く

# それぞれを execute_param_fn に渡して実行
result1 = execute_param_fn([1, 2, 3], 4, lambda1)
result2 = execute_param_fn([1, 2, 3], 4, lambda2)

# 結果を表示
print("結果1:", result1)  # 7が返却される
print("結果2:", result2)  # -3が返却される
