# 파이썬과 DB연동 실습

import pymysql

dbConn = pymysql.connect(host='localhost', user='root', password='domybest2024@', db='shopdb')
# 파이썬과 mysql간의 connection을 생성해서 변수에 저장
# 다음으로 실행시킬 sql을 만든다.

sql = "INSERT INTO membertbl VALUES ('dragon','다공룡','서울 공릉구')" # 큰 따음표 안에 반드시 작은 따음표로 표기해야 함.

cur = dbConn.cursor()
result = cur.execute(sql)
print(result)  # 이렇게 하면 1이 찍힌다. 아무 에러 없이 성공하면 1을 리턴해줌. 리절트값이 1이면 실행이 성공했다는 의미.
#예를 들어 회원가입할 때 회원가입하고 아무 에러가 없으면 회원가입을 축하합니다.고 표시되는 것이 이렇게 성공했을 때의 표시를 보여주는 것.
# insert, update, delete문이 싱행된 후 성공결과를 반환해줌. ->1이면 성공. 1인 아니면 실패인 것.

if result == 1:
    print("회원 가입이 성공하였습니다.!")

# records = cur.fetchall() # 전부다 가져오라는 명령문. sql문에서 실행된 select문의 결과를 records라는 이름으로 작명해서 받은 것.

cur.close()
dbConn.commit() # insert,delete,update문을 사용한 경우에는 반드시 commit함수를 호출해야 함.!!!!
dbConn.close()

# select문은 db에 변화를 주는 것은 아니지만 그 외의 것은 모두 db의 내용에 변화를 줌. 그래서 commit확정을 시켜주어야 함.
# 파이썬에 가져온 것을 예쁘게 찍히게 하려면.





















