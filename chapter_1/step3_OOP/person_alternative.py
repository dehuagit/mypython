"""
Alternative impoementation of person classes with data behavior and operationoverload
"""

class Person:
  """
    a general person: data + logic
  """
  def __init__(self, name, age, pay=0, job=None):
    self.name = name
    self.age = age
    self.pay = pay
    self.job = job
  def lastName(self):
    return self.name.split()[-1]
  def giveRaise(self, percent):
    self.pay *= (1.0 + percent)
  def __str__(self):
    return '<%s = > %s>' % (self.__class__.__name__, self.name)

class Manager(Person):
  """
    a person with custom raise inherit general lastname, str
  """
  def __init__(self,name,age,pay):
    Person.__init__(self, name, age, pay, 'manager')
  def giveRaise(self, percent, bonus = 0.1):
    Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
  bob = Person('Bob smith', 44)
  sue = Person('sue Jones', 47, 400, 'hw')
  tom = Manager(name='Tom Ded', age = 50, pay =500)
  print(sue, sue.pay, sue.lastName())
  for obj in (bob, sue, tom):
    obj.giveRaise(.10)
    print(obj)



