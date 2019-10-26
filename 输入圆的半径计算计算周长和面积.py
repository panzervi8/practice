"""
输入半径计算圆的周长和面积
"""
import math
r = float(input("输入圆的半径："))

l = 2 * math.pi * r
S = math.pi * r * r

print("圆的半径为%.1f, 周长为%.1f，面积为%.1f"%(r, l , S))