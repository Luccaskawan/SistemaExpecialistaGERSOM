processador = 99
memoria = 99
disco = 99
placa_de_video = 99
jogos = 0
edicao = 0
programacao = 0
orcamento = 0

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

print("Bem vindo ao SistExpecialista GERSOM para montagem de maquinas")
print("Responda as perguntas para montar o computador ideal para voce")
print("Voce tem um orcamento alto para montar o computador?")
resposta = input("Digite S ou N: ")
if resposta == "S":
    orcamento = 1
else:
    orcamento = 0

print("Voce deseja usar seu computador para jogos?")
resposta = input("Digite S ou N: ")
if resposta == "S":
    jogos = 1
else:
    jogos = 0


print("Voce deseja usar seu computador para edicao audiovisual?")
resposta = input("Digite S ou N: ")
if resposta == "S":
    edicao = 1
else:
    edicao = 0

print("Voce deseja usar seu computador para programacao?")
resposta = input("Digite S ou N: ")
if resposta == "S":
    programacao = 1
else:
    programacao = 0

if jogos == 1:
    print("Falando sobre jogos")
    print("Voce deseja jogar league of legends?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
        if orcamento == 1:
            if processador > 9:
                processador = 9
            if memoria > 6:
                memoria = 6
            if placa_de_video > 10:
                placa_de_video = 10
            if disco > 11:
                disco = 11
        else:
            if processador > 14:
                processador = 14
            if memoria > 6:
                memoria = 6
            if placa_de_video > 14:
                placa_de_video = 14
            if disco > 11:
                disco = 11

    print("Voce deseja jogar Counter-Strike: Global Offensive?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja jogar Valorant?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja jogar Fortnite?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja jogar Apex Legends?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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
            if processador > 12:
                processador = 12
            if memoria > 6:
                memoria = 6
            if placa_de_video > 12:
                placa_de_video = 12
            if disco > 9:
                disco = 9

    print("Voce deseja jogar World of Warcraft?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja jogar Minecraft?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
        if orcamento == 1:
            if processador > 9:
                processador = 9
            if memoria > 6:
                memoria = 6
            if placa_de_video > 9:
                placa_de_video = 9
            if disco > 14:
                disco = 14
        else:
            if processador > 16:
                processador = 16
            if memoria > 6:
                memoria = 6
            if placa_de_video > 16:
                placa_de_video = 16
            if disco > 14:
                disco = 14

    print("Voce deseja jogar Grand Theft Auto V?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja jogar Dota 2?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja jogar Overwatch?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

if edicao == 1:
    print("Falando sobre edicao")
    print("Voce deseja usar Adobe Photoshop?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
            if processador > 8:
                processador = 8
            if memoria > 3:
                memoria = 3
            if placa_de_video > 4:
                placa_de_video = 4
            if disco > 4:
                disco = 4

    print("Voce deseja usar Adobe Premiere Pro?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja usar Adobe After Effects?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja usar Sony Vegas Pro?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja usar Final Cut Pro X?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja usar Avid Media Composer?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
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

    print("Voce deseja usar Audacity?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
        if processador > 10:
            processador = 10
        if memoria > 5:
            memoria = 5
        if placa_de_video > 17:
            placa_de_video = 17
        if disco > 5:
            disco = 5

    print("Voce deseja usar FL Studio?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
        if processador > 4:
            processador = 4
        if memoria > 2:
            memoria = 2
        if placa_de_video > 17:
            placa_de_video = 17
        if disco > 3:
            disco = 3

    print("Voce deseja usar Adobe Illustrator?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
        if processador > 5:
            processador = 5
        if memoria > 3:
            memoria = 3
        if placa_de_video > 5:
            placa_de_video = 5
        if disco > 3:
            disco = 3
    
    print("Voce deseja usar Cinema 4D?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
        if processador > 1:
            processador = 1
        if memoria > 1:
            memoria = 1
        if placa_de_video > 1:
            placa_de_video = 1
        if disco > 1:
            disco = 1

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
    print("Voce deseja usar seu computador para tarefas basicas?")
    resposta = input("Digite S ou N: ")
    if resposta == "S":
        print("Compra um notebook novo, qualquer um serve para voce")   
    else:
        print("Compra um celular, nao precisa de computador")

if jogos == 1 or edicao == 1 or programacao == 1:
    print("Computador ideal para voce")
    if processador == 0 and memoria == 0 and placa_de_video == 0 and disco == 0:
        print("Nao foi possivel encontrar um computador ideal para voce")

match processador:
    case 1:
        print("Processador: Intel Core i9-11900K ou equivalente AMD Ryzen 9 5950X")
    case 2:
        print("Processador: Intel Core i9-10900K ou equivalente AMD Ryzen 9 5900X")
    case 3:
        print("Processador: Intel Core i9-9900K ou equivalente AMD Ryzen 9 3900X")
    case 4:
        print("Processador: Intel Core i7-11700K ou equivalente AMD Ryzen 7 5800X")
    case 5:
        print("Processador: Intel Core i7-10700K ou equivalente AMD Ryzen 7 3700X")
    case 6:
        print("Processador: Intel Core i7-9700K ou equivalente AMD Ryzen 7 3700X")
    case 7:
        print("Processador: Intel Core i7-9700 ou equivalente AMD Ryzen 7 3700")
    case 8:
        print("Processador: Intel Core i5-9600k ou equivalente AMD Ryzen 5 3600")
    case 9:
        print("Processador: Intel Core i5-9400 ou equivalente AMD Ryzen 5 2600")
    case 10:
        print("Processador: Intel Core i3-10100")
    case 11:
        print("Processador: Intel Core i3-6300")
    case 12:
        print("Processador: Intel Core i3-530 / AMD Phenom X3 8650")
    case 13:
        print("Processador: Intel Core i5-4460 / AMD Ryzen R5 1600X")
    case 14:
        print("Processador: Intel Core i3-4130 / AMD equivalente")
    case 15:
        print("Processador: Intel Core i3-3225")
    case 16:
        print("Processador: Intel Core i3-3210 / AMD A8-7600 APU")
    case 17:
        print("Processador: Intel Core 2 Quad CPU Q6600 / AMD Phenom 9850 Quad-Core Processor")
    case 18:
        print("Processador: Intel Core 2 Duo E8400 / AMD Phenom II X4 965")

match memoria:
    case 1:
        print("Memoria RAM: 64 GB DDR4")
    case 2:
        print("Memoria RAM: 32 GB DDR4")
    case 3:
        print("Memoria RAM: 16 GB DDR4 ou mais")
    case 4:
        print("Memoria RAM: 16 GB DDR4")
    case 5:
        print("Memoria RAM: 8 GB DDR4 ou mais")
    case 6:
        print("Memoria RAM: 8 GB")
    case 7:
        print("Memoria RAM: 4 GB")

match placa_de_video:
    case 1:
        print("Placa de vídeo: NVIDIA GeForce RTX 3080 ou AMD Radeon RX 6800 XT")
    case 2:
        print("Placa de vídeo: NVIDIA GeForce RTX 3070 ou AMD Radeon RX 6700 XT")
    case 3:
        print("Placa de vídeo: NVIDIA GeForce RTX 3060 Ti ou AMD Radeon RX 6700 XT")
    case 4:
        print("Placa de vídeo: NVIDIA GeForce RTX 3080 ou AMD Radeon RX 5700")
    case 5:
        print("Placa de vídeo: NVIDIA GeForce GTX 1660 Ti ou AMD Radeon RX 5700")
    case 6:
        print("Placa de vídeo: NVIDIA Quadro RTX 5000")
    case 7:
        print("Placa de vídeo: AMD Radeon Pro W6800X")
    case 8:
        print("Placa de vídeo: NVIDIA GeForce GTX 1080 / AMD Radeon RX Vega 64 ou superior")
    case 9:
        print("Placa de vídeo: NVIDIA GeForce GTX 1660 / AMD Radeon RX 580 ou superior")
    case 10:
        print("Placa de vídeo: NVIDIA GeForce GTX 1060 / AMD Radeon RX 580 ou superior")
    case 11:
        print("Placa de vídeo: NVIDIA GeForce GTX 1050 Ti / AMD Radeon RX 560 ou superior")
    case 12:
        print("Placa de vídeo: NVIDIA GeForce GTX 970 / AMD Radeon R9 290 ou superior")
    case 13:
        print("Placa de vídeo: NVIDIA GeForce GTX 1050 Ti / AMD Radeon RX 560 ou superior")
    case 14:
        print("Placa de vídeo: NVIDIA GeForce GTX 1060 / AMD Radeon RX 570 ou superior")
    case 15:
        print("Placa de vídeo: NVIDIA GeForce GTX 9800 GT 1GB / AMD HD 4870 1GB")
    case 16:
        print("Placa de vídeo: Intel HD Graphics 4000 / AMD Radeon R5 Series / NVIDIA GeForce 400 Series")
    case 17:
        print("Placa de vídeo: NVIDIA GeForce GTX 8600/9600GT / ATI/AMD Radeon HD2600/3600")

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
        print("Armazenamento: SSD NVMe de 2 TB")
    case 2:
        print("Armazenamento: SSD NVMe de 1 TB")
    case 3:
        print("Armazenamento: SSD NVMe de 512 GB")
    case 4:
        print("Armazenamento: SSD de 512 GB")
    case 5:
        print("Armazenamento: SSD de 256 GB")

print("Fim do programa")
