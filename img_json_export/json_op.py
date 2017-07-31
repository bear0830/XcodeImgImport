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



#path = raw_input("path:")
#width =int(raw_input("the width U want:"))
#imgslist = glob.glob(path+'/*.*')
#format = raw_input("format:")

#默认输入的图片存放在当前路径input目录下
path = "input"
#默认输出位置存放在当前路径output目录下
output_path = "output"
#imgslist = glob.glob(path+'/*.*')
#默认输出为png格式
#format = "png"

#存放尺寸数组 (width,height)
#size_list = [(450,300),(120,120),(80,80),(16,16),(367,653),(164,164),(476,653),(20,20),(29,29),(30,30),(32,32),(40,40),(50,50),(57,57),(58,58),(60,60),(64,64),(72,72),(88,88),(100,100),(114,114),(120,120),(128,128),(144,144),(320,320),(512,512),(640,640),(1024,1024)]
#width =size_list[0][0]
#height = size_list[0][1]
#print width
#print height


#由1个输入图片批量输出不同尺寸的图片
def resize_img():
	for imgs in imgslist:
		#split分解为路径+文件名
		imgspath, filename = os.path.split(imgs)
		#splitext分解为文件+后缀名
		name, ext = os.path.splitext(filename)
		print name
		img = Image.open(imgs)
		(x,y) = img.size
		
		for size in size_list:
			output_img =img.resize((size[0],size[1]),Image.ANTIALIAS)
			output_img.save(output_path +"/"+ name + " "+ str(size[0]) +"x" + str(size[1]) + "."+format)
	print "done"

if __name__ == '__main__':
	#resize_img()
	json_op()