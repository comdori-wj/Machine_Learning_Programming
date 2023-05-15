import math # math 라이브러리를 불러온다.
a = 1; b = -2; c = 1 # 각 변수에 값을 저장한다.

print((-b + math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a)) # 변수에 저장해준 값을 이용하여 근의 공식을 이용해 계산한다.
print((-b - math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a))