# This Python file uses the following encoding: utf-8
class Pizza:
    def __init__(self):
        self.toppings = []

    def prepare(self):
        print("Preparing ", self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings...")
        for topping in self.toppings:
            print(topping)

    def bake(self):
        print("Bake for 25 min at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official box")


class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Cheese Pizza"
        self.dough = "Thin crust dough"
        self.sauce = "Marinara sauce"
        self.toppings.append("Cheese")


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Extra thick crust dough"
        self.sauce = "Plum tomato sauce"
        self.toppings.append("Pepperoni")


class SimplePizzaFactory:
    def createPizza(self, pizzaType):
        if pizzaType == "cheese":
            pizza = CheesePizza()
        elif pizzaType == "pepperoni":
            pizza = PepperoniPizza()
        return pizza


class PizzaStore:
    def __init__(self, pizzaFactory):
        self.factory = pizzaFactory

    def orderPizza(self, pizzaType):
        pizza = self.factory.createPizza(pizzaType)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


if __name__ == "__main__":
    pizzaFactory = SimplePizzaFactory()
    pizzaStore = PizzaStore(pizzaFactory)
    pizza = pizzaStore.orderPizza("cheese")
    print("Your pizza", pizza.name)
    pizza2 = pizzaStore.orderPizza("pepperoni")
    print("Your pizza", pizza2.name)

