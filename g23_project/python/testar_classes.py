# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:47:23 2026
@author: GabrielaOliveiraSousa
"""

import datetime
from classes.podcast import Podcast
from classes.guest import Guest
from classes.participation import Participation
from classes.theme import Theme
from classes.sponsor import Sponsor


Podcast.read('data/DadaBase_Podcast.db')
Guest.read('data/DadaBase_Podcast.db')


# test_class = Participation
# ob = '150;983;2026-05-12;500'  


# test_class = Guest
# ob = '999;Nome do Convidado'


test_class = Podcast
ob = '200;O Meu Novo Podcast;Saude;2026-05-12'


# test_class = Sponsor
# ob = '0;150;Anuncio de 30 segundos'  


# test_class = Theme
# ob = '0;Tecnologia;150'  



test_class.read('data/DadaBase_Podcast.db')

op = ''
while op != 'q':
    print('')
    print(f'--- TESTING CLASS: {test_class.__name__} ---')
    print('Choose one letter for select the option')
    print('---------------')
    print('l - list')
    print('b - beginning')
    print('n - next')
    print('p - previous')
    print('e - end')
    print('---------------')
    print('i - insert')
    print('m - modify')
    print('r - remove')
    print('---------------')
    print('s - sort by attribute')
    print('f - find by attribute')
    print('---------------')
    print('q - quit')
    print('---------------')
    
    p = test_class.current()
    print(f'\n{p}')
    op = input('?')
    
    if op == 'b':
        test_class.first()
    elif op == 'n':
        test_class.nextrec()
    elif op == 'p':
        test_class.previous()
    elif op == 'e':
        test_class.last()
    elif op == 'i':
        p1 = None
        if len(test_class.lst) == 0:
            p = eval('test_class.from_string("' + ob + '")')
            p1 = p
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        print('leave blank to auto-increment')
        id = input(f'{attrib[1:]} = ')
        if id == "":
            id = 0
        else:
            id = int(id)
        strarg = f'test_class({id}'
        for i in range(1, len(str_list)):
            attrib = str_list[i]
            atype = type(getattr(p, attrib))
            if atype == datetime.date or atype == str:
                value = input(f'{attrib[1:]} = ')
                strarg += f',"{value}"'
            else:
                value = atype(input(f'{attrib[1:]} = '))
                strarg += f',{value}'
        strarg += ')'
        if p1 != None:
            test_class.remove(getattr(p, str_list[0]))
        print(strarg)
        pobj = eval(strarg)
        attrib = str_list[0]
        code = getattr(pobj, attrib)
        obj = test_class.current(code)
        test_class.insert(code)

    elif op == 'm':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        id = input(f'Record {attrib[1:]} = ') 
        if id != "":
            id = int(id)
            obj = test_class.current(id)
            print('Leave blank or new value to modify')
            for attrib in str_list[1:]:
                value = input(f'{attrib[1:]} = ') 
                if value != "":
                    atype = type(getattr(p, attrib))
                    if atype == datetime.date:
                        setattr(obj, attrib, datetime.ate.fromisoformat(value))
                    else:
                        setattr(obj, attrib, atype(value))
        test_class.update(id)
        
    elif op == 'r':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        cod = atype(input(f'{attrib[1:]} = '))
        if cod in test_class.lst:
            print(test_class.obj[cod])
            print('Confirm that you want to delete the record (y/n)?', end='')
            if input().upper() == 'Y':
                test_class.remove(cod)
                
    elif op == 'l':
        for code in test_class.lst:
            print(test_class.obj[code])
            
    elif op == 's':
        attrib = input('sort by attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            reverse = False
            if input('Reverse (False):'):
                reverse = True
            codep = p.id         
            test_class.sort(attrib, reverse)
            for code in test_class.lst:
                print(test_class.obj[code])
            test_class.current(codep)
            
    elif op == 'f':
        attrib = input('Attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            atype = type(getattr(p, attrib))
            value = atype(input('Value:'))
            fobjs = test_class.find(value, attrib)
            if len(fobjs) > 0:
                test_class.current(fobjs[0].id)
                for obj in fobjs:
                    print(obj)
