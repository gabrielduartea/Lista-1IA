from operator import attrgetter
class Tarefa(object):
    def __init__(self,descricao,prioridade):
        self.descricao=descricao        
        self.prioridade=int (prioridade)
    
    def __str__(self):
        return "%s - %s" % (str(self.prioridade), str(self.descricao))
 
    
    def setTarefa(self,descricao,prioridade):
        self.descricao=descricao
        self.prioridade=prioridade

    
    def getPrioridade(self):
        return self.prioridade

    def getDescricao(self):
        return self.descricao
    
    def Imprimir(self):
        print(self.getPrioridade()+self.getDescricao)
    


fila=[]
for aux in range(10):
    a= input("digite a descricao: ")
    b=int(input("digite a a prioridade de 0 a 5: "))
    tarefa=Tarefa(a,b)
    tarefa.setTarefa(a,b)
    fila.append(tarefa)
 
prio=fila.sort(key=lambda a: a.prioridade, reverse=True)
print("\nprioridade - descricao")
for aux in range(10):
    print (fila[aux].__str__())
