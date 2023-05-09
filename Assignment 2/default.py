def print_something_2(my_name, your_name = "TEAMLAB"): #your_name매개변수가 기본값인 TEAMLAB으로 되어있다.
    print("Hello {0}, My name is {1}".format(your_name, my_name))#{0}에는 print_something_2("Sungchul")값이 들어가고 {1}에는 4행에 있는 Sungchul이 들어가게 된다.

print_something_2("Sungchul", "TEAMLAB") #함수를 호출 할 때에는 인수가 순서대로 들어간다는 것을 알 수 있다.
print_something_2("Sungchul") #your_name이 지정되지 않았는데 이러한 디폴트 인수는 초깃값을 0으로 하기 때문에 init=0과 같은 형태로 입력된다. 