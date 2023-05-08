def print_something(my_name, your_name): #이 함수는 my_name과 your_name의 인터페이스를 가짐.
    print("Hello {0}, My name is {1}".format(your_name, my_name)) #4행에서 Sungchul은 my_name에 대입되고, TEAMLAB는 your_name에 대입된다.

print_something("Sungchul", "TEAMLAB")
print_something(your_name = "TEAMLAB", my_name = "Sungchul") #변수명이 이미 제시 되어 있어서 순서에 상관없이 출력된다.

