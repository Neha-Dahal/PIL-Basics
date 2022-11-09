from PIL import Image, ImageChops
image1=Image.open('picture.jpg')
image2=Image.open('picture2.png') #bg removed image
image3=Image.open('picture3.jpg')
image4=Image.open('picture3.jpg')

# print(image1.size)
# print(image2.size)
# print(image3.size)
#combination of two
image3.paste(image2,(1300,500),mask=image2)
image3.save('outputs/combined-image.jpg')

def concat_image_horizontal(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def concat_multiple(images_list):
    image=images_list.pop(0)
    for i in images_list:
        image=concat_image_horizontal(image,i)
    return image
concat_multiple([image1,image4,image1]).save('outputs/concatenated-h.jpg')