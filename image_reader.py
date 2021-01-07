from PIL import Image, ImageFilter


img = Image.open("./dog-cycle-car.png")
print(type(img))
print(img.size)

w, h = img.size

#缩放
img.thumbnail((w / 2, h / 2))
img.save("img_scale.png")

img = Image.open("./dog-cycle-car.png")

#裁剪
crop = img.crop((100, 100, 200, 200))
crop.save("img_crop.png")

#模糊
blur = img.filter(ImageFilter.BLUR)
blur.save("img_blur.png")
