import os

folder = 'F:/Shoe_2023/Rearfoot/'


sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
for i in range(len(sub_folders)):
    s = sub_folders[i]
    subject = s[1:]
    print(subject)

#print(sub_folders)