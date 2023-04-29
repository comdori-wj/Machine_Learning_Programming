def spam(eggs):
    eggs.append(1) #기존 객체의 주소값에 1을 추가 한다.
    eggs = [2, 3] #새로운 리스트를 만든다.

ham = [0]
spam(ham)
print(ham) #eggs.append로 실행한 결과를 출력함.
