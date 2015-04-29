# coding=utf-8


class Number(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "({value})".format(value=self.value)

    def is_reducible(self):
        return False


class Add(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "({left}*{right})".format(left=self.left, right=self.right)

    def is_reducible(self):
        return True

    def reduce(self):
        if self.left.is_reducible():
            return Add(self.left.reduct(), self.right)
        elif self.right.is_reducible():
            return Add(self.left, self.right.reduce())
        else:
            return Number(self.left.value + self.right.value)


class Mul(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "({left}*{right})".format(left=self.left, right=self.right)

    def is_reducible(self):
        return True

    def reduce(self):
        if self.left.is_reducible():
            return Mul(self.left.reduct(), self.right)
        elif self.right.is_reducible():
            return Mul(self.left, self.right.reduce())
        else:
            return Number(self.left.value * self.right.value)
            
            
class Variable(object):

    def __str__(self):
        pass

    def is_reduceable(self):
        return True


class Machine(object):

    def __init__(self, expression):
        self.expression = expression

    def step(self):
        self.expression = self.expression.reduce()

    def run(self):
        while self.expression.is_reducible():
            print self.expression
            self.step()

        else:
            print self.expression


if __name__ == "__main__":
    Machine(Mul(Number(4),
            Mul(Number(4),
                Number(4)))).run()



