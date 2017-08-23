# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import cairosvg
import cv2
from skimage import morphology,feature
impath=r'E:/Python/data/cancer_subset00/2017-06-09_18.08.16.ndpi.16.14788_15256.2048x2048.tiff'
svgpath=r'E:/Python/data/labels/2017-06-09_18.08.16.ndpi.16.14788_15256.2048x2048.svg'


cairosvg.svg2png(bytestring=open(svgpath).read().encode('utf-8'),write_to=r"tmp/output.png")

im=cv2.imread(r"tmp/output.png")
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
contour=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)[1]#二值化

edgs=feature.canny(contour, sigma=3, low_threshold=10, high_threshold=50)#检查边缘
convex_hull = morphology.convex_hull_object(edgs)#填充

fig, axes = plt.subplots(1,3,figsize=(8,8))
ax0, ax1,ax2= axes.ravel()
ax0.imshow(plt.imread(impath))
ax0.set_title('original image')
ax1.imshow(plt.imread(r"tmp/output.png"))
ax1.set_title('label image')
ax2.imshow(convex_hull,plt.cm.gray)
ax2.set_title('convex_hull image')
plt.show()
