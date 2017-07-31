# -*- coding:utf-8 -*- 

'''

自动生成 Xcode的 imageasset
生成后直接复制到Xcode  imageasset 目录即可
'''

import os, glob
import json




#path = raw_input("path:")
#width =int(raw_input("the width U want:"))
#imgslist = glob.glob(path+'/*.*')
#format = raw_input("format:")

#默认输入的图片存放在当前路径input目录下
path = "input"
#默认输出位置存放在当前路径output目录下
output_path = "output"
imgslist = glob.glob(path+'/*.*')
#默认输出为png格式
format = "png"

#存放尺寸数组 (width,height)
size_list = [(450,300),(120,120),(80,80),(16,16),(367,653),(164,164),(476,653),(20,20),(29,29),(30,30),(32,32),(40,40),(50,50),(57,57),(58,58),(60,60),(64,64),(72,72),(88,88),(100,100),(114,114),(120,120),(128,128),(144,144),(320,320),(512,512),(640,640),(1024,1024)]
#width =size_list[0][0]
#height = size_list[0][1]
#print width
#print height

#创建imageaset目录与Contents.json  
def create_img_dir():
	for imgs in imgslist:
		#split分解为路径+文件名
		imgspath, filename = os.path.split(imgs)
		#splitext分解为文件+后缀名
		name, ext = os.path.splitext(filename)
		print name
		
		#在输出目录下，创建imageset目录
		out_imageset =  output_path+"/"+ name + ".imageset"
		if(not os.path.exists(out_imageset)):
			os.mkdir(out_imageset)
			
		#data为python对象  filename为读取到的图片文件名，此处只配置1x大小的图片
		#如果没有指定 2x 3x 则留空
		data = {
			"images" : [
				{
				  "idiom" : "universal",
				  "filename" : filename,
				  "scale" : "1x"
				},
				{
				  "idiom" : "universal",
				  "scale" : "2x"
				},
				{
				  "idiom" : "universal",
				  "scale" : "3x"
				}
			  ],
			  "info" : {
				"version" : 1,
				"author" : "xcode"
			  }
			}
		print 'DATA:', repr(data)

		#dumps   python 对象转换为 json string
		data_string = json.dumps(data)
		#print 'JSON:', data_string
		
		#原图片文件复制到 输出目录out_imageset下 
		open(out_imageset + "/" + filename, "wb").write(open(imgspath +"/"+ filename, "rb").read())
		
		#将python对象直接通过 dump方法  输出json到文件
		with open(out_imageset + "/" + "Contents.json",'w') as fp:
			json.dump(data,fp)


if __name__ == '__main__':
	#resize_img()
	create_img_dir()
	print "done"