def asterisk3(*args): #언패킹하여 가변인수를 사용
    x, y, *z = args 
    return x, y, z

print(asterisk3(3, 4, 5)) #3,4를 제외한 나머지 숫자는 묶여져서 출력.