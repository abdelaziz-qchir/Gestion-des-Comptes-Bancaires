# import tkinter
# root = tkinter.Tk()
# but = tkinter.Button(text="changement légende")
# but.pack()
# def change_legende() :
#     global but
#     but.config (text = "nouvelle légende")

# but.config (command = change_legende)
# root.mainloop()

import tkinter as tk
from tkinter import ttk
import Comptes, CompteEpargne, CompteCourant

root = tk.Tk()
root.geometry('1200x600')
root.title('Gestion des Comptes')

numLabel = tk.Label(root, text='Numéro:')
numLabel1 = tk.Label(root, text='1')  
numLabel1.config(state=tk.DISABLED)
numLabel.place(x=20, y=20)
numLabel1.place(x=100, y=20)

propLabel = tk.Label(root, text='Propriétaire:')  
propText = tk.Entry(root)  
propLabel.place(x=20, y=50)
propText.place(x=100, y=50)

SoldeLabel = tk.Label(root, text='Solde Initial:')  
SoldeText = tk.Entry(root)  
euroLabel = tk.Label(root, text='Euro')  
SoldeLabel.place(x=20, y=80)
SoldeText.place(x=100, y=80)
euroLabel.place(x=240, y=80)

TypeLabel = tk.Label(root, text='Type:')  

v = tk.IntVar()
case1 = tk.Radiobutton(root, variable=v, value=1)  
case2 = tk.Radiobutton(root, variable=v, value=2)  
case1.config(text='Courant')
case2.config(text='Epargne')
v.set(1)  
TypeLabel.place(x=20, y=110)
case1.place(x=100, y=110)
case2.place(x=240, y=110)
case1.config(state=tk.NORMAL)

tauxIntLabel = tk.Label(root, text='Taux Interêt')  
tauxIntText = tk.Entry(root)  
pourcentLabel = tk.Label(root, text='%')  
tauxIntLabel.place(x=20, y=140)
tauxIntText.place(x=100, y=140)
pourcentLabel.place(x=240, y=140)

decouvertLabel = tk.Label(root, text='M. Découvert')  
decouvertext = tk.Entry(root)  
decouvertEuroLabel = tk.Label(root, text='Euro')  
decouvertLabel.place(x=20, y=170)
decouvertext.place(x=100, y=170)
decouvertEuroLabel.place(x=240, y=170)  
tauxIntText.config(state=tk.DISABLED)

ajouter = tk.Button(text='Création Compte')
ajouter.place(x=100, y=210)

area = ('Numéro', 'Propriétaire', 'soldeInitial', 'type', 'Taux Intérêt', 'Montant Découvert')
ac = ('n', 'e', 's', 'ne', 'nw', 'sw')

tv = ttk.Treeview(root, columns=ac, show='headings', height=7)

for i in range(6):
    tv.column(ac[i], width=160, anchor='e')
    tv.heading(ac[i], text=area[i])

tv.place(x=150, y=300)

####################################################
o = ""

def add():
    print(str(v.get()))
    if(str(v.get()) =='1'):
        o = 'courant'
        c = CompteCourant.CompteCourant(propText.get(), SoldeText.get(), decouvertext.get())
        cc = (str(c.getNum), propText.get(), SoldeText.get(), 'Courant', '', decouvertext.get())
    else:
        o = 'epargne'
        c = CompteEpargne.CompteEpargne(propText.get(), SoldeText.get(), tauxIntText.get())
        cc = (str(c.getNum), propText.get(), SoldeText.get(), 'Epargne', tauxIntText.get(), '')
    
    numLabel1.config(text=str(Comptes.Compte.nb + 1))
    tv.insert('', 'end', values=cc)
    propText.delete(0, 'end')
    SoldeText.delete(0, 'end')
    decouvertext.delete(0, 'end')
    tauxIntText.delete(0, 'end')

def modifVisib(evt):
    print(str(v.get()))
    if(str(v.get()) == '2'):
        tauxIntText.config(state=tk.DISABLED)
        decouvertext.config(state=tk.NORMAL)
    if(str(v.get()) == '1'):
        tauxIntText.config(state=tk.NORMAL)
        decouvertext.config(state=tk.DISABLED)

ajouter.config(command=add)
case1.bind("<Button-1>", modifVisib)
case1.focus_set()
case2.bind('<Button-1>', modifVisib)
case2.focus_set()

root.mainloop()