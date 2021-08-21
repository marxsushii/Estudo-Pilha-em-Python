
class pilha: 
    def __init__(self):
        self.__TAM_MAX = 4
        self.__valores = []
        self.__topo = -1

    def empty(self):
        if(self.__topo == -1):
            print("Esta pilha e vazia.")
        else:
            print("Esta pilha nao esta vazia")
    
    def push(self,value):
        if(len(self.__valores)<self.__TAM_MAX):
            self.__valores.append(value)
            self.__topo +=1
        else:
            print("Tamanho excedido!")
    

    def multiPush(self,multiValues):
        for item in multiValues:
            if(len(self.__valores)<self.__TAM_MAX):
                self.__valores.append(item)
                self.__topo +=1
            else:
                print("Tamanho excedido!")

    def megaPush(self,Pile): 
        for item in Pile.__valores:
            if(len(self.__valores)<self.__TAM_MAX):
                self.__valores.append(item)
                self.__topo +=1
            else:
                print("Tamanho excedido! Não é possivel empilhar mais itens.")

    
    def pop(self):
        if self.__topo>-1:
            self.__topo -=1
            return self.__valores.pop()
     

    def megaPop(self,quantity):     
        if quantity<len(self.__valores):
            while(quantity>0):
                self.__topo -=1
                quantity -=1
                self.__valores.pop()
        else:
            quantity=len(self.__valores)
            while(quantity>0):
                self.__topo -=1
                quantity -=1
                self.__valores.pop()


    def Top(self):
        if (self.__topo>-1):
            return(self.__valores[-1])
        else:
            print("Pilha vazia!")

    def Printer(self):
        print(self.__valores)

    def __repr__(self):
        return str ("Pilha atual: ") + str(self.__valores)