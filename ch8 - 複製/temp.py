# E_8_5: 多重繼承
class ParentClass1():
    def Parent_method1(self):
        print("呼叫父類別1方法(Parent_method1)")
class ParentClass2():
    def Parent_method2(self):
        print("呼叫父類別2方法(Parent_method2)")
class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("子類別方法(child method)")
c = ChildClass()
c.Parent_method1()
c.Parent_method2()
c.child_method() 


#class Animal(object):
#    def run(self):
#        print('Animal is running...')
#
#class Dog(Animal):
#    def run(self):
#        print('Dog is running...')
#
#class Cat(Animal):
#    def run(self):
#        print('Cat is running...')
#
#def run_twice(animal):
#    animal.run()
#    animal.run()
#
#a = Animal()
#d = Dog()
#c = Cat()
#
#print('a is Animal?', isinstance(a, Animal))
#print('a is Dog?', isinstance(a, Dog))
#print('a is Cat?', isinstance(a, Cat))
#
#print('d is Animal?', isinstance(d, Animal))
#print('d is Dog?', isinstance(d, Dog))
#print('d is Cat?', isinstance(d, Cat))
#
#class Animal:
#def __init__(self, name): # Constructor of the class
#self.name = name
#def talk(self): # Abstract method, defined by convention only
#raise NotImplementedError("Subclass must implement abstract
#method")
#class Cat(Animal):
#def talk(self):
#return 'Meow!'
#class Dog(Animal):
#def talk(self):
#return 'Woof! Woof!'
#animals = [Cat('Missy'), Cat('Garfield'), Dog('Lassie')]
#for animal in animals:
#print(animal.name + ': ' + animal.talk())


#while True: 
#    try: 
#        print('呼叫物件實體的公有屬性i(正常)',Love.i)
#        print('呼叫物件實體的私有屬性(發生屬性錯誤)',Love.__i)
#    except AttributeError as A: 
#        print('錯誤', str(A))
#        print(Love.__str__())
#    except AttributeError as A:         
#        print('呼叫物件實體的公有方法hello()(正常)',Love.hello())
#        print('呼叫物件實體的公有方法hello()(正常)',Love.__hello())        
#        print('錯誤11', str(A))
##    print('呼叫物件實體的私有方法(__hello, 發生屬性錯誤)',Love.__hello())
#    else: 
#        print('sss')
#    finally:
#        break        