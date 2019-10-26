import deffun

num = int(input('请输入正整数：'))
if deffun.is_palindrome(num) and deffun.is_prime(num):
    print('%d是回文素数'%num)
else:
    print('x')