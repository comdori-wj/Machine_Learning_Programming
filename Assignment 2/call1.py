def f(x):#매개변수 선언 함수는 실행하지 않는다.
    y=x #y는 x값과 같다고 변수 선언 한다.
    x=5 #x는 5값을 선언한다.
    return y*y

x=3
print(f(x)) #def함수에 3값을넣어  y*y를 실행한다
print(x) #x값을 출력한다.

