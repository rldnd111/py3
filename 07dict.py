# 딕셔너리
ages = { '박찬호':48, '박지성':40,
         '박세리:':50, '이승엽':43}
type(ages)

person = {'이름':'홍길동', '나이':25, '몸무게':88.8,
          '주소':'서울 종로구 종로로',
          '취미':['운동','독서','영화감상']}

sungjuk = {'C/C++':'A', 'Java':'B+', '네트워킹':'C',
           '보안':'A','해킹':'F','시스템':'C+'}

# 홍길동의 나이와 취미 조회
person['나이']
person['취미']

# 홍길동의 혈액형 추가
# dict에 새로운 항목을 추가할때는
# 새로운키와 값으로 구성해야 함
person['혈액형'] = 'A'
person

# dict에 기존 키와 값으로 구성한 항목을
# 추가하려 하면 기존키에 저장된 값이 변경됨
person['혈액형'] = 'O'

# dict에서 항목 삭제 : pop(키)
person.pop('몸무게')

# dict 모든 항목 출력
person = {'이름':'홍길동', '나이':25, '몸무게':88.8,
          '주소':'서울 종로구 종로로',
          '취미':['운동','독서','영화감상']}

for key in person.keys():
    print(person[key])

# dict의 키와 값 모두 가져오기 : items
person.items()

for k, v in person.items():
    print(k, v)

#1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C,
# 보안은 A+, 해킹은F, 시스템은C+)을 저장하는 딕셔너리
sungjuk = {'C/C++':'A', 'Java':'B+', '모바일':'C',
           '보안':'A+','해킹':'F','시스템':'C+'}

#2 : 'Java'와 '시스템' 과목의 성적을 조회
sungjuk['Java']
sungjuk['시스템']

#3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
sungjuk['파이썬'] = 'A'
sungjuk['OS'] = 'A+'

#4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다
sungjuk['Java'] = 'F'
sungjuk['시스템'] = 'A'

#5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력
sungjuk.items()
for k, v in sungjuk.items():
    print(k, v)

# 딕셔너리 for 축약문
# { 키/값 표현식 for 키,값 in zip(반복가능객체1, 반복가능객체2) }

# 이름과 성적 리스트를 dict 객체로 재생성하세요
name = ['혜교','지현','수지']     # 키
grd = ['수','양','미']           # 값
sj = {}

# 반복문을 사용하지 않음
sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]

# 반복문을 사용함
for i in range(3):
    sj[name[i]] = grd[i]

# dict 컴프리헨션
# { 키/값 표현식 for 키,값 in zip(반복가능객체1, 반복가능객체2) }
sj2 = { key:val for key, val in zip(name, grd) }

# zip: 여러 개의 데이터를 하나로 합쳐서
# iterable한 객체로 생성해 줌 - 개별 객체는 튜플로 반환
for pair in zip(name, grd):
    print(pair)

