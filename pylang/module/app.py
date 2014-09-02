# coding=utf-8

class Base(object):
    pass

class AttackMixin(Base):

    def attack(self):
        print "%s attack\n" % self.__name

class User(Base, AttackMixin):

    __name = ""

    def __init__(self, name):
        self.__name = name

    def display(self):
        print self.__name



user = User("vincent")
user.display()


