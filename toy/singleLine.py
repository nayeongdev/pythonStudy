# 불필요한 줄 삭제하는 코드
str_content = """
문장

띄어쓰기가

거슬릴때


"""
str_list = str_content.splitlines() # 각 줄에 있는 문자열 추출 (list)
str_list = list(filter(None,str_list)) # 배열 안 ''(빈값) 제거
print()
print(*str_list,sep='\n')
# 함수(*리스트) → 언패킹 : https://dojang.io/mod/page/view.php?id=2345
