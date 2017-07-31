# -*- coding:utf-8 -*- 

'''

json 基本操作
读取input目录下的图片文件
读取stations.json作为json模板
输出stations_output.json 作为新的json文件 （填入图片文件名等信息）
'''
import os, glob
import json
import copy

#默认输入的图片存放在当前路径input目录下
path = "input"
#默认输出位置存放在当前路径output目录下
output_path = "output"
imgslist = glob.glob(path+'/*.*')
#默认输出为png格式
format = "png"

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
		

#从文件中读取json作为模板, 并根据模板生成新的json 为其赋值 输出到文本中
def export_json():
	#读取作为模板的json
	with open('stations.json',"r") as fp:
		#lj means loaded json
		lj = json.load(fp)
		#print lj
		print lj["station"][0]["name"]
		print lj["station"][0]["streamURL"]
		print lj["station"][0]["imageURL"]
		print lj["station"][0]["desc"]
		print lj["station"][0]["longDesc"]
	
	#清空原有json
	template_obj =  lj["station"].pop()
	lj["station"] = []
	
	
	#读取input目录下的图像文件
	for imgs in imgslist:
		#split分解为路径+文件名
		imgspath, filename = os.path.split(imgs)
		#splitext分解为文件+后缀名
		name, ext = os.path.splitext(filename)
		print name
		#print i
		append_obj = copy.deepcopy(template_obj)
		append_obj["name"] = name
		append_obj["streamURL"] = name + ".mp3"
		append_obj["imageURL"] = name
		append_obj["desc"] = ""
		append_obj["longDesc"] = ""
		lj["station"].append(append_obj)

		
	#将python对象直接通过 dump方法  输出json到文件
	with open("stations_output.json",'w') as fp:
		json.dump(lj,fp)
		


if __name__ == '__main__':
	#json_op()
	export_json()