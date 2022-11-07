from PIL import Image
#create new image by import
image=Image.open('picture.jpg')

#alternative way to import
# with Image.open('picture.jpg')as image:
#     image.show()
#show the picture
image.show()
print(image.filename)