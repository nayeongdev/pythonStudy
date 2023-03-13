# 프로그램은 콘솔에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다.
# 사용자가 입력한 영어 단어가 정답이면 "맞았습니다!"라고 출력하고, 틀리면 "아쉽습니다. 정답은 OOO입니다."가 출력되어야 합니다.
# 문제를 내는 순서는 vocabulary.txt에 정리된 순서입니다.

# with open('vocabulary.txt','r',encoding='utf-8') as f :
#     for line in f:
#         voca_list = line.strip().split(': ')
#         word_eng = voca_list[0]
#         word_kor = voca_list[1]

#         guess = input("{}: ".format(word_kor))

#         if guess == word_eng:
#             print("맞았습니다.\n")
#         else :
#             print("아쉽습니다. 정답은 {}입니다.\n".format(word_eng))

import random

voca_list = []

with open('./python_basic/codeit_python/vocabulary.txt', 'r', encoding='utf-8') as f:
    
    for line in f:
        voca_list.append(line.strip().split(': '))

while 1:
    pick = random.randint(0,len(voca_list)-1)
    word_eng = voca_list[pick][0]
    word_kor = voca_list[pick][1]

    guess = input("{}: ".format(word_kor))

    if guess == 'q':
        break
    
    if guess == word_eng:
        print("맞았습니다.\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(word_eng))

# voca_list = {}

# with open('vocabulary.txt', 'r', encoding='utf-8') as f:

#     for line in f:
#         data = line.strip().split(': ')
#         word_eng, word_kor = data[0], data[1]
#         voca_list[word_eng] = word_kor

# keys = list(voca_list.keys())

# while 1:
#     pick = random.randint(0, len(voca_list)-1)
#     word_eng = keys[pick]
#     word_kor = voca_list[word_eng]

#     guess = input("{}: ".format(word_kor))

#     if guess == 'q':
#         break

#     if guess == word_eng:
#         print("맞았습니다.\n")
#     else:
#         print("아쉽습니다. 정답은 {}입니다.\n".format(word_eng))
