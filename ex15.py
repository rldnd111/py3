# 혈액 보관 시스템
A = []
B = []
AB = []
O = []

for i in range(10):
    blood = input('헌혈해주셔서 감사합니다\n'
            '혈액형을 선택하세요 (A,B,AB,O) ')
    if blood == 'A' or blood == 'a' : A.append(blood)
    elif blood == 'B' or blood == 'b' : B.append(blood)
    elif blood == 'AB' or blood == 'ab' : AB.append(blood)
    elif blood == 'O' or blood == 'o' : O.append(blood)

print(f'혈액형 수급 현황\n'
      f'A형 : {len(A)}\n'
      f'B형 : {len(B)}\n'
      f'AB형 : {len(AB)}\n'
      f'O형 : {len(O)}')

bloods = []
for i in range(10):
    blood = input('헌혈 해주셔서 감사합니다.\n'
                  '혈액형을 선택하세요 (A,B,AB,O)')
    bloods.append(blood)

print('-'*30)
print('혈액형 수급 현황')
print('-'*30)
print(f'A형 : {bloods.count("A")}')
print(f'B형 : {bloods.count("B")}')
print(f'AB형 : {bloods.count("AB")}')
print(f'O형 : {bloods.count("O")}')
print('-'*30)