
def biggest_substr(str1: str, str2: str) -> int:
    l1 = len(str1)
    l2 = len(str2)

    # cálculos de quantidade de caracteres da combinação das palavras
    mem = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(l1 + 1):
        for j in range(l2 + 1):
            # testando todas as combinações de letras

            # a primeira linha e coluna representam as strings individuais, portanto
            # devem ser prenchidas apenas com a contagem de caracteres de cada uma
            # das strings separadamente 
            if i == 0:
                mem[i][j] = j
            elif j == 0:
                mem[i][j] = i

            # se os caracteres sendo comparados atualmente são iguais,
            # adiciono 1 caracter na palavra final
            elif str1[i - 1] == str2[i - 1]:
                mem[i][j] = mem[i - 1][j - 1] + 1

            # se eles não são iguais, pego qual a menor string já gerada até o
            # momento e adiciono o caractere nela
            else:
                s1 = mem[i - 1][j]
                s2 = mem[i][j - 1]
                if s1 < s2:
                    mem[i][j] = s1 + 1
                else:
                    mem[i][j] = s2 + 1

    return mem[l1][l2]


str1 = input()
str2 = input()
print(biggest_substr(str1, str2))
