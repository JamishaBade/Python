class Bird:
    def sound(self):
        print("Birds make sound")


class parrot(Bird):
    def sound(self):
        print("parrot souds, squawk")


class crow(Bird):
    def sound(self):
        print("crow says 'caw caw'")


bird1 = crow()
bird2 = parrot()

bird1.sound()
bird2.sound()
# Polymorphism means same function performs diff tasks (same interface, different behaviours)
