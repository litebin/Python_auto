#coding:utf-8
import codecs
def get_webinfo(path):
	web_info = {}
	#config = open(path)
	config = codecs.open(path, 'r', 'utf-8')
	for line in config:
		result = [ele.strip() for  ele in line.split('=')]
		web_info.update(dict([result]))
	return web_info

def get_userinfo(path):
        user_info = {}
	#config = open(path)
        config = codecs.open(path, 'r', 'utf-8')
        for line in config:
                result2 = [ele.strip() for  ele in line.split('=')]
                user_info.update(dict([result2]))
        return user_info
if __name__ == '__main__':
    info = get_webinfo(r'C:\Users\Administrator\Desktop\python脚本\webinfo.txt')
    user = get_userinfo(r'C:\Users\Administrator\Desktop\python脚本\userinfo.txt')
    for key in info:
        print(key,info[key])
    for value in user:
            print (value,user[value])
