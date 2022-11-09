import os
import glob
import matplotlib.pyplot as plt 
import numpy as np
from  random import randint
def convert_img_to_npy(path,name):
    data = []
    files = glob.glob (path)
    for myFile in files:
        image = plt.imread (myFile)
        print(image.shape)

        column = np.arange(15000)
        column.fill(1)
        column = np.reshape(column, (-1, 1))
        data.append (image)
    new_data = np.array(data)
    save_path = "D://AI//Deep Learning//raw_input_files//"
    completeName = os.path.join(save_path, name)
    np.save(completeName,new_data)

def show_np(name,index):
    np_data = np.load(name)
    plt.imshow(np_data[index])
    print(np_data.shape)
    # plt.show()
if __name__=="__main__":
    file_names = ["Ipsala.npy","Arborino.npy","Jasmine.npy","Karacadag.npy","Basmati.npy"]
    # for file_name in file_names:
    path = "D://AI//Deep Learning//Rice_Image_Dataset//Ipsala//*.jpg"
    names = ["Ipsala.npy","Arborino.npy","Jasmine.npy","Karacadag.npy","Basmati.npy"]
    index = randint(0,1500)
    for name in names:
        convert_img_to_npy(path,name)






