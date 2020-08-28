# 开源超级HSV分析工具
## 功能：  
> 输入图像
>> 允许程序图像动态载入（文件名称和路径不变）

> 依据下限(h,s,v)和上限(H,S,V)二值化图像  

> 将二值化后的边缘在原图上绘制（精确检验数值合理性）

> 依据配置文件设置默认值  
>> 允许动态改变（文件名称和路径不变）
## 使用指南：
> 1,配置hsv.py里的 `img_name`(图像文件) `quick_config_file`(默认值配置文件) 的路径
~~~python
#!/usr/bin/env python3
import cv2 as cv
import numpy as np

img_name = './AB.jpg' # here
quick_config_file = './data.txt' # here
~~~
> 2,运行python文件
~~~bash
$ python3 ./hsv.py
~~~
或者
~~~bash
$ ./hsv.py #非Windows环境，得给hsv.py添加x权限
~~~
## 开发指南：
> 动态调试的过程中只要保证配置文件的文件名称和路径不改变即可