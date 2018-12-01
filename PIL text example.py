from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("sable_antelope.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("GOUDOSI.ttf", 16) #copy and paste ttf font file from 
#C:\Windows\Fonts
draw.text((50, 100),"Sample Text",(0,255,255),font=font)
img.save('sample-out.jpg')