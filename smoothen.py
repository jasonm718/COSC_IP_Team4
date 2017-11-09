import cv2
import numpy as np

class smoothening:
	
	image = None
	filter = None
	size = None


	"""docstring for Smoothening"""
	def __init__(self, size, filter_name, image):

		self.image  = image
		self.size = size

		if filter_name == 'gaussian':
			self.filter = self.get_gaus_img
		elif filter_name == 'averaging_filter':
			self.filter = self.get_avg_img

	def get_gaus_img(self, shape, image):
		"""Will return an image with gau"""
		x = shape[0]
		y = shape[1]

		image = cv2.GaussianBlur(image,shape,0)
		
		return image

	def get_avg_img(self, shape, image):
		"""Will return image with average smoothening"""
		x = shape[0]
		y = shape[1]
		dim = x*y
		kernel = np.ones(shape,np.float32)/dim
		image = cv2.filter2D(image,-1,kernel)

		return image

	def smoothening(self):
		img = self.filter(self.size,self.image)
		return img

#CODE TO RUN INDIVIDUALLY
#TYPE IN  "python smoothen.py"
input_image = cv2.imread("Lenna0.jpg", 0)
app = smoothening((10,10), "averaging_filter", input_image)
output = app.smoothening()
cv2.imwrite("output/blurred.jpg", output)
