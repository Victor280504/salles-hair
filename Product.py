from datetime import datetime, timedelta

class Product:
  # Quando for registrar a venda, o id vai ser o id_product+firt_letter_of_name+amount_before_sell

  # A classe Produto foi implementada com atributos que fossem condizentes com as funcionalidades propostas
  # Preço, custo condizem com as informações que o rellatório
  # A data diz respeito aos produtos perecíveis
  def __init__(self,id_product, name, price, cost, amount, perishable = False, validate_date = None):
      self.id_product = id_product
      self.name = name
      self.price = price
      self.cost = cost
      self.amount = amount
      self.perishable = perishable
      self.validate_date = validate_date # Colocar um Exeption pra verificar se a data é válida
      self.register_date = datetime.now().date()

  def win(self):
    now = datetime.now()
    if self.validate_date < now:
      return True
    
    return False

  def __str__(self): # Representação string do produto
      return f"\nId: {self.id_product}\nNome: {self.name}\nCusto: R$ {self.cost:,.2f} \nPreço: R$ {self.price:,.2f}\nQuantidade: {self.amount}\nPerecível: {self.perishable} \nData de validade: {self.validate_date}"

  def __eq__(self, other):
    if isinstance(other, Product):
        if other.name == self.name and other.id_product == self.id_product:
            return True
    return False