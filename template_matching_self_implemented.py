import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def show_results(image_result,image_template_result):
    image_result_rgb=cv2.cvtColor(image_result,cv2.COLOR_BGR2RGB)
    plt.imshow(image_result_rgb)
    plt.title('Matching Result')
    plt.show()
    plt.imshow(image_template_result,cmap = 'gray')
    plt.title('Template Result')
    plt.show()

def calculate_sum(x,y,w,h,img):
    result=0
    for i in range(0,w):
        for j in range (0,h):
            result+=int(img[h+y,w+x])
    return result    

def sqdiff_normed_method():
    x=0
    y=0
    img_original_temp=img_original.copy()
    img_result=np.zeros((img_height-height,img_width-width))
    for i in range(0, img_height-height):
        for j in range(0, img_width-width):
            for k in range(0,height):
                for l in range(0,width):
                    img_result[i,j]+=(int(img_template[k,l])-int(img[i+k,j+l]))**2
                    x+=int(img_template[k,l])**2
                    y+=int(img[i+k,j+l])**2
            img_result[i,j]=img_result[i,j]/math.sqrt(x*y)
            x=0
            y=0
    positions=np.where(img_result<=threshold)
    for i in range(0,positions[0].size):
        cv2.rectangle(img_original_temp,(positions[1][i],positions[0][i]),(positions[1][i]+width,positions[0][i]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def ccoeff_normed_method():
    img_original_temp=img_original.copy()
    img_result=np.zeros((img_height-height,img_width-width))
    temp_sum=0
    x=0
    y=0
    for o in range(0,height):
        for m in range(0,width):
            temp_sum+=img_template[o,m]
    for i in range(0, img_height-height):
        for j in range(0, img_width-width):
            c=calculate_sum(j,i,width,height,img)
            for k in range(0,height):
                for l in range(0,width):
                    a=img_template[k,l]-(1/(width*height))*temp_sum
                    x+=a**2
                    b=img[i+k,j+l]-(1/(height*width))*c
                    y+=b**2
                    img_result[i,j]+=int(a)*int(b)
            img_result[i,j]=img_result[i,j]/math.sqrt(x*y)
            if (np.isnan(img_result[i,j])):
                img_result[i,j]=0
            x=0
            y=0
    positions=np.where(img_result>=threshold)
    for i in range(0,positions[0].size):
        cv2.rectangle(img_original_temp,(positions[1][i],positions[0][i]),(positions[1][i]+width,positions[0][i]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def ccorr_normed_method():
    x=0
    y=0
    img_original_temp=img_original.copy()
    img_result=np.zeros((img_height-height,img_width-width))
    for i in range(0, img_height-height):
        for j in range(0, img_width-width):
            for k in range(0,height):
                for l in range(0,width):
                    img_result[i,j]+=(int(img_template[k,l])*int(img[i+k,j+l]))
                    x+=int(img_template[k,l])**2
                    y+=int(img[i+k,j+l])**2
            img_result[i,j]=img_result[i,j]/math.sqrt(x*y)
            x=0
            y=0
    positions=np.where(img_result>=threshold)
    for i in range(0,positions[0].size):
        cv2.rectangle(img_original_temp,(positions[1][i],positions[0][i]),(positions[1][i]+width,positions[0][i]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def sqdiff_method():
    img_original_temp=img_original.copy()
    img_result=np.zeros((img_height-height,img_width-width))
    for i in range(0, img_height-height):
        for j in range(0, img_width-width):
            for k in range(0,height):
                for l in range(0,width):
                    img_result[i,j]+=(int(img_template[k,l])-int(img[i+k,j+l]))**2	
    min_value,max_value,min_location,max_location=cv2.minMaxLoc(img_result)
    cv2.rectangle(img_original_temp,min_location,(min_location[0]+width,min_location[1]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def ccoeff_method():
    img_original_temp=img_original.copy()
    img_result=np.zeros((img_height-height,img_width-width))
    temp_sum=0
    for o in range(0,height):
        for m in range(0,width):
            temp_sum+=img_template[o,m]
    for i in range(0, img_height-height):
        for j in range(0, img_width-width):
            c=calculate_sum(j,i,width,height,img)
            for k in range(0,height):
                for l in range(0,width):
                    a=img_template[k,l]-(1/(width*height))*temp_sum
                    b=img[i+k,j+l]-(1/(height*width))*c
                    img_result[i,j]+=int(a)*int(b)
    min_value,max_value,min_location,max_location=cv2.minMaxLoc(img_result)
    cv2.rectangle(img_original_temp,max_location,(max_location[0]+width,max_location[1]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def ccorr_method():
    img_original_temp=img_original.copy()
    img_result=np.zeros((img_height-height,img_width-width))
    for i in range(0, img_height-height):
        for j in range(0, img_width-width):
            for k in range(0,height):
                for l in range(0,width):
                    img_result[i,j]+=(int(img_template[k,l])*int(img[i+k,j+l]))
    min_value,max_value,min_location,max_location=cv2.minMaxLoc(img_result)
    cv2.rectangle(img_original_temp,max_location,(max_location[0]+width,max_location[1]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

img_name=input("Unesi ime slike:")
img_template_name=input("Unesi ime templatea:")

img_original=cv2.imread(img_name)
img=cv2.imread(img_name,0)
img_template=cv2.imread(img_template_name,0)

height,width=img_template.shape
img_height,img_width=img.shape
method=int(input("Choose a method: \n1.CCOEFF \n2.CCORR \n3.SQDIFF \n4.CCOEFF Normed\n5.CCORR Normed\n6.SQDIFF Normed\n"))
if (method==1):
    ccoeff_method()
elif (method==2):
    ccorr_method()    
elif (method==3):
    sqdiff_method()
elif (method<7):
    threshold=float(input("Input threshold value:"))
    if (method==4):
        ccoeff_normed_method()
    elif (method==5):
        ccorr_normed_method()
    elif (method==6):
        sqdiff_normed_method()

    
