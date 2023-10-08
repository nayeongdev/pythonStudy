import re

# 파일을 읽어올 경로와 파일 이름을 지정합니다.
file_path = "toy/blindCode.txt"

# 파일을 엽니다.
try:
    with open(file_path, "r") as file:
        # 파일의 내용을 읽어와 변수에 저장합니다.
        file_contents = file.read()
except FileNotFoundError:
    print(f"파일 '{file_path}'을(를) 찾을 수 없습니다.")
else:
    #
    while True:
        codeType = input("코드 언어를 영어로 작성하세요 : ")

        if re.compile(r"[a-zA-Z]*$").match(codeType):
            # 입력값이 영어 알파벳으로만 구성되었을 경우
            break
        else:
            print("영어로만 입력하세요.")

    # 파일의 내용을 출력합니다.
    print("||")
    print(f"```{codeType}")
    print(file_contents)
    print("```")
    print("||")
