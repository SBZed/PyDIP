#!usr/bin/Python3
# Pythonista - Saurabh Zinjad 
# HISTOGRAM EQUALIZATION 

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('./img/hist1.bmp')


# Show Image
cv2.imshow('Image', img)
cv2.waitKey(3000)
cv2.destroyAllWindows()
#Histogram
# unique_pixel = Unique Pixels in Image
# count = Count of each Unique Pixel
unique_pixel, count = np.unique(img, return_counts = True)
print('unique Pixel : \n', unique_pixel, '\n')
print('Length unique Pixel : ', len(unique_pixel), '\n')
print('Count : \n', count, '\n')

print('Pixel with max count : ', unique_pixel[np.where(count == max(count))][0], '\tcount : ', max(count))


#Probability Density Function
pdf = []
for i in range(len(count)):
    pdf.append(count[i]/sum(count))
print('PDF : \n', pdf, '\n')

#Cumulative Density Function
for i in range(1, len(pdf)):
    pdf[i] += pdf[i-1]
print('CDF : \n', pdf, '\n')
pdf = np.around(np.array(pdf)*255).astype(int)
print('Equalized pixel Values : \n',pdf, '\n')

# Plot Histogram 
plt.subplot(1,2,1)
plt.bar(unique_pixel, count)
plt.title('Histogram')
plt.xlabel('Pixel')
plt.ylabel('Count of Pixel')

# Plot Equalized Histogram
plt.subplot(1,2,2)
plt.bar(pdf, count)
plt.title('\n Equalized Histogram')
plt.xlabel('Pixel')
plt.ylabel('Count of Pixel')
plt.show()
cv2.waitKey(0)