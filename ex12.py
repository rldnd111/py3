# 열차 교차 시간 알아내기
train1 = 10
train2 = 25
train3 = 30

# 0 => 9 : 00
# 60 => 10 : 00

# (0 // 60) + 9
# 0 % 60


for i in range(1, 540+1):
    hour = (i // 60) + 9
    min = i % 60

    if i % train1 == 0 and i % train2 == 0:
            print(f'A열차와 B열차 충돌! {hour}시 {min}분')
    elif i % train2 == 0 and i % train3 ==0:
            print(f'B열차와 C열차 충돌! {hour}시 {min}분')
    elif i % train3 == 0 and i % train1 ==0:
            print(f'C열차와 A열차 충돌! {hour}시 {min}분')