# Image-Ident

# Idee: ein Bild als Matrix aus Pixeln als Input. Erste Layer ist eine neue Matrix, die jeden ursprünglichen Pixel (bzw matrix element) 8 weitere, insgesamt 9 elemente zuteilt (rezeptives Feld?) Der Randbereich
#       ist hier die Differenz aus dem Wert des ursprünglichen Pixels mit dem des Pixels x-1 y-1 etc. -> Kantenerkennung
# 
# 




import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

pic = r"C:\Users\Armagetdown\Downloads\Screenshot 2025-05-20 at 19-26-08 depositphotos_118245826-black-and-white-photo-of-sensual-glamour-beautiful-woman-model-lady-with-fresh-daily-makeup-and-clean-healthy-skin-face.jpg (WEBP Image 529 × 600 pixels).png"

img = Image.open(pic)




def create_rf_array(image):

    # gonna be used later on
    valued_list = []

    npdata = np.array(img)

    npdata = (npdata - npdata.min()) / (npdata.max() - npdata.min())

    img_shape = npdata.shape

    rf_array = np.zeros((img_shape[0], img_shape[1], 3, 3))

    for x, row in enumerate(npdata):
        for y, pixel in enumerate(row):

            if pixel != 0: 

                rf_array[x, y][1,1] = npdata[x, y]

                #print(f'{x, y}')

                for i in range(rf_array[x, y].shape[0]):

                    for j in range(rf_array[x, y].shape[1]):
                        
                        d = 1
                        
                        #print(f'pixel loc: {i, j}, adressing npsimple {x+(i-d), y+(j-d)} make pixel value to {0.5*npdata[x+(i-d), y+(j-d)]}')
                        rf_array[x, y][i, j] += 0.5*npdata[x+(i-d), y+(j-d)]

                        
                rf_array[x, y][1,1] = npdata[x, y]
                
                valued_list.append((x, y))

                #print(f'one 3x3: {rf_array[x, y]}')

                #print(f'row: {x} column: {y}')

    print(rf_array)
    #print(valued_list)

    return rf_array


create_rf_array(img)

plt.imshow(create_rf_array(img).transpose(0, 2, 1, 3).reshape(np.array(img).shape[0]*3, np.array(img).shape[1]*3), cmap='gray_r', vmin=0, vmax=1)
plt.axis('off')
plt.show()