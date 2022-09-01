# Command prompt
from model.inventory import Inventory
from model.item import Item

fridge = Inventory("Navn", "Bekrivelse")

inv = Item("hej", "med", "dig", "hej", "med", "dig")

print(fridge)

print(inv.item_name)

