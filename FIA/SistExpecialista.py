from customtkinter import *

tela = CTk()   
tela.geometry("800x600")

#Definindo variaveis para os botoes
Bsim = BooleanVar()
Bnao = BooleanVar()
Bsim.set(False)
Bnao.set(False)

fechar = False

#Usando StringVar para atualizar dinamicamente o texto do label
TXT = StringVar()
TXT.set("test")

#Definindo funcoes para os botoes
def sim():
    global Bsim
    Bsim.set(True)
      
def nao():
    global Bnao
    Bnao.set(True)
    
#Criando os widgets
title = CTkLabel(tela, text="Sistema Expecialista\nG.E.R.S.O.M", font=("Arial", 30))
title.pack(pady=100)

#Vinculando o texto do label ao StringVar
texto = CTkLabel(tela, textvariable=TXT, font=("Arial", 20))
texto.pack(pady=10)

#Definindo os comandos dos botoes sem argumentos
sim_button = CTkButton(tela, text="Sim", font=("Arial", 20), command=sim)
sim_button.place(x=250, y=450)

nao_button = CTkButton(tela, text="Não", font=("Arial", 20), command=nao)
nao_button.place(x=410, y=450)

#Processador:
#1.	Intel Core i9-11900K ou equivalente AMD Ryzen 9 5950X (Adobe After Effects, Cinema 4D)
#2.	Intel Core i9-10900K ou equivalente AMD Ryzen 9 5900X (Adobe After Effects)
#3.	Intel Core i9-9900K ou equivalente AMD Ryzen 9 3900X (World of Warcraft, Grand Theft Auto V)
#4.	Intel Core i7-11700K ou equivalente AMD Ryzen 7 5800X (Adobe Premiere Pro)
#5.	Intel Core i7-9700K ou equivalente AMD Ryzen 7 3700X (Adobe Premiere Pro, Avid Media Composer)
#6.	Intel Core i7-10700K ou equivalente AMD Ryzen 7 3700X (Adobe Illustrator)
#7.	Intel Core i7 / AMD Ryzen 7 ou superior (World of Warcraft, Grand Theft Auto V)
#8.	Intel Core i5-7600K ou equivalente AMD Ryzen 5 1600X (Adobe Photoshop)
#9.	Intel Core i5 / AMD Ryzen 5 ou superior (League of Legends, Counter-Strike: Global Offensive, Valorant, Fortnite, Apex Legends, Minecraft, Dota 2, Overwatch)
#10.	Intel Core i3-10100 (Audacity)
#11.	Intel Core i3-6300 (Apex Legends)
#12.	Intel Core i3-530 / AMD Phenom X3 8650 (Dota 2, Overwatch)
#13.	Intel Core i5-4460 / AMD Ryzen R5 1600X (Valorant)
#14.	Intel Core i3-4130 / AMD equivalente (League of Legends)
#15.	Intel Core i3-3225 (Fortnite)
#16.	Intel Core i3-3210 / AMD A8-7600 APU (Minecraft)
#17.	Intel Core 2 Quad CPU Q6600 / AMD Phenom 9850 Quad-Core Processor (GTA V)#
# 18.	Intel Core 2 Duo E8400 / AMD Phenom II X4 965 (Valorant)

# Memória RAM:
# 1.	64 GB DDR4 (Adobe After Effects, Cinema 4D, Avid Media Composer)
# 2.	32 GB DDR4 (Adobe Premiere Pro, Sony Vegas Pro, FL Studio, Final Cut Pro X)
# 3.	16 GB DDR4 (Adobe Photoshop, Adobe Illustrator)
# 4.	16 GB ou mais (World of Warcraft)
# 5.	8 GB DDR4 (Audacity)
# 6.	8 GB ou mais (League of Legends, Counter-Strike: Global Offensive, Valorant, Fortnite, Apex Legends, Minecraft, Grand Theft Auto V, Dota 2, Overwatch)
# 7.	4 GB (Minecraft)

# Placa de vídeo:
# 1.	NVIDIA GeForce RTX 3080 ou AMD Radeon RX 6800 XT (Adobe After Effects, Cinema 4D)
# 2.	NVIDIA GeForce RTX 3070 ou AMD Radeon RX 6700 XT (Adobe Premiere Pro, Sony Vegas Pro)
# 3.	NVIDIA GeForce RTX 3060 Ti ou AMD Radeon RX 6700 XT (Adobe Premiere Pro)
# 4.	NVIDIA GeForce RTX 3080 ou AMD Radeon RX 5700 (Adobe Photoshop)
# 5.	NVIDIA GeForce GTX 1660 Ti ou AMD Radeon RX 5700 (Adobe Photoshop, Adobe Illustrator)
# 6.	NVIDIA Quadro RTX 5000 (Avid Media Composer)
# 7.	AMD Radeon Pro W6800X (Final Cut Pro X)
# 8.	NVIDIA GeForce GTX 1080 / AMD Radeon RX Vega 64 ou superior (World of Warcraft, Grand Theft Auto V)
# 9.	NVIDIA GeForce GTX 1660 / AMD Radeon RX 580 ou superior (Minecraft, Dota 2, Overwatch)
# 10.	NVIDIA GeForce GTX 1060 / AMD Radeon RX 580 ou superior (League of Legends, Fortnite, Overwatch)
# 11.	NVIDIA GeForce GTX 1050 Ti / AMD Radeon RX 560 ou superior (Valorant, Counter-Strike: Global Offensive)
# 12.	NVIDIA GeForce GTX 970 / AMD Radeon R9 290 ou superior (Apex Legends)
# 13.	NVIDIA GeForce GTX 1050 Ti / AMD Radeon RX 560 ou superior (Valorant)
# 14.	NVIDIA GeForce GTX 1060 / AMD Radeon RX 570 ou superior (League of Legends)
# 15.	NVIDIA GeForce GTX 9800 GT 1GB / AMD HD 4870 1GB (GTA V)
# 16.	Intel HD Graphics 4000 / AMD Radeon R5 Series / NVIDIA GeForce 400 Series (Minecraft)
# 17.	NVIDIA GeForce GTX 8600/9600GT / ATI/AMD Radeon HD2600/3600 (Dota 2)

# Armazenamento:
# 1.	SSD NVMe de 2 TB (Adobe After Effects, Cinema 4D)
# 2.	SSD NVMe de 1 TB (Adobe Premiere Pro, Sony Vegas Pro)
# 3.	SSD NVMe de 512 GB (FL Studio, Adobe Illustrator)
# 4.	SSD de 512 GB (Adobe Photoshop)
# 5.	HDD de 256 GB (Audacity)
# 6.	100 GB (World of Warcraft)
# 7.	72 GB (Grand Theft Auto V)
# 8.	30 GB (Overwatch)
# 9.	22 GB (Apex Legends)
# 10.	20 GB (Fortnite)
# 11.	16 GB (League of Legends)
# 12.	15 GB (Counter-Strike: Global Offensive, Dota 2)
# 13.	7.2 GB (Valorant)
# 14.	4 GB (Minecraft)

#GERSOM: Gerenciamento Especializado em Recomendação Sofisticada e Optimizada de Máquinas
while fechar == False:
    
    resposta = ""
    processador = 99
    memoria = 99
    disco = 99
    placa_de_video = 99
    jogos = 0
    edicao = 0
    programacao = 0
    orcamento = 0
    setprocessador = ""
    setmemoria = ""
    setdisco = ""
    setplaca_de_video = ""

    TXT.set("Voce tem um orcamento alto para montar o computador?")
    while True:
        if Bsim.get() == True:
            orcamento = 1
            Bsim.set(False)
            break
        if Bnao.get() == True:
            orcamento = 0
            Bnao.set(False)
            break
        tela.update()

    TXT.set("Voce deseja usar seu computador para jogos?")
    while True:
        if Bsim.get() == True:
            jogos = 1
            Bsim.set(False)
            break
        if Bnao.get() == True:
            jogos = 0
            Bnao.set(False)
            break
        tela.update()
        
    TXT.set("Voce deseja usar seu computador para edicao audiovisual?")
    while True:
        if Bsim.get() == True:
            edicao = 1
            Bsim.set(False)
            break
        if Bnao.get() == True:
            edicao = 0
            Bnao.set(False)
            break
        tela.update()
        
    TXT.set("Voce deseja usar seu computador para programacao?")
    while True:
        if Bsim.get() == True:
            programacao = 1
            Bsim.set(False)
            break
        if Bnao.get() == True:
            programacao = 0
            Bnao.set(False)
            break
        tela.update()

    if jogos == 1:
        TXT.set("Falando sobre jogos \n Voce deseja jogar league of legends?")
        while True:
            if Bsim.get() == True:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 9:
                        processador = 9
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 10:
                        placa_de_video = 10
                    if disco > 11:
                        disco = 11
                break
            if Bnao.get() == True:
                Bnao.set(False)
                if orcamento == 0:
                    if processador > 14:
                        processador = 14
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 14:
                        placa_de_video = 14
                    if disco > 11:
                        disco = 11
                break
            tela.update()

        TXT.set("Voce deseja jogar Counter-Strike: Global Offensive?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 9:
                        processador = 9
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 11:
                        placa_de_video = 11
                    if disco > 15:
                        disco = 15
                else:
                    if processador > 18:
                        processador = 18
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 11:
                        placa_de_video = 11
                    if disco > 11:
                        disco = 11
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()
            
        TXT.set("Voce deseja jogar Valorant?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 9:
                        processador = 9
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 11:
                        placa_de_video = 11
                    if disco > 13:
                        disco = 13
                else:
                    if processador > 18:
                        processador = 18
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 13:
                        placa_de_video = 13
                    if disco > 13:
                        disco = 13
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()
                

        TXT.set("Voce deseja jogar Fortnite?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 9:
                        processador = 9
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 11:
                        placa_de_video = 11
                    if disco > 12:
                        disco = 12
                else:
                    if processador > 15:
                        processador = 15
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 10:
                        placa_de_video = 10
                    if disco > 10:
                        disco = 10
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja jogar Apex Legends?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 9:
                        processador = 9
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 12:
                        placa_de_video = 12
                    if disco > 9:
                        disco = 9
                else:
                    if processador > 15:
                        processador = 15
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 10:
                        placa_de_video = 10
                    if disco > 10:
                        disco = 10
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()


        TXT.set("Voce deseja jogar World of Warcraft?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 7:
                        processador = 7
                    if memoria > 4:
                        memoria = 4
                    if placa_de_video > 8:
                        placa_de_video = 8
                    if disco > 6:
                        disco = 6
                else:
                    if processador > 9:
                        processador = 9
                    if memoria > 4:
                        memoria = 4
                    if placa_de_video > 8:
                        placa_de_video = 8
                    if disco > 6:
                        disco = 6
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja jogar Minecraft?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 7:
                        processador = 7
                    if memoria > 4:
                        memoria = 4
                    if placa_de_video > 8:
                        placa_de_video = 8
                    if disco > 6:
                        disco = 6
                else:
                    if processador > 9:
                        processador = 9
                    if memoria > 4:
                        memoria = 4
                    if placa_de_video > 8:
                        placa_de_video = 8
                    if disco > 6:
                        disco = 6
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja jogar Grand Theft Auto V?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 7:
                        processador = 7
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 8:
                        placa_de_video = 8
                    if disco > 7:
                        disco = 7
                else:
                    if processador > 17:
                        processador = 17
                    if memoria > 4:
                        memoria = 4
                    if placa_de_video > 15:
                        placa_de_video = 15
                    if disco > 7:
                        disco = 7
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja jogar Dota 2?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 9:
                        processador = 9
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 9:
                        placa_de_video = 9
                    if disco > 12:
                        disco = 12
                else:
                    if processador > 12:
                        processador = 12
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 17:
                        placa_de_video = 17
                    if disco > 15:
                        disco = 15
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja jogar Overwatch?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 9:
                        processador = 9
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 9:
                        placa_de_video = 9
                    if disco > 8:
                        disco = 8
                else:
                    if processador > 12:
                        processador = 12
                    if memoria > 6:
                        memoria = 6
                    if placa_de_video > 10:
                        placa_de_video = 10
                    if disco > 8:
                        disco = 8
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

    if edicao == 1:
        TXT.set("Falando sobre edicao")
        TXT.set("Voce deseja usar Adobe Photoshop?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if processador > 8:
                    processador = 8
                if memoria > 3:
                    memoria = 3
                if placa_de_video > 4:
                    placa_de_video = 4
                if disco > 4:
                    disco = 4
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja usar Adobe Premiere Pro?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 4:
                        processador = 4
                    if memoria > 2:
                        memoria = 2
                    if placa_de_video > 2:
                        placa_de_video = 2
                    if disco > 2:
                        disco = 2
                else:
                    if processador > 6:
                        processador = 6
                    if memoria > 2:
                        memoria = 2
                    if placa_de_video > 3:
                        placa_de_video = 3
                    if disco > 2:
                        disco = 2
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja usar Adobe After Effects?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 1:
                        processador = 1
                    if memoria > 1:
                        memoria = 1
                    if placa_de_video > 1:
                        placa_de_video = 1
                    if disco > 1:
                        disco = 1
                else:
                    if processador > 2:
                        processador = 2
                    if memoria > 1:
                        memoria = 1
                    if placa_de_video > 1:
                        placa_de_video = 1
                    if disco > 1:
                        disco = 1
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja usar Sony Vegas Pro?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 4:
                        processador = 4
                    if memoria > 2:
                        memoria = 2
                    if placa_de_video > 2:
                        placa_de_video = 2
                    if disco > 2:
                        disco = 2
                else:
                    if processador > 6:
                        processador = 6
                    if memoria > 2:
                        memoria = 2
                    if placa_de_video > 2:
                        placa_de_video = 2
                    if disco > 2:
                        disco = 2
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja usar Final Cut Pro X?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 4:
                        processador = 4
                    if memoria > 2:
                        memoria = 2
                    if placa_de_video > 7:
                        placa_de_video = 7
                    if disco > 2:
                        disco = 2
                else:
                    if processador > 6:
                        processador = 6
                    if memoria > 2:
                        memoria = 2
                    if placa_de_video > 7:
                        placa_de_video = 7
                    if disco > 2:
                        disco = 2
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja usar Avid Media Composer?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if orcamento == 1:
                    if processador > 6:
                        processador = 6
                    if memoria > 5:
                        memoria = 5
                    if placa_de_video > 6:
                        placa_de_video = 6
                    if disco > 5:
                        disco = 5
                else:
                    if processador > 6:
                        processador = 6
                    if memoria > 5:
                        memoria = 5
                    if placa_de_video > 6:
                        placa_de_video = 6
                    if disco > 5:
                        disco = 5
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja usar Audacity?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if processador > 10:
                    processador = 10
                if memoria > 5:
                    memoria = 5
                if placa_de_video > 17:
                    placa_de_video = 17
                if disco > 5:
                    disco = 5
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja usar FL Studio?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if processador > 4:
                    processador = 4
                if memoria > 2:
                    memoria = 2
                if placa_de_video > 17:
                    placa_de_video = 17
                if disco > 3:
                    disco = 3
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

        TXT.set("Voce deseja usar Adobe Illustrator?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if processador > 5:
                    processador = 5
                if memoria > 3:
                    memoria = 3
                if placa_de_video > 5:
                    placa_de_video = 5
                if disco > 3:
                    disco = 3
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()
        
        TXT.set("Voce deseja usar Cinema 4D?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                if processador > 1:
                    processador = 1
                if memoria > 1:
                    memoria = 1
                if placa_de_video > 1:
                    placa_de_video = 1
                if disco > 1:
                    disco = 1
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                break
            tela.update()

    if programacao == 1:
            if processador > 9:
                processador = 9
            if memoria > 6:
                memoria = 6
            if placa_de_video > 11:
                placa_de_video = 11
            if disco > 12:
                disco = 12

    if jogos == 0 and edicao == 0 and programacao == 0:
        TXT.set("Voce deseja usar seu computador para tarefas basicas?")
        while True:
            if Bsim.get() == TRUE:
                Bsim.set(False)
                TXT.set("Compra um notebook novo, qualquer um serve para voce")
                tela.update()
                break
            if Bnao.get() == TRUE:
                Bnao.set(False)
                TXT.set("Compra um celular, nao precisa de computador")
                tela.update()
                break
            tela.update()

    if jogos == 1 or edicao == 1 or programacao == 1:
        if processador == 99 and memoria == 99 and placa_de_video == 99 and disco == 99:
            TXT.set("Nao foi possivel encontrar um computador ideal para voce")

    match processador:
        case 1:
            setprocessador = "Processador: Intel Core i9-11900K ou equivalente AMD Ryzen 9 5950X"
        case 2:
            setprocessador = "Processador: Intel Core i9-10900K ou equivalente AMD Ryzen 9 5900X"
        case 3:
            setprocessador = "Processador: Intel Core i9-9900K ou equivalente AMD Ryzen 9 3900X"
        case 4:
            setprocessador = "Processador: Intel Core i7-11700K ou equivalente AMD Ryzen 7 5800X"
        case 5:
            setprocessador = "Processador: Intel Core i7-10700K ou equivalente AMD Ryzen 7 3700X"
        case 6:
            setprocessador = "Processador: Intel Core i7-9700K ou equivalente AMD Ryzen 7 3700X"
        case 7:
            setprocessador = "Processador: Intel Core i7-9700 ou equivalente AMD Ryzen 7 3700"
        case 8:
            setprocessador = "Processador: Intel Core i5-9600k ou equivalente AMD Ryzen 5 3600"
        case 9:
            setprocessador = "Processador: Intel Core i5-9400 ou equivalente AMD Ryzen 5 2600"
        case 10:
            setprocessador = "Processador: Intel Core i3-10100"
        case 11:
            setprocessador = "Processador: Intel Core i3-6300"
        case 12:
            setprocessador = "Processador: Intel Core i3-530 / AMD Phenom X3 8650"
        case 13:
            setprocessador = "Processador: Intel Core i5-4460 / AMD Ryzen R5 1600X"
        case 14:
            setprocessador = "Processador: Intel Core i3-4130 / AMD equivalente"
        case 15:
            setprocessador = "Processador: Intel Core i3-3225"
        case 16:
            setprocessador = "Processador: Intel Core i3-3210 / AMD A8-7600 APU"
        case 17:
            setprocessador = "Processador: Intel Core 2 Quad CPU Q6600 / AMD Phenom 9850 Quad-Core Processor"
        case 18:
            setprocessador = "Processador: Intel Core 2 Duo E8400 / AMD Phenom II X4 965"

    match memoria:
        case 1:
            setmemoria = "Memoria RAM: 64 GB DDR4"
        case 2:
            setmemoria = "Memoria RAM: 32 GB DDR4"
        case 3:
            setmemoria = "Memoria RAM: 16 GB DDR4 ou mais"
        case 4:
            setmemoria = "Memoria RAM: 16 GB DDR4"
        case 5:
            setmemoria = "Memoria RAM: 8 GB DDR4 ou mais"
        case 6:
            setmemoria = "Memoria RAM: 8 GB"
        case 7:
            setmemoria = "Memoria RAM: 4 GB"

    match placa_de_video:
        case 1:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce RTX 3080 ou AMD Radeon RX 6800 XT"
        case 2:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce RTX 3070 ou AMD Radeon RX 6700 XT"
        case 3:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce RTX 3060 Ti ou AMD Radeon RX 6700 XT"
        case 4:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce RTX 3080 ou AMD Radeon RX 5700"
        case 5:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 1660 Ti ou AMD Radeon RX 5700"
        case 6:
            setplaca_de_video = "Placa de vídeo: NVIDIA Quadro RTX 5000"
        case 7:
            setplaca_de_video = "Placa de vídeo: AMD Radeon Pro W6800X"
        case 8:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 1080 / AMD Radeon RX Vega 64 ou superior"
        case 9:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 1660 / AMD Radeon RX 580 ou superior"
        case 10:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 1060 / AMD Radeon RX 580 ou superior"
        case 11:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 1050 Ti / AMD Radeon RX 560 ou superior"
        case 12:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 970 / AMD Radeon R9 290 ou superior"
        case 13:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 1050 Ti / AMD Radeon RX 560 ou superior"
        case 14:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 1060 / AMD Radeon RX 570 ou superior"
        case 15:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 9800 GT 1GB / AMD HD 4870 1GB"
        case 16:
            setplaca_de_video = "Placa de vídeo: Intel HD Graphics 4000 / AMD Radeon R5 Series / NVIDIA GeForce 400 Series"
        case 17:
            setplaca_de_video = "Placa de vídeo: NVIDIA GeForce GTX 8600/9600GT / ATI/AMD Radeon HD2600/3600"

    if jogos == 1 and edicao == 1 and programacao == 1 or jogos == 1 and edicao == 1 and programacao == 0 or jogos == 0 and edicao == 1 and programacao == 1 or jogos == 1 and edicao == 0 and programacao == 1:
        if disco > 4:
            disco = 4
    else:
        if jogos == 0 and edicao == 0 and programacao == 0:
            disco = 0
        else:
            if disco > 5:
                disco = 5

    match disco:
        case 1:
            setdisco = "Armazenamento: SSD NVMe de 2 TB"
        case 2:
            setdisco = "Armazenamento: SSD NVMe de 1 TB"
        case 3:
            setdisco = "Armazenamento: SSD NVMe de 512 GB"
        case 4:
            setdisco = "Armazenamento: SSD de 512 GB"
        case 5:
            setdisco = "Armazenamento: SSD de 256 GB"

    if jogos == 1 or edicao == 1 or programacao == 1:
        TXT.set("Seu Computador Ideal:\n" + setprocessador + "\n" + setmemoria + "\n" + setplaca_de_video + "\n" + setdisco + "\nDeseja fazer outra configuracao?")
        
    while True:
        if Bsim.get() == TRUE:
            Bsim.set(False)
            processador = 99
            memoria = 99
            placa_de_video = 99
            disco = 99
            break
        if Bnao.get() == TRUE:
            Bnao.set(False)
            tela.destroy()
            fechar = True
            break
        tela.update()
    
tela.mainloop()
