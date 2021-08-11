import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy
import scipy.ndimage as ndimage
import time
import cv2
from PIL import Image

# Create an Image object from an Image
colorImage  = Image.open("test1.jpg")

# Rotate it by 45 degrees
rotated     = colorImage.rotate(20)

# Display the Original Image
colorImage.show()

# Display the Image rotated by 45 degrees
rotated.show()
