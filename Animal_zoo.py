class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


''' define a Turtle class that inherits from the Animal class '''
class Turtle(Animal):
    category = 'reptile'


print(Turtle.category)

''' define a Snake class that inherits from the Animal class '''
class Snake(Animal):
    category = 'reptile'


class Zoo:
    ''' To organize various animals created from the animal class '''

    def __init__(self):
        self.current_animals = {}

    ''' Add the instances of animal subclasses into the current_animals dictionary'''
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    '''Tell you exactly how many individual Animal types the Zoo has for each category!'''
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result


turtle = Turtle("Turtle")  # create an instance of the Turtle class
snake = Snake("Snake")  # create an instance of the Snake class

zoo = Zoo()

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile"))  # how many zoo animal types in the reptile category


