pilha=[]
for emp in range(10):
    a=input("Digite um número:\n")
    pilha.append(a)

for des in range(10):
    print(pilha[-1])
    pilha.pop()
