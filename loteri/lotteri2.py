import random

class lotteri:

    def __init__(self):
        self.list_vinster = [
            "Solstol",
            "Röd Porche",
            "Handduk",
            "Ockelbo 500",
            "100 kubik meter Tvål",
            "BMX cykel",
            "Surf Bräda",
            "Snowboard",
            "Hawai >Resa",
            "En biltvätt På OKQ8",
            "Lyx Yatch",
            "Android mobil",
            "Iphone",
            "JBL Hörlurar",
            "100 kubik meter kattmat",
            "En Blåval",
            "AK-47",
            "StatTrak™ Glock-18 | Sacrifice",
            "StatTrak™ M4A1-S | Night Terror"
         ]

    def get_vinst (self) :
        slumptal = random.randint (0,   19)
        return self.list_vinster [slumptal]