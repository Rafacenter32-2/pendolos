import pendulo
import json
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

ttk.Label(frm, text="tamaho dos eixos").grid(column=1,row=2)
escala = ttk.Scale(frm,from_=0.1,to=3,orient="horizontal")
escala.grid(column=0,row=2)

ttk.Label(frm, text="velocidade dos eixos").grid(column=1,row=3)
velocidade = ttk.Scale(frm,from_=0.005,to=0.03,orient="horizontal")
velocidade.grid(column=0,row=3)

ttk.Label(frm, text="Cor do eixo (em ingles)").grid(column=1,row=4)
cor_eixo = ttk.Entry(frm)
cor_eixo.grid(column=0,row=4)

ttk.Label(frm, text="Cor da trilha (em ingles)").grid(column=1,row=5)
cor_trilha = ttk.Entry(frm)
cor_trilha.grid(column=0,row=5)

ttk.Label(frm, text="Cor do fundo (em ingles)").grid(column=1,row=6)
cor_trilha = ttk.Entry(frm)
cor_trilha.grid(column=0,row=6)

ttk.Button(frm, text="iniciar", command=lambda: pendulo.start(json.loads("["+eixos.get()+"]"),int(escala.get()),int(velocidade.get()),"white","gray","black"),).grid(column=0,row=7)

root.mainloop()