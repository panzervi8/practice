'''
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续摇骰子，直到分出胜负。
'''

from random import randint

times = 0
money = 1000
point = 0
goon = 'y'

while True:
    print("你的资金为：%d"%money)
    debt = int(input("请下注："))
    if 0 < debt < money:
        break
    else :
        print("下注额有误。请重新下注。\n")

while goon == 'y' or goon == 'Y':
    times += 1
    point = randint(1, 6) + randint(1, 6)
    print("本局为第%d局。摇出的点数为%d"%(times, point))
    if times ==1:
        if point == 7 or point == 11:
            money += debt
            print("你在第一局赢了。你现在有资金%d元"%money)
            break
        elif point == 2 or point == 3 or point == 12:
            money -= debt
            print("你在第一局输了。你现在剩下%d元。"%money)
            break
        else :
            your_point = point
            continue

    if point == 7:
        money -= debt
        print("你在第%d局输了。你现在还剩下%d元。"%(times, money))
        break
    elif point == your_point:
        money += debt
        print("你在第%d局赢了。你现在拥有资金%d元。"%(times, money))
        break
    goon = input("继续请输入y或Y。否则输入任意字母。不继续将输掉本局。")
    if goon != 'y' and goon != 'Y':
        money -= debt
        print("你在第%d局输了。你现在还剩下%d元。"%(times, money))
        break