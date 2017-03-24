import swiftclient
import tkinter
import os
from tkinter import *
from tkinter.filedialog import askopenfilename


user = 'satyateja27'
key = 'satya@27'
top = tkinter.Tk()
file_var = tkinter.StringVar(top, name='file_var')
command = lambda: openFile(file_var)
comm=lambda: ListContainers()


def openFile(file_var):
    file_name = askopenfilename()
    print (file_name)
    file_var.set(file_name)
    helloComplete(file_name)
    ListContainers=file_name
    

def connectToSwift():
    try:
        conn = swiftclient.Connection(
       user=user,
        key=key,
        authurl='http://52.53.194.27/auth/v1.0',
       )
    except Exception as e:
        print (e)
        print ("Authorization error.")
    return conn

def ListContainers():
    res=""
    conn = connectToSwift()
    try:
        for container in conn.get_account()[1]:
            res = res +  container['name'] + "\n"
    except Exception as e:
        print (e)
        res = e
    print (res)
    messagebox.showinfo("containers", res)

        

def helloComplete(abc):
    uploadFile(abc)
    messagebox.showinfo("abc",abc)


def uploadFile(ListContainersam):
    (head, tail)=os.path.split(ListContainersam)
    print(tail)
    conn=connectToSwift()
    try:
        fp = open(ListContainersam, "r")
    except Exception as r:
        print ("couldn't open file")
    try:
        container_name = 'container3'
        with open(tail, 'r') as hello_file:
            conn.put_object(container_name, 'h.txt',
                                        contents= hello_file.read(),
                                        content_type='text/plain')
        result="cont"
    except Exception as e:
        print (e)
        result = e
    print (result)


def main():
    title = Label(top, text="SIMPLE OBJECT STORAGE APP")
    title.pack(fill=X)
    title = Label(top, text=" ")
    title.pack(fill=X)
    title = Label(top, text=" ")
    title.pack(fill=X)
    print ("List Containers")
    conn=connectToSwift()
    print(connectToSwift)
    open_file = tkinter.Button(top, command=command,
                           padx=100, text="UPLOAD FILE")
    
    open_file.pack()
    title = Label(top, text=" ")
    title.pack(fill=X)
    ListContainers = tkinter.Button(top, command=comm,
                           padx=100, text="SHOW CONTAINERS")
    title = Label(top, text="   ")
    title.pack(fill=X)
    ListContainers.pack()
    title = Label(top, text="   ")
    title.pack(fill=X)
    file_name = file_var.get()
    #print("inmain ", openFile())
    top.mainloop()
    


if __name__ == "__main__":
    main()
