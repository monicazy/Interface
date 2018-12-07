# from tools.http_request import HttpRequests
import requests
url1 = "https://www-beta.mycloudhawk.com/api/v1/login"
data1={"username": "cloudhawkadmin@rongrongzhang.com", "password": "123456"}
url2 = "https://www-beta.mycloudhawk.com/api/v1/trackers/9ad3a9f3022d4a4198ce2c3f32ed69e3/asset"
data2={"name":"Chengdu11"}
url3= "https://www-beta.mycloudhawk.com/api/v1/labels/81b18ab5c1194efb84595a0c2f2c5e02"
data3={"color": "#f00081","tids": ["0bd6c9d8406d4cc2ac5d10a09b74979a"]}

res1=requests.post(url1,json=data1)
cookies = res1.cookies
# print(cookies)
res2 = requests.put(url2,json=data2, cookies=cookies)
print("修改终端名",res2.json())
# res3 = requests.put(url3,json=data3, cookies=cookies)
# print("修改标签颜色",res3.json())
