# Arquivo que gera o código em hexadecimal apartir do código em assembly MIPS
# Comentario teste
fileIn = open("teste.asm", "r")
fileOut = open("teste.txt", "w")

functions = {'sub':34, 'or':37, 'addu':33, 'subu':35, 'slt':42, 'sll':0, 'srl':2  } # Codigo de cada funcao na ULA
#imm funcions: addiu, xori, lui, sltiu, andi,   
#offset: beq, bne, lw, sw
#target: j
type_r = { 'addu':0, 'addiu':9 , 'subu':0, 'sub':0, 'or':0, 'slt':0, 'sll':0, 'srl':0 } # Instrucoes do tipo R
type_i = ["xori":14, "lui":15, "sltiu":11, "andi":12, "beq":4, "bne":5] # Instrucoes do tipo I
type_j = ["j":2] #Instrucoes do tipo J
type_i_special = ["lw":35, "sw":43] # Instrucoes especiais

register = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", # registradores do MIPS
            "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1",
            "$s2", "$s3", "$s4", "$s5","$s6", "$s7", "$t8", "$t9", "$k0",
            "$k1", "$gp", "$sp", "$fp", "$ra"]



def decode_r(ins, rd, rs, rt):
    shamt = '0'



    instruction = bin(type_r[ins])[2:].zfill(6)
    reg1 = bin(register.index(rs))[2:].zfill(5)
    reg2 = bin(register.index(rt))[2:].zfill(5)
    reg3 = bin(register.index(rd))[2:].zfill(5)
    shamt = bin( int(shamt.zfill(6)) )[2:].zfill(5)
    fun = bin(functions[ins])[2:].zfill(6)

    outBin = instruction + reg1 + reg2 + reg3 + shamt + fun
    output = "0x"

    for i in range(0, len(outBin) - 3, 4 ):
        aux = outBin[i : i+4]
        aux = int(aux, 2)
        aux = hex(aux)[2:]
        output = output + aux

    fileOut.write(output+'\n')


def decode_i(rt, rs, im):
    print("FAZER")


for line in fileIn:
    if line != '\n':
        instruction = line.split()

        for i in range(0, len(instruction)):  # elimina as virgulas e espacos dos elementos do array
            instruction[i] = instruction[i].strip(",")
            #instruction[i] = instruction[i].strip(" ")

        if instruction[0] in type_r:
            decode_r(instruction[0], instruction[1], instruction[2], instruction[3])

        if instruction[0] in type_i:
            decode_i(instruction[1], instruction[2], instruction[3])

fileIn.close()
fileOut.close()
