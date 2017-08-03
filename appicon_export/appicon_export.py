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

#imglist1 存放AppIcon尺寸数组 一般处理一个AppIcon就可以了
imgslist1 = glob.glob(path+'/AppIcon.*')

#存放AppIcon尺寸数组 (width,height)
size_list1 = [ (167,167),(152,152),(120,120),(80,80),(16,16),(164,164),(20,20),(29,29),(30,30),(32,32),(40,40),(50,50),(57,57),(58,58),(60,60),(64,64),(72,72),(76,76),(88,88),(87,87),(100,100),(80,80),(180,180),(114,114),(120,120),(128,128),(144,144)]
#存放LaunchImage尺寸数组 (width,height)
size_list2 = [ (2048,2732),(1242,2208),(450,300),(167,167),(152,152),(120,120),(80,80),(16,16),(367,653),(164,164),(476,653),(20,20),(29,29),(30,30),(32,32),(40,40),(50,50),(57,57),(58,58),(60,60),(64,64),(72,72),(76,76),(88,88),(87,87),(100,100),(80,80),(180,180),(114,114),(120,120),(128,128),(144,144),(320,320),(512,512),(640,640),(1024,1024)]


#data1为python对象 完全按照Xcode AppIcon的Contents.json生成
data1 = {
		  "images" : [
			{
			  "idiom" : "iphone",
			  "size" : "20x20",
			  "scale" : "2x"
			},
			{
			  "idiom" : "iphone",
			  "size" : "20x20",
			  "scale" : "3x"
			},
			{
			  "size" : "29x29",
			  "idiom" : "iphone",
			  "filename" : "appicon_animenz 58x58.png",
			  "scale" : "2x"
			},
			{
			  "size" : "29x29",
			  "idiom" : "iphone",
			  "filename" : "appicon_animenz 87x87.png",
			  "scale" : "3x"
			},
			{
			  "size" : "40x40",
			  "idiom" : "iphone",
			  "filename" : "Icon-40@2x.png",
			  "scale" : "2x"
			},
			{
			  "size" : "40x40",
			  "idiom" : "iphone",
			  "filename" : "Icon-40@3x.png",
			  "scale" : "3x"
			},
			{
			  "size" : "60x60",
			  "idiom" : "iphone",
			  "filename" : "appicon_animenz 120x120.png",
			  "scale" : "2x"
			},
			{
			  "size" : "60x60",
			  "idiom" : "iphone",
			  "filename" : "appicon_animenz 180x180.png",
			  "scale" : "3x"
			},
			{
			  "idiom" : "ipad",
			  "size" : "20x20",
			  "scale" : "1x"
			},
			{
			  "idiom" : "ipad",
			  "size" : "20x20",
			  "scale" : "2x"
			},
			{
			  "size" : "29x29",
			  "idiom" : "ipad",
			  "filename" : "Icon-29.png",
			  "scale" : "1x"
			},
			{
			  "size" : "29x29",
			  "idiom" : "ipad",
			  "filename" : "Icon-29@2x-1.png",
			  "scale" : "2x"
			},
			{
			  "size" : "40x40",
			  "idiom" : "ipad",
			  "filename" : "Icon-40.png",
			  "scale" : "1x"
			},
			{
			  "size" : "40x40",
			  "idiom" : "ipad",
			  "filename" : "Icon-40@2x-1.png",
			  "scale" : "2x"
			},
			{
			  "size" : "76x76",
			  "idiom" : "ipad",
			  "filename" : "Icon-76.png",
			  "scale" : "1x"
			},
			{
			  "size" : "76x76",
			  "idiom" : "ipad",
			  "filename" : "Icon-76@2x.png",
			  "scale" : "2x"
			},
			{
			  "idiom" : "ipad",
			  "size" : "83.5x83.5",
			  "scale" : "2x"
			}
		  ],
		  "info" : {
			"version" : 1,
			"author" : "xcode"
		  }
		}


#默认输出为png格式
format = "png"

#width =size_list[0][0]
#height = size_list[0][1]
#print width
#print height


#由输入图片批量输出不同尺寸的图片,并配套生成Contents.json 和AppIcon.imageset目录
def get_imageset():

	for imgs in imgslist1:
		#split分解为路径+文件名
		imgspath, filename = os.path.split(imgs)
		#splitext分解为文件+后缀名
		name, ext = os.path.splitext(filename)
		print name
		#在输出目录下，创建imageset目录
		out_imageset =  output_path+"/"+ name + ".imageset"
		if(not os.path.exists(out_imageset)):
			os.mkdir(out_imageset)
			
	
	#将python对象直接通过 dump方法  输出json到文件
	with open(out_imageset + "/" + "Contents.json",'w') as fp:
		json.dump(data1,fp)
			
	
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
	print "done" 

if __name__ == '__main__':
	get_imageset()
	