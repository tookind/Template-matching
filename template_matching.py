import numpy as np
import cv2
import matplotlib.pyplot as plt

def show_results(image_result,image_template_result):
    image_result_rgb=cv2.cvtColor(image_result,cv2.COLOR_BGR2RGB)
    plt.imshow(image_result_rgb)
    plt.title('Matching Result')
    plt.show()
    plt.imshow(image_template_result,cmap = 'gray')
    plt.title('Template Result')
    plt.show()

def sqdiff_normed_method():
    img_original_temp=img_original.copy()
    img_result=cv2.matchTemplate(img,img_template,cv2.TM_SQDIFF_NORMED)
    positions=np.where(img_result<=threshold)
    for i in range(0,positions[0].size):
        cv2.rectangle(img_original_temp,(positions[1][i],positions[0][i]),(positions[1][i]+width,positions[0][i]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def ccoeff_normed_method():
    img_original_temp=img_original.copy()
    img_result=cv2.matchTemplate(img,img_template,cv2.TM_CCOEFF_NORMED)
    positions=np.where(img_result>=threshold)
    for i in range(0,positions[0].size):
        cv2.rectangle(img_original_temp,(positions[1][i],positions[0][i]),(positions[1][i]+width,positions[0][i]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def ccorr_normed_method():
    img_original_temp=img_original.copy()
    img_result=cv2.matchTemplate(img,img_template,cv2.TM_CCORR_NORMED)
    positions=np.where(img_result>=threshold)
    for i in range(0,positions[0].size):
        cv2.rectangle(img_original_temp,(positions[1][i],positions[0][i]),(positions[1][i]+width,positions[0][i]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def sqdiff_method():
    img_original_temp=img_original.copy()
    img_result=cv2.matchTemplate(img,img_template,cv2.TM_SQDIFF)
    min_value,max_value,min_location,max_location=cv2.minMaxLoc(img_result)
    cv2.rectangle(img_original_temp,min_location,(min_location[0]+width,min_location[1]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def ccoeff_method():
    img_original_temp=img_original.copy()
    img_result=cv2.matchTemplate(img,img_template,cv2.TM_CCOEFF)
    min_value,max_value,min_location,max_location=cv2.minMaxLoc(img_result)
    cv2.rectangle(img_original_temp,max_location,(max_location[0]+width,max_location[1]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

def ccorr_method():
    img_original_temp=img_original.copy()
    img_result=cv2.matchTemplate(img,img_template,cv2.TM_CCORR)
    min_value,max_value,min_location,max_location=cv2.minMaxLoc(img_result)
    cv2.rectangle(img_original_temp,max_location,(max_location[0]+width,max_location[1]+height),(0,255,0),2)
    show_results(img_original_temp,img_result)

img_name=input("Unesi ime slike:")
img_template_name=input("Unesi ime templatea:")

img_original=cv2.imread(img_name)
img=cv2.imread(img_name,0)
img_template=cv2.imread(img_template_name,0)

height,width=img_template.shape
threshold=0.9
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

    
