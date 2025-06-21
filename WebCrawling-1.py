# 선생님이 만든 코드 멜론 최신곡 50곡의 순위 제목 가수 앨범명 선택 출력이 가능한 코드
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# Headers = {'User-Agent' : 'Mozilla/5.0 (Window NT 10.0 : Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) chrome / 128.0.0.0 Sarari/537.36'}
# Url = "https://www.melon.com/new/index.htm"
# Req = requests.get(Url,headers = Headers)
# Html = Req.text
# Soup = BeautifulSoup(Html,'html.parser')
# NewList50 = Soup.select('tbody tr')
# data_list = []
#
# for Memo in NewList50:
#     temp = []
#     Rank = Memo.select_one('td div span.rank').get_text()
#     Title = Memo.select_one('td div div  div.ellipsis.rank01  span  a').get_text()
#     Artist = Memo.select_one('td div div div.ellipsis.rank02  a').get_text()
#     Album = Memo.select_one('td div div div.ellipsis.rank03  a').get_text()
#
#     temp.append(Rank)
#     temp.append(Title)
#     temp.append(Artist)
#     temp.append(Album)
#
#     data_list.append(temp)
#
#
#
# columns = ['순위','제목','가수','앨범']
# df_list = pd.DataFrame(data_list, columns=columns)
# address = r'D:\파이썬 수업\git\pythonstart'
# df_list.to_excel(excel_writer = address+r'\melon.xlsx')


# 새로운 크롤링 연습
# 1. <body> 태그 안에 <div> 태그가 두개 포함  <body> 태그의 내용을 추출
import requests
from bs4 import BeautifulSoup
import pandas as pd

# # 1번 예제
# html_doc ="""
# <!doctype html>
# <html>
#     <head>
#         기초 웹 크롤링 따라하기
#     </head>
#     <body>
#         <div>첫 번재 부분</div>
#         <div>두 번째 부분</div>
#     </body>
# </html>
# """
# bs_obj = BeautifulSoup(html_doc,"html.parser")
# body = bs_obj.find("body")
# print(body)
#
# # 1번 만약 <div> 태그의 내용만 불러오고 싶다면 find 메서드에 div 를 입력하면 된다.
# body= bs_obj.find("div")
# print(body)
#
# # 2번 <div> 가 2개 이므로 2개의 내용을 모두 불러오고 싶다면 find 메서드를 find_all 메서드로 바꾸면 된다.
# body= bs_obj.find_all("div") # div 태그의 내용이 2개 이상으므로 리스트로 작성되어 나온다. 결과값)[<div>첫 번재 부분</div>, <div>두 번째 부분</div>]
# print(body)# 이때 나온 <div>첫 번재 부분</div> 는 body[0]번째 태그 내용이고 <div>두 번째 부분</div>]은 body[1]번째 내용이다.
# # 리스트 자료형이기 때문에 인덱스를 이용하여 요소에 접근할 수 있다.
#
# # 3번 리스트 body의 2번째 요소만 가져오고 싶을 때
# div2 = body[1] # 인덱스를 이용하여 2분째 요소만 div2에 반환한다.
# print(div2)
#
# # 4번 위 코드처럼 출력하면 텍스트와 태그가 같이 출력하게 된다. 텍스트만 출력하는 코드
# div2 = body[1]
# print(div2.text) # .text를 붙여서 태그가 아닌 텍스트만 출력하게 한다.  출력문) 두 번째 부분


# 2번 예제

# html_doc ="""
# <!doctype html>
# <html>
#     <head>
#         <title> 기초 웹 크롤링 </title>
#     </head>
#         <body>
#             <table border ="1">
#                 <caption> 과일가격 </caption>
#                 <tr>
#                     <th>상품</th>
#                     <th>가격</th>
#                 </tr>
#                 <tr>
#                     <td> 오렌지 </td>
#                     <td> 100 </td>
#                 </tr>
#                 <tr>
#                     <td> 사과 </td>
#                     <td> 150 </td>
#                 </tr>
#             </table>
#             <table border ="2">
#                 <caption> 의류가격 </caption>
#                 <tr>
#                     <td> 상품 </td>
#                     <td> 가격 </td>
#                 </tr>
#                 <tr>
#                     <td> 셔츠 </td>
#                     <td> 3000 </td>
#                 </tr>
#                 <tr>
#                     <td> 바지 </td>
#                     <td> 5000</td>
#                 </tr>
#             </table>
#         </body>
#     </html>
# """
#
# # 5번 태그의 속성을 이용해 html 문서를 검색 내용추출
# bs_obj = BeautifulSoup(html_doc , "html.parser")
# clothes = bs_obj.find_all("table",{"border" : "2"})
# print(clothes)  #<table border="2">의 내용만 출력