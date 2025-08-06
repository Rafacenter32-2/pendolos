import pendulo
import json
import asyncio
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("explorador de pendulo")
root.iconbitmap("./icone.ico")

frm = ttk.Frame(root, padding=10,)
frm.grid()

ttk.Label(frm, text="explorador de pendulo").grid(column=0,row=0)

ttk.Label(frm, text="escreva clocando numeros e virgulas\nex:2,1,0.5\nquanto mais numeros,mais eixos").grid(column=1,row=1)
eixos = ttk.Entry(frm)
eixos.grid(column=0,row=1)

ttk.Label(frm, text="tamaho dos eixos (de 0.1 a 3)").grid(column=1,row=2)
escala = ttk.Spinbox(frm,from_=0.1,to=3)
escala.grid(column=0,row=2)

ttk.Label(frm, text="velocidade dos eixos (de 0.5 a 2)").grid(column=1,row=3)
velocidade = ttk.Spinbox(frm,from_=0.5,to=2)
velocidade.grid(column=0,row=3)

ttk.Label(frm, text="Cor do eixo (em ingles)").grid(column=1,row=4)
cor_eixo = ttk.Entry(frm)
cor_eixo.insert(0,"white")
cor_eixo.grid(column=0,row=4)

ttk.Label(frm, text="Cor da trilha (em ingles)").grid(column=1,row=5)
cor_trilha = ttk.Entry(frm)
cor_trilha.insert(0,"gray")
cor_trilha.grid(column=0,row=5)

ttk.Label(frm, text="Cor do fundo (em ingles)").grid(column=1,row=6)
cor_fundo = ttk.Entry(frm)
cor_fundo.insert(0,"black")
cor_fundo.grid(column=0,row=6)
ttk.Button(frm, text="iniciar", command=lambda: asyncio.run(pendulo.start(json.loads("["+eixos.get()+"]"),escala.get(),velocidade.get(),cor_eixo.get(),cor_trilha.get(),cor_fundo.get())),).grid(column=0,row=7)

root.mainloop()