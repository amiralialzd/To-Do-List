import os.path

to_do_list = []
def load_task():
 if os.path.exists("tasks.txt"):
    with open("tasks.txt","r") as f:
        for line in f.readlines():
           to_do_list.append(line.strip())


 else:
    print("file doesnt exits")





load_task()



def save_task():
    with open("tasks.txt","w") as f:
        for item in to_do_list:
            f.write(f"{item}\n")







def add(task):
  to_do_list.append(task)
  save_task()




def rem(rem):

     if rem in to_do_list:
           to_do_list.remove(rem)
           print("task has been removed")
           save_task()

     else:
            print("not found!")






def display():
    if len(to_do_list)==0:
        print("it is empty ")
    else:

     for index ,item in  enumerate(to_do_list,start=1):

      print(f"{index}.{item}")









choice=int(input("do u wanna see list or add/remove(for see the list press 1\n"
      "for add press 2 \n "
      "for remove press 3 \n"
                 "for exit from program press 0 )\n"))
while choice!=0:
 if choice==2:
    wrting=input("enter the task: ")
    add(wrting)
 elif choice==3:
     if len(to_do_list) == 0:
         print("list is empty")
     else:
      wrting=input("which task you have done?")
      rem(wrting)
 elif choice==1:
     display()

 choice=int(input("do u wanna do something else: (for see the list press 1\n"
      "for add press 2 \n "
      "for remove press 3 \n"
                 "for exit from program press 0)\n"))



