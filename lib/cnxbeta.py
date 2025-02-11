from tkinter import *
import os
import datetime
import time

openw = {}

def flex(btn,color1,color2):
    
            def get_color1(e):
                btn.config(background=color1)
            #bar.config(background='grey')
    
            def get_color2(e):
                btn.config(background=color2)
            #bar.config(background='white'
    
            for b in [btn]:
                btn.bind("<Enter>",get_color1)
                btn.bind("<Leave>",get_color2)

def new_window(win,ttitle,wd,hg):
    #global app_window
    def sair():
        window.destroy()
        try:
            
            tk_button.destroy()
        except Exception:
            tk_button.config(text='Exited',fg='red')
            #pass
    
    def minx():
        #title.config(text=texto)
        #print('min')
        window.config(width=1,height=1)
        window.place(x=0,y=0)
        #window.geometry(size)
    
    def minv():
        try:
            window.place(x=0,y=0)
            window.pack(expand=False,fill='y')
            window.config(width=wd,height=hg)
        except Exception:
            #tk_button.config(text='Error',fg='red')
            tk_button.destroy()
         # try:
            # tk_button.destroy()
         # except Exception:
            # pass
        #title.config(text=texto_sigla)
        
    global fullscreen
    fullscreen = False
    
    def maxv():
        global fullscreen
        #title.config(text=texto)
        height = window.winfo_screenheight()
        width = window.winfo_screenwidth()
        resol =  str(width) + 'x' + str(height)
        if fullscreen == True:
            #cute anumation down bellow
            #window.config(width=int(wd)/2,height=int(hg)/2)
            #time.sleep(1)
            window.config(width=wd,height=hg)  # Reduz para um tamanho padrão
            window.pack(expand=False,fill='y')
            window.place(x=0,y=0)
            fullscreen = False
        else:
            #window.place(x=0,y=0)
            #window.pack(expand=True)  # Centraliza
            window.place(x=0,y=0)
            window.pack(expand=True,fill=BOTH)
            fullscreen = True

    def restore():
        window.config(width=wd,height=hg)  # Reduz para um tamanho padrão
        window.pack(expand=False,fill='y')
        window.place(x=0,y=0)

    def maxv_d():
        window.place(x=(int(window.winfo_screenwidth()/2)),y=0)
        window.config(width=(int(window.winfo_screenwidth()/2)),height=(window.winfo_screenheight()))
    def maxv_e():
        window.place(x=0,y=0)
        window.config(width=(int(window.winfo_screenwidth()/2)),height=(window.winfo_screenheight()))
        
    #global window
    window = win
    #window = ttitle
    window.place(x=0,y=0)
    window.config(width=wd,height=hg,bg='white')
    window.pack_propagate(False)
    #window.pack(side='top')
    
    bar = Frame(window,height=50,bg='white')
    bar.pack(fill='x',side='top')
    
    title = Label(bar,text =ttitle,bg='white')
    title.pack(side='left')
    
    
    fechar = Button(bar,text=' X ',command= sair,bd=0,highlightthickness=0,activebackground='red',activeforeground='red',bg='white')
    fechar.pack(side="right")
    
    maxb = Button(bar,text=' ☐ ',command=maxv,bd=0,highlightthickness=0,activebackground='lightblue',bg='white')#> □
    maxb.pack(side="right")
    
    minb = Button(bar,text=' - ',command=minx,bd=0,highlightthickness=0,activebackground='lightblue',bg='white')#> □
    minb.pack(side="right")
    
    flex(fechar,'red','white')
    flex(maxb,'lightblue','white')
    flex(minb,'lightblue','white')
    #flex(bar,'lightgrey','white')
    #flex(window,'lightblue','white')
    
    global tk_button
    tk_button = Button(taskbar,text=ttitle,command= minv,bd=0,highlightthickness=0,activebackground='red',activeforeground='red',bg='white')
    tk_button.pack(side="left")
    flex(tk_button,'lightblue','white')

    #Criar um enuw*
    enuww = Menu(root, tearoff=0)
    enuww.add_command(label="Maximizar", command=maxv)
    enuww.add_command(label="Minimizar", command=minx)
    enuww.add_command(label="Restaurar", command=restore)
    enuww.add_command(label="Fechar", command=sair)
    enuww.add_separator()
    enuww.add_command(label="Redimensionsr para Direita",command=maxv_d)
    enuww.add_command(label="Redimensionsr para Esquerda",command=maxv_e)
    
    
    
    #Criar um botão que mostra o enuw*
    def mostrar_enuww(event):
        enuww.post(event.x_root, event.y_root)

    
    def start_drag(event):
        global drag_start_x
        drag_start_x = event.x
        global drag_start_y
        drag_start_y = event.y

    def drag(event):
        x = window.winfo_x() - drag_start_x + event.x
        y = window.winfo_y() - drag_start_y + event.y
        window.place(x=x, y=y)

    def stop_drag(event):
       
        
        if window.winfo_y() > window.winfo_screenheight()-200:
              window.place(x=0,y=0)
        elif window.winfo_x() > window.winfo_screenwidth()-400:
            window.place(x=(int(window.winfo_screenwidth()/2)),y=0)
            window.config(width=(int(window.winfo_screenwidth()/2)),height=(window.winfo_screenheight()))
        elif window.winfo_y() < -1:
             window.place(x=0,y=0)
             window.config(width=(int(window.winfo_screenwidth())),height=(window.winfo_screenheight()))  # Maximiza
        elif window.winfo_x() < -1:
            window.place(x=0,y=0)
            window.config(width=(int(window.winfo_screenwidth()/2)),height=(window.winfo_screenheight()))
        else:
            window.x = window.y = None

    bar.bind("<ButtonPress-1>", start_drag,lambda:window.wm_attributes('-topmost', True))
    bar.bind('<ButtonRelease-1>',stop_drag)
    bar.bind("<B1-Motion>", drag)
    bar.bind("<Button-3>", mostrar_enuww) 
    
        


root = Tk()
root.geometry('800x600')
root.config(bg='black')
root.attributes('-fullscreen',True)

file = 'bg.png'

with open('rec//bg_config.cfg','r') as cpf:
    fig = cpf.read()
    
if os.path.exists(fig):
    try:
        bg = PhotoImage(file = fig)

        imagem_de_fundo = Label(root,image= bg,bg='white')
        imagem_de_fundo.place(x=0,y=0, relwidth=1, relheight=1)
    except Exception:
        root.config(bg='black')
        
else:
    root.config(bg='black')


taskbar = Frame(root,height=20)
taskbar.pack(fill='x',side='bottom')
flex(taskbar,'lightgrey','white')

def reniciar():
	pass

#Criar um enuw*

enuw = Menu(root, tearoff=0)

enuw.add_command(label="Sair", command=root.quit)
enuw.add_command(label="Reniciar", command=reniciar)
enuw.add_separator()
enuw_bar = Menu(enuw,tearoff=0)
enuw.add_cascade(label='Aplicaçoes',menu=enuw_bar)

#Criar um botão que mostra o enuw*
def mostrar_enuw(event):
    #enuw.post(event.x_root, event.y_root)
    ry = root.winfo_screenheight()
    rpy = ry - 22
    enuw.post(0,rpy)

#Criar o botão estilo "Iniciar"*
botao = Button(taskbar, text="enuw Iniciar", relief=RAISED,bd=0,highlightthickness=0,bg='white',height=1)
botao.bind("<Button-1>", mostrar_enuw)  # Bind para mostrar o enuw ao clicar
botao.pack(side='left')
flex(botao,'lightgrey','white')
#root.bind("<Button-3>", mostrar_enuw) 
#enuwb = Button(taskbar,text='enuw')#,command=mnw)
#enuwb.pack(side='left')
#enuwb.bind("<Button-1>",mnw)

def mostrar_data():
	dia = datetime.date.today()
	label_dia['text'] = dia
	label_dia.after(1000, mostrar_hora)

def mostrar_hora():
	agora = datetime.datetime.now()
	hora_atual = agora.strftime("%H:%M:%S")
	label_hora['text'] = hora_atual
	label_hora.after(1000, mostrar_hora) 

label_hora = Label(taskbar)
label_hora.config(height=0)
label_hora.pack(side="right")
mostrar_hora() # Inicia a atualização da hora

label_dia = Label(taskbar)
label_dia.config(height=0)
label_dia.pack(side="right")
mostrar_data()
    
def rw(name,e):
    try:
        #reportp.destroy()
        report.insert('1.0',time.strftime('%d/%m/%Y %H:%M:%S')+'\nErro ao executar aplicaçao: '+name+'\n\nErro:\n'+str(e))
    except Exception:
        
        ry = root.winfo_screenheight()
        rx = root.winfo_screenwidth()
        rpx = rx - rx/4
        rwd = rx/4
        rhg = ry - 20
        rp = Frame(root,width=rwd,height=rhg)
        rp.place(x=rpx,y=0)
        rp.config(bg='white')
        rp.pack_propagate(False)
        bar = Frame(rp,height=50,bg='white')
        bar.pack(fill='x',side='top')
        fechar = Button(bar,text=' X ',command= rp.destroy,bd=0,highlightthickness=0,activebackground='red',activeforeground='red',bg='white')
        bug_rp = Label(bar,text='Bug Report',bg='white')
        bug_rp.pack(side="left")
        fechar.pack(side="right")
        flex(fechar,'red','white')
        report = Text(rp,wrap='word')
        report.pack()
        report.insert('1.0',time.strftime('%d/%m/%Y %H:%M:%S')+'\nErro ao executar aplicaçao: '+name+'\n\nErro:\n'+str(e))
        


def load_app(app_name):
    #print(app_name)
    with open(app_name,'r') as app:
        cont = app.read()
        g = cont.split('//')
        tt = g[0]
        szx = g[1].split('x')[0]
        szy = g[1].split('x')[1]
        code = g[2]
    app.close()
    global app_window
    app_window = Frame(root)
    app_window.pack()
    new_window(app_window,tt,szx,szy)
    #enuw.add_command(label=tt, command=lambda: new_window(app_window,tt,szx,szy))
    try:
        exec(code)
    except Exception as e:
        rw(tt,e)

appd = []
for j in os.listdir('apps'):
    appd.append(j)
    #appd.append(os.listdir(j))
    #appd.append(j)
#print(appd)
    

apps = {}

for i in appd:
    #print(i)
    #dire.append(i)
    #print(dire)
    for a in os.listdir('apps\\'+i):
        #print(a)
        f = 'apps\\'+a
        #apps.append(f)
        
        if a.endswith('.app'):
            
            
            #print(f)
            with open('apps\\'+i+'\\'+a,'r') as ap:
                conta = ap.read()
                gx = conta.split('//')
                name = gx[0]
                apps[f] = name
            enuw_bar.add_command(label=name, command=lambda f = 'apps\\'+i+'\\'+a: load_app(f))
            ap.close()
    

    
#load_app('apps\\about.app')
#new_window('Test',600,400)
def op():

    open_window = Frame(root)
    open_window.pack()
    new_window(open_window,'Open Windows',400,400)
    label = Label(app_window, text="URL:")
    label.grid(row=0, column=0, padx=5)
    button = Button(app_window, text="Abrir")
    button.grid(row=0, column=2, padx=5)
    



root.mainloop()
