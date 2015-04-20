#!/usr/bin/env python


class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)

        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class User(Subject):
    
    def __init__(self):
        pass

    def login(self):
        # update score
        pass


if __name__ == "__main__":

    user = User()
    user.login()


