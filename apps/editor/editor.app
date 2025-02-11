Editor//620x420//




from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter import messagebox
import subprocess
import os
import time


dr = 'apps\\editor\\files'
#time.strftime('%d/%m/%Y %H:%M:%S') + '\n'

about_lm = '''
ZOM Editor

Version: 1.0
Created by Klit Zets(CFZ)


You are Welcome !

The ZOM editor !


'''

def exit():
    messagebox.showinfo(title='Exit',message='Are you sure that want to exit?')
    app_window.destroy()


def help():
        def sair():
                help_window.destroy()
                
        help_window = Toplevel()
        help_window.title('Help')
        help_window.geometry('600x400')
        help_window.config(bg='white')
        help_label = Text(help_window,height=25,wrap="word", undo=True)
        help_label.pack(side='top')
        help_label.insert('1.0',dcl.doc)

def about():
        def novw():
                
                def sair():
                        nov.destroy()
                        
                nov = Toplevel(app_window)
                nov.title('Novidades')
                nov.geometry('300x300')
                #about_window.config(expand= False)
                nov_label = Label(nov,text='Aqui aparecerao as novidades!')
                nov_label.pack()
                
        def sair():
                about_window.destroy()
                
        about_window = Toplevel(app_window)
        about_window.title('About')
        about_window.geometry('300x300')
        #about_window.config(expand= False)
        about_label = Label(about_window,text=about_lm)
        about_label.pack()
        frame = Frame(about_window)
        frame.pack(side='bottom',fill='x') 
        about_button = Button(frame,text='Close',command=sair)
        about_button.pack(side='right')
        about_button = Button(about_window,text='News',command=novw)
        about_button.pack(side='bottom')

def docs():
    def sair():
        nov.destroy()
            
    nov = Toplevel(app_window)
    nov.title('Documentaçao')
    nov.geometry('300x300')
    #about_window.config(expand= False)
    nov_label = Label(nov,text='Documentaçao')
    nov_label.pack()
                
    #os.startfile('resources/documentaçao_lm.py')


#root.config(menu=menu_bar)
def mostrar_menu(event):
    menu_bar.post(event.x_root, event.y_root)
    #ry = root.winfo_screenheight()
    #rpy = ry - 22
    #menu.post(0,rpy)

#bar
bar = Frame(app_window,height=50,bg='white')
bar.pack(fill='x',side='top')

#Criar o botão estilo "Iniciar"*
botao = Button(bar, text="Menu", relief=RAISED,bd=0,highlightthickness=0,bg='white')
botao.bind("<Button-1>", mostrar_menu)  # Bind para mostrar o menu ao clicar
botao.pack(side='left')
flex(botao,'lightgrey','white')


editor = Text(app_window,wrap="word",undo=True)
editor.pack(fill=BOTH,expand=True)
#editor.pack()

dir_label = Text(app_window,height=1,state='disabled')
dir_label.pack(fill=BOTH,side='top')


file_path = ''


def restart():
        os.startfile('ZOM.py')
        exit()

def set_file_path(path):
        global file_path
        file_path = path
        dir_label.config(state='normal')
        dir_label.delete('1.0',END)
        dir_label.insert('1.0',file_path)
        dir_label.config(state='disabled')
        


def new_file():
        
        path = asksaveasfilename(filetypes=[('Text','*.txt'),('EXT','*.ext')])
        if path == '':
            pass
        else:
            with open(path+'.txt','a') as file:
                pass
            set_file_path(path+'.txt')
        

def open_file():
        
        path = askopenfilename(filetypes=[('Text','*.txt'),('EXT','*.ext')])

        if os.path.exists(path):
            with open(path,'r') as file:
                    code = file.read()
                    editor.delete('1.0',END)
                    editor.insert('1.0',code)
        else:
            messagebox.showinfo(title='Open File',message="This file doesn't exist")
            
        

        set_file_path(path)
        
def save():
    if os.path.exists(file_path):
        with open(file_path,'w') as file:
            code = editor.get('1.0',END)
            file.truncate(0)
            file.write(code)
    else:
        messagebox.showinfo(title='Save File',message="You must open or create a file to save")
                    
    
def save_as():
       
    path = asksaveasfilename(filetypes=[('Text','*.txt'),('EXT','*.ext')])
    with open(path+'.txt','w') as file:
        code = editor.get('1.0',END)
        file.truncate(0)
        file.write(code)

    set_file_path(path+'.txt')

                #path = file_path
                
        
scroll = Scrollbar(editor)
editor.configure(yscrollcommand=scroll.set)
scroll.config(command=editor.yview)
scroll.pack(side="right", fill="y")

global menu_bar
menu_bar = Menu(app_window,tearoff=0)

global file_menu
file_menu = Menu(app_window,tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save)
file_menu.add_command(label='Save As',command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Restart',command=restart)
file_menu.add_command(label='Exit',command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

#about_bar = Menu(menu_bar,tearoff=0)
#about_bar.add_command(label='Run',command=run)

global about_bar
about_bar = Menu(menu_bar,tearoff=0)
about_bar.add_command(label='About',command=about)
about_bar.add_separator()
about_bar.add_command(label='Docs',command=docs)
menu_bar.add_cascade(label='Help',menu=about_bar)





