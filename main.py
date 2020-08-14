from PIL import Image, ImageDraw, ImageFont
def desain(img,widthImage,heightImage):
    kata='“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.”'
    kata2=''
    x=0
    fonMax=[]
    draw=ImageDraw.Draw(img)
    font=ImageFont.truetype('./amertha.ttf',int(widthImage/28))
    print('luas : %s'%(widthImage*heightImage))
    print('quotes : %s'%(kata))
    maksWidthText=widthImage
    for i in kata:
        dra=draw.textsize(i, font)
        fonMax.append(dra[1])
        if x > maksWidthText:
            kata2+='\n%s'%(i)
            x=0
        else:
            kata2+=i
        x+=dra[0]
    print((x, maksWidthText))
    FM=max(fonMax)
    heightFm=0
    arr=kata2.split('\n')
    arr.append('')
    arr.append('')
    arr.append('#krypton')
    for i in arr:
        length=draw.textsize(i, font)
        width=(widthImage/2)-(length[0]/2)
        height=(heightImage/3)-(length[1]/2)
        heightFm+=FM/3
        draw.text((width, height+heightFm), i, align='center', font=font, fill=(204,100,204))
        print((width, height))
    img.save('main.jpg')
#img=Image.open('pil.jpg')
#x=1000
#y=500
#desain(Image.new('RGB',(x,y),color=(255,255,255)),x,y)
    