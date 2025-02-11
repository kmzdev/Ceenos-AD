Navegador//480x400//
import webbrowser

global open_link
def open_link():
 url = entry.get()
 webbrowser.open(url)

frame = Frame(app_window)
frame.pack(pady=10)

label = Label(frame, text="URL:",bg='white')
label.grid(row=0, column=0, padx=5)


global entry
entry = Entry(frame, width=50)
entry.grid(row=0, column=1, padx=5)

button = Button(frame, text="Abrir", command=open_link)
button.grid(row=0, column=2, padx=5)




