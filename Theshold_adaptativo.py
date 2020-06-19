import cv2
import numpy as np


def Thresholding(image1):

	#full_filename = os.path.join(folder, filename)#importante
	#res= cv2.imread(full_filename)#importante
	#img= cv2.imread(full_filename , cv2.IMREAD_GRAYSCALE)

	#img = cv2.imread('thresh2.jpg')
	#gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	#neg=255-gray
	#img = cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
	#cv2.imshow('thresh2', img)
	#cv2.imshow('gray', gray)
	#cv2.imshow('neg',neg)

	img1 = cv2.cvtColor(image1, cv2.cv2.COLOR_BGR2GRAY)

	res = cv2.cvtColor(image1, cv2.cv2.COLOR_BGR2GRAY)

	#img1 = img1.astype(int)
	#img2 = img2.astype(int)


	h, w = img1.shape
	#res = cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
	winsize=3
	const=2
	
	for i in range(h):
	    for j in range(w):
	        if(0 < img1[i][j] and img1[i][j]<=110):
	            res[i][j]=0
	        else:
	            res[i][j]=255

	#cv2.imshow('Sin celulas saludables',gray)

	return res
	#img_result = res #importante
	#full_filename_new = os.path.join(folder, 'Thresholding' + filename) #importante
	#cv2.imwrite(full_filename_new, img_result) #importante

	#return full_filename_new #importante

imagen1 = cv2.imread("paper6.jpg")
#imagen2 = cv2.imread("log_4.png")
result = Thresholding(imagen1)
cv2.imwrite("pruebathres2.png", result)
cv2.waitKey(0)  

#operador_raiz('./img/' , 'thresh2.jpg')

 