class Stock:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def buy(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
        else:
            print("Not enough stocks to sell.")

    def get_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Stock: {self.symbol}, Price: {self.price}, Quantity: {self.quantity}"

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, stock):
        self.stocks.remove(stock)

    def portfolio_value(self):
        total_value = 0
        for stock in self.stocks:
            total_value += stock.get_value()
        return total_value

# Criação de instâncias de ações
stock1 = Stock("AAPL", 150.0, 10)
stock2 = Stock("GOOGL", 2500.0, 5)

# Criação de instância de portfólio
portfolio = Portfolio()

# Adiciona ações ao portfólio
portfolio.add_stock(stock1)
portfolio.add_stock(stock2)

# Compra mais ações
stock1.buy(5)
stock2.buy(3)

# Remove uma ação do portfólio
portfolio.remove_stock(stock1)

# Vende algumas ações
stock2.sell(2)

# Imprime informações do portfólio
print("Portfolio:")
for stock in portfolio.stocks:
    print(stock)

# Calcula o valor total do portfólio
value = portfolio.portfolio_value()
print(f"Portfolio value: ${value:.2f}")
