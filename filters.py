from PIL import Image,ImageFilter
#image import
image=Image.open('picture.jpg')

#basic filters
image_blur=image.filter(ImageFilter.BLUR) #fixed blur amount
image_emboss=image.filter(ImageFilter.EMBOSS) #and many such more

#multiband filters
image_boxblur=image.filter(ImageFilter.BoxBlur(radius=20))
image_gaussblur=image.filter(ImageFilter.GaussianBlur(radius=4))
image_unsharp=image.filter(ImageFilter.UnsharpMask(radius=10))

#combine filters
image_embossed=image.filter(ImageFilter.EMBOSS) 
image_emboss_unsharp=image_embossed.filter(ImageFilter.UnsharpMask(radius=10))


#display
image.show()
image_blur.show()
image_emboss.show()
image_boxblur.show()
image_gaussblur.show()
image_unsharp.show()
image_emboss_unsharp.show()