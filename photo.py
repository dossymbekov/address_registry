import base64

image_b = open('bl.txt', 'r')
image = open('image.png', 'wb')

s = image_b.read()
image.write(base64.decodestring(s))
