# -*- coding:utf-8 -*- 

'''

必须安装PIL库

自动生成Xcode图标和启动画面所需要的AppIcon与LaunchImage
输入 input 目录下放置 AppIcon.png（或jpg） LaunchImage.png（或jpg）
输出 output目录下 AppIcon.imageset 目录，内含转换好尺寸的图片和Contents.json
在Finder中将输出内容直接复制到Xcode对应的图片资源位置，即可在Xcode中看到更新的图片资源

默认输出为png格式
'''

import os, glob
from PIL import Image
import json


#path = raw_input("path:")
#width =int(raw_input("the width U want:"))
#imgslist = glob.glob(path+'/*.*')
#format = raw_input("format:")

#默认输入的图片存放在当前路径input目录下
path = "input"
#默认输出位置存放在当前路径output目录下
output_path = "output"

#imglist1 存放AppIcon应用图标文件 一般处理一个AppIcon就可以了
imgslist1 = glob.glob(path+'/AppIcon.*')

#imglist2 存放LaunchImage启动画面图片文件 一般处理一个AppIcon就可以了
imgslist2 = glob.glob(path+'/LaunchImage.*')

#存放AppIcon尺寸数组 (width,height)
size_list1 = [ (1024,1024),(167,167),(152,152),(120,120),(80,80),(16,16),(164,164),(20,20),(29,29),(30,30),(32,32),(40,40),(50,50),(57,57),(58,58),(60,60),(64,64),(72,72),(76,76),(88,88),(87,87),(100,100),(80,80),(180,180),(114,114),(120,120),(128,128),(144,144)]
#存放LaunchImage尺寸数组 (width,height)
size_list2 = [ (2048,2732),(1242,2208),(750,1334),(640,960),(640,1136)]


#f1 当前目录下 完全按照Xcode AppIcon的Contents.json生成的模板文件，不用修改，直接复制
f1 = "Contents.json" 

#f1 当前目录下 完全按照Xcode LaunchImage的Contents.json生成的模板文件，不用修改，直接复制
f2 = "Contents 2.json"



#默认输出为png格式
format = "png"

#width =size_list[0][0]
#height = size_list[0][1]
#print width
#print height


#由输入图片批量输出不同尺寸的图片,并配套生成Contents.json 和AppIcon.imageset目录
def get_imageset():

	#imglist1中只存放一个AppIcon
	for imgs in imgslist1:
		#split分解为路径+文件名
		imgspath, filename = os.path.split(imgs)
		#splitext分解为文件+后缀名
		name, ext = os.path.splitext(filename)
		print name
		#在输出目录下，创建imageset目录
		out_imageset =  output_path+"/"+ name + ".appiconset"
		if(not os.path.exists(out_imageset)):
			os.mkdir(out_imageset)
			
	#AppIcon对应的 Content.json 复制到 输出目录out_imageset下 
	open(out_imageset + "/" + "Contents.json", "wb").write(open(f1, "rb").read())

	
	#将python对象直接通过 dump方法  输出json到文件
	#with open(out_imageset + "/" + "Contents.json",'w') as fp:
		#json.dump(data1,fp)
			
	
	for imgs in imgslist1:
		#split分解为路径+文件名
		imgspath, filename = os.path.split(imgs)
		#splitext分解为文件+后缀名
		name, ext = os.path.splitext(filename)
		print name
		img = Image.open(imgs)
		(x,y) = img.size
		
		for size in size_list1:
			output_img =img.resize((size[0],size[1]),Image.ANTIALIAS)
			output_img.save(out_imageset +"/"+ name + " "+ str(size[0]) +"x" + str(size[1]) + "."+format)
			
			#由于存在多个 40x40 120x120 的图片 冗余生成2份  40x40-1.png 40x40-2.png图片文件
			output_img.save(out_imageset +"/"+ name + " "+ str(size[0]) +"x" + str(size[1]) + "-1."+format)
			output_img.save(out_imageset +"/"+ name + " "+ str(size[0]) +"x" + str(size[1]) + "-2."+format)
			
	#AppIcon处理结束############################################
	
	
	#以下是LaunchImage处理
	#imglist2中只存放一个LaunchImage
	for imgs in imgslist2:
		#split分解为路径+文件名
		imgspath, filename = os.path.split(imgs)
		#splitext分解为文件+后缀名
		name, ext = os.path.splitext(filename)
		print name
		#在输出目录下，创建imageset目录
		out_imageset =  output_path+"/"+ name + ".launchimage"
		if(not os.path.exists(out_imageset)):
			os.mkdir(out_imageset)	
			
	#LaunchImage 对应的 Content 2.json 复制到 输出目录out_imageset下 重命名为 Contents.json
	open(out_imageset + "/" + "Contents.json", "wb").write(open(f2, "rb").read())		
	
	for imgs in imgslist2:
		#split分解为路径+文件名
		imgspath, filename = os.path.split(imgs)
		#splitext分解为文件+后缀名
		name, ext = os.path.splitext(filename)
		print name
		img = Image.open(imgs)
		(x,y) = img.size
		
		for size in size_list2:
			output_img =img.resize((size[0],size[1]),Image.ANTIALIAS)
			output_img.save(out_imageset +"/"+ name + " "+ str(size[0]) +"x" + str(size[1]) + "."+format)
			
			
	print "done" 

if __name__ == '__main__':
	get_imageset()
	
