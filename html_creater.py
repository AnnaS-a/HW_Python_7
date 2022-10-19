from input_data import surname
from input_data import name
from input_data import number_tel
from input_data import comment


def new_create(data):                  
    style = 'style="font-size:22px;"'                
    html = '<html>\n <head></head>\n <body>\n'         
    html += '    <p {}>Surname: {} </p>\n'\
        .format(style, surname())                              
    html += '    <p {}>Name: {} </p>\n'\
        .format(style, name())                               
    html += '    <p {}>Number_tel: {} </p>\n'\
        .format(style, number_tel())   
    html += '    <p {}>Comment: {} </p>\n'\
        .format(style, comment())     

    with open('new_index.html', 'w') as page:              # записываем файл 
        page.write(html)                               # и его сохраняем
    return html                                     
    