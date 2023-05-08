def a_rectangle_area(): #매개변수와 반환값을 선언하지 않는다.
    print(5*7) #a_rectangle_area변수에 아무 값도 없어서 그냥 ()에 있는 값을 출력하는 기능을 한다.
def b_rectangle_area(x, y):#매개변수는 11행에 있지만반환값이 없다.
    print(x*y) #x,y값을 곱한다.
def c_rectangle_area(): #매개변수는 없지만 반환값이 12행에 있다.
    return(5*7) 
def d_rectangle_area(x,y):#매개변수와 반환값 모두 있다.
    return(x*y)

a_rectangle_area()
b_rectangle_area(5,7)
print(c_rectangle_area()) #return 받은 값을 대입해서 출력한다.
print(d_rectangle_area(5,7)) #x와 y값을 대입해서 출력한다.
 