# to_do=[]
 
# def add_task():
#     name=input("enter the task u want to add : ")
#     if name not in to_do:
#         to_do.append(name)
#         print(f"{name} (task added in your list)")
#     else:
#         print("task already in lists (duplicates not allowed)")

# def view_task():
#     if not to_do:
#         print("dodo list is empty")
#     else:
#         for i,j in enumerate(to_do):
#             print(f"{i+1} : {j}")


# def update_task():
#     name=input("enter the task u want to update : ")
#     name2=input("enter your new task : ")
#     if name in to_do:
#         for name in to_do:
#             to_do[name]=to_do[name2]
#     else:
#         print("task not found in list to update")

# def delete_task():
#     name=input("enter the task u want to delete : ")
#     if name in to_do:
#         to_do.remove(name)
#     else:
#         print("taks not found in the list to delete")

# while True:    

#     print("press 1 to create a new task into list")
#     print("press 2 to view tasks")
#     print("press 3 to update tasks")
#     print("press 4 to delete task")
    
#     check=input("enter your responce : (1/2/3/4) : ")
#     if check=='stop':
#         print("process ends, (THANK YOU)")
#         break
#     try:
#         check=int(check)
#     except ValueError:
#         print("you have entered wrong value of word please enter (1/2/3/4) or 'stop'")
#         continue

#     if check==1:
#         add_task()

#     elif check==2:
#         view_task()

#     elif check==3:
#         update_task()

#     elif check==4:
#         delete_task()

#     else:
#         print("Inavlid Input")


