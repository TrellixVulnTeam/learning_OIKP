import os
import re

root = "C:\Learnings\Python"
for i, filename in enumerate(os.listdir(root)):
    rename = "".join(filename.split('_',maxsplit=1)[1:])


    #print(os.path.join("",filename))

#os.path

class A:
    def __init__(self,root,item):
        self.root = root
        self.file_list = []
        for filename in os.listdir(root):
            self.file_list.append(os.path.join(root, filename))

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):  # 하나의 데이터를 반환
        file_dir = self.file_list[idx]
        return print(file_dir)


if __name__ == '__main__':
    pass
