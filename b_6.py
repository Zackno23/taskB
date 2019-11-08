import random

n = int(input("サイコロの面の数は？"))
m = int(input("何回振りますか？"))

print([random.randint(1,n) for i in range(m)])