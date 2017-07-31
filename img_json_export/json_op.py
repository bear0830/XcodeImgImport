# -*- coding:utf-8 -*- 

'''

json 基本操作
'''
import os, glob
import json

def json_op():
	#data为python对象
	data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
	print 'DATA:', repr(data)

	#dumps   python 对象转换为 json string
	data_string = json.dumps(data)
	print 'JSON:', data_string
	
	#将python对象直接通过 dump方法 输出到文件
	with open('json_op_output.json','w') as fp:
		json.dump(data,fp)


if __name__ == '__main__':
	json_op()