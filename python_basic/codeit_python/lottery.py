from random import randint


def generate_numbers(n):
    num_li = []
    while len(num_li)<n:
        num = randint(1, 45)
        if num not in num_li:
            num_li.append(num)
    return num_li


def draw_winning_numbers():
    win = generate_numbers(7)
    return sorted(win[:6]) + win[6:]

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count


def check(numbers, winning_numbers):
    num_cnt = count_matching_numbers(numbers, winning_numbers[:6])
    bonus = count_matching_numbers(numbers, winning_numbers[6:])
    if num_cnt == 6:
        return 1000000000
    if num_cnt == 5 and bonus == 1:
        return 50000000
    if num_cnt == 5:
        return 1000000
    if num_cnt == 4:
        return 50000
    if num_cnt == 3:
        return 5000
    else :
        return 0