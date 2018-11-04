# Rômulo Ponciano
# 03 Nov 2018
# This script replace all the pixels of a defined color, in an image, for another defined color. E.g. If you want to replace all red pixels with white pixels.

from PIL import Image 

imgPathWithFormat = ''
rgb = (0, 0, 0)
finalColor = (255, 255, 255)
imgOutputPathWithFormat = ''

im = Image.open(imgPathWithFormat)
pixels = list(im.getdata())

idx = 0
for i in pixels:
	if i == rgb:
		pixels[idx] = finalColor
	idx = idx + 1

im2 = Image.new(im.mode, im.size)
im2.putdata(pixels)
im2.save(imgOutputPathWithFormat)
