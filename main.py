import json
import os.path
from abc import ABC, abstractmethod
 
class Inventory(ABC):
    products = {}

    def __init__(self):
        self.load()

    def add(self,key,quantity):
        q = 0
        if key in self.products:
            v = self.products[key]
            q = v + quantity
        else:
            q = quantity
        self.products[key] = q
        print(f'Adicionado {quantity} {key}: total = {self.products[key]}')
        

    def remove(self,key,quantity):
        q = 0
        if key in self.products:
            v = self.products[key]
            q = v - quantity
        if q < 0:
            q = 0
        self.products[key] = q
        print(f'Removido {quantity} {key}: total = {self.products[key]}')

    def display(self):
        for key, value in self.products.items():
            print(f'{key} = {value}')

    def save(self):
        print('Salvando dados de inventário...')
        with open('inventory.txt', 'w') as f:
            json.dump(self.products,f)
        print('Sucesso!')

    def load(self):
        print('Baixando inventário...')
        if not os.path.exists('inventory.txt'):
            print('Nenhum dado pré-instalado.')
            return
        with open('inventory.txt', 'r') as f:
            self.products = json.load(f)

def main():
    inv = Inventory()
    print("\n")
    print("Seja bem-vindo ao inventário do Petshop FIAP.")

    while True:    
        action = input('Comandos: add - remover - listar - salvar - sair\n')
        if action =='sair':
            break
        if action =='add' or action == 'remover':
                key = input('Nome do produto:')
                quantity = int(input('Quantidade:'))
                if action == 'add':
                    inv.add(key,quantity)
                if action == 'remover':
                    inv.remove(key,quantity)
        if action =='listar':
            inv.display()
        if action =='salvar':
            inv.save()

    inv.save()


if __name__ == "__main__":
    main()