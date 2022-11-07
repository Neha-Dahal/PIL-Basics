from PIL import Image, ImageEnhance
#image import
image=Image.open('picture.jpg')

#create an enhancer
color_enhancer=ImageEnhance.Color(image) #vibrance
contrast_enhancer=ImageEnhance.Contrast(image) #contrast
brightness_enhancer=ImageEnhance.Brightness(image) #brightness
sharpness_enhancer=ImageEnhance.Sharpness(image) #sharpness

#applying the enhancer
enhanced_image=color_enhancer.enhance(2)
#for black and white, use 0

enhanced_image2=contrast_enhancer.enhance(2)
enhanced_image3=brightness_enhancer.enhance(2)
enhanced_image4=sharpness_enhancer.enhance(50)



#display
image.show()
enhanced_image.show()
enhanced_image2.show()
enhanced_image3.show()
enhanced_image4.show()


