to_do={}
def add_task():
  while True:
    try:
        name=input("input your task to add or (no to stop) : ")
        
        if name=='no':
            print("stopping task addition & status")
            break
        
        else:
            status=input("input your status of task : ")
            if name not in to_do:
                to_do[name]=status
                print(f"{name} & {status} added in your todo list")

            else:
                print(f"{name} alrealy exists (duplicates not allowed)")
    except Exception as err:
      print("an error occured during initialization")
    
def view_task():
    try:
        if not to_do:
            print("No task to view")
        else:
            count=1
            for i,j in to_do.items():
                print(f"{count} - {i} : {j}")
                count+=1
    except Exception as err:
          print("an error occured during initialization")

def delete_task():
    try:
        name=input("input your task which u want to delete : ")
        if name not in to_do:
            print("no such task found to delete")
        else:
            to_do.pop(name)
            print(f"{name} removed from your todo list")
    except Exception as err:
            print("an error occured during initialization")

def update_task():
  while True:
    try:
        name=input("input your task which u want to update or ('no' to stop): ")
        
        if name=='no':
            print("updating stopped")
            break
        else:
            if name not in to_do:
                print("no such task found to update")
            else:
                print("what u want to update")
                print("1 . task name and task status both")
                print("2 . task name only")
                print("3 . task status only")
                choice=int(input("inpur your choice (1/2/3) : "))
                if choice==1:
                    name2=input(f"enter your new task to replace with {name} : ")
                    status=input("input status to your newtask to update : ")
                    to_do.pop(name)
                    to_do[name2]=status
                    print(f"you have successfully update your task {name} with task {name2} & status {status} ")
                elif choice==2:
                    name2=input(f"enter your new task to replace with {name} : ")
                    cr=to_do.pop(name)
                    to_do[name2]=cr
                elif choice==3:
                    status=input("input status u want to update : ")
                    to_do[name]=status
                else:
                    print("invalid input")

                    

                    
    except Exception as err:
          print("an error occured during initialization")

while True:
  print("press 1 to add task")
  print("press 2 view task")
  print("press 3 to update task")
  print("press 4 to delete task")
  print("press 5 to exit")
  
  try:
      check=int(input("enter yuour choice (1/2/3/4/5) : "))
      if check==5:
        print("process ends here, Thank You")
        break
  
  
  except ValueError:
    print("Your have entered a wrong value")
    print("try again! : ")
    continue
  

  if check==1:
    add_task()
  elif check==2:
    view_task()
  elif check==3:
    update_task()
  elif check==4:
    delete_task()