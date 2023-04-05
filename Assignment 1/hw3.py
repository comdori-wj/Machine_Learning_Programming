import random #랜덤 함수 라이브러리를 불러옴
ans_num = random.randint(1,100) #1에서 100까지의 난수를 임의적으로 정함
count = 0 #몇번만에 맞추는지 세는 변수 설정

while True:  #반복문 
 num = int(input("숫자를 맞춰 보십시오. >> "))
 if ans_num < num: #난수보다 사용자 입력 숫자가 클때 크다고  알림
    print( "숫자가 큽니다!")
    count += 1 #카운터 1증가
 elif  ans_num > num: #난수보다 사용자 입력 숫자가 작을때 작다고 알림

    print("숫자가 작습니다")
    count +=1 #카운터 1증가
 else: #정답과 동시에 게임이 종료됨.
    print('정답! {}번 만에 정답을 맞췄습니다, 정답은 {} 이였습니다'.format(count, ans_num))
    break
    