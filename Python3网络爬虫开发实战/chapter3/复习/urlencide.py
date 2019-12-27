from urllib.parse import urlencode

dic = {'name': 'zhangsan', 'age': 18}

print(type(urlencode(dic)), urlencode(dic), sep='\n')
