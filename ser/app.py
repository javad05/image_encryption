from PIL import Image
import os

path = f"inp/{os.listdir("inp")[0]}"
img = Image.open(path)
(w,h)=(img.size)
#print(w,h)
print(f"opened file name: {img.filename.split('/')[-1]}")



print("enter your text(don't use '~' charechter!):")
text = iter(input() + '~')


'''
print("inp:")
b =False
for i in range(0,w,10):
    for j in range(0,h,10):
        print(i,j)
        pixel = img.getpixel((i,j))
        print(pixel)
        if j == 100:
            b = True
            break
    if b:
        break
'''
brk = False
for i in range(0,w,10):
    for j in range(0,h,10):
        pixel = img.getpixel((i,j))
        try:
            img.putpixel((i,j),(ord(next(text)),pixel[1],pixel[2]))
        except:
            brk = True
            break
    if brk:
        break
          
    '''
print("out:")
b =False
for i in range(0,w,10):
    for j in range(0,h,10):
        print(i,j)
        pixel = img.getpixel((i,j))
        print(pixel)
        if j == 100:
            b = True
            break
    if b:
        break
'''


try: 
    a = next(text)
    print("the image is so small")
except:
    print("serialize was successfull!")
    
    try:
        file_name = img.filename.split('/')[-1].split('.')[-2]
        
        img.save(f"out/{file_name}.PNG")
        # img.save(f"out/{img.filename.split('/')[-1]}")
        print("new image saved in 'out' folder")
    except Exception as e:
        print(f"failed to save image: {e}")
        