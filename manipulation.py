from PIL import Image
#image import
image=Image.open('picture.jpg')

#rotate
image_rotate=image.rotate(60, expand=True)

#flipping
image_flip_horizonatal=image.transpose(Image.FLIP_LEFT_RIGHT)
image_flip_vertical=image.transpose(Image.FLIP_TOP_BOTTOM)

#resize
# image_resize=image.resize((w,h))
#or using scale factor
# scale_factor=2
# new_image_size=(image.size[0]*scale_factor,image.size[1]*scale_factor)
# image_resize=image.resize(new_image_size)

#display
image_rotate.show()
image_flip_horizonatal.show()
image_flip_vertical.show()

