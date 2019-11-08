gyo = int(input("行数を入力してください"))
retsu = int(input("列数を指定してください"))




for a in range (1,gyo + 1):
    [print(f"{a * b} ", end="") for b in range(1,retsu + 1)]
    print("\n")
