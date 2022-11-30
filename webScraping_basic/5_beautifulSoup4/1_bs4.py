import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# html 문서를 lxml 파서를 통해서 BeautifulSoup 객체로 만듬
soup = BeautifulSoup(res.text, "lxml")

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음으로 발견되는 a 요소 출력
# print(soup.a.attrs) # a 태그가 가지고 있는 속성 정보 출력
# print(soup.a["href"]) # a 요소의 href 속성 '값' 정보 출력

# print(soup.find("a", attrs={"class": "Nbtn_upload"}))  # class="Nbtn_upload"인 a element 찾기
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 어떤 element 찾기

# print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class": "rank01"})

# print(rank1.a)  # rank1의 처음으로 발견되는 a태그 출력
# print(rank1.a.get_text())

# print(rank1.next_sibling)  # next_sibling : 다음 element로 넘어감
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent) # rank1의 부모태그 출력

# rank2 = rank1.find_next_sibling("li")  # next_sibling 몇번 쓸지 상관없이 li 태그에 해당되는 다음 태그를 찾아줌
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))  # li 태그에 해당되는 다음 모든 태그 출력

webtoon = soup.find("a", text="마루는 강쥐-25화. 이빨 요정을 만나고 싶어!")
print(webtoon)
