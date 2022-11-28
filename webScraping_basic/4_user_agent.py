# !! 주의 : 현재 아래 페이지는 403에러가 안나기 때문에 UserAgent를 변경하지 않아도 정상적으로 html을 받아온다 !!
import requests
url = "http://nadocoding.tistory.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
res.raise_for_status()  # 사이트에 문제있으면 에러발생 시킴

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
