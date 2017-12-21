# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"

class CandyShop():
    def __init__(self, amount_of_sugar):
        self.amount_of_sugar = amount_of_sugar
        self.lollipop_number = 0
        self.candy_number = 0
        self.income = 0
        self.lollipop_price = 10
        self.candy_price = 20
        self.candy_sugar_amount = 10
        self.lollipop_sugar_amount = 5

    def create_sweets(self, type_of_sweet):
        if type_of_sweet == "candy":
            self.candy_number += 1
            self.amount_of_sugar -= self.candy_sugar_amount

        if type_of_sweet == "lollipop":
            self.lollipop_number += 1
            self.amount_of_sugar -= self.lollipop_sugar_amount

    def sell(self, type_of_sweet, quantity):

        if type_of_sweet == "candy":
            self.candy_number -= quantity
            self.income += self.candy_price
        if type_of_sweet == "lollipop":
            self.lollipop_number -= quantity
            self.income += self.lollipop_price

    def raise_prices(self, price):
        self.candy_price += (self.candy_price * price / 100)
        self.lollipop_price += (self.lollipop_price * price / 100)

    def buy_sugar(self, buy_amount_of_sugar):
        self.amount_of_sugar += buy_amount_of_sugar
        self.income -= buy_amount_of_sugar / 10

    def __str__(self):
        return "Inventory: {} candies, {} lollopops, Income: {}, Sugar: {}gr".\
            format(self.candy_number, self.lollipop_number, self.income, self.amount_of_sugar)

candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 270gr"
candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:30.5, Sugar: 270gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 570gr"