from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.subway.co.kr/?mobile')
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
name = soup.find_all('strong', 'title')
# category = ["클래식", "프레쉬&라이트", "프리미엄", "아침메뉴"]

# for i in range(len(name)):
#     print(name[i].get_text())

print("클래식")
for i in range(0, 5):
    print("-", name[i].get_text())
print("-------")

print("프레쉬&라이트")
for i in range(6, 10):
    print("-", name[i].get_text())
print("-------")

print("프리미엄")
for i in range(11, 16):
    print("-", name[i].get_text())
print("-------")

print("아침메뉴")
for i in range(17, 19):
    print("-", name[i].get_text())