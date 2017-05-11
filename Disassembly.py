# Arquivo que gera o código em hexadecimal apartir do código em assembly MIPS

fileIn = open("teste.asm", "r")
fileOut = open("teste.txt", "w")

functions = {'sub':34}
type_r = { 'addu':0, 'addiu':0 , 'subu':0, 'sub':0, 'or':0, 'slt':0, 'sll':0, 'srl':0 }
type_i = ["xori", "lui", "sltiu", "andi", "beq", "bne"]
type_j = ["j"]
type_i_special = ["lw", "sw"]
register = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0",
            "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1",
            "$s2", "$s3", "$s4", "$s5","$s6", "$s7", "$t8", "$t9", "$k0",
            "$k1", "$gp", "$sp", "$fp", "$ra"]



def decode_r(ins, rd, rs, rt): # precisa colocar com os tamanhos de bits certinhos, ins = 6 bits; rs,rt,rd,shamt = 6 bits e etc
    shamt = 0
    instruction = int( bin(type_r[ins]).replace('0b','') )
    print(instruction)
    reg1 = int( bin(register.index(rs)).replace('0b','') )
    print(reg1)
    reg2 = int( bin(register.index(rt)).replace('0b','') )
    print(reg2)
    reg3 = int( bin(register.index(rd)).replace('0b','') )
    print(reg3)
    fun = int( hex(functions[ins]).replace('0x','') )
    print(fun)
    out = hex(instruction + reg1 + reg2 + reg3 + shamt + fun)
    print(out)

def decode_i(rt, rs, im):
    print("Compara " + rt + " com " + rs + " e salta ou não para " + im)


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
