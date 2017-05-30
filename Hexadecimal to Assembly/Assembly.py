"""
Program that generates code in assembly language from code in hexadecimal
"""
import random


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

words = ['label', 'label2', 'label3', 'label4', 'label5', 'loop', 'volta', 'denovo', 'vuelta']
labels = {}
###### tamanho do arquivo | imm
file_out = [".text\n", ".globl  main\n\n", "main:\n"]

def two_complements(binario):
    trigger = 0
    out = ""
    array = [None] * len(binario)


    for x in range(0, len(binario)):
        array[x] = binario[x]

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

    out = (-1)*int(out,2)
    return out
   
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

def already_value(val):
    aux = 0
    for item in labels:
        if labels.get(item) == val:
            aux += 1
    return aux > 1

def print_labels():
    for dic in labels:
        #aux = labels.get(dic, "nao achei")
        #boolean = already_value(aux)
        #if not(boolean):
        file_out.insert(labels[dic], "\n"+dic+"\n")

def decode_r(binary):
    #000000|01010|01011|01001|00000|101010 sem shift

    #000000|00000|01001|01000|00100|000010 com shift

    func = int(binary[26:], 2) #->[2]
    func = functions[func]     #->[srl]

    rs = int(binary[6:11],2)
    rs = register[rs]

    rt = int(binary[11:16],2)
    rt = register[rt]

    rd = int(binary[16:21],2)
    rd = register[rd]

    shamt = int(binary[21:26],2)

    if shamt != 0:
        aux = rt
        rt = shamt
        rs = aux
    
    out = '\t' +func+', '+rd+', '+rs+', '+str(rt)+'\n'     
    file_out.append(out)
    return out


def decode_i(binary):
    
    opcode = int(binary[0:6],2)

    if opcode in type_i:
        #xori $s1, $s4, 5
        #001110|10100|10001|0000000000000101
        opcode = type_i[opcode]

        rs = int(binary[6:11],2)
        rs = register[rs]

        rt = int(binary[11:16],2)
        rt = register[rt]

        if binary[16] == '1':
            imm = two_complements(binary[16:])
        else:    
            imm = int(binary[16:],2)

        out = '\t' +opcode+', '+rt+', '+rs+', '+str(imm)+'\n'

        file_out.append(out)


    if opcode in type_i_branch:
        #000100|01001|01010|0000000000001100
    	#beq, $t1, $t2, volta(distancia:12)

        opcode = type_i_branch[opcode]

        rs = int(binary[6:11], 2)
        rs = register[rs]

        rt = int(binary[11:16], 2)
        rt = register[rt]

        if binary[16] == '1':
            imm = two_complements(binary[16:])
        else:
            imm = int(binary[16:], 2)

        label = random.choice(words)
        out = '\t' + opcode + ', ' + rs + ', ' + rt + ', '+ label + ', ' + str(imm) + '\n'

        file_out.append(out)
        labels[label] = len(file_out) + imm

    if opcode in type_i_save_load_lui:
        #lui $t1, 0x0123
        #001111|00000|01001|0000000100100011
        opcode = type_i_save_load_lui[opcode]

        if opcode is 'lui':
            
            rt = int(binary[11:16],2)
            rt = register[rt]

            imm = hex(int(binary[16:],2))

            out = '\t' +opcode+', '+rt+', '+str(imm)+'\n'

            file_out.append(out)

        else:
        #sw $t1, -10($t2)
        #10101101010010011111111111110110

            rs = int(binary[6:11],2)
            rs = register[rs]

            rt = int(binary[11:16],2)
            rt = register[rt]

            if binary[16] == '1':
                imm = two_complements(binary[16:])
            else:    
                imm = int(binary[16:],2)
               
            out = '\t' +opcode+', '+rt+', '+str(imm)+'('+rs+')'+'\n'

            file_out.append(out)




    

    return out


def decode_j(binary):
#000010|00000100000000000000011011
    addressSignal = binary[6]

    if addressSignal == '0':
        address = int(binary[6:], 2)
    elif addressSignal == '1':
        address = two_complements(binary[6:])


####################################################################################

file = input.readlines()

for line in file:
    line = converteBinario(line)
    print(line)
    if int(line[0:6],2) == 0: 
        print (decode_r(line))

    if int(line[0:6],2) != 0 and int(line[0:6],2) != 2:
        print (decode_i(line))

    if int(line[0:6], 2) == 2:
        print('j')

print_labels()
print_file()

output.close()
input.close()
