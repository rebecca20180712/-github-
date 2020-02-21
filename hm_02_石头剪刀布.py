import random

player = int(input("请出拳 石头【1】剪刀【2】布【3】："))
computer = random.randint(1, 3)
print("您出的是%d,电脑出的是%d" % (player, computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("恭喜你赢了，电脑弱爆了！")
elif player == computer:
    print("平局哦！")
else:
    print("不服再来一局哦！")

# print("hello python " *5)
