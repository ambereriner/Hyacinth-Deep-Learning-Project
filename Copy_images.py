import os
import shutil
import pandas as pd
from tkinter.filedialog import askdirectory, askopenfilename

#Select directory of images
directory1_path = askdirectory(initialdir="C:/",title='Choose a directory of images to copy.')
dir_list = os.listdir(directory1_path)

#select output path
directory2_path = askdirectory(initialdir="C:/",title='Choose directory to copy images to')

#select csv file
csv = askopenfilename(initialfile="C:/",title='Choose the csv.')

#input name hyacinth scoring column
binary = input("Enter Name of Hyacinth Scoring Column: ")
folder = input('Enter Folder Name (100MEDIA or 101MEDIA: ')
df = pd.read_csv(csv, usecols = ["filename", "directory", str(binary)])
df_filtered1 = df[df[binary] == 1]
df_filtered2 = df_filtered1[df_filtered1.directory.str.endswith(str(folder))]
print(df_filtered2)

#loop through directory1 and copy file to directory 2
for f in df_filtered2["filename"]:
    file1_path = directory1_path + '/' + f + '.JPG'
    file2_path = directory2_path + '/' + f + '.JPG'
    print(file2_path)
    shutil.copy2(file1_path, file2_path)
