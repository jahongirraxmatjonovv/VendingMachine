import random

class VendingMachine:
    def __init__(self):
        self.beverages = {}
        self.cards = {}
        self.columns = []

    def addBeverage(self, beverage_name, price):
        self.beverages[beverage_name] = price

    def getPrice(self, beverage_name):
        return self.beverages.get(beverage_name, -1.0)

    def rechargeCard(self, card_id, credit):
        if card_id not in self.cards:
            self.cards[card_id] = 0
        self.cards[card_id] += credit

    def getCredit(self, card_id):
        return self.cards.get(card_id, -1.0)

    def refillColumn(self):
        column_number = len(self.columns) + 1
        beverage_name = random.choice(list(self.beverages.keys()))
        cans_number = random.randint(1, 20)
        self.columns.append({
            "Column_number": column_number,
            "Beverage_name": beverage_name,
            "Cans_number": cans_number
        })

    def availableCans(self, beverage_name):
        total_cans = sum(column["Cans_number"] for column in self.columns if column["Beverage_name"] == beverage_name)
        return total_cans

    def sell(self, beverage_name, card_id):
        for column in self.columns:
            if column["Beverage_name"] == beverage_name and column["Cans_number"] > 0:
                if card_id in self.cards and self.cards[card_id] >= self.beverages[beverage_name]:
                    self.cards[card_id] -= self.beverages[beverage_name]
                    column["Cans_number"] -= 1
                    return column["Column_number"]
                else:
                    return -1.0
        return -1.0
