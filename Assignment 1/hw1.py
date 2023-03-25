num = int(input("당신이 태어난 연도 입력 하십시오 ")) #NUM 값에 태어난 연도를 저장 합니다
age = 2020-num+1 #나이 계산식 입니다

if age <=26 and age >20: #20세 이상 26세 이하는 대학생 입니다
    print("대학생 입니다")
elif age <20 and age >=17: #17세 이상 20세 미만은 고등학생 입니다
    print("고등학생 입니다")
elif age <17 and age >=14: #14세 이상 17세 미만은 중학생 입니다
    print("중학생")
elif age < 14 and age >=8: #8세 이상 14세 미만은 초등학생 입니다
    print("초등학생")
else:
    print("당신은 학생이 아닙니다") #그외 나이는 학생으로 취급하지 않습니다.