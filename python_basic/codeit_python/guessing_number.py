# 1과 20 사이의 숫자를 맞히는 게임
# 1. 프로그램을 실행하면 "기회가 *번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "가 출력됩니다.
#    총 네 번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회 횟수가 줄어듭니다.
# 2. 정답을 맞히면 "축하합니다. *번 만에 숫자를 맞히셨습니다."가 출력되고 프로그램은 종료됩니다.
# 3.사용자가 입력한 수가 정답보다 작은 경우 "Up"이 출력되고, 입력한 수가 정답보다 큰 경우 "Down"이 출력됩니다.
# 4.정답이 틀렸으면 1번부터 다시 진행합니다. 만약 네 번의 기회를 모두 사용했는데도 답을 맞히지 못했으면, "아쉽습니다. 정답은 *입니다."가 출력되고 프로그램은 종료됩니다.
import random

ANSWER = random.randint(1, 20)
CHANCE = 4

tries = 0
while tries < CHANCE:
    guess = int(
        input("기회가 {} 번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(CHANCE - tries)))
    if guess == ANSWER:
        break
    if guess > ANSWER:
        print("Down")
    elif ANSWER > guess:
        print("Up")
    tries += 1

if tries == CHANCE:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))
else:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries+1))
