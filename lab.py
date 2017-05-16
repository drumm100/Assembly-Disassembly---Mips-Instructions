fileIn = open("teste.asm", "r")

file = fileIn.readlines()
for item in range(0, len(file) - 1):
    if item >= len(file): break
    if ".text" in file[item]: file.pop(item)
    if ".globl" in file[item]:file.pop(item)
    if "main:" in file[item]: file.pop(item)

for xline in file:
    if xline == '\n': file.remove(xline)


def find_label(label, currentLine):

    #file.index(label)

    none_ins = 0
    for i in file:
        if i != '\n':
            instruction = i.split()
            if len(instruction) == 1: none_ins += 1

            if label in instruction[0]:
                none_ins -= 1
                out = file.index(i) - currentLine - none_ins - 1
                if out < 0: return out - 1
                return out

