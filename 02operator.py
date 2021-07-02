num1 = 10
num2 = 20
num3 = num1 + num2 # 정수 + 정수 = 정수

num1 = 30.5
num2 = 50.5
num3 = num1 + num2 # 실수 + 실수 = 실수

num1 = 10
num2 = 30.5
num3 = num1 + num2 # 정수 + 실수 = 실수

month1 = int(input('1월매출입력'))
month2 = int(input('2월매출입력'))
month3 = int(input('3월매출입력'))
quater1 = month1+month2+month3
print('1분기 전체 매출 : {0} %'.format(quater1))

num1 = 3.14
num2 = 0.25
num3 = num1 + num2
float(num3)
int(num3)

# 이익 구하기
sales1 = int(input('1분기 매출'))
buy1 = int(input('1분기 매입'))
    
profit = sales1 - buy1
print('수익 : {0} 원'.format(profit))

# 방 너비 구하기

width = int(input('가로길이'))
height = int(input('세로길이'))
area = width * height
print ("방의 너비는 {0}".format(area))

str1 = 'Hello, World!! '
str1 * 3

# BMI 구하기
weight = int(input('몸무게를 입력하세요'));
height = float(input('신장을 입력하세요'));
height = height / 100

bmi = weight / (height * height)
print('BMI : {0:.2f}'.format(bmi))
print(f'BMI : {bmi:.2f}')  # py 3.6부터 지원
# print 출력 속도 : .format > % > f-string

# 동전 갯수 알아보기

coins = int(input('손 안에 동전 수를 입력하세요'))
isEven = coins % 2
print(f'동전의 홀짝 여부 (0:짝) {isEven}')

10 / 3
10 // 3
# 빵 나누어 주기
# 빵, 나눠줄 빵 갯수 입력받음
# 최대 몇명까지 나눠줄수 있는지와 남는 빵 갯수 출력
bread = int(input('빵의 총 갯수는? '))
diver = int(input('나눠줄 빵의 갯수는? '))

stud = bread // diver
divmod = bread % diver
print(f'{bread}개의 빵은 {diver}개 씩 {stud}명의 학생에게 나눠줄 수 있고,')
print(f'{divmod}개의 빵이 남음')

2**3
2 ** 7
2 ** 8

2 ** 30

# 복리 계산기
# 원금, 유치기간, 연이율을 입력받아 복리계산후 총 수령액 출력
# 1년차 : 원금 * 이율 = 원금
# 2년차 : 원금 * 이율 = 원금
# ...
# 5년차 : 원금 * 이율 = 원금

money = 5_000_000
duration = 5
interest = 5.0

takes = money + (money * 0.05) # 1년차
# takes = takes + (takes * 0.05) # 2년차
takes += takes * 0.05
# takes = takes + (takes * 0.05) # 3년차
takes += takes * 0.05
# takes = takes + (takes * 0.05) # 4년차
takes += takes * 0.05
# takes = takes + (takes * 0.05) # 5년차
takes += takes * 0.05

print(takes)

# 범퍼카 탑승 가능 판별
height = int(input('어린이의 신장을 입력하세요 '))
isRide = height > 120
print(f'탑승 가능 여부 : {isRide} (True : 탑승가능)')

'a' == 'b'
'a' > 'b' # 아스키 코드 변환 후 비교

height = int(input('어린이의 신장을 입력하세요 '))
# isRide = height >= 120 and height < 170
isRide = 120 <= height < 170
print(f'탑승 가능 여부 : {isRide} (True : 탑승가능)')

# short circuit evaluation
num1 = 17
num2 = 20
(num1 < 15) and (num2 < 15) # False and True

num1 = 10
num2 = 20
(num1 < 15) and (num2 < 15) # False and True

# (num1 < 5) and xyz        #py 38만 지원

# 삼항 연산자
# 참값 if 조건식 else 거짓일때값

num = 10
'짝수' if (num % 2 == 0) else '홀수'

# 적자 / 흑자 판단하기

income = int(input('수입을 입력해주세요'))
outcome = int(input('지출을 입력해주세요'))

result = '흑자' if(income>outcome) else '적자'
print (result)

# 윤년여부 알아보기
# 4로 나눠 떨어지고 100으로 나눠 떨어지지 않음
# 400으로 나눠 떨어짐
year = int(input('년도는? '))
isLeap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
result = '윤년' if(isLeap) else '평년'
print (result)


# operator 모듈을 이용하면 대량의 데이터 처리시 속도 향상이 존재함
import operator as op

op.add(10, 20)
op.sub(10, 20)
op.mul(10, 20)
op.floordiv(10, 3) # 정수 몫 : //
op.truediv(10, 3)  # 실수 몫 : /
op.mod(10, 3)
op.pow(2, 30)

op.eq(10,20)
op.ne(10,20)
op.gt(10,20)
op.lt(10,20)
op.ge(10,20)
op.le(10,20)

x = op.eq(10, 20)
y = op.lt(10, 20)
op.and_(x, y)
op.or_(x, y)

# 긴급 재난 지원금 대상자 판별
income = int(input('월 소득을 입력하세요'))
another = int(input('다른 지원금을 받고 있습니까? 1번 받고있다, 2번 받고있지 않다.'))
isTarget = op.and_(op.le(income, 4_000_000), op.eq(another, 2))
result = '수급 대상자' if (isTarget) else '수급 미대상자'
print(result)


