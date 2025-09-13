# Inheritance allows reusability


class Animal:
    def speak(self):
        print("animal makes sound")


class dog(Animal):
    def bark(self):
        print("Dog barks")


myDog = dog()
myDog.bark()
myDog.speak()
