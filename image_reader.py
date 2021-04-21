from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random


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

#生成识别码
def rand_char():
    return chr(random.randint(65,90))

def rand_color():
    return random.randint(125, 255)

def rand_color2():
    return random.randint(32, 127)

img = Image.new('RGB',(60*4, 60), (255,255,255))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', size=28)

for i in range(60 * 4):
    for j in range(60):
        draw.point((i,j), (rand_color(), rand_color(), rand_color()))

for i in range(4):
    draw.text((i*60 + 10, 10), rand_char(), fill=(rand_color2(), rand_color2(), rand_color2()), font=font)

img = img.filter(ImageFilter.BLUR)
img.show()
