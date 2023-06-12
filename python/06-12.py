"""
A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em objetos, que são instâncias de classes. A POO é baseada em quatro conceitos principais: encapsulamento, herança, polimorfismo e abstração.

Encapsulamento é um dos pilares da POO e refere-se ao ato de esconder os detalhes internos de um objeto e fornecer uma interface externa para interagir com ele. Ele ajuda a proteger os dados dentro de um objeto e permite que a implementação interna seja alterada sem afetar o código externo.

Uma classe é uma estrutura que define um tipo de objeto. Ela contém atributos (variáveis que armazenam os dados associados ao objeto) e métodos (funções que realizam ações relacionadas ao objeto). As classes são usadas para criar objetos específicos, que são instâncias dessas classes.

As classes são usadas para organizar e modularizar o código, facilitando o desenvolvimento de software estruturado e reutilizável. Elas ajudam a modelar o mundo real em termos de objetos e suas interações, permitindo uma compreensão e manipulação mais fáceis de sistemas complexos.

Herança, em programação orientada a objetos (POO), é um conceito que permite que uma classe herde atributos e métodos de outra classe. A classe que herda é chamada de classe filha ou classe derivada, e a classe da qual ela herda é chamada de classe pai ou classe base.
"""

class Rectangle:
   def __init__(self, width, height):
      self.width = width
      self.height = height
  
   def calculate(self):
      return self.width * self.height

ret = Rectangle(5, 8)
ret2 = Rectangle(10, 5)

area = ret.calculate()
area2 = ret2.calculate()

print(f"The area of rectangle is {area}")
print(f"The area of rectangle 2 is {area2}")

class Person:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def get_name(self):
      return self.__name

   def get_age(self):
      return self.__age

   def set_age(self, age):
      if age > 0:
         self.__age = age

person = Person("John", 25)

print(person.get_name())
print(person.get_age())

person.set_age(30)
print(person.get_age())