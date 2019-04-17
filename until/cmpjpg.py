#coding=utf-8
# import cv2
# import numpy as np
#均值hash算法无法对比两张图片是否相同
# def aHash(img):
#     #缩放为8*8
#     img=cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
#     #转换为灰度图
#     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     #s为像素和初值为0，hash_str为hash值初值为''
#     s=0
#     hash_str=''
#     #遍历累加求像素和
#     for i in range(8):
#         for j in range(8):
#             s=s+gray[i,j]
#     #求平均灰度
#     avg=s/64
#     #灰度大于平均值为1相反为0生成图片的hash值
#     for i in range(8):
#         for j in range(8):
#             if  gray[i,j]>avg:
#                 hash_str=hash_str+'1'
#             else:
#                 hash_str=hash_str+'0'
#     return hash_str
#
# def cmpHash(hash1,hash2):
#     n=0
#     #hash长度不同则返回-1代表传参出错
#     if len(hash1)!=len(hash2):
#         return -1
#     #遍历判断
#     for i in range(len(hash1)):
#         #不相等则n计数+1，n最终为相似度
#         if hash1[i]!=hash2[i]:
#             n=n+1
#     return n
#
# img1=cv2.imread('1.png')
# img2=cv2.imread('2.png')
# hash1= aHash(img1)
# hash2= aHash(img2)
# print(hash1)
# print(hash2)
# n=cmpHash(hash1,hash2)
# print('均值哈希算法相似度：'+ str(n))

from PIL import Image
from PIL import ImageChops


def compare_images(one, two: object, save_diff_location: object) -> object:
    """
    比较图片，如果有不同则生成展示不同的图片

    @参数一: one: 第一张图片的路径
    @参数二: two: 第二张图片的路径
    @参数三: save_diff_location: 不同图的保存路径
    """
    image_one = Image.open(one)
    image_two = Image.open(two)
    try:
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            # print("【+】We are the same!")
            return 'T'
        else:
            diff.save(save_diff_location)
            # print('图片不一样')
            return 'F'
    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e, text))

# aa='D:\\work\\3DAuto\\snapshot\\选择省份截图.png'
# bb='D:\\work\\3DAuto\\snapshot\\选择城市截图.png'
# if __name__ == '__main__':
#     print(compare_images(aa,bb,'不一样截图.png'))
