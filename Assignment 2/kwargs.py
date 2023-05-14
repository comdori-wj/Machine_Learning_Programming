def kwargs_test(**kwargs): #키워드 가변인수는 반드시 **를 2개 이상 사용해야 함.
    print(kwargs) #인수를 출력
    print("First value is {first}".format(**kwargs)) #이렇게 사용하는 것을 딕셔너리 자료형을 사용함. 변수명과 값이 쌍으로 저장됨.
    print("Second value is {second}".format(**kwargs)) #개별 변수명을 사용할 수 있다.
    print("Third value is {third}".format(**kwargs))

kwargs_test(first = 3, second = 4, third = 5)
