class Hello:
    # This is instance method, also intilizlizes Class Hello
    def __init__(self):
        self.x = 4
        self.y = 5

    def add(self):
        print(self.x + self.y)



class World:

    def __init__(self, x, y): # x is parameter of __init__ method
        self.x = x #self.x is instance variable, field, attribute
        self.y = y

    def add(self, x , y):
        print(x + y)


class HelloWorld:

    def __init__(self ):
        self.hello = Hello()
    
    def create_world(self):
      self.world = World(4,5)
    

def main():
    print('main')

hello = Hello()
print(hello.x, hello.y)
hello.add()

world = World(4,5)
print(world.x, world.y)
world.add(5,6)

helloworld = HelloWorld()
helloworld.hello.add()
helloworld.create_world()
print(helloworld.world.x)
