from random import *
from math import *
print(5)
print(3.14)
print('apple')
print("Hello World!")
sentence = """
이것은 문장입니다.
변수를 활용한 문장쓰기
"""
print(sentence)  # 앞뒤공백해서 총 4줄 출력
print(True)
print(not False)


print('-----------변수')

# 애완동물 소개하기~
animal = "고양이"
name = "아쿵이"
age = 4
is_adult = age >= 3
print("우리집" + animal + "의 이름은 " + name)
# 문자열형식이 아닌 변수는 문자열로 형변환 해야한다.
print(name + "는 " + str(age) + "살")
# 쉼표 사용할 경우 빈칸이 하나 들어간다
print(name, "이는 어른일까요? ", str(is_adult))


print('-----------퀴즈1')

# 퀴즈
# 변수명 : station 이고 변수값을 "사당" 입력
# 출력문장 : xx행 열차가 들어오고 있습니다.
station = "사당"  # input()
print(station+"행 열차가 들어오고 있습니다.")
print('================================================')


print('-----------연산자')

# 연산자
print(2**3)  # 2^3 = 8
print(5 % 3)  # 나머지 구하기 2
print(5//3)  # 몫 구하기 1
print(not (1 != 3))  # False
print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True
print((3 > 0) or (3 < 5))  # True
print((3 > 0) | (3 < 5))  # True
print(5 > 4 > 3)  # True
print(5 < 4 > 3)  # False


print('-----------숫자 함수')

# 숫자처리 함수
print(abs(-5))  # 5
print(pow(4, 2))  # 4^2 = 16
print(max(5, 12))  # 12, 최소는 min
print(round(3.14))  # 3
print(round(4.99))  # 5

# from math import *
print(floor(4.99))  # 내림 4
print(ceil(3.14))  # 올림 4
print(sqrt(16))  # 제곱근 4


print('-----------랜덤함수')

# 랜덤 함수
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10)+1)  # 1 ~ 10 이하의 임의의 값 생성

# from random import *
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45이하의 임의의 값 생성


print('-----------퀴즈2')

# 퀴즈
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인이다.
# 오프라인 모임 날짜를 정해주는 프로그램 작성
# 조건1 : 랜덤 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
# 출력문 : 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
select_day = int((random()*25)+4)  # 4~29미만
select_day = randrange(4, 29)  # 4~29미만
select_day = randint(4, 28)  # 4~28이하
print("오프라인 스터디 모임 날짜는 매월 ", select_day, "일로 선정되었습니다.")
print('================================================')


print('-----------슬라이싱')

# 슬라이싱 -> 슬라이싱(:)을 하면 문자열 취급
idNum = "001225-1234567"
print("성별 :", idNum[7])
print("년 :", idNum[0:2])  # 0번째에서 2번째 전까지(0,1)
print("월 :"+idNum[2:4])
print("생년월일 :", idNum[:6])  # 처음부터 6직전까지
print("뒷자리 :" + idNum[7:])
print("주민등록번호 : " + idNum[:-1])


print('-----------문자열 함수')

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)  # 문자 위치 찾아줌 5
index = python.index("n", index + 1)
print(index)  # 시작위치(index+1)부터 문자 위치 찾아줌 15

# find는 원하는 것이 없으면 -1 반환, index는 에러발생
print(python.find("Java"))
# print(python.index("Java"))

print(python.count("n"))  # n이 몇번있는지


print('-----------문자열 포맷')

# 문자열 포맷
print("나는 %d살 입니다." % 20)
print("나는 %s색과 %s색을 좋아해요" % ("파란", "노란"))

print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "노란"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "노란"))

print("나는 {age}살이고, {color}색을 좋아해요".format(age=20, color="노란"))

age = 20
color = "노란"
print(f"나는 {age}살이고, {color}색을 좋아해요")


print('-----------특수문자')

# 특수 문자
print("백문이 불여일견\n백문이 불여일타")
print("이것은 '사과'입니다.")  # "''", '""'
print("이것은 \"사과\"입니다.")  # \', \"
print("C:\\Users\\user\\py\\pratice.py")  # \\

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")


print('-----------퀴즈3')

# 퀴즈
# 사이트별로 비밀번호를 만들어 주는 프로그램
# 예) http://naver.com
# 규칙1 : http:// 부분 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분 제외 -> naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e'개수 + "!"로 구성
#                   nav               5               1
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
# hint = url[7:url.find('.')]
hint = url.replace("http://", "")
hint = hint[:hint.index(".")]
password = hint[:3]+str(len(hint))+str(hint.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
print('================================================')


print('-----------리스트')

# 리스트
subway = ["미미", "토토", "라라"]
# 미미는 몇 번째 칸에 타고 있는가?
print(subway.index("미미"))
# 도도가 다음 정류장에서 지하철에 탐
subway.append("도도")
print(subway)
# 비비를 토토 / 라라 사이에 태우기
subway.insert(1, "비비")
print(subway)
# 지하철에 있는 사람들 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
# 같은 이름의 사람이 몇명 있는지 확인
subway.append("미미")
print(subway)
print(subway.count("미미"))

# 정렬
num_list = [3, 5, 2, 1, 4]
num_list.sort()  # 오름차순
print(num_list)
num_list.reverse()  # 내림차순
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [3, 5, 2, 1, 4]
mix_list = ["모모", 20, True]

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


print('-----------사전')

# 사전 (dictionary)
cabinet = {3: "미미", 100: "라라"}
print(cabinet[3])  # 값이 없으면 error
print(cabinet.get(3))  # 값이 없으면 None
print(cabinet.get(5, "사용가능"))  # None대신 사용가능 출력
print(3 in cabinet)  # True, in키워드를 사용해 t/f반환

# 사전 추가
cabinet = {"A-3": "미미", "B-100": "라라"}
print(cabinet["A-3"])
cabinet["A-3"] = "비비"
cabinet["C-5"] = "쿠쿠"
print(cabinet)
# 사전 삭제
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())

# 사전 아예 삭제
cabinet.clear()
print(cabinet)


print('-----------튜플')
# 튜플 <- 값 추가, 변경 불가능
menu = ("돈까스", "치즈까스")
print(menu[0])

(name, age, hobby) = ("미미", 20, "십자수")
print(name, age, hobby)


print('-----------세트')

# 집합(set) : 중복 x, 순서 없음
my_set = {1, 2, 3, 3}
print(my_set)

java = {"미미", "코코", "도도"}
python = set(["미미", "토토"])
# 교집합 (java, python 둘다 가능한 사람)
print(java & python)
print(java.intersection(python))
# 합집합 (java 또는 python 가능한 사람)
print(java | python)
print(java.union(python))
# 차집합 (java만 가능한 사람)
print(java - python)
print(java.difference(python))

# 집합 원소 추가(python 가능한 사람 늘어남)
python.add("코코")
print(python)
# 집합 원소 삭제(java를 잊었다)
java.remove("코코")
print(java)


print('-----------자료구조 변경')

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


print('-----------퀴즈4')

# 댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받는다.
# 추첨 프로그램 작성하기
# 조건1 : 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨함되, 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

# from random import *
id_lst = list(range(1, 21))
shuffle(id_lst)
winners = sample(id_lst, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("-- 축하합니다 --")
