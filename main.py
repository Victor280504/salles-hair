from datetime import datetime, timedelta
import random
from Stock import Stock
from Product import Product
from Sale import Sale
from Report import ReportSales

class System:
    def __init__(self):
        self.estoque = Stock()
        self.make_stock()
        self.menu = Menu(self)
        self.currently_menu = 0
        self.historico = []

    def start(self):
      while True:
        if self.currently_menu == 0:
          self.currently_menu = self.menu.first_menu()
        elif self.currently_menu == 1:
          self.currently_menu = self.menu.menu_crud()
        elif self.currently_menu == 2:
          venda = Sale(self.set_id_sale)
          self.currently_menu = self.menu.menu_sales(venda)
        elif self.currently_menu == 3:
           self.currently_menu = self.menu.menu_adm()
        elif self.currently_menu == 4:
          return print("Obrigado por usar o sistema - Por: Jamile Sales e Victor Emanuel  =) ")
        else:
          return "Opção Inválida"
  
    def make_stock(self):
      names = ["Xuxinha", "Shampoo", "Creme", "Presilha"]
      value = len(names)
      count = 0

      while count < value:
        name_aleatorio = names[count]
        price = random.randint(1, 100)
        cost = random.randint(1, price)
        amount = random.randint(1, 10)
        if name_aleatorio == "Xuxinha" or name_aleatorio == "Presilha":
          perishable = False
        else:
          perishable = True

        validate_date = None

        if perishable == True:
          year = random.randint(2023, 2024)
          month = random.randint(1, 12)
          day = random.randint(1, 28)
          validate_date = datetime(year, month, day)

        new_product = Product(self.estoque.set_id_product(), name_aleatorio, price, cost, amount, perishable, validate_date)
        self.estoque.stock.append(new_product)
        count +=1
        
    def set_id_sale(self):
      if len(self.historico) == 0:
        new_id = 1
      else:
        new_id = self.historico[len(self.historico) - 1].id + 1 
      return new_id

class Menu:
    def __init__(self, sistema):
        self.sistema = sistema

    def first_menu(self):
        while True:
           print("\n===== Salles Hair =====")
           print("\nO que você deseja fazer ? ")
           print("\n ")
           print("1. Gerenciar Estoque")
           print("2. Vender Produtos")
           print("3. Administração")
           print("4. Sair")
           escolha = int(input("Escolha uma opção: "))
           escolhas = [1,2,3,4]
           if escolha in escolhas: 
             return escolha
           else:
             print("Opção inválida. Tente novamente.")   

    def menu_sales(self, venda):
        while True:
          
           print("\n===== Salles Hair =====\n")
           print("Venda \n")
           print(venda)
           print("1. Adicionar Produto")
           print("2. Vender")
           print("3. Cancelar")
           escolha = input("Escolha uma opção: ")
          
           if escolha == "1":
              self.sistema.estoque.get_id_products()
              print("\nQual o id do seu produto?")
              id = int(input("id: "))
             
              if not self.sistema.estoque.verify_id(id):
                print("\nId não encontrado\n")
                return 2
              product = self.sistema.estoque.get_product(id)
              amount = int(input(f"Qual a quantidade ? Disponível: {product.amount} \n:  "))
              if amount <= product.amount:
                if venda.verify_item(product, amount):
                    venda.add_amount(product, amount)
                else:
                    venda.add_item(product, amount)
              else:
                print('Quantidade inválida')
                
                
           elif escolha == "2":
              value = float(input(f"Valor a se pagar: R${venda.total:.2f}\n: "))
              if venda.process_payment(value):
                for produto in self.sistema.estoque.stock:
                  for prod in venda.itens:
                    if produto == prod['produto']:
                        if produto.amount >= prod['quantidade']:
                             produto.amount -= prod['quantidade']
                  
                self.sistema.historico.append(venda)
                print(venda)
                self.sistema.estoque.control_products_amount()
                print("Sucesso")
                return 0
              else:
                print("Valor insuficiente")
                return 2
           elif escolha == "3":
              return 0
           else:
              print("\n Opção inválida. Tente novamente.")

    def menu_crud(self):
      while True:
       print("\n===== Salles Hair =====\n")
       print("Gerenciar Estoque ")
       print("\n ")
       print("1. Verificar Estoque")
       print("2. Cadastrar Produto")
       print("3. Remover Produto")
       print("4. Atualizar Produto")
       print("5. Fazer controle de prod. Perecíveis")
       print("6. Voltar")
       escolha = input("Escolha uma opção: ")
       if escolha == "1":
          self.sistema.estoque.show_stock()
       elif escolha == "2":
          self.sistema.estoque.register_product()
          print("\nProduto Registrado com Sucesso")
       elif escolha == "3":
          print("Qual o id do seu produto?")
          id = int(input("id: "))
          produto = self.sistema.estoque.get_product(id)
          print(produto)
          print(f"Você deseja remover todos? \n1. Sim \n2. Não")
          response = int(input("Escolha uma opção: "))
          if response == 1:
            print(f"{self.sistema.estoque.remove_product(id, produto.amount)}")
            return
          elif response == 2:
            amount = int(input("Quantos você deseja remover? "))
            self.sistema.estoque.remove_product(id, amount)
          else:
            print("Opção Inválida")
          
       elif escolha == "4":
         self.sistema.estoque.get_id_products()
         print("\nQual o id do seu produto?")
         id = int(input("id: "))
         if not self.sistema.estoque.verify_id(id):
            print("\nId não encontrado\n")
            return 1
           
         product = self.sistema.estoque.get_product(id)
         print(f"\nO que você deseja alterar?\n1 - Nome: {product.name}\n2 - Custo: R$ {product.cost:,.2f} \n3 - Preço: R$ {product.price:,.2f}\n4 - Quantidade: {product.amount}\n5 - Perecível: {product.perishable} \n6 - Data de validade:  {product.validate_date.date()if product.perishable else product.validate_date}\n7 - Voltar\n")
         change = int(input("Escolha uma opção: "))
         if change == 1:
           new_thing = str(input("Qual é o novo nome do produto? "))
           self.sistema.estoque.update_product(id, 'name', new_thing)
         elif change == 2:
           new_thing = float(input("Qual é o novo custo do produto? "))
           self.sistema.estoque.update_product(id, 'cost', new_thing)
         elif change == 3:
           new_thing = float(input("Qual é o novo preço do produto? "))
           self.sistema.estoque.update_product(id, 'price', new_thing)
         elif change == 4:
           new_thing = int(input("Qual é a nova quantidade do produto? "))
           self.sistema.estoque.update_product(id, 'amount', new_thing)
         elif change == 5:
           perishable = bool(input("Qual é o novo status de perecibilidade do produto? - true ou false ").lower() in ['true','1', 'sim'])
           self.sistema.estoque.update_product(id, 'perishable', perishable)
           if perishable == True:
             year = int(input("Qual é o ano? "))
             month = int(input("Qual é o mês? "))
             day = int(input("Qual é o dia? "))
             new_date = datetime(year, month, day)
             self.sistema.estoque.update_product(id, 'validate_date', new_date)
         elif change == 6:
           year = int(input("Qual é o ano? "))
           month = int(input("Qual é o mês? "))
           day = int(input("Qual é o dia? "))
           new_date = datetime(year, month, day)
           self.sistema.estoque.update_product(id, 'validate_date', new_date)
         elif change == 7:
           return 1
         else:
           return "Opção inválida"
         print(product)
       elif escolha == "5":
          self.sistema.estoque.control_products_perishable()
          print("\nProdutos Verificados")
       elif escolha == "6":
          return 0
       else:
          print("\n Opção inválida. Tente novamente.")

    def menu_adm(self):
      while True:
         print("\n===== Salles Hair =====\n")
         print("Administração \n")
         print("1. Verificar Histórico")
         print("2. Gerar Relatório")
         print("3. Voltar")
         escolha = input("Escolha uma opção: ")
         if escolha == "1":
            print("\n Histórico \n")
            for sale in self.sistema.historico:
              for item in sale.itens:
                print(f"{sale.date.date()} | {item['produto'].name:<10} | R${item['quantidade']*item['produto'].price}")
            return 3
         if escolha == "2":
            relatorio = ReportSales(self.sistema.historico, self.sistema.estoque.make_report_stock())
            relatorio.make_report()
            return 3
         if escolha == "3":
            return 0
         else:
            print("\n Opção inválida. Tente novamente.")
      
if __name__ == "__main__":
    sistema = System()
    sistema.start()

                   
