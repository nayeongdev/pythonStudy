with open('./python_basic/codeit_python/vocabulary.txt', 'w', encoding="utf-8") as f:
    while 1:
        word_eng = input("영어 단어를 입력하세요: ")
        if (word_eng == 'q'):
            break

        word_kor = input("한국어 뜻을 입력하세요: ")
        if (word_kor == 'q'):
            break

        f.write('{}: {}\n'.format(word_eng, word_kor))
