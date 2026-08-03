#Nintendo© / GameFreak© / POKÉMONtm (Caracter: Koraidon)
#Sprites base: darkusshadow
#Melhorias: shaderr31
#Edit on Photshop: Adelton
#Programador: Adelton

import tkinter
import random
import time
from pathlib import Path

number = 17
number1 = 225

root = tkinter.Tk()

Koraidon = Path(__file__).parent / "KoraidonSpritesteste"

sprit = {
    "back": tkinter.PhotoImage(file=str(Koraidon / "olhandopratras.png")),
    "front": tkinter.PhotoImage(file=str(Koraidon / "defrente.png")),
    "rightway": tkinter.PhotoImage(file=str(Koraidon / "viradopradireita.png")),
    "rightway2": tkinter.PhotoImage(file=str(Koraidon / "viradopradireita2.png")),
    "leftway": tkinter.PhotoImage(file=str(Koraidon / "viradopraesquerda.png")),
    "leftway2": tkinter.PhotoImage(file=str(Koraidon / "viradopraesquerda2.png")),
    "heart": tkinter.PhotoImage(file=str(Koraidon / "heart.png")),
    "talk": tkinter.PhotoImage(file=str(Koraidon / "fala.png")),
    "Sandwichincloud": tkinter.PhotoImage(file=str(Koraidon / "sandwichwcloud.png")),
    "sandwich": tkinter.PhotoImage(file=str(Koraidon / "sandwich.png")),
    "happy": tkinter.PhotoImage(file=str(Koraidon / "happy.png")),
    "anger": tkinter.PhotoImage(file=str(Koraidon / "anger.png")),
    "bed": tkinter.PhotoImage(file=str(Koraidon / "cama.png")),
    "bg": tkinter.PhotoImage(file=str(Koraidon / "fundo.png"))
}
root.geometry("300x80+580+600")
root.resizable(False, False)
root.title("Koraidon")
# root.overrideredirect(True)
root.wait_visibility(root)

#canvas.itemconfig(item_dentro_do_canvas, image=imagem_pra_colocar_no_lugar_a_1º)
canvas = tkinter.Canvas(root, width=sprit["bg"].width(), height=sprit["bg"].height(), highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=sprit["bg"])

def cama():
    bede = canvas.create_image(220, 35, anchor="nw") #normal é o x sendo 220
    canvas.itemconfig(bede, image=sprit["bed"])
    root.update()
    
cama()
if number1 == 225:
    kr = canvas.create_image(225, 20, anchor="nw", image=sprit["front"])
    canvas.itemconfig(kr, image=sprit["front"])
    root.update()
def rd():
    global number,number1
    if number > 20:
        number = 17

    number += 1
    canvas.moveto(kr, number1, number)
    canvas.after(300, rd)
rd()

cd1 = [1,0]
reserva = cd1[0]
def posicaokoraidon():
    global cd1, kr, number1, number, randomizarescolha, reserva
    cd1[0],cd1[1] = number1, number
    paradooumovendo = ""
    if randomizarescolha == 0:
        if cd1[0] == reserva:
                paradooumovendo = "parado"
        else:
            paradooumovendo = "indo para esquerda"
        print(f"{cd1} Ele está {paradooumovendo} {randomizarescolha}")
    else:
        if cd1[0] == reserva:
            paradooumovendo = "parado"
        else:
            paradooumovendo = "indo para direita"
        print(f"{cd1} Ele está {paradooumovendo} {randomizarescolha}")
    reserva = cd1[0]
    canvas.after(250, posicaokoraidon)

# posicaokoraidon()

def mover():
    global number1, number, reserva_contador, frenteprioridadeprimeiro, contador, randomizarescolha
    chancerandom = random.randint(1,3)
    contador = 1
    if chancerandom == 3:
        randomizarescolha = random.randint(0,1)
        posicaokoraidon()
        localaleatorio = random.randint(1,10)
        if reserva_contador == 0: # fará o primeiro movimento ser sempre pra esquerda, só uma vez
            randomizarescolha = 0
            reserva_contador = 1
        if randomizarescolha == 0: # ir para esquerda
            for i in range(20):
                time.sleep(0.2)
                number1 = number1 - localaleatorio
                # print(number1)
                if number1 < 25:
                    number1 = 25
                    break
                canvas.moveto(kr, number1, number)
                root.update()

                if contador == 4:
                    canvas.itemconfig(kr, image=sprit["leftway"])
                    root.update()
                elif contador == 1:
                    canvas.itemconfig(kr, image=sprit["leftway2"])
                    root.update()
                if contador == 1:
                    contador = 2
                elif contador == 2:
                    contador = 3
                elif contador == 3:
                    contador = 4
                elif contador == 4:
                    contador = 1
        elif randomizarescolha == 1: # ir para direita
            contador = 1
            for i in range(20):
                time.sleep(0.2)
                number1 = number1 + localaleatorio
                # print(number1)
                if number1 > 225:
                    number1 = 225
                    break
                canvas.moveto(kr, number1, number) # LEMBRETE SUPER IMPORTANTE, NUNCA COLOCAR ISTO DENTRO DA CONDIÇÃO KSKSK fica todo bugado "Tá travaaaaaaââÂâÂãÂ"
                root.update()

                if contador == 4:
                    canvas.itemconfig(kr, image=sprit["rightway2"])
                    root.update()
                elif contador == 1:
                    canvas.itemconfig(kr, image=sprit["rightway"])
                    root.update()
                if contador == 1:
                    contador = 2
                elif contador == 2:
                    contador = 3
                elif contador == 3:
                    contador = 4
                elif contador == 4:
                    contador = 1
    if frenteprioridadeprimeiro == 0:
        rmddefrenteecostas = "front"
        frenteprioridadeprimeiro = 1
    else:
        rmddefrenteecostas = random.choice(["back","front"])
    canvas.itemconfig(kr, image=sprit[rmddefrenteecostas])
    root.update()
    tempoaleatorio = random.choice([9000,5000,10000,8000,7000,1000])

    canvas.after(tempoaleatorio, mover)
reserva_contador, frenteprioridadeprimeiro = 0, 0
mover()

px1, py2 = number1 + 30, number + 5
contador = 0
def clickinteravel(event):
    global px1, py2, contador, intervalo
    px1, py2 = number1 + 30, number + 5
    # intervalo = time.time()
    if time.time() - intervalo >= 1:
        nomedict = random.choice(["heart","talk","happy","anger","Sandwichincloud"])
        if (nomedict == "talk") or (nomedict == "Sandwichincloud"):
            px1 = number1 - 7
        ht = canvas.create_image(px1, py2, anchor="nw", image=sprit[nomedict])
        canvas.itemconfig(ht, image=sprit[nomedict])
        for i in range(7):
            if (nomedict == "talk") or (nomedict == "Sandwichincloud"):              
                canvas.moveto(ht, px1, py2 - 7)
                root.update()
                time.sleep(0.1)
            elif nomedict == "anger":               
                canvas.moveto(ht, px1, py2 - 7)
                root.update()
                time.sleep(0.07)
            else:
                canvas.moveto(ht, px1, py2 - i)
                root.update()
                time.sleep(0.07)
        canvas.delete(ht)
    intervalo = time.time()

intervalo = time.time()
canvas.bind("<Button-1>", clickinteravel)

root.update()
root.mainloop()