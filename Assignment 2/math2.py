import math

def get_result_quadratic_equation(a, b, c):
    values = [] # 함수화 하여 출력하도록 한다.
    values.append((-b + math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a)) 
    values.append((-b - math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a))
    return values

print(get_result_quadratic_equation(1, -2, 1))