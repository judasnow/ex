#!/usr/bin/env python

import types
import functools


def is_admin(type_or_func):
    
    @functools.wraps(type_or_func)
    def _is_admin(x):
        pass

    if isinstance(type_or_func, types.FunctionType):
        return _is_admin(type_or_func)
        
    else:
        return _is_admin


@is_admin
def get_user_info():
    pass

