# Arquivo que gera o código em assembly apartir da decodificação em hexadecimal

fileIn = open("teste.txt", "r")
# coisa.fill



aux = hex(fileIn)
vetor = aux.split('x')                 
vetor = vetor[0] #vetor agora possui binario


fileOut = open("teste.asm", "w")




def converteBinario():
    #converte binarios com numero de bits adequados

def separaBinario():
    #separa o todo para cada instrução

def binarioParaInstrucao():
    #le o binario e retorna a instrução    
