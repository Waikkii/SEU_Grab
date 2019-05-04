import requests
import re
import json
import cv2
req = requests.Session()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

response = req.get('http://xk.urp.seu.edu.cn/jw_css/getCheckCode')
codeImg = response.content
fn = open('C:\\Users\\OMEN\\Desktop\\jwc\\code.png', 'wb')
fn.write(codeImg)
fn.close()
pic = cv2.imread('C:\\Users\\OMEN\\Desktop\\jwc\\code.png', 1)
cv2.imshow("code", pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
code =  input("Please intput the code:")
data = {
          'checkCode': code ,
          'userId': 'xxxxxxxxxxxx',
          'userPassword': 'xxxxxxxxxxxxx'
        }
signin = req.post('http://xk.urp.seu.edu.cn/jw_css/system/login.action', data = data, headers = headers)
#info = signin.text
#print (signin.text)
#print (info.find('星期天'))
#print(signin.text)
tag = 1
flag1 = 1
print("运行中")
while tag == 1:
#数据库
    if flag1 == 1:
        getjson = req.post('http://xk.urp.seu.edu.cn/jw_css/xk/runSelectclassSelectionAction.action?select_jxbbh=04030608201820000&select_xkkclx=11&select_jhkcdm=04030608', headers = headers)
        tjson = json.loads(getjson.text)
        if tjson["rso"]["isTjJxbbh"]!= None:
            flag1 = 0
            print("数据库成功")


