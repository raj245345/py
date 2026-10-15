import random
import string
from pathlib import Path


class Bank:
    database='data1.json'
    d=[]

    p=Path(database)
    if p.exists():
        with open(database,'r') as fs:
            d=json.loads(fs.read())
    else:
        print("no such file found")

    @classmethod
    def __updatejson(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.d))

    @classmethod
    def __accnumgen(cls):
        alpha=random.choices(string.ascii_letters,k=4)
        nums=random.choices(string.digits,k=4)
        spec=random.choices("@#$",k=2)
        id=alpha+nums+spec
        return "".join(id)
    
    def createaccout(self):
        try:
            info ={
                "name":input("enter the name : "),
                "age":int(input("ente your age : ")),
                "email":input("enter your email id : "),
                "pin":int(input("enter pin for your account: ")),
                "accountnum": Bank.__accnumgen(),
                "balance":0
                }

            if info['age']<10:
                print("you are underage to open a bank account")
            if len(str(info['pin']))!=6:
                print("invalid pin format (only 6 digits allowed)")
            else:
                print("Congrats Your has been successfilly created")
                print("Your Account Detailys Are : - ")
                count=1
                for i,j in info.items():
                    print(f"{count} - {i} : {j}")
                    count+=1

                Bank.d.append(info)
                Bank.__updatejson()
        except Exception as err:
            print(f"an error occured {err}")

    def depositmoney(self):
        try:
            ac_n=input("enter your account number : ")
            pin=int(input("enter your pin : "))

            storedata=[i for i in Bank.d if i['accountnum']==ac_n and i['pin']==pin]
            if not storedata:
                print("Your entered recored not found in the database")
            else:
                amount=int(input("enter amount to deposit into your account : "))
                if amount<=0:
                    print("invalid amount entered")
                else:
                    storedata[0]['balance']+=amount
                    print(f"Your Amount Rs. {amount} successfully deposited in Account, New balance is Rs. {storedata[0]['balance']}  ")

                    Bank.__updatejson()
        except Exception as err:
            print(f"an error occured {err}")

    def withdrawmoney(self):
        try:
            ac_n=input("enter your account number : ")
            pin=int(input("enter your pin : "))

            storedata=[i for i in Bank.d if i["accountnum"]==ac_n and i['pin']==pin]
            if not storedata:
                print("Your entered record not found in the database")
            else:
                amount=int(input("enter amount to withdraw from your account : "))
                if amount>storedata[0]['balance'] or amount<=0:
                    print("insufficeint Balance or invalid amount entered")
                else:
                    storedata[0]['balance']-=amount
                    print(f"Your Amount Rs. {amount} successfully withdrew from your Account, New balance is Rs. {storedata[0]['balance']}  ")
                    
                    Bank.__updatejson()
        except Exception as err:
            print(f"an error occured {err}")

    def viewdetails(self):
        try:
            ac_n=input("enter your account number : ")
            pin=int(input("enter your pin : "))
        
            storedata=[i for i in Bank.d if i["accountnum"]==ac_n and i['pin']==pin]
            if not storedata:
                print("Your entered record not found in the database")
            else:
                print("your account details are : - ")        
                count=1
                for i,j in storedata[0].items():
                    print(f'{count} - {i} : {j}')
                    count+=1

        except Exception as err:
            print(f"an error occured {err}")                
             

    def updatedetails(self):
        try:
            ac_n=input("enter your account number : ")
            pin=int(input("enter your pin to procees : "))

            storedata=[i for i in Bank.d if i['accountnum']==ac_n and i['pin']==pin]
            if not storedata:
                print("Your entered code not found in the database")

            else:
                print("You cannot change Age , Account No and Balance")
                print("if u dont want to update detail press enter to ignore")

        except Exception as err:
            print(f"an error occured as {err}")         
            
            try:
                name=input("enter your new name or press enter to ignore : ")
                pin=input("enter new pin or press enter to ignore : ")
                email=input("enter new email or press enter to ignore : ")
                

                newdata={"name":name,"email":email,"pin":pin}

            except ValueError:
                print("step passed")
            
        try:    

            if newdata["name"]=="":
                newdata["name"]=storedata[0]["name"]
            if newdata['pin']=="":
                newdata['pin']=storedata[0]['pin']
            if newdata['email']=="":
                newdata['email']=storedata[0]['email']

            newdata['age']=storedata[0]['age']
            newdata['accountnum']=storedata[0]['accountnum']
            newdata['balance']=storedata[0]['balance']

            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])

            
            for i in newdata:
                if newdata[i]==storedata[0][i]:
                    continue
                else:
                    storedata[0][i]=newdata[i]

            Bank.__updatejson()
            print("update successful")
        except Exception as err:
            print(f"an error occurred {err}")
            
        

while True:

    print("press 1 for creating an Bank Account")
    print("press 2 for Depositing the money in your Bank Account")
    print("press 3 for withdrawing the money from your Bank Account")
    print("press 4 for details of your Bank Account")
    print("press 5 for updating the details")
    
    try:
        res=input("enter your responce (1/2/3/4/5) or 'stop' to stop process : ")

        if res=='stop':
            print("process ends")
            break

    
        res=int(res)
    except Exception as err:
        print("wrong input entered")
        print("try again")
        continue


    user=Bank()

    if res==1:
        user.createaccout()

    elif res==2:
        user.depositmoney()

    elif res==3:
        user.withdrawmoney()

    elif res==4:
        user.viewdetails()

    elif res==5:
        user.updatedetails()

    else:
        print("invalid input")
        

