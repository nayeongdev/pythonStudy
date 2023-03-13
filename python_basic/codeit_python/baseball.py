from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []

    while len(new_guess) < 3:
        tries = len(new_guess) + 1
        guess = int(input(f"{tries}번째 숫자를 입력하세요: "))
        if not 0 <= guess <= 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(guess)

    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    # 스트라이크 : 숫자의 위치가 같아야한다.
    # 볼 : 숫자가 포함되어있으면 ok
    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0
borad = ""

while 1:
    tries += 1

    guesses = take_guess()
    strike, ball = get_score(guesses, ANSWER)
    result = "{}S {}B".format(strike, ball)
    print(result)

    if tries % 3 == 0:
      borad += str(guesses)+" "+result+"\n"
    else:
      borad += str(guesses)+" "+result+"\t"
    print(borad)
    
    if strike == 3:
        break


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
