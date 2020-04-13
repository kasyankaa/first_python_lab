class Radiator:
    number_of_radiators = 0

    def __init__(self, name="Usual", thermal_power_in_watts=80, color="white", producer="Ukraine", wheelbase_in_mm=5,
                 price_in_uah=432, type_of_radiator="gorgeous"):
        self.name = name
        self.thermal_power_in_watts = thermal_power_in_watts
        self.color = color
        self.producer = producer
        self.wheelbase_in_mm = wheelbase_in_mm
        self.price_in_uah = price_in_uah
        self.type_of_radiator = type_of_radiator
        Radiator.number_of_radiators += 1

    def __del__(self):
        print("Deleted radiator")

    def __str__(self):
        return 'Radiator(name:' + self.name \
               + ', thermal power:' + str(self.thermal_power_in_watts) \
               + ', color:' + self.color \
               + ', producer:' + self.producer \
               + ", wheelbase in mm:" + str(self.wheelbase_in_mm) \
               + ', price' + str(self.price_in_uah) \
               + ', type=' + str(self.type_of_radiator) + ')'

    @staticmethod
    def create_radiator():
        return Radiator.number_of_radiators


def main():
    First = Radiator("TYC", 45, "blue", "USA", 23, 232, "beautiful")
    Second = Radiator("Mishimoto", 34, "white", "Germany", 34,)
    Third = Radiator("Koyo",23, "black", "China")

    print(First)
    print(Second)
    print(Third)

    print("Number of created radiators", Radiator.number_of_radiators)


main()
