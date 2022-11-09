import os
import glob
import matplotlib.pyplot as plt 
import numpy as np
names_y = ["Y_Arborino.npy","Y_Jasmine.npy","Y_Basmati.npy"]
names = ["Arborino.npy","Jasmine.npy","Basmati.npy"]
first_name_y = "Y_Ipsala.npy"
first_name_x = "Ipsala.npy"

def append_X_Data():
    path = f"D://AI//Deep Learning//CNN//Deep-Learning-Rice-Image-Classification//processed_input_files//{first_name_x}"
    data = np.load(path)
    data = data[:500]
    for name in names:
        path = f"D://AI//Deep Learning//CNN//Deep-Learning-Rice-Image-Classification//processed_input_files//{name}"
        np_data = np.load(path)
        np_data = np_data[:500]
        data = np.append(data,np_data, axis=0)
        print(data.shape)
    path2 = "D://AI//Deep Learning//CNN//Deep-Learning-Rice-Image-Classification//Main_data//x_main_data.npy"
    np.save(path2,data)
    print("Done")

def append_Y_Data():
    path = f"D://AI//Deep Learning//CNN//Deep-Learning-Rice-Image-Classification//processed_input_files//{first_name_y}"
    data = np.load(path)
    data = data[:500]
    for name in names_y:
        path = f"D://AI//Deep Learning//CNN//Deep-Learning-Rice-Image-Classification//processed_input_files//{name}"
        np_data = np.load(path)
        np_data = np_data[:500]
        data = np.append(data,np_data, axis=0)
        print(data.shape)
    path2 = "D://AI//Deep Learning//CNN//Deep-Learning-Rice-Image-Classification//Main_data//y_main_data.npy"
    np.save(path2,data)
    print("Done")    

if __name__=="__main__":
    append_X_Data()
    append_Y_Data()