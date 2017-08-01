# -*- coding:utf-8 -*- 

'''

csv 基本操作
读取当前目录下的csv文件
animenz.csv
selected2.csv
'''
import os, glob
import json
import csv

#默认输入的图片存放在当前路径input目录下
#path = "input"
#默认输出位置存放在当前路径output目录下
#output_path = "output"
#imgslist = glob.glob(path+'/*.*')
#默认输出为png格式
#format = "png"


#从文件中读取json作为模板, 并根据模板生成新的json 为其赋值 输出到文本中
def read_csv():
	#读取csv
	reader = csv.reader(file("selected2.csv", 'rb'))
	for line in reader:
		#if reader.line_num == 0: 
            # 跳过第一行属性名
			#continue
			
		print (line[0])
		print (line[1])
		print (line[2])
	
		


if __name__ == '__main__':
	read_csv()