from concurrent.futures import process
from tkinter import*
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from turtle import back, width

#main
compiler=Tk()
compiler.title("CIDE")
fr=Frame(compiler)

#Number line
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
    width=2,
    state='disabled',
    takefocus=0,
    background='grey',
    wrap='none',
    font=10,padx = 10, pady = 5
)
lineNumber.pack(side='left',fill='y') 
#path
def set_file_path(path):
    global file_path
    file_path = path
#save a file
def save():
    if file_path =='':
        path=asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path= file_path
    with open(path, 'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)
#save as a file
def save_as():
    path=asksaveasfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)
#Open a file
def open_file():
    path=askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)
#Rum the code
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
#menu bar
menu_bar=Menu(compiler)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save)
file_menu.add_command(label="Save As",command=save_as)
file_menu.add_command(label="Exit",command=exit)
menu_bar.add_cascade(label="File",menu=file_menu)
# run bar
run_bar=Menu(menu_bar,tearoff=0)
run_bar.add_command(label="Run",command=run)
menu_bar.add_cascade(label="Run",menu=run_bar)
compiler.config(menu=menu_bar)
#Main body

editor=Text(height=10,bg='#000', fg='#ff0',font=10,insertbackground='white')
v_s=Scrollbar(editor)
editor.config(yscrollcommand=v_s.set)
v_s.pack(side=RIGHT,fill='y')
v_s.config(command=editor.yview)


editor.bind('<Any-KeyPress>',upln)
editor.pack(fill='both',expand=True)

#output body
code_output=Text(height=2,bg='#FFFFFF',fg='#FF0000', padx = 10, pady = 5,font=10,insertbackground='white')
# v_sk=Scrollbar(editor)
# code_output.config(yscrollcommand=v_sk.set)
# v_sk.pack(side=RIGHT,fill=Y) 
# v_sk.config(command=code_output.yview)
code_output.pack(fill='both',expand=True)
compiler.mainloop()