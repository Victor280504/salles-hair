from datetime import datetime

class Sale:
    def __init__(self, id):
        self.id = id
        self.itens = []  
        self.date = datetime.now()
        self.total = 0.0

    def verify_item(self, product, amount):
      for item_t in self.itens:
          if item_t['produto'].id_product == product.id_product:
              return True
      return False
          
    def add_item(self, product, amount):
        item = {"produto": product, "quantidade": amount}
        self.itens.append(item)
        self.calc_total()

    def add_amount(self, product, amount):
      for item_t in self.itens:
          if item_t['produto'] == product:
              total_quantity = item_t['quantidade'] + amount
              if total_quantity <= product.amount:
                  item_t['quantidade'] = total_quantity
                  self.calc_total()
                  return True
              else:
                  print(f"Quantidade indisponível no estoque. Disponível: {product.amount}")
                  return False

      # Se o item não estiver na venda, adicione-o
      self.add_item(product, amount)
      return True

          
    def __eq__(self, other):
      if isinstance(other, Sale):
          if other.itens == self.itens:
              return True
      return False
      
    def process_payment(self, value):
        if value >= self.total:
            change = value - self.total
            print(f"Pagamento processado. Troco: R${change:.2f}")
            return True
        else:
            print("Pagamento insuficiente. Transação cancelada.")
            return False

    def calc_total(self):
      self.total = sum(item["produto"].price * item["quantidade"] for item in self.itens)

    def __str__(self):
     note = f"\nRecibo da Venda:\n"
     note += f"Data: {self.date.date()}\n"
     note += "Itens:\n"
     for item in self.itens:
        note += f"  {item['produto'].name} - Quantidade: {item['quantidade']} - Preço: R${item['produto'].price:.2f}\n"
     note += f"Total: R${self.total:.2f}\n"
     return note

