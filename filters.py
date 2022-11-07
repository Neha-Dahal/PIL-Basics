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

#save
image_blur.save('Blurred.jpg')
image_emboss.save('Embossed.jpg')
image_boxblur.save('Boxblur.jpg')
image_gaussblur.save('Gaussblur.jpg')
image_unsharp.save('Unsharp.jpg')
image_emboss_unsharp.save('EmbossAndUnsharp.jpg')

# #display
# image.show()
# image_blur.show()
# image_emboss.show()
# image_boxblur.show()
# image_gaussblur.show()
# image_unsharp.show()
# image_emboss_unsharp.show()