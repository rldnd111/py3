# 출석부 관리 시스템
#1 : 학급 학생수가 10명(정우람, 박으뜸, 배힘찬, 천영웅, 신석기, 배민규, 전민수, 박건우, 박찬호, 이승엽)
student = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규',
           '전민수', '박건우', '박찬호', '이승엽']

#2 : 가나다 순으로 정렬
student.sort()

#3 : 박찬호 학생 전학
student.remove('박찬호')
student

#4 : 선생님을 돕기 위한 3명을 앞에서 부터 출력
student[:3]

#5 : 이병규 전학
student.append('이병규')
student.sort()

#6 : 자리를 바꾸기위해 순서 역순
student.sort(reverse=True)

#7 : 정우람 학생이 정잘남으로 개명
student[1] = '정잘남'