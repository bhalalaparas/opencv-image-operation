import cv2
import numpy as np
import time

dict_1 = {1:'click your photo',2:'Binary image',3:'blue',4:'red',5:'blurring the image',6:'green',7:'gray scale image'}

for i in range(1,len(dict_1)+1):
    print(i ,':',dict_1.get(i))
    
while(True):
  
    num = int(input("enter the number which type of image you want"))
      
    if num ==1:
        print("when you want click photo then press 'q' button ")    
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while(True):
            ret, img1 = cap.read()
            cv2.imshow('frame',img1)          
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()  
        cv2.destroyAllWindows()          
                 
    else:
        #print('ok')
    
    
        if num > 1 and num < 8 :
            path = input("Enter the path of file")
            img = cv2.imread(path,1)
            cv2.imshow('image',img)
            height = img.shape[0]
            width = img.shape[1]
    
            if num == 2:
                ret, img1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
                cv2.imshow('binary imge',img1)
    
            elif num =='3':
                print("3")
                B,G,R = cv2.split(img)
                zeros = np.zeros((height,width),dtype='uint8')
                cv2.imshow("blue",cv2.merge([B,zeros,zeros]))
                img1 = cv2.merge([B,zeros,zeros])
    
            elif num =='4':
                B,G,R = cv2.split(img)
                zeros = np.zeros((height,width),dtype='uint8')
                cv2.imshow("red",cv2.merge([zeros,zeros,R]))
                img1 = cv2.merge([zeros,zeros,R])        

            elif num =='5':
                gaussian = cv2.GaussianBlur(img,(7,7),0)
                cv2.imshow('Gaussian image',gaussian)
                img1 = gaussian
        
            elif num =='6':
                B,G,R=cv2.split(img)
                zeros=np.zeros((height,width),dtype="uint8")
                cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
                img1=cv2.merge([zeros,G,zeros])
            
            elif num =='7':
                g_img = cv2.imread(path,0)
                cv2.imshow('gray scale image:',g_img)
            
        else:
            print('invalid input') 
   
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    save = input('if you want save image(y/n)')
    if save == 'y':
        file = input('Enter the image name to be saved')
        cv2.imwrite(file+'.jpg',img1)
    elif save =='n':
        print("it's ok")
    else:
        print("invalid input")
     
    a =  input("Do you break(y/n)?")
    if a=='y':
        break
    elif a=='n':
        print("it's ok")
    else:
        print("Invalid input")
        pass
