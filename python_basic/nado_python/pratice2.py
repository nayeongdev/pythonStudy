# if
from random import *
weather = "맑아요"  # input("오늘 날씨 어때요? ")
if weather == "비" or weather == "눈":
  print("우산 챙겨요")
elif weather == "미세먼지":
  print("마스크 챙겨요")
else:
  print("챙길게 없어요")

temp = 10  # int(input("기온은 어때요? "))
if 30 <= temp:
  print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
  print("나가기 좋아요")
elif 0 <= temp < 10:
  print("외투 챙기세요")
else:
  print("너무 추워요. 실내가 좋아요")


print('-----------반복문')

# for
for waiting_no in range(1, 4):
  print("대기번호 : {0}".format(waiting_no))

cgv = ["아이언맨", "엘사"]
for combo in cgv:
  print("{} 콤보가 준비되었습니다.".format(combo))

# 출석번호가 1 2 3, 앞에 100을 붙이기로 함 -> 101, 102, 103
students = [1, 2, 3]
print(students)
students = [i+100 for i in students]
print(students)

students = ["momo", "Iron man", "i am groot"]
# 학생 이름을 대문자로 치환
students = [i.upper() for i in students]  # lower
print(students)
# 학생 이름을 길이로 변환
students = [len(i) for i in students]
print(students)


# while
customer = "토르"
index = 2
while index >= 1:
  print("{0}님, 커피 나왔습니다. 리필 가능횟수 : {1}번".format(customer, index))
  index -= 1
  if index == 0:
    print("커피는 폐기되었습니다.")

customer = "안나"
person = "Unknown"
while person != customer:
  print("{0}님, 커피 나왔습니다.".format(customer))
  person = "안나"  # input("이름이 어떻게 되세요? "), p와 c가 똑같을때까지 반복


# continue 와 break
absent = [2, 5]  # 결석
no_book = [4]  # 책 안가져옴
for student in range(1, 6):
  if student in absent:
      continue
  elif student in no_book:
      print("수업끝. {}는 교무실로 따라와".format(student))
      break
  print("{}, 책읽어봐".format(student))


print('-----------퀴즈5')

# 택시기사가 50명의 승객과 매칭 기회가 있을 때, 총 탑승객 수를 구하는 프로그램
# 조건 1 : 승객별 운행 소요 시간 -> 5 ~ 50분 사이의 난수
# 조건 2 : 택시기사는 소요 시간 5 ~ 15분 사이의 승객만 매칭되야 한다

# (출력 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승객 : 2 분
total = 5
time_lst = [randint(5, total) for i in range(total)]  # 소요시간
cnt = 0  # 총 탑승객 수

for i in range(total):
  check = " "
  if (time_lst[i] <= 15):  # 5<=i<=15
      check = "O"
      cnt += 1
  print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, i+1, time_lst[i]))
print()
print(f"총 탑승객 : {cnt} 분")

print('================================================')
print('-----------함수')


def open_account():
  print("new 계좌 생성 완료")

def deposit(balance, money):  # 입금
  print("입금 완료. 잔액 : {}원".format(balance+money))
  return balance+money

def withdraw(balance, money):  # 출금
  if balance < money:  # 잔액이 출금보다 적으면
    print(f"출금이 완료되지 않았습니다. 잔액 : {balance}원")
    return balance
  print("출금이 완료되었습니다. 잔액 : {}원".format(balance-money))
  return balance-money

def withdraw_night(balance, money): # 영업시간이후 출금
  commission = 100 #수수료 100원
  return commission, balance-money-commission

open_account()
balance = 0  # 잔액
balance = deposit(balance, 2000)
balance = withdraw(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {}원, 잔액 : {}원".format(commission, balance))

# 기본값 -> 기본적으로 값을 부여
def profile(name, age=20, main_lang="python"):
  print("이름 : {0}\t나이: {1}\t주 언어: {2}"
  .format(name,age,main_lang))
profile("미미")

# 키워드값 -> 키워드를 사용하면 순서영향을 받지않는다.
def profile(name, age, main_lang):
  print(name,age,main_lang)
profile(main_lang="java",name="비비",age=19)

# 가변 인자 -> 길이에 상관없이 사용가능
# 아래 코드는 일일이 쳐야하고, 길이에 제한이 있다
# def profile(name, age, lang1, lang2, lang3):
#   print("이름 : {0}\t나이: {1}\t주 언어:".format(name,age), end=" ")  # 이어서 출력
#   print(lang1, lang2, lang3)
# profile("미미",20,"python","java","C")
# profile("미미",20,"python","","")

def profile(name, age, *language):
  print("이름 : {0}\t나이: {1}\t주 언어:".format(name,age), end=" ")  # 이어서 출력
  for lang in language:
    print(lang, end=" ")
  print()
profile("미미",20,"python","java","C")
profile("미미",20,"python")

# 지역변수와 전역변수
gun = 10

def checkpoint(soldiers): # 경계근무
  global gun   # 전역 공간에 있는 gun 사용
  gun -= soldiers
  print("[함수 내] 남은 총 : {}".format(gun))

def checkpoint_ret(gun, soldiers):
  gun -= soldiers
  print("[함수 내] 남은 총 : {}".format(gun))
  return gun
  
print("전체 총 : {}".format(gun))
# checkpoint(2) # 2명이 경계근무
gun = checkpoint_ret(gun, 2)  # 2명이 경계근무
print("남은 총 : {}".format(gun))


print('-----------퀴즈6')

# 표준 체중 구하는 프로그램
# 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자: 키(m) x 키(m) x 22
# 여자: 키(m) x 키(m) x 21

# 조건1 : 표준 체중을 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 두째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height,gender):
  if(gender=="남자"):
    bmi = height * height * 22
  elif(gender=="여자"):
    bmi = height * height * 21
  return bmi

height = 175  # cm로 입력
gender = "남자"
weight = round(std_weight(height/100, gender),2)
print(f"키 {height}cm {gender}의 표준 체중은 {weight}입니다.")

print('================================================')

print('-----------입출력')

# sep = "" -> 구문자, 쌍따옴표안에 해당되는 문자로 글자를 구분
# end = "" -> 끝문자, 연속적으로 출력 가능하게 한다
print("Python", "Java", sep = ", ", end="?")

import sys
print("Python", "Java", file=sys.stdout)  # 표준출력 처리
print("Python", "Java", file=sys.stderr)  # 표준에러 처리

# ljush(x) -> x칸을 확보하며 왼쪽정렬
# rjush(x) -> x칸을 확보하며 오른쪽정렬
scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items():
  print(subject.ljust(4), str(score).rjust(4), sep=":")

# zfill(n) -> n만큼 0을 채워줌
for num in range(1,4):
  print("대기번호 : "+str(num).zfill(3))

# input() -> 입력, 문자열로 입력되므로 특정한 자료형을 원할때 형변환 필요
# answer = input("아무 값이나 입력 : ")
# print("입력값은 {}입니다. \n자료형 : ".format(answer),end="")
# print(type(answer))

# 빈자리는 빈공간, 오른쪽 정렬, 총 10자리 공간 확보
print("{0: >10}".format(500))

# 양수일 때 +, 음수일때 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리마다 콤마 찍기
print("{0:,}".format(10000000000))
# 3자리마다 콤마 찍기, + - 부호 붙이기
print("{0:+,}".format(10000000000))
# 3자리마다 콤마 찍기, + - 부호 붙이기, 자리수 확보
# 빈자리 $로 채우기
print("{0:$<+20,}".format(10000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수까지 표시 (반올림)
print("{0:.2f}".format(5/3))


print('-----------파일 입출력')

# 파일 쓰기
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 기존 파일에 쓰기
score_file = open("score.txt","a",encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 파일 읽기
score_file = open("score.txt","r",encoding="utf8")
print(score_file.read())  # 모두 읽기
# print(score_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동

# 파일 줄 수를 모를때
# while True:
#   line = score_file.readline()
#   if not line:
#     break
#   print(line, end="")

# 리스트 형태로 저장
# lines = score_file.readlines()
# for line in lines:
#   print(line, end="")

score_file.close()

# pickle -> 데이터 값을 파일로 만들어 줌
import pickle
profile_file = open("profile.pickle","wb") #쓰기+바이너리타입
profile = {"이름":"미미","나이":20,"취미":["십자수","뜨개질","수영"]}
# print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle","rb") #읽기+바이너리타입
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# with -> with를 쓰면 파일을 안 닫아줘도 된다
with open("profile.pickle","rb") as profile_file:
  print(pickle.load(profile_file))

with open("study.txt","w",encoding="utf8") as study_file:
  study_file.write("Hard study python")

with open("study.txt","r",encoding="utf8") as study_file:
  print(study_file.read())


print('-----------퀴즈7')

# 매주 1회 작성해야 하는 보고서 파일 만들기

# (출력 형식)
# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 5주차까지의 보고서 파일을 만드는 프로그램 작성
# 조건: 파일명은 '1주차.txt', '2주차.txt', ..로 한다

for i in range(1,3):
#   report = open("{0}주차.txt".format(i),"w",encoding="utf8")
#   print("- {} 주차 주간보고 -".format(i),file=report)
#   print("부서 : ",file=report)
#   print("이름 : ",file=report)
#   print("업무 요약 : ",file=report)
#   report.close()

  with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
    report_file.write("- {}주차 주간 보고\n".format(i))
    report_file.write("부서 : \n")
    report_file.write("이름 : \n")
    report_file.write("업무 요약 : ")