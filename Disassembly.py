# Arquivo que gera o código em hexadecimal apartir do código em assembly MIPS

fileIn = open("teste.asm", "r")
fileOut = open("teste.txt", "w")

def decode_R(rt, rs, rd):
    print("Soma " + rt + " com " + rs + " e armazena em " + rd)

def decode_I(rt, rs, im):
    print("Compara " + rt + " com " + rs + " e salta ou não para " + im)



for line in fileIn:
    instruction = line.split()

    for i in range(0, len(instruction)): # elimina as virgulas e espacos dos elementos do array
        instruction[i] = instruction[i].strip(",")

    if instruction[0] == "add" or instruction[0] == "sub":
        decode_R(instruction[2], instruction[3], instruction[1])

    if instruction[0] == "beq" or instruction[0] == "bne":
        decode_I(instruction[1], instruction[2], instruction[3])