"""
英制单位英寸和公制单位厘米互换
1英才 = 2.54 厘米
"""

value = float(input("请输入数值："))
unit = input("请输入单位（英寸或厘米)：")

if unit == "英寸":
    print("%f英寸 = %f厘米",(value,value*2.54))
elif unit == "厘米":
    print("%f厘米 = %f英寸"%(value, value / 2.54))
else :
    print("输入有误。")