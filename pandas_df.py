import numpy as np
import os
'''
Not working well
    Karacadag.npy

'''
names = ["Y_Ipsala.npy","Y_Arborino.npy","Y_Jasmine.npy","Y_Basmati.npy"]

def add_column():
    for label,name in enumerate(names):
        column = np.arange(0,15000)
        column.fill(label)
        column = np.reshape(column, (-1, 1))
        print(column)
        print(column.shape)
        save_path = "D://AI//Deep Learning//processed_input_files//"
        completeName = os.path.join(save_path, name) 
        np.save(completeName,column)


if __name__=="__main__":
    add_column()



