
#START class StudentObject:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    # Functions in Object
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
#End class StudentObject:
class Phone:
    def __init__(self, brand, model, color, price, weight, count):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.weight = weight
        self.count = count
