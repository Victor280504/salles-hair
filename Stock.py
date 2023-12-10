from datetime import datetime, timedelta
from Product import Product

class Stock:
  def __init__(self):
      self.stock = []
      self.miss = 0.0
    
  def verify_id(self, id):
    ids = []
    for product in self.stock:
      ids.append(product.id_product)
      
    if id in ids:
      return True
      
    return False

  def make_report_stock(self):
    all_products = len(self.stock)
    all_amount = self.get_amount()
    all_cost = self.get_total_cost()
    all_value = self.get_total_value()
    all_prejudice = self.get_prejudice()

    report = f"Relatório de Estoque:\n"
    report += f"Total de Produtos: {all_products}\n"
    report += f"Total de Unidades: {all_amount}\n"
    report += f"Total de Custo: R${all_cost:,.2f}\n"
    report += f"Valor Total: R${all_value:,.2f}\n"
    report += f"{all_prejudice}\n"

    return report
  
  def register_product(self):
    name = input("Qual é o nome do produto? ")
    price = float(input("Qual é o preço do produto? "))
    cost = float(input("Qual é o custo do produto? (Esta informação é para calcular o lucro) "))
    amount = int(input("Qual é a quantidade do produto? "))
    perishable = bool(
        input("Este produto possui prazo de validade? - digite um valor (True/False, 1/0, sim/não) ").lower() in ['true', '1', 'sim'])
    validate_date = None
    if perishable:
        year = int(input("Qual é o ano? "))
        month = int(input("Qual é o mês? "))
        day = int(input("Qual é o dia? "))
        validate_date = datetime(year, month, day)

    return self.stock.append(Product(self.set_id_product(), name, price, cost, amount, perishable, validate_date))


  def show_stock(self):
    print(f"+----+-------------------+---------+-------+------+------------+-------+")
    print(f"| ID | Nome              |Preço    |Quant. |Perec.|Validade    |")
    print(f"+----+-------------------+---------+-------+------+------------+-------+")

    for produto in self.stock:
        self.add_line_table(produto)

    print(f"+----+-------------------+---------+-------+------+------------+-------+")

  def add_line_table(self, produto):
    print(f"| {produto.id_product:<2} | {produto.name:<17} | R${produto.price:<5.2f} | {produto.amount:<5} | "
          f"{'Sim' if produto.perishable else 'Não'}  | "f"{str(produto.validate_date.date()) if produto.perishable else str(produto.validate_date):<10} |")

  def get_amount(self):
    all = 0
    for t in range(0, len(self.stock)):
      all += self.stock[t].amount
      
    return all
    
  def remove_product(self,id, amount):
      for t in range(0, len(self.stock)):
        if self.stock[t].id_product == id:
          if amount < self.stock[t].amount:
            self.stock[t].amount = self.stock[t].amount - amount
            print(f"\n{amount} {self.stock[t].name} foram removidos com sucesso")
            return
          else:
            return self.stock.pop(t)
        
  def control_products_perishable(self):
    rem_prod = []
    for t in range(0, len(self.stock) - 1):
      if self.stock[t].perishable == True and self.stock[t].win() == True:
        self.miss+= (self.stock[t].cost * self.stock[t].amount)
        rem_prod.append(self.stock.pop(t))
  
    print(f"\nProdutos removidos:\n")
    for prod in rem_prod:
      print(f"{prod}")

  def control_products_amount(self):
    for t in range(0, len(self.stock) - 1):
      if self.stock[t].amount == 0:
        self.stock.pop(t)
        
  def confirmate_action(self):
    while True:
      print("Você Tem certeza da sua ação?\n1. Sim\n2. Não")
      response = int(input("Escolha uma opção: "))
      if response == 1:
        return True
      elif response == 2:
        return False
      else:
        print("Opção inválida")
    
  def get_prejudice(self):
    return f"Perdas: R$ {self.miss :,.2f}"
    
  def update_product(self, id, item, new):
    product = self.get_product(id)
    setattr(product, item, new)
    return

  def get_product(self, id):
    for product in self.stock:
      if product.id_product == id:
        return product
    return "Produto não encontrado"
    
  def get_total_cost(self):
    cost = 0
    for t in range(0, len(self.stock)):
      cost += (self.stock[t].cost * self.stock[t].amount)
    return cost

  def get_total_value(self):
    price = 0
    for t in range(0, len(self.stock)):
      price += (self.stock[t].price * self.stock[t].amount)
    return price

  def get_id_products(self): # ver o id correspondente aos produtos
    for t in range(0, len(self.stock)):
      print(f"\n{self.stock[t].id_product} - {self.stock[t].name}")
      
    
  def set_id_product(self):
    if len(self.stock) == 0:
      new_id = 1
    else:
      new_id = self.stock[len(self.stock) - 1].id_product + 1 
    return new_id

  def __str__(self):
    products_str = "\n".join(str(product) for product in self.stock)
    return f"Lista de produtos:\n{products_str}"