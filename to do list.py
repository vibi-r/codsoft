to_do_list=[]
while True:
    print("\n to do list:")
    print("1. add task")
    print("2. view tasks")
    print("3.quit")
    choice=input("enter the choice(1/2/3):")
    if choice=='1':
       task=input("enter the task:")
       to_do_list.append(task)
       print("task added successfully!")
    elif choice=='2':
        if to_do_list:
           print("\nyour task:")
           for index,task in enumerate(to_do_list,start=1):
               print(f"{index}.{task}")
        else:
            print("no task added yet")
    elif choice=='3':
        print("exiting the to_do_list program.goodbye!")
        break
    else:
        print("invalid choice.please enter 1,2,or 3.")
           
       
    
