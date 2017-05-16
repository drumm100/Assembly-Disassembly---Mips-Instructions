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

num = bin(-11)[3:].zfill(16)
x = two_complements(num)
print(x)
print(len(x))