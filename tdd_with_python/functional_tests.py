# coding=utf-8

from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://lo:19000")

assert "Django" in browser.title
