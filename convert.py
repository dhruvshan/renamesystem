import os
import shutil

convertVal = input("Please enter the filenames(s) you want to add to a new folder:\n")
count = 0

isdir = os.path.isdir('Cover_Letters')
if isdir==0 :
    os.mkdir("Cover_Letters")
    print("Made directory Cover_Letters") 
for file in os.listdir():
    if convertVal in file:
        count += 1
        new_path = 'Cover_Letters/' + file
        print("Moved:" + file) 
        shutil.move(file, new_path)
        
if count == 0:
    print("No files found/moved")
else:
    print(f"Moved {count} files")