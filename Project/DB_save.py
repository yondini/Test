import requests
import json

ID = 2 #아이디값
DATA = 4
data = {"ID":ID,"DATA":DATA}
r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/saveData.php",params = data)
print(r.text)
#값 넣는 코드----------------------------------------
