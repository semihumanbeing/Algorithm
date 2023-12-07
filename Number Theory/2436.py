# 최대 공약수, 최소 공배수 구하기
import math

def _gcd(a,b):
    while a % b != 0:
        tmp = a % b 
        a = b 
        b = tmp
    return b 

def _lcd(a,b):
    return a*b // math.gcd(a,b)

print(_gcd(30, 36), _lcd(30, 36))