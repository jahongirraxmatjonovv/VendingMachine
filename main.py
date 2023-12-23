from veding_machine import VendingMachine

# Foydalanish
vending_machine = VendingMachine()

# Ichimliklar qo'shish
vending_machine.addBeverage("Coca Cola", 3200)
vending_machine.addBeverage("Suv", 1000)
vending_machine.addBeverage("Pepsi", 2500)

# Tolov kartalari to'ldirish
vending_machine.rechargeCard(12, 12000)
vending_machine.rechargeCard(21, 5600)
vending_machine.rechargeCard(99, 15800)

# Mashina ustunlarini to'ldirish
for _ in range(4):
    vending_machine.refillColumn()

# Test methods
price_coca_cola = vending_machine.getPrice("Coca Cola")
credit_card_12 = vending_machine.getCredit(12)
available_cans_coca_cola = vending_machine.availableCans("Coca Cola")

# Ichimlik sotish
sold_column_number = vending_machine.sell("Coca Cola", 12)

print(f"Coca Cola narxi: {price_coca_cola}")
print(f"Card 12 krediti: {credit_card_12}")
print(f"Coca Cola borligi: {available_cans_coca_cola}")
print(f"Sotilgan ichimlik ustuni raqami: {sold_column_number}")
