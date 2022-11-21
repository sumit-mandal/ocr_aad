import glob,os
import random

# current directory
imgs_path = "/home/sumit/Work/proxgy/OCR/Training/img_aadhar/"

total_imgs = glob.glob(imgs_path+"*.png")+glob.glob(imgs_path+"*.jpg")
train_imgs = random.sample(total_imgs,int(len(total_imgs)*0.95))
print(len(total_imgs),len(train_imgs))

with open("train.txt","a") as f:
    for i in train_imgs:
        f.write(i+"\n")

with open("test.txt","a") as f:
    for i in total_imgs:
        if i not in train_imgs:
            f.write(i+"\n")
