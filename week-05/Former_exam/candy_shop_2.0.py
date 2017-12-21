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
        self.dictionary_of_sweets = {}
        self.income = 0

    def check_sweet(self, type_of_sweet):
        if type_of_sweet == "candy":
            return candy
        elif type_of_sweet == "lollipop":
            return lollipop

    def create_sweets(self, type_of_sweet):
        if type_of_sweet not in self.dictionary_of_sweets:
            self.dictionary_of_sweets[type_of_sweet] = 1
        else:
            self.dictionary_of_sweets[type_of_sweet] += 1
        self.amount_of_sugar -= self.check_sweet(type_of_sweet).sugar_amount

    def sell(self, type_of_sweet, quantity):
        self.price_check = type_of_sweet
        self.dictionary_of_sweets[type_of_sweet] -= quantity
        self.income += self.check_sweet(type_of_sweet).price * quantity

    def raise_prices(self, price):
        candy.price += candy.price * price / 100
        lollipop.price += lollipop.price * price / 100

    def buy_sugar(self, buy_amount_of_sugar):
        self.amount_of_sugar += buy_amount_of_sugar
        self.income -= buy_amount_of_sugar / 10

    def __str__(self):
        return "Inventory: {} candies, {} lollipops, Income: {}, Sugar: {}gr ".format(self.dictionary_of_sweets["candy"],
                self.dictionary_of_sweets["lollipop"], self.income, self.amount_of_sugar)

class Sweets():
    def __init__(self, name, price, sugar_amount):
        self.name = name
        self.price = price
        self.sugar_amount = sugar_amount

candy = Sweets("candy", 20, 10)
lollipop = Sweets("lollipop", 10, 5)

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