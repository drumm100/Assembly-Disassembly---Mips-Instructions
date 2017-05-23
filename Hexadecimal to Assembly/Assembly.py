"""
Program that generates code in assembly language from code in hexadecimal
"""

input = open("Input.txt", "r")
output = open("output.asm", "w")

functions = {34:'sub', 37:'or', 33:'addu', 35:'subu', 42:'slt', 0:'sll', 2:'srl' }
type_i = {9:'addiu', 14:"xori", 11:"sltiu", 12:"andi"}
type_i_branch = {5:"bne", 4:"beq"}
type_i_save_load_lui = {35:"lw", 43:"sw", 15:"lui"}
type_j = {2:"j"}
register = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0",
            "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1",
            "$s2", "$s3", "$s4", "$s5","$s6", "$s7", "$t8", "$t9", "$k0",
            "$k1", "$gp", "$sp", "$fp", "$ra"]

file_out = [".text\n", ".globl  main\n\n", "main:\n"]


def print_file():
    for line in file_out:
        output.write(line)

def converteBinario(hexadecimal):
    output = "" #binario final

    #converte binarios com numero de bits adequados
    
    aux = hexadecimal.split('x')
    hexadecimal = aux[1] #(014b482a)
    
    for i in range(0, len(hexadecimal) - 1):

        aux = hexadecimal[i]  # i=0, aux = 0
        aux = bin( int(aux, 16) )[2:].zfill(4)
        output = output + aux

    return output


def separaBinario(binario):
    opcode_binario = binario[:6]
    opcode_decimal = int(opcode_binario,2)

    f



    #separa o todo para cada instrução



    return 0
    #separa o todo para cada instrução

def binarioParaInstrucao():
    return 0
    #le o binario e retorna a instrução    


file = input.readlines()

for line in file:
    #line = line[2:]
    line = converteBinario(line)
    #line = int(line[6:], 2)
    print(line)

    if int(line) == 0:
        print_file("Achei uma instrução da ULA, teste")



print_file()


input.close()
output.close()