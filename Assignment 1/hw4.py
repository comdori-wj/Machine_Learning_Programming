while True:
    x = int(input("구구단 몇 단을 할까?(1~9, 0입력시 종료)")) 
    if x == 0: #0을 입력시 바로 종료
        print("구구단 계산을 종료 합니다.")
        break
    elif not 1 <= x <= 9: #1에서 9까지의 숫자만을 인식하며 그외 숫자는 다시 입력해야 한다.
        print("다시 입력 하세요.")
        continue    #처음으로 다시 이동해서 반복문을 실행한다
    else: #조건이 맞을경우 구구단 계산을 실행한다.
     print("구구단", x,"단을 출력 합니다.") 
     for y in range(1,10): #range배열에1 부터 10까지 만듭니다.
         print(x, "x", y, "=", x * y) #x*y값을 출력합니다