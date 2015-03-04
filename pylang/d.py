#!/usr/bin/env python
# coding=utf8

# generator 返回一个迭代对象的函数

"""
The yield statement is only used when defining a generator function, 
and is only used in the body of the generator function. 
Using a yield statement in a function definition
is sufficient to cause that definition to create a generator function instead of a normal function.

When a generator function is called, it returns an iterator known as a generator iterator,
or more commonly, a generator. 
生成器函数被调用 返回一个生成器（本身也是迭代器）
The body of the generator function is executed by calling the generator’s next() 
method repeatedly until it raises an exception.
迭代器的 next() 方法被调用，生成器函数体将会被调用。

When a yield statement is executed, the state of the generator is frozen 
and the value of expression_list is returned to next()‘s caller. By “frozen” 
we mean that all local state is retained, including the current bindings of 
local variables, the instruction pointer, and the internal evaluation stack: 
enough information is saved so that the next time next() is invoked, 
the function can proceed exactly as if the yield statement were just another external call.
当 yield 语句被执行的时候，生成器的状态将会被保存。yield 后表达式的值将会被返回。

As of Python version 2.5, the yield statement is now allowed in the try 
clause of a try ... finally construct. If the generator is not resumed before it 
is finalized (by reaching a zero reference count or by being garbage collected), 
the generator-iterator’s close() method will be called, allowing any pending 
finally clauses to execute.

For full details of yield semantics, refer to the Yield expressions section.


generator.next()
Starts the execution of a generator function or resumes it at the last executed yield expression. When a generator function is resumed with a next() method, the current yield expression always evaluates to None. The execution then continues to the next yield expression, where the generator is suspended again, and the value of the expression_list is returned to next()‘s caller. If the generator exits without yielding another value, a StopIteration exception is raised.

generator.send(value)
Resumes the execution and “sends” a value into the generator function. The value argument becomes the result of the current yield expression. The send() method returns the next value yielded by the generator, or raises StopIteration if the generator exits without yielding another value. When send() is called to start the generator, it must be called with None as the argument, because there is no yield expression that could receive the value.

generator.throw(type[, value[, traceback]])
Raises an exception of type type at the point where generator was paused, and returns the next value yielded by the generator function. If the generator exits without yielding another value, a StopIteration exception is raised. If the generator function does not catch the passed-in exception, or raises a different exception, then that exception propagates to the caller.

generator.close()
Raises a GeneratorExit at the point where the generator function was paused. If the generator function then raises StopIteration (by exiting normally, or due to already being closed) or GeneratorExit (by not catching the exception), close returns to its caller. If the generator yields a value, a RuntimeError is raised. If the generator raises any other exception, it is propagated to the caller. close() does nothing if the generator has already exited due to an exception or normal exit.

"""

def stream():
    x = 0
    while True:
        yield x
        x = x+1


s = stream()
while True:
    print s.next()









