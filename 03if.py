# if문
num = int(input('숫자를 하나 입력하세요'))
if num > 10:
    print('num은 10보다 크다')

# 속도위반 경고 : 50km/h
speed = int(input('자동차의 현재 속도는? '))
if speed > 50:
    print('속도 위반!!')
    print('주의하세요~')

if speed > 50: print('속도 위반!!')

# 합격/불합격 출력 : if ~ else
score = int(input('점수를 입력하세요 '))
if (score >= 80):
    print('합격입니다')
else:
    print('아쉽습니다. 다시 도전해주세요~')

# 실행문이 아직 정해지지 않은 경우 pass 키워드로 대체 작성 가능
# if (score >= 80):
#     pass
# else:
#     pass

# 기계의 온도를 감지하여 팬을 자동으로 구동하는 장치
# 기계온도가 40 이상이면 팬가동
# 기계온도가 40 미만이면 팬중지

ondo = int(input('기계 온도를 입력하세요. '))
if ondo >= 40:
    print('팬 가동')
else:
    print('팬 중지')

# 입력받은 정수를 3으로 나눠 소수점 첫째자리가 0.5이상인 경우
# 반올림해서 출력하고, 그렇지 않은 경우 그대로 출력하는 프로그램
num = int(input('정수를 하나 입력하세요 '))

result = num / 3
if (result - int(result) >= 0.5):
    result = int(result) + 1    # 소수이하자리 버린후 올림
else:
    result = int(result)        # 소수이하자리만 버림

print(f'결과 : {result}')


mileage = int(input('마일리지를 입력하세요'))
if (mileage >= 1000):
    print('마일리지 사용가능')
else:
    print('마일리지 사용불가')

# 성적처리
jumsu = int(input('점수를 입력하세요'))

if 60 <= jumsu < 70:
    print('양')
elif 70 <= jumsu < 80:
    print('미')
elif 80 <= jumsu < 90:
    print('우')
elif 90 <= jumsu <= 100:
    print('수')
else :
    print('가')

# 번호에 따라 다른나라 언어 표시
num = int(input('Good morning. Nice to meet you.\n'
      'Where are you from?\n'
      'Please select a number\n'
      '1.대한민국 2.USA 3.中國'))

if (num == 1):
    print('주문하시겠어요?')
elif (num == 2):
    print('Would you like to order?')
elif (num == 3):
    print('主文河時?')
else:
    print('Would you like to order?')

# 국가 재난 지원금 수령액 조회
count = int(input('인원수를 입력하세요 '))

if(count == 1):
    money = 400_000
elif count == 2:
    money = 600_000
elif count == 3:
    money = 800_000
else:
    money = 1_000_000
print(f'{money:,.1f}원 지원')

# BMI 지수를 계산하고 그에 따른 다양한 결과 출력
# < 18.5 : 저체중
# < 23 : 정상
# < 25 : 과체중
# < 30 : 비만
# > 30 : 고도비만

weight = int(input('몸무게는? '))
height = int(input('신장은? '))
height = height / 100

bmi = weight / (height * height)

if bmi > 30: print('고도 비만')
elif bmi > 25: print('비만')
elif bmi > 23: print('과체중')
elif bmi > 18.5: print('정상체중')
else: print('저체중')

# 버스 전용차로 단속 프로그램
day = int(input('1.월~금, 2.토요일, 3.공휴일\n'
                '요일을 선택하세요. '))

if day == 1:
    car = int(input('버스 전용차로 단속 중입니다\n'
                    '1.버스, 2.승용차\n'
                    '차종을 선택하세요. '))
    if car == 1:
        print('버스 입니다')
    elif car == 2:
        print('버스 전용차로 위반!!')
elif day == 2:
    print('토요일 및 공휴일은 단속하지 않습니다')
elif day == 3:
    print('토요일 및 공휴일은 단속하지 않습니다')


msg = '1.월~금, 2.토요일, 3.공휴일\n'\
     '요일을 선택하세요 (1~3)'
day = input(msg)

if day =='1':
    msg = '버스 전용차로 단속중입니다'
else:
    msg = '토요일 및 공휴일은 단속하지 않습니다'
print(msg)

msg = '1.버스 2.승용차\n'\
    '차종을 선택하세요 (1~2)'
car = input(msg)

if car =='1':
    msg ='버스입니다 - 단속대상 아님'
elif car == '2':
    if day =='1':
        msg = '버스전용차로 위반'
    else:
        msg = '승용차입니다 - 단속대상 아님'
print(msg)

# 공적 마스크 구매 가능 요일 계산
year = input('출생연도 끝자리는? ')
age = input('만 나이는? ')

day = ''
if int(age) < 65:
    if year == '1' or year == '6': day = '월'
    elif year == '2' or year == '7': day = '화'
    elif year == '3' or year == '8': day = '수'
    elif year == '4' or year == '9': day = '목'
    elif year == '5' or year == '0': day = '금'
    print(f'{day}요일에 구매 가능합니다')
else:
    print('언제든지 구매가능합니다')