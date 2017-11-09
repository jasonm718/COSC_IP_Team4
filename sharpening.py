import cv2
import numpy as np

class sharpening:
	
	inp_image = None
	blur_image = None
	filter = None


	"""docstring for Sharpening"""
	def __init__(self, input_image, blurred_img, mask):

		self.inp_image  = input_image
		self.blur_image = blurred_img

		if mask == 'mask1':
			self.filter = self.get_mask1
		elif mask == 'mask2':
			self.filter = self.get_mask2
		elif mask == 'mask3':
			self.filter = self.get_mask3
		elif mask == 'mask4':
			self.filter = self.get_mask4
		elif mask == 'sobelX':
			self.filter = self.get_sobelX
		elif mask == 'sobelY':
			self.filter = self.get_sobelY	

	def get_mask1(self, image):
		kernel = np.array([[0,1,0], [1,-4,1], [0,1,0]])
		image = cv2.filter2D(self.blur_image, -1, kernel)
		return image
	def get_mask2(self, image):
		kernel = np.array([[1,1,1], [1,-8,1], [1,1,1]])
		image = cv2.filter2D(self.blur_image, -1, kernel)
		return image	
	def get_mask3(self, image):
		kernel = np.array([[0,-1,0], [-1,4,-1], [0,-1,0]])
		image = cv2.filter2D(self.blur_image, -1, kernel)
		return image	
	def get_mask4(self, image):
		kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
		image = cv2.filter2D(self.blur_image, -1, kernel)
		return image

	def get_sobelX(self, image):
		image = cv2.Sobel(self.blur_image,cv2.CV_64F,1,0,ksize=5)
		image = np.uint8(np.log(np.abs(image)))		
		return image
	def get_sobelY(self, image):
		image = cv2.Sobel(self.blur_image,cv2.CV_64F,0,1,ksize=5)
		image = np.uint8(np.log(np.abs(image)))		
		return image

	def post_process_image(self, image):
   
		x = image.shape[0]
		y = image.shape[1]

		min = image.min()
		max = image.max()

		for i in range(1,x):
			for j in range(1,y):
				image[i,j] = ((image[i,j] - min)/(max-min))*255

		return image

	def sharpening(self):
		
		img = self.filter(blurred_img)
		
		return img

#CODE TO RUN INDIVIDUALLY
#TYPE IN  "python sharpening.py"
input_image = cv2.imread("house.jpg", 0)
#blur the image using gaus
#blurred_img = cv2.GaussianBlur(input_image,(3,3),0)
# blur the image using median
blurred_img = cv2.medianBlur(input_image,3) 

app = sharpening(input_image,blurred_img, "sobelX")
masked_image = app.sharpening()
sharp_image =  input_image - masked_image
cv2.imwrite("blurred.jpg", blurred_img)
cv2.imwrite("masked.jpg", masked_image)
cv2.imwrite("sharp.jpg", sharp_image)
