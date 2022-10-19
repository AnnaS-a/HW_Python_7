from datetime import datetime as dt
from input_data import surname
from input_data import name
from input_data import number_tel
from input_data import comment


def surname_logger(data): 
    time = dt.now().strftime('%d.%m.%H:%M')    
    with open('log.csv', 'a', encoding= "utf-8") as file:    
        file.write('{}, surname, {}\n'.format(time, data))

def name_logger(data):
    time = dt.now().strftime('%d.%m.%H:%M')     
    with open('log.csv', 'a', encoding= "utf-8") as file:    
        file.write('{}, name, {}\n'.format(time, data))

def number_tel_logger(data):
    time = dt.now().strftime('%d.%m.%H:%M')     
    with open('log.csv', 'a', encoding= "utf-8") as file:    
        file.write('{}, number_tel, {}\n'.format(time, data))

def comment_logger(data):
    time = dt.now().strftime('%d.%m.%H:%M')     
    with open('log.csv', 'a', encoding= "utf-8") as file:    
        file.write('{}, comment, {}\n'.format(time, data))        

def read_log():
    with open('log.csv', "r", encoding="UTF-8") as f: 
        print(f.read())        
