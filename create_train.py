import os

path = "test/"

image_list = os.listdir("test")

textFile = open('test.txt', 'w')

for image in image_list:
    #if i % 2 == 1:
        image_path = path+image+"\n"
        textFile.write(image_path)