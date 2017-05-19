"""
Program that generates code in assembly language from code in hexadecimal
"""

input = open("input.txt", "r")
output = open("output.asm", "w")

functions = {'sub':34, 'or':37, 'addu':33, 'subu':35, 'slt':42, 'sll':0, 'srl':2 }
type_r = { 'addu':0, 'subu':0, 'sub':0, 'or':0, 'slt':0, 'sll':0, 'srl':0 }
type_i = {'addiu':9, "xori":14, "sltiu":11, "andi":12}
type_i_branch = {"bne":5, "beq":4}
type_i_save_load_lui = {"lw":35, "sw":43, "lui":15}
type_j = {"j":2}
register = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0",
            "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1",
            "$s2", "$s3", "$s4", "$s5","$s6", "$s7", "$t8", "$t9", "$k0",
            "$k1", "$gp", "$sp", "$fp", "$ra"]

file_out = [".text\n", ".globl  main\n\n", "main:\n"]
# coisa.fill



# aux = hex(input)
# vetor = aux.split('x')
# vetor = vetor[0] #vetor agora possui binario


def print_file():
    for line in file_out:
        output.write(line)

def converteBinario(decimal):
    output = ""
    #converte binarios com numero de bits adequados

    for i in range(0, len(decimal) - 1):
        aux = decimal[i]
        aux = bin( int(aux, 16) )[2:].zfill(4)
        output = output + aux

    return output


def separaBinario():
    return 0
    #separa o todo para cada instrução

def binarioParaInstrucao():
    return 0
    #le o binario e retorna a instrução    


file = input.readlines()

for line in file:
    line = line[2:]
    line = converteBinario(line)
    line = int(line[6:], 2)
    print(line)

    if int(line) == 0:
        print_file("Achei uma instrução da ULA, teste")



print_file()


input.close()
output.close()