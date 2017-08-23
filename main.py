#!/usr/bin/env python 
#-*- coding: utf-8 -*-
import json
import sys

try:   #проверка на наличие файла в текущей дирекиории
    open('file.json')
except IOError as e:
    print("error: this file dosen't exist in this repository")
    sys.exit()

class repliceJson: #класс для замены данных в .json файле
    def replice(self, path, fileName, data):  #функция которая отвечает за замену
        self.path = path
        self.fileName = fileName
        self.data = data
        filePathNameExt = './' + path + './' + fileName + '.json'   #переменная которая хранит имя и диреуторию файла
        with open(filePathNameExt, 'w') as fp:
            json.dump(data, fp)  #замена

class printJson:  #функция которая отвечает за вывод определенного поля в .json файлк
    def call(self, name):  #функция которая отвечает за вывод
        self.name = name
        with open('file.json') as json_data:
            d=json.load(json_data)   #поиск данных
        print(d[name])   #вывод заданных данных из поля

"""
m = printJson()  #тестовый код для проверки вывода данных
n="region"
m.call(n)
"""

"""
data = {}   #тестовый код для проверки замены данных в файле
data ['region'] = 'russia'
rep = repliceJson()
rep.replice('./', 'test', data)
"""




