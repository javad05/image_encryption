from PIL import Image
import os

path = f"inp/{os.listdir("inp")[0]}"
img = Image.open(path)
(w,h)=(img.size)
#print(w,h)
print(f"opened file name: {img.filename.split('/')[-1]}")

text = ""

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
    
try:
    brk = False
    for i in range(0,w,10):
        for j in range(0,h,10):
            pixel = img.getpixel((i,j))
            ch = chr(pixel[0])
            if ch == '~':
                brk = True
                break            
            text += ch
        if brk:
            break
    print("deserialize was successfull!")
    print(text)
except Exception as e:
    print(f"can't deserialize! e: {e}")
    
        