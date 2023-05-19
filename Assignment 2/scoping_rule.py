def test(t): # test(x)의 함수를 t로 치환함.
    print(x)
    t = 20
    print("In Fuction:", t)

x=10 # x변수에 10대입
test(x) # x에 저장된 10 함수를 호출함.
print("In Main:", x)
print("In Main:", t) # 오류가 발생함. 이유는 t 함수에서 만 사용 할 수 있는 지역함수 이기 때문이다.