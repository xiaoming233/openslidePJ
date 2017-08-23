# -*- coding: utf-8 -*-


import openslide
import numpy
import matplotlib.pyplot as plt


slide = openslide.OpenSlide(r'pic/boxes.tiff')
level_count = slide.level_count  
print( 'level_count = ',level_count ) 
[m,n] = slide.dimensions #得出高倍下的（宽，高）
print (m,n) 

[m1,n1] = slide.level_dimensions[6] #级别k，且k必须是整数，下采样因子和k有关
print (m1,n1)      # m1 = m/下采样因子 此时k为1
slide_level_downsamples = slide.level_downsamples[6]
print( slide_level_downsamples)
tile = numpy.array(slide.read_region((6400,18000),6, (500,500)))
plt.figure()
plt.imshow(tile)
plt.show()

