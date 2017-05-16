# Arquivo que gera o código em hexadecimal apartir do código em assembly MIPS
# Comentario teste
fileIn = open("teste.asm", "r")
fileOut = open("teste.txt", "w")

functions = {'sub':34, 'or':37, 'addu':33, 'subu':35, 'slt':42, 'sll':0, 'srl':2 } # Codigo de cada funcao na ULA
#imm funcions: addiu, xori, lui, sltiu, andi,   
#offset: beq, bne, lw, sw
#target: j
type_r = { 'addu':0, 'subu':0, 'sub':0, 'or':0, 'slt':0, 'sll':0, 'srl':0 } # Instrucoes do tipo R
type_i = {'addiu':9, "xori":14, "lui":15, "sltiu":11, "andi":12, "lw":35, "sw":43} # Instrucoes do tipo I
type_i_branch = {"bne":5, "beq":4}
type_j = {"j":2} #Instrucoes do tipo J

register = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0",
            "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1",
            "$s2", "$s3", "$s4", "$s5","$s6", "$s7", "$t8", "$t9", "$k0",
            "$k1", "$gp", "$sp", "$fp", "$ra"]



def two_complements(binario):
    print("Numero que estou usando: " + binario)
    trigger = 0
    out = ""
    array = [None] * len(binario)

    for x in range(0, len(binario)):
        array[x] = binario[x]

    print("len binario: " + str(len(binario)))
    print("len array: " + str(len(array)))

    print(array[0])
    for i in range(len(array)-1, -1, -1):
        if trigger == 1:
            if array[i] == "1":
                array[i] = "0"
            else:
                array[i] = "1"

        if array[i] == "1":
            trigger = 1

    for j in range(0, len(array)):
        out = out + array[j]

    return out

def find_label(label, currentLine):
    none_ins = 0

    label = label+':\n'
    print(label)
    if currentLine > file.index(label): it = -1
    else: it = 1

    for i in range( currentLine+1, file.index(label), it ):
        aux = file[i].split()
        if len(aux) == 1: none_ins += 1

    out = file.index(label) - (currentLine + 1)
    if out < 0: out += none_ins + 1
    else: out -= none_ins

    return out


def decode_r(ins, rd, rs, rt):
    shamt = '0'

    instruction = bin(type_r[ins])[2:].zfill(6)

    if ins == "sll" or ins == "srl":
        out_rs = '00000'
        shamt = bin(int(rt))[2:].zfill(5)
        fun = bin(functions[ins])[2:].zfill(6)
        out_rt = bin(register.index(rs))[2:].zfill(5)

    else:
        out_rs = bin(register.index(rs))[2:].zfill(5)
        shamt = bin(int(shamt.zfill(6)))[2:].zfill(5)
        fun = bin(functions[ins])[2:].zfill(6)
        out_rt = bin(register.index(rt))[2:].zfill(5)


    out_rd = bin(register.index(rd))[2:].zfill(5)


    outBin = instruction + out_rs + out_rt + out_rd + shamt + fun
    #print(outBin)
    output = "0x"

    for i in range(0, len(outBin) - 3, 4 ):
        aux = outBin[i : i+4]
        #print(aux)
        aux = int(aux, 2)
        aux = hex(aux)[2:]
        #print(aux)
        output = output + aux
        #print(aux)

    fileOut.write(output+'\n')


# def decode_i(ins, r1, r2, im, line):
#     if ins == "addiu" or ins == "xori" or ins == "sltiu" or ins == "andi":
#         instruction = bin(type_r[ins])[2:].zfill(6)
#
#         out_r2 = bin(register.index(r2))[2:].zfill(5)
#         out_r1 = bin(register.index(r1))[2:].zfill(5)
#         imm =
#
#         outBin = instruction + out_r2 + out_r1 + imm


    # addiu r1, r2, im | opcode(6) ; r2 ; r1 ; imm(16)
    # xori r1, r2, im  | opcode(6) ; r2 ; r1 ; imm(16)
    # lui r1, r2       | opcode(6) ; 0 ; r1 ; r2(16)       --- caso especial
    # sltiu r1, r2, imm | opcode(6) ; r2 ; r1 ; im(16)
    # andi r1, r2, imm | opcode(6) ; r2 ; r1 ; im(16)
    # lw r1, imm       | opcode(6) ; r1 ; r2 ; imm(16)    --- caso especial
    # sw r1, imm       | opcode(6) ; r1 ; r2 ; imm(16)    --- caso especial


def decode_branch(ins, rs, rt, label, line):
    #print(line)
    #print(find_label(label, line))

    instruction = bin(type_i_branch[ins])[2:].zfill(6)
    out_rs = bin(register.index(rs))[2:].zfill(5)
    out_rt = bin(register.index(rt))[2:].zfill(5)
    findLine = find_label(label, line)
    print(findLine)

    if findLine < 0:

        aux = bin(findLine)[3:].zfill(16)
        offset = two_complements(aux)
        print(offset)
    else:
        offset = bin(findLine)[2:].zfill(16)

    outBin = instruction + out_rs + out_rt + offset
    print(outBin)
    print(len(outBin))
    output = "0x"

    for i in range(0, len(outBin) - 3, 4 ):
        aux = outBin[i : i+4]
        print(aux)
        aux = int(aux, 2)
        aux = hex(aux)[2:]
        print(aux)
        output = output + aux
        print(aux)

    fileOut.write(output+'\n')


file = fileIn.readlines()
for item in range(0, len(file) - 1):
    if item >= len(file): break
    if ".text" in file[item]: file.pop(item)
    if ".globl" in file[item]:file.pop(item)
    #if "main:" in file[item]: file.pop(item)

for xline in file:
    if xline == '\n': file.remove(xline)

print(file)

for line in file:
    if line != '\n':
        instruction = line.split()

        for i in range(0, len(instruction)):
            instruction[i] = instruction[i].strip(",")

        if instruction[0] in type_r:
            decode_r(instruction[0], instruction[1], instruction[2], instruction[3])
        if instruction[0] in type_i_branch:
            decode_branch(instruction[0], instruction[1], instruction[2], instruction[3], file.index(line))


fileIn.close()
fileOut.close()
