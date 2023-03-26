x = int(input("구구단 몇 단을 할까?")) #몇 단 출력 할지 입력 받기
print("구구단", x,"단을 출력 합니다.") 
for y in range(1,10): #range배열에1 부터 10까지 만듭니다.
	print(x, "x", y, "=", x*y) #x*y값을 출력합니다