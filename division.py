import cv2
import numpy as np
from matplotlib import pyplot as plt


def pixel_divisiontext (image1, image2):
	img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
	img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
	imageOut = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

	img1 = img1.astype(int)
	img2 = img2.astype(int)

	img2.shape = img1.shape #Adecuamos los tamaños de Ambos archivos para que sean iguales

	alto1,ancho1 = img1.shape
	alto2,ancho2 = img2.shape
	alto3, ancho3 = imageOut.shape

	c = 100
	for x in range(alto1):
			for y in range(ancho1):
				imageOut[x][y] = int((img1[x][y] / img2[x][y])*c)

	imaMin =np.min(imageOut)
	imaMax =np.max(imageOut)
	newMin =0
	newMax =255
	plt.imshow(imageOut)
	def escalar(pixel):
		return (pixel - imaMin)*((newMax - newMin)/(imaMax - imaMin) + newMin)
	

	for x in range(alto3):
		for y in range(ancho3):
			imageOut[x][y] = escalar(imageOut[x][y])

	############### Thresholding ################
	result = img1

	for x in range(alto3):
		for y in range(ancho3):
			if (10 < imageOut[x][y] and imageOut[x][y] < 150):
				result[x,y]=0
			else:
				result[x,y]=255


	return result

imagen1 = cv2.imread("paper6.jpg")
imagen2 = cv2.imread("paper7.jpg")
imagen2=cv2.resize(imagen2 , (1482 , 829))
imagen1=cv2.resize(imagen1 , (1482 , 829))
result = pixel_divisiontext(imagen1, imagen2)
cv2.imwrite("8ejer2.png", result)
cv2.waitKey(0)