# -*- coding: utf-8 -*-
from flask import request
import uuid
from app import app
from flask import render_template, flash, redirect
from app.models import Command
from app import db
import os


@app.route('/')
def index():
    c = Command()
    commands = c.query.all()
    print(commands)
    return render_template('index.html', commands_list = commands)

def search(commands, id):
    for elem in commands:
        print(elem)
        if elem.id == id:
            return elem

# Нажатие кнопки Запустить - запуск команды
@app.route("/run/", methods=['POST'])
def run():
    print('---------------------------------- RUN -----------------------------------------')
    print('run method')
    num = request.form['num'] # Запросить id команды с формы
    c = Command()
    commands = c.query.all()
    name = search(commands=commands, id=num).name
    command = search(commands=commands, id=num).command


    login = str(request.form['login'])
    psw = str(request.form['pasw'])

    command = command.replace('<login>', login)
    command = command.replace('<pasw>', psw)

    print('NAME: ',name)
    print('COMMAND: ', command)
    print('LOGIN: ', login)
    print('PASSWORD: ',psw)

    # filename =
    # full_command = command + f' > {}.txt'
    # os.system(full_command)
    path = os.getcwd()
    print(os.getcwd())
    os.chdir('..')
    os.chdir('..')
    print(os.getcwd())

    # Перенаправить поток консольного вывода команды в переменную
    r = os.popen(command)
    print('-----------------------------Console Pytest Output---------------------------------')
    for line in r.readlines():
        print(line,end='')

    os.chdir(path)
    print(os.getcwd())

    return redirect('/')

# Нажатие кнопки Сохранить - Сохранить измененную команду
@app.route("/save/", methods=['POST'])
def save():
    print('save method')
    name = request.form['name']
    command = request.form['command']
    num = request.form['num']
    print(num)
    print(name)
    print(command)
    el = {
        'id': num,
        'name': name,
        'command': command}
    com = Command(id=num, name=name, command=command)
    com.query.filter(Command.id == num).update(el)
    db.session.commit()
    return redirect('/')

# Нажатие кнопки Удалить - Удалить команду
@app.route("/del/", methods=['POST'])
def dell():
    print('del method')
    num = request.form['num']
    print(num)
    com = Command()
    com.query.filter(Command.id == num).delete()
    db.session.commit()
    return redirect('/')

# Нажатие кнопки Добавить - Открытие меню добавления команды
@app.route("/add_c/", methods=['POST'])
def add_c():
    print('add_c method')
    return render_template('add_com.html')

# Меню добавления команды - Нажатие кнопки Сохранить
@app.route("/save_new/", methods=['POST'])
def save_new():
    print('save_new method')
    name = request.form['name']
    command = request.form['command']

    print(name)
    print(command)

    #  Генерация ID и сохранение команды в БД
    com = Command(id=str(uuid.uuid4()), name=name, command=command)
    db.session.add(com)
    db.session.commit()
    return redirect('/')

# Меню добавления команды - Нажатие кнопки Отменить
@app.route("/cancel/", methods=['POST'])
def cancle():
    print('cancel method')
    return redirect('/')


