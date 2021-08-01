asteriscos = ""
N = int(input("Digite o número de linhas: "))
M = int(input("Digite o número de colunas: "))

for i in range(0, N):
    for j in range(0, M):
        asteriscos += "* "
    asteriscos += "\n"

print(asteriscos)
