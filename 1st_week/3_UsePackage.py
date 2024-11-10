from pprint import pprint

import requests
#requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

# pprint(rjson)

#필요 데이터만 보기
# rows = rjson['RealtimeCityAir']['row']
# pprint(rows)

#구이름, 현재 대기질 상태만 보기
#ex) 중구 좋음
# for row in rows:
#     print(row['MSRSTE_NM'], row['IDEX_NM'])

def get_gu_mise(name):
    gus = rjson['RealtimeCityAir']['row']

    for gu in gus:
        gu_name = gu['MSRSTE_NM']
        gu_mise = gu['IDEX_MVL']
        if gu_name == name:
            return gu_mise
    return '미세먼지 수치가 없습니다'

print(get_gu_mise("중구"))
print(get_gu_mise("종로구"))
print(get_gu_mise("수지구"))