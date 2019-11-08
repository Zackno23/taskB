str = input("データを入力してください")
data_list = str.split()
data_list = [int(i) for i in data_list]


def total(data_list):
    total = 0
    for i in data_list:
        total += i
    return total


def max(data_list):
    max = 0
    for i in data_list:
        if i >= data_list[0]:
            max = i
    return max


def min(data_list):
    min = 0
    for i in data_list:
        if i <= data_list[0]:
            min = i
    return min


def ave(data_list):
    return int(total(data_list) / len(data_list))


print(f"合計値：{total(data_list)}\n最大値：{max(data_list)}\n最小値：{min(data_list)}\n平均値：{ave(data_list)}")
