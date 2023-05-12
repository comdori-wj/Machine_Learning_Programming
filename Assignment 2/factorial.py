def factorial(n): #factorial함수 n의 변수값을 입력받아 1이 아닐때 까지 반복하여 자신의 함수로 돌아오게 된다.
    if n == 1:
        return 1 #1로 돌아옴
    else:
        return n * factorial(n - 1) #그렇지 않다면 n값에서 1을 빼고 곱셈을 한다.

print(factorial(int(input("Input Number for Factorial Calculation: ")))) #사용자의 입력값을 받는다.