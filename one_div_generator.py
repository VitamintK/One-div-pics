from PIL import Image
im = Image.open("demo.jpg")
width, height = im.size
print(width, height)
pix = im.load()
box_shadows=[]
#iterate through each pixel of the image, and append a string.
#The string is a css rule for a box shadow at the position x,y, with the color of the pixel.
for y in range(height):
    for x in range(width):
        box_shadows.append('{x}px {y}px 0 0 rgb{rgb}'.format(x=x,y=y,rgb=pix[x,y]))
box_shadows = ','.join(box_shadows)

css = """div#pic{{
    display:inline-block;
    height:{height}px;
    width:{width}px;
}}
div#pic::after{{
    display:block;
    position:relative;
    content:'';
    height:1px;
    width:1px;
    box-shadow: {box_shadows};
}}""".format(height=height, width = width, box_shadows = box_shadows)
with open('onediv.css', 'w') as f:
    f.write(css)
