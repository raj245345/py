from pathlib import Path
import os

def listoffile():
    path=Path('')
    items=path.rglob('*')
    for i,j in enumerate(items):
        print(f"{i+1}:{j}")
        

def createfile():
    listoffile()
    name=input("enter the name of file which u want to create : ")
    p=Path(name)
    if not p.exists():
        with open(name,'w') as fs:
            data=input("enter the data u want to write in your new file : ")
            fs.write(data)
            print(f"{name} created successfully")
    else:
        print("file name already exists in the file list")

def readfile():
    listoffile()
    name=input("enter the name of the file which u want to read : ")
    p=Path(name)
    if p.exists() and p.is_file():
        with open(p,'r') as fs:
            data=fs.read()
            print(data)
    else:
        print("not such file found to read")

def deletefile():
    listoffile()
    name=input("enter the name of the file which u want to delete : ")
    p=Path(name)
    if p.exists and p.is_file():
        os.remove(p)

def updatefile():
    listoffile()
    name=input("enter the name of the file which u want to update : ")
    p=Path(name)
    if p.exists and p.is_file():
        print("press 1 to change file name")
        print("press 2 to overwrite file data")
        print("press 3 to add new data into file")

        while True:
            res=input("enter your responce for update (1/2/3) to stop updating enter 'stop': - ")
            if res=="stop":
                print("updation complete")
                break

            try:
                res=int(res)
            except ValueError:
                print("plz enter valid input (1/2/3) or 'stop' ")
                continue

            if res==1:
                name2=input("enter file's new name : ")
                p2=Path(name2)
                p.rename(p2)
                print(f"You have successfully change file name new name is {name2}")

            elif res==2:
                with open(p,'w') as fs:
                    data=input("enter the data u want to overwrite in file : ")
                    fs.write(data)
                    print("you have succesfully overwrite file")

            elif res==3:
                with open(p,'a') as fs:
                    data=input('ente the data u want to add in file : ')
                    fs.write(data)
                    print('You have successfully add data in the file')

            else:
                print("plz choose a valid option (1/2/3)")



while True:
    print("press 1 to create a new file")
    print("press 2 to read file")
    print("press 3 to delete a file")
    print("press 4 to update file")

    check=input("enter your choice (1/2/3/4) or press 'stop' to end the process : ")
    if check=='stop':
        print('process ends, Thank You')
        
        break
    try:
        check=int(check)
    except ValueError:
        print("Invalid input, Please enter valid value (1/2/3/4 or 'stop' )")
        continue


    if check==1:
        createfile()
    elif check==2:
        readfile()
    elif check==3:
        deletefile()
    elif check==4:
        updatefile()

    else:
        print("invalid input plz enter value (1/2/3/4) ")

