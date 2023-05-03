def asterisk4(*args): #언패킹하여 가변인수를 사용
    x, y, *z = args
    return x, y, z

print(asterisk4(3, 4, 5, 10, 20)) #asterisk3와 마찬가지로 x,y를 제외한 나머지 숫자를 묶여서 처리 한다.

