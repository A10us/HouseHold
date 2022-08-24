# Klassen skal bruges til at registrerer opbevaring i en husholdning, eksempelvis skab, fryser,køleskab etc.
# Klassen kobles sammen med klassen Items som er indholdet af opbevaringsstedet.

# ## Attributter
# name - Navn på opbevaring f.eks. køkkenskab 1
# description - Beskrivelse af opbevaring, f.eks. køkkenskab til højre for skuffer
# image - billedesti af opbevaring

# ## Hændelser
# create - Opret “Inventory”
# read - Læs "Inventory"
# delete - “Inventory”
# update - “Inventory”


class Inventory(object):
    def __init__(self, inventory_name, description, image):
        self.inventory_name = inventory_name
        self.description = description
        self.image = image

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass