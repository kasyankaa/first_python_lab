class Radiator:
    number_of_radiators = 0

    def __init__(self, thermal_power_in_watts=0, color="Default", producer="Default", wheelbase_in_mm=0, price_in_uah=0,
                 connection_type="Default", type_of_radiator="Default"):
        self.thermal_power_in_watts = thermal_power_in_watts
        self.color = color
        self.producer = producer
        self.wheelbase_in_mm = wheelbase_in_mm
        self.price_in_uah = price_in_uah
        self.type = type_of_radiator
        self.connection_type = connection_type
        Radiator.number_of_radiators += 1

    def __del__(self):
        print("Deleted radiator")

    def __str__(self):
        return ', '.join((f"{name[:]} = {value}" for name, value in self.__dict__.items()))
    __repr__ = __str__

    @staticmethod
    def create_radiator():
        return Radiator.number_of_radiators


def main():
    TYC = Radiator(45, "blue", "USA", 23, 232, "upper", "silver")
    Mishimoto = Radiator(34, "white", "Germany", 34, 3456)
    Koyo = Radiator(23, "black", "China")

    print(TYC)
    print(Mishimoto)
    print(Koyo)

    print("Number of created radiators", Radiator.number_of_radiators)


main()
