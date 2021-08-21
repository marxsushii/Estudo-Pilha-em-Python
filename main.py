from info.Pilha import pilha

class Principal:

    newPile = []
    secondPile = []

    def main(self):
        self.newPile = pilha()
        self.secondPile = pilha()

        self.newPile.push(10)
        print(self.newPile)
        self.newPile.push(20)
        print(self.newPile)
        self.newPile.push(30)
        print(self.newPile)

        lista = [10,20,30]
        self.secondPile.multiPush(lista)
        print("Pilha complementar: " ,self.secondPile)

        self.newPile.megaPush(self.secondPile)
        print(self.newPile)

        print("Item retirado: ",self.newPile.pop())
        print(self.newPile)

        self.newPile.push("arroz")
        print(self.newPile)

        self.newPile.megaPop(3)
        print(self.newPile)

        print("Topo da pilha : ",self.newPile.Top())

        print("Item retirado: ",self.newPile.pop())
        print(self.newPile)

        


Try = Principal()
Try.main()
