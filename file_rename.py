import os
os.getcwd()

#renames files inside directory
img_folder = r'C:\Users\chris\OneDrive\Desktop\Personal Coding Projects\Habbit Tracker and ToDo List\habbit\src\frog_photos'

#gets count of images/files inside a folder
img_name = os.listdir(img_folder)
print(len(img_name), " images in the folder")

#loop to renam all files with i - itterate count
for i, filename in enumerate(os.listdir(img_folder)):
 os.rename(img_folder + "/" + filename, "frog_" + str(i) + ".png")