class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self, speed: int):
        self.speed += speed
        print(f'The {self.make} {self.model} sped up by {speed} miles per hour.')



mustang = Vehicle('Ford', 'Mustang')
ranger = Vehicle('Ford', 'Ranger')

print(f"The Mustang's speed is {mustang.speed}. The Ranger's speed is {ranger.speed}.")
mustang.accelerate(10)

print(f"The Mustang's speed is {mustang.speed}. The Ranger's speed is {ranger.speed}.")
ranger.accelerate(30)

print(f"The Mustang's speed is {mustang.speed}. The Ranger's speed is {ranger.speed}.")

#First, I initialize the two different instances.
#Next, I show they both have a speed of 0.
#I then use the accelerate function on the mustang instance, which increases its self.speed by 10.
#You then see me showing how they are definitely different speeds for each instance. That's because each of their self.speed is unique to them, it is not shared.
#I repeat this for the ranger instance to show the difference again.

#After that, practice makes perfect. Make a Account class that
#has 2 members, account_num and balance. Make a single class
#function called deposit that takes a amount argument
#and increases the balance by that amount.
