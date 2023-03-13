print('-----------클래스')
class Unit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{} 유닛 생성".format(self.name), end = " → ")
    print("체력 {0}, 공격력{1}".format(self.hp,self.damage))

marine1 = Unit("마린", 50, 5)
marine2 = Unit("마린", 50, 5)
tank = Unit("탱크", 150, 35)


# 멤버변수
print("유닛 이름 : {0}, 공격력 : {1}".format(marine1.name, marine1.hp))
marine2.clocking = True
if marine2.clocking == True:
  print("{}는 현재 클로킹 상태입니다".format(marine2.name))


# 메소드
class AttackUnit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage

  def attack(self, location):
    print("{0} : {1} 방향으로 적군 공격 [공격력 {2}]"
          .format(self.name, location, self.damage))
  
  def damaged(self, damage):
    print("{0} : {1} 데미지 입었다".format(self.name, damage))
    self.hp -= damage
    print("{0} : 현재 체력 {1}".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴".format(self.name))
    
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# 상속
class Unit:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp

class AttackUnit(Unit):
  def __init__(self, name, hp, damage):
    Unit.__init__(self, name, hp)
    self.damage = damage

  def attack(self, location):
    print("{0} : {1} 방향으로 적군 공격 [공격력 {2}]"
          .format(self.name, location, self.damage))

  def damaged(self, damage):
    print("{0} : {1} 데미지 입었다".format(self.name, damage))
    self.hp -= damage
    print("{0} : 현재 체력 {1}".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴".format(self.name))


# 다중 상속
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed

  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아가 [속도 {2}]"
          .format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, damage)
    Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")


# 메소드 오버라이딩
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
  
  def move(self, location):
    print("{0} : {1} 방향 이동 [속도: {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
  def __init__(self, name, hp, speed, damage):
    Unit.__init__(self, name, hp, speed)
    self.damage = damage

class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
    Flyable.__init__(self, flying_speed)
  
  def move(self, location): # 재정의
    self.fly(self.name, location)

# 지상 유닛
vulture = AttackUnit("벌쳐", 80, 10, 20)
# 공중 유닛
battlecruiser = FlyableAttackUnit("배클",500,25,3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("11시")


# pass -> 그냥 넘어가는 것
class BuildingUnit(Unit):
  def __init__(self, name, hp, location):
    pass
depot = BuildingUnit("디폿",500,"9시")

def game_start():
  print("새로운 게임 시작")
def game_over():
  pass

game_start()
game_over()


# super -> 상속된 클래스(부모 클래스)에서 불러옴, 다중 상속에서는 쓰일수있지만 하나만 상속받아오기 때문에 안쓰는게 좋다
class BuildingUnit(Unit):
  def __init__(self, name, hp, location):
    # Unit.__init__(self,name,hp,0)
    super().__init__(name,hp,0)
    self.location = location


print('-----------퀴즈8')

# 부동산 프로그램 작성

# (출력 예제)
# 총 3대의 매물이 잇다
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
  # 매물 초기화
  def __init__(self, location, house_type, deal_type, price, completion_year):
    self.location = location
    self.house_type = house_type
    self.deal_type = deal_type
    self.price = price
    self.completion_year = completion_year

  # 매물 정보 표시
  def show_detail(self):
    print(self.location, self.house_type, self.deal_type, 
          self.price, self.completion_year)

houses = []
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print(f"총 {len(houses)}대의 매물")
for house in houses:
  house.show_detail()


print('================================================')

print('-----------예외처리')
try:
  nums = []
  print("나누기 계산기")
  nums.append(int(input("num 1 : ")))
  nums.append(int(input("num 2 : ")))
  nums.append(int(nums[0]/nums[1]))
  print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError:
  print("에러! 잘못된 값 입력")
except ZeroDivisionError as err:
  print(err)
except Exception as err: # 모든 에러
  print("알 수 없는 에러 발생")
  print(err)


# 에러 발생시키기 -> raise
try:
  print("한 자리 숫자 전용 나누기 계산기")
  n1 = 10#int(input("num 1 : "))
  n2 = 5#int(input("num 2 : "))
  if n1 >= 10 or n2 >= 10:
    raise ValueError
  print(f"{n1} / {n2} = {n1/n2}")
except ValueError:
  print("잘못된 값입력. 한 자리 숫자만 입력")


# 사용자 정의 예외처리

class BigNumberError(Exception):
  def __init__(self, msg):
    self.msg=msg
    
  def __str__(self):
    return self.msg

try:
  print("한 자리 숫자 전용 나누기 계산기")
  n1 = 10#int(input("num 1 : "))
  n2 = 5#int(input("num 2 : "))
  if n1 >= 10 or n2 >= 10:
    raise BigNumberError(f"입력값 : {n1}, {n2}")
  print(f"{n1} / {n2} = {n1/n2}")
except ValueError:
  print("잘못된 값입력. 한 자리 숫자만 입력")
except BigNumberError as err:
  print("에러 발생. 한 자리 숫자만 입력")
  print(err)

  
# finally -> 무조건 실행되는 코드
try:
  print("나누기 계산기")
  n1 = 10#int(input("num 1 : "))
  n2 = 5#int(input("num 2 : "))
  print(f"{n1} / {n2} = {n1/n2}")
except Exception as err:
  print(err)
finally:
  print("계산기를 이용해 주셔서 감사합니다")

print('-----------퀴즈9')

# 자동 주문 시스템
# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError로 처리
#         (출력 메시지) : "잘못된 값 입력"
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         (출력 메시지) : "재고 소진"

chicken = 10  # 남은 치킨 수
waiting = 1   # 대기번호 1부터

class SoldOutError(Exception):
  pass

while(True) :
  try:
    print(f"[남은 치킨 : {chicken}]")
    order = 10#int(input("치킨 몇마리?"))
    if order > chicken:   # 남은 치킨보다 주문량이 많을때
      print("재료 부족")
    elif order < 1:
      raise ValueError
    else:
      print(f"[대기번호 {waiting}] {order}마리 주문 완료")
      waiting += 1
      chicken -= order
    if chicken == 0:
      raise SoldOutError
  except ValueError:
    print("잘못된 값 입력")
  except SoldOutError:
    print("재고 소진이라 주문 안 받아요")
    break


print('================================================')

print('-----------모듈')
import theater_module
theater_module.price(1) # 3명의 영화값
theater_module.price_morning(1) # 3명 조조할인 영화
theater_module.price_soldier(1) # 3명 군인할인 영화

import theater_module as mv
mv.price(2)  # 3명의 영화값
mv.price_morning(2)  # 3명 조조
mv.price_soldier(2)  # 3명 군인

from theater_module import *
price(3)
price_morning(3)
price_soldier(3)

from theater_module import price, price_morning
price(4)
price_morning(4)
# price_soldier(4)

from theater_module import price_soldier as price
price(5)


print('-----------패키지')
import travel.thailand
# import travel.thailand.TailandPackage # 사용불가
trip_to = travel.thailand.TailandPackage()
trip_to.detail()

from travel.thailand import TailandPackage  # 이렇게는 가능
trip_to = TailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# travel > __init__파일에서 __all__를 이용하여 아래 코드가 실행되게 한다
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.TailandPackage()
trip_to.detail()


# 패키지, 모듈 위치 -> inspect.getfil(패키지명|모듈명)
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))


# pip install -> pypi 페이지에서 가져오는 패키지 설치
# BeautifulSoup 검색해서 설치하면 아래 코드 실행 가능

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# 내장 함수 -> 구글에 list of python builtins 검색 해보기
# input : 사용자 입력을 받는 함수
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())

# print(dir(random))


# 외장 함수 -> 구글에 list of python modules 검색 해보기
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("python_basic\\*.py"))  # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())  # 현재 디렉 토리

# folder = "sample_dir"

# if os.path.exists(folder):
#   print("이미 존재하는 폴더입니다.")
#   os.rmdir(folder)
#   print(folder,"폴더를 삭제하였습니다.")
# else:
#   os.makedirs(folder) # 폴더 생성
#   print(folder, "폴더를 생성하였습니다.")

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()     # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은 ", today+td) # 오늘부터 100일후


print('-----------퀴즈10')

# 모듈 만들기 (파일명 : byme.py)

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.

import byme
byme.sign()