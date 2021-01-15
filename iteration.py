import os
path="/Users/salimakazab/Desktop/petalwinternproject2021/uploads"
os.chdir(path)
for filename in os.listdir(path):
    if filename.endswith(".txt, .pdf, .png, .jpg, .jpeg, .gif"):
        f = open(filename)
filename = path + "/" + filename
print(filename)