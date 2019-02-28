import requests
import json

ID = 2 #아이디값
data = {"ID":ID} #request에 params를 보내지 않으면 전체 값을 가져올 수 있음
r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data)
print(r.text)
r.encoding = 'UTF-8'
Data = json.loads(r.text)

print(Data[0]['ID']+" // "+Data[0]['DATA']) #<<첫번째 DB값의 아이디,DATA 출력

#값 넣는 코드----------------------------------------
