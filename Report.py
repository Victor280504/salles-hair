class ReportSales:
  def __init__(self, sales,stock):
      self.sales = sales
      self.stock = stock

  def add_sale(self, sale):
      self.sales.append(sale)

  def calcular_gastos_lucros_perdas(self):
    gastos = 0.0
    lucros = 0.0
    perdas = 0.0
    quantidade_total_vendida = 0

    for venda in self.sales:
        for item in venda.itens:
            produto = item['produto']
            quantidade = item['quantidade']
            valor_total_item = produto.cost * quantidade

            if produto.amount >= quantidade:
                gastos += valor_total_item
                quantidade_total_vendida += quantidade
            else:
                perdas += valor_total_item

        lucros += venda.total - gastos

    return gastos, lucros, perdas, quantidade_total_vendida

  def make_report(self):
    gastos, lucros, perdas, quantidade_total_vendida = self.calcular_gastos_lucros_perdas()

    print(self.stock)
    print("\nRelatório de Vendas:")
    print(f"Gastos totais: R${gastos:.2f}")
    print(f"Lucro total: R${lucros:.2f}")
    print(f"Lucros Bruto: R${lucros-perdas:.2f}")
    print(f"Perdas totais: R${perdas:.2f}")
    print(f"Quantidade total vendida: {quantidade_total_vendida} unidades")
    print("-" * 30)
    for i, venda in enumerate(self.sales, start=1):
        print(f"\nVenda #{i}")
        print(f"Data: {venda.date}")
        print("Itens:")
        for item in venda.itens:
            print(f"{item['produto'].name} - Quantidade: {item['quantidade']} - Preço: R${item['produto'].price:.2f}")
        print(f"Total: R${venda.total:.2f}")
        print("-" * 30)


