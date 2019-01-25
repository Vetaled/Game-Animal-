class Pet_game(object):
    """Virtual pet"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "excellent"
        elif 5 <= unhappiness <= 10:
            m = "good"
        elif 11 <= unhappiness <= 15:
            m = "not bad"
        else:
            m = "bad"
        return m

    def talk(self):
        print("My name is", self.name, "and i am feeling", self.mood, "now")
        self.__pass_time()

    def eat(self, food=4, fun=1):
        print("Yummy")
        self.hunger -= food
        self.boredom += fun
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4, food=1):
        print("It is fun.")
        self.boredom -= fun
        self.hunger += food
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    pet_name = input("Pls , give the name for your pet...\n")
    pet = Pet_game(pet_name)

    choice = None
    while choice != 0:
        print("""
        My pet
        0 - Exit
        1 - Feel
        2 - Food
        3 - Play
        """)
        choice = int(input())
        if choice == 0:
            print("Goodbye")
        elif choice == 1:
            pet.talk()
        elif choice == 2:
            pet.eat()
        elif choice == 3:
            pet.play()
        else:
            print("Wrong choice")


main()
input("Push 'Enter' if you want to close programme.")
