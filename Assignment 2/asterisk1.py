def asterisk1(a, b, *args): #가변인수 args를 사용한다.
    return a + b + sum(args) #변수a,b만 입력 받고 그외 나머지 변수들은 순서에 상관 없이 가변인수를 사용하여 처리한다.

print(asterisk1(1, 2, 3, 4, 5))
