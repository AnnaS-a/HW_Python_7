from input_data import surname
from input_data import name
from input_data import number_tel
from input_data import comment


def new_create(data):                                 
    # s, n, t, c = data
    xml = '<xml>\n'                                              
    xml += '    <surname unit = "">{}</surname>\n'\
        .format(surname())                                                  
    xml += '    <name unit = "">{}</name>\n'\
        .format(name())                           
    xml += '    <number_tel unit = "">{}</number_tel>\n'\
        .format(number_tel())   
    xml += '    <comment unit = "">{}</comment>\n'\
        .format(comment())    

    with open('new_data.xml', 'w') as page:              
        page.write(xml)                               
    return xml                                      
