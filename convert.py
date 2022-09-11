import os
import shutil

isdir = os.path.isdir('Cover_Letters')
if isdir==0 :
    os.mkdir("Cover_Letters")
    print("Made directory Cover_Letters") 
for file in os.listdir():
    if "CoverLetter" in file:
        new_path = 'Cover_Letters/' + file
        print("Moved:" + file) 
        shutil.move(file, new_path)
        