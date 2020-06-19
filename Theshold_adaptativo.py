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
	winsize=11 #tamaño de la subventana para cada pixel
	const=2 #constate


	for i in range(h):
	    for j in range(w):
	    	y0=i-int(winsize/2)
	    	y1=i+int(winsize/2)+1
	    	x0=j-int(winsize/2)
	    	x1=j+int(winsize/2)+1

	    	if y0 < 0:
	    		y0 = 0
	    	if y1 > h: #filas
	    		y1 = h
	    	if x0 < 0:
	    		x0 = 0
	    	if x1 > w:	#columnas
	    		x1 = w
	    	
	    	block =img1[y0:y1, x0:x1]
	    	#print(block)

	    	threshold =np.mean(block)-const # sacamos el promedio de la sub ventana restado por la constante
	    	if img1[i,j]<threshold:
	    		res[i,j]=0
	    	else:
	    		res[i,j]=255


	return res
	#img_result = res #importante
	#full_filename_new = os.path.join(folder, 'Thresholding' + filename) #importante
	#cv2.imwrite(full_filename_new, img_result) #importante

	#return full_filename_new #importante

imagen1 = cv2.imread("paper6.jpg")
#imagen2 = cv2.imread("log_4.png")
result = Thresholding(imagen1)
cv2.imwrite("resThresAdaptativo.png", result)
cv2.waitKey(0)  
