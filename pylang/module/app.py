#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import importlib

for file in [file[:-3] for file in os.listdir(".") if file.find("py") != -1 and file.find("pyc") == -1]:
    m = importlib.import_module(file)

