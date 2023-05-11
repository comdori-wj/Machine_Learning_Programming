def f():
    s = "I love London!" #5번째 줄하고 다른 메모리 주소를 가져서 다른 변수s로 저장된다.
    print(s)

s = "I love Paris!" #s변수에 저장
f()  #값출력
print(s) #값 출력
