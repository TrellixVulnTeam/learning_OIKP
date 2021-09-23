import zipfile, os

def size_check_zip():
    os.chdir("C:/Users\Administrator/Downloads/")
    with zipfile.ZipFile("기상청19_동네예보 통보문 조회서비스_오픈API활용가이드.zip") as example_zip:
        print(example_zip.namelist())
        for i in example_zip.namelist():
            info = example_zip.getinfo(i)
            print(info.file_size,info.compress_size)
            print("Compressed file is %sx smaller" % (round(info.file_size/info.compress_size,2)))

def extract_from_zip():
    os.chdir("C:/Users\Administrator/Downloads/")
    with zipfile.ZipFile("기상청19_동네예보 통보문 조회서비스_오픈API활용가이드.zip",'r') as example_zip:
        for i in example_zip.namelist():
            filename = i
            print(example_zip.extract(filename))

extract_from_zip()