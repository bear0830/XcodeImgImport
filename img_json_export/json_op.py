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
import csv

#默认输入的图片存放在当前路径input目录下
path = "input"
#默认输出位置存放在当前路径output目录下
output_path = "output"
imgslist = glob.glob(path+'/*.*')
#默认输出为png格式
#format = "png"

#基本json操作 练习用
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
		
#先读取模板json
#然后从当前目录读取csv, 获取图像文件名（P99） 音乐文件名（P99） 曲名等信息（Unravel） 并生成stations_output.json
def export_json_from_csv():


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
	
	#读取csv文件 selected2.csv
	reader = csv.reader(file("selected2.csv", 'rb'))
	for line in reader:
		#if reader.line_num == 0: 
            # 跳过第一行属性名
			#continue
			
		print (line[0]) #P99 文件名与图像名
		print (line[1]) #Unravel 曲名
		print (line[2]) #东京食种 OP 描述
		append_obj = copy.deepcopy(template_obj)
		append_obj["name"] = line[1]
		append_obj["streamURL"] = line[0] + ".mp3"
		append_obj["imageURL"] = line[0]
		append_obj["desc"] = line[2]
		append_obj["longDesc"] = ""
		lj["station"].append(append_obj)

		
	#将python对象直接通过 dump方法  输出json到文件
	with open("stations_output.json",'w') as fp:
		json.dump(lj,fp)
		

#从文件中读取json作为模板, 并根据模板生成新的json 为其赋值 输出到文本中
#文件名取自input目录下的图片文件名
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
	#export_json()
	export_json_from_csv()