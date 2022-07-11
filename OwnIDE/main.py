from concurrent.futures import process
from tkinter import*
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from turtle import back, width

# class

 

compiler=Tk()
compiler.title("CIDE")
def getln():
    output=''
    raw,col= editor.index('end').split('.')
    for i in range(1,int(raw)):
        output+=str(i)+'\n'
    return output

def upln(event=None):
    lineNumber_bar=getln()
    lineNumber.config(state='normal')
    lineNumber.delete(1.0,END)
    lineNumber.insert(1.0,lineNumber_bar)
    lineNumber.config(state='disabled')



lineNumber = Text(
    compiler,
    width=4,
    state='disabled',
    takefocus=0,
    background='grey',
    wrap='none'
)
lineNumber.pack(side='left',fill='y')  

def set_file_path(path):
    global file_path
    file_path = path

def save():
    if file_path =='':
        path=asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path= file_path
    with open(path, 'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)

def save_as():
    path=asksaveasfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)


def open_file():
    path=askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)

def run():
    if file_path=='':
        save_prompt=Toplevel()
        text= Label(save_prompt,text="Please save your code",bg='#000', fg='#ff0', padx = 20, pady = 5,font=10)
        text.pack()
        return
    command = f'python {file_path}'
    process=subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE , shell=True)
    output,error=process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

menu_bar=Menu(compiler)

file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save)
file_menu.add_command(label="Save As",command=save_as)
file_menu.add_command(label="Exit",command=exit)
menu_bar.add_cascade(label="File",menu=file_menu)

run_bar=Menu(menu_bar,tearoff=0)
run_bar.add_command(label="Run",command=run)
menu_bar.add_cascade(label="Run",menu=run_bar)
compiler.config(menu=menu_bar)



editor=Text(bg='#000', fg='#ff0', padx = 10, pady = 5,font=10,insertbackground='white')
editor.bind('<Any-KeyPress>',upln)
editor.pack()

code_output=Text(height=10,bg='#FFFFFF',fg='#FF0000', padx = 10, pady = 5,font=10,insertbackground='white')
code_output.pack()
compiler.mainloop()