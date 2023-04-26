kor = [49, 80, 20, 100, 80] #국어점수
math = [43, 60, 85, 30, 90] #수학점수
eng = [49, 82, 48, 50, 100] #영어점수
midterm = [kor, math, eng] #중간고사 점수

student = [0, 0, 0, 0, 0] #나눌 점수를 0으로 초기화
i = 0
for sub in midterm:
    for score in sub:
        student[i] += score #학생마다 개별로 교과 점수를 저장한다
        i += 1 # 학생 인덱스 구분
    i = 0 # 과목이 바뀔 떄 학생 인덱스 초기화
else:
            a, b, c, d, e = student #학생별 점수 언팩
            average = [a/3, b/3, c/3, d/3, e/3] #학생별 과목을 평균계산
            print("평균", average) #점수 출력