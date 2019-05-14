from typing import Any, Union, Tuple
 
import pymysql
 
 
conn = pymysql.connect(host = 'localhost', user = 'root', password = 'password' ,db = '공공데이터')
# host = DB주소(localhost 또는 ip주소), user = DB id, password = DB password, db = DB명
curs = conn.cursor()
 
search=input("검색할것을 입력해주세요")
sql = "SELECT companyko FROM 공공데이터.globalcompany WHERE companyko LIKE '%"+ search + "%' ORDER BY nation ASC"
# 실행 할 쿼리문 입력
curs.execute(sql)
 
# curs.execute(sql) # 쿼리문 실행
conn.commit()
curs.execute(sql)
rows: Union[Tuple, Any] = curs.fetchall() # 데이터 패치
 
cnt=0
 
 
for i in rows :
    cnt= cnt + 1
    print(i)
 
 
print(cnt, "개의 "+search,"을 발견함")
conn.close()
