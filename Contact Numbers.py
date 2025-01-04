import os
os.system('cls')

#Q10

x = 'i love python'

a = x.split()
a.reverse() 
print(' '.join(a))


#Q17

names = []
contact_numbers = []
num = int(input("Enter the total number of contacts you want to save: "))
for i in range(num):
    name = input("Name: ")
    contact_number = int(input("Contact Number: ")) 
    names.append(name)
    contact_numbers.append(contact_number)
print("\nName\t\t\tContact Number\n")
for i in range(num):
    print("{}\t\t\t{}".format(names[i], contact_numbers[i]))
search_term = input("\nEnter search term: ")
print("Search result:")
if search_term in names:
    index = names.index(search_term)
    contact_number = contact_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, contact_number))
else:
    print("No records")


#Q25

my_numbers = [5, 102, 99, 127]

my_numbers.sort()

print(my_numbers)

#Q14

list1= ['ali:1234','reza:5678','arash:2468','Maryam:1357']
letter=input("please input a word : ")
if letter in list1:
    list1.remove(letter)
    print('The name has been removed!', list1)
else:
    print('The name not exist!', '\n',list1)


#Q21

num_list = []

def add_nums():
    while len(num_list) < 5:
        user_num = int(input('please enter a number to add:'))
        num_list.append(user_num)
    print('You have these numbers: ',num_list)
    total_num_sum = 0
    for x in num_list:
        total_num_sum += x 
    print('total sum of numbers = ',total_num_sum)
add_nums()


#Q18

from tkinter import *

win = Tk() 
win.geometry("312x324")  
win.resizable(0, 0) 
win.title("Calculator")



def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)



def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 

 
def bt_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
 
expression = ""
 

 
input_text = StringVar()
 

 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) 
 
 
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
 
btns_frame.pack()
 
# first row
 
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()


#Q12

import re

while True:

  user_input = input("Enter a password : ")
  is_valid = False

  if (len(user_input)<6 or len(user_input)>12):
    
    print("Check it! Total characters should be between 6 and 12")
    continue
  elif not re.search("[A-Z]",user_input):
    
    print("Check it! It should contain one letter between [A-Z]")
    continue
  elif not re.search("[a-z]",user_input):
    
    print("Check it! It should contain one letter between [a-z]")
    continue
  elif not re.search("[1-9]",user_input):

    print("Check it! It should contain one digit between [1-9]")
    continue
  elif not re.search("[~!@#$%^&*]",user_input):
    
    print("Check it! It should contain at least one letter in [~!@#$%^&*]")
    continue
  elif re.search("[\s]",user_input):
    
    print("Check it! It should not contain any space")
    continue
  else:
    
    is_valid = True
    break


if(is_valid):
  print("Password is valid")


#Q19


n=20
for i in range(1, 11):
    print(' '*n, end='') 
    print('* '*(i)) 
    n-=1

#Q20

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')



    

#Q15

from tkinter import *

def login():
    
    uname=username.get()
    pwd=password.get()
   
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      if uname=="mollaee" and pwd=="123":
       message.set("Login success")
      else:
       message.set("Wrong username or password!!!")

def Loginform():
    global login_screen
    login_screen = Tk()
    
    login_screen.title("Login Form")
    
    login_screen.geometry("300x250")
    
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    
    Label(login_screen, text="Username * ").place(x=20,y=40)
    
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    
    Label(login_screen, text="Password * ").place(x=20,y=80)
    
    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)

    #Login
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()

Loginform()