def f():
    global s #전역변수로 선언된 변수 global
    s = "I love London!" #s변수에 i love london! 문자열 값을 저장
    print(s)

s = "I lovve Paris!"
f() #global s가 선언되어서 메모리주소에 새로운 값을 저장
print(s) 
