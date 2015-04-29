#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger("d")
logger.setLevel(logging.DEBUG)

logging_formater = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging_formater)

file_handler = logging.FileHandler("log/log.txt", "a", encoding="utf8")
#file_handler.setLevel(logging.DEBUG)
#file_handler.setFormatter(logging_formater)

logger.addHandler(console_handler)
logger.addHandler(file_handler)



