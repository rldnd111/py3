#업무 컴퓨터 수량 파악
time = (int(input('근무시간 입력')))
computer = 3 * 8 // time
addCom = 1 if (3 * 8 % time) > 0 else 0
print (f'필요한 컴퓨터수 : {computer + addCom}')