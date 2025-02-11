Agenda//400x400//
import os
    
# with open('apps/notas/notas.txt','a') as apr:
        # apr.truncate(0)


# Crie uma área de texto
text_area = Text(app_window, wrap="word", undo=True)
text_area.pack(expand=True, fill="both")

# Adicione uma barra de rolagem
##scroll = Scrollbar(text_area)
##text_area.configure(yscrollcommand=scroll.set)
##scroll.config(command=text_area.yview)
##scroll.pack(side="right", fill="y")
# Crie o menu de opções

with open('apps/notas/notas.txt','r+') as notas:

    texto = notas.read()
    text_area.insert(END,texto)



