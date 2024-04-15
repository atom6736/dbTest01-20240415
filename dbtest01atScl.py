# 파이썬과 DB연동 실습

import pymysql  # mysql과 연동시켜주는 라이브러리
#디비가 현재 백그라운드에서 돌고 있다. 서버컴에 접속하려면 네개의 항목이 필요함. 네이버에 로그인하려면 아이디 비번이 필요한 것과 마찬가지.
# 계정 아이디. root. 비번(sql비번), 본인 ip접속은localhost,
# 파이썬과 mysql 서버간의 커넥션 생성
# 1) 계정: root(관리자계정)
# 2) 비밀번호: 내 비번
# 3) 데이터베이스가 설치된 컴퓨터의 IP주소.
#  - 본인 컴퓨터면 localhost, 다른 컴퓨터면 그 컴퓨터의 ip wnth
#  - 교수님 것은 192.168.0.100(교수용 컴퓨터 ip)
# 4)데이터베이스 스키마의 이름(ex: shopdb 등)

# 첫번쨰로 파이썬과 mysql과의 커넥션(다리)을 먼저 만들어야 한다.

dbConn = pymysql.connect(host='localhost', user='root', password='domybest2024@', db='shopdb')
# 파이썬과 mysql간의 connection을 생성해서 변수에 저장
# 다음으로 실행시킬 sql을 만든다.

sql = "SELECT * FROM membertbl"  #세미콜론은 넣지 않는다. DB에 실행할 SQL문 생성

cur = dbConn.cursor()
#커서를 호출에 어딘가에 저장.

cur.execute(sql)  # 연결된 DB의 스키마에 지정된 SQL문이 실행됨. select는 다른 것과 다르다.
# 셀렉트만 보내준 것을 받아야 함.

records = cur.fetchall() # 전부다 가져오라는 명령문. sql문에서 실행된 select문의 결과를 records라는 이름으로 작명해서 받은 것.

print(records)
print([0]) # 특정레코드(1행)만 출력
print(records[0][1]) # 특정레코드의 특정 값 출력. 이렇게 하면 값 하나에 접근하여 빼낼 수 있음. 왼쪽 코딩으로 하면 이순신만 출력되게 됨.

for member in records:
    print(member)



#DB커넥션을 열어서 볼일을 받았으면 닫아주어야 DB에 부하가 안난다고. 안 닫아도 에러는 안 나지만,
# 섬과 섬이 있는데 사람이 지나갈 때마다 다리를 만들고 안 없어지면 나중에는 다리를 만들 수 없음.

#커넥션의 사용이 종료된 후에는 반드시 받아줄 것. 아래와 같이 두개 를 순서대로 닫아주어야 함.
#즉 cur을 먼저 닫고 dbConn을 닫아야 함. 왜냐하면 dbConn을 만들고 그 안에 cur을 만들었으니
cur.close()
dbConn.close()

# 이상을 실행시키면 튜플구조로 결과물이 옴. 튜플 안에 튜틀이 있는 형태로 옴. Null 값이 파이썬에서는 None값.
# 파이썬에 가져온 것을 예쁘게 찍히게 하려면.
# 크롤링한 데이터를 db에 저장하고 저장한 것을 분석할 수 있는 단계까지 실습.





















