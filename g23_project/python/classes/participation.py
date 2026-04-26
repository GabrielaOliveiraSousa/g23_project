#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:16:56 2026

#@author: barbarasilva
"""
#Class Participation
from classes.guest import Guest
from classes.podcast import Podcast
# Import the generic class
from classes.gclass import Gclass

class Participation(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
 
    att = ['_id','_creation_date','_amount']
    
    header = 'Participation'

    des = ['Id','Creation_date','Amount']
    
    def __init__(self, id, creation_date, amount,podcast_id,guest_id):
        super().__init__()
        podcast_id = int(podcast_id)
        guest_id = int(guest_id)
        if podcast_id in Podcast.lst:
            if guest_id in Guest.lst:
                id = Participation.get_id(id)
                self._id = id
                self._creation_date = creation_date
                self._amount = int(amount)
              
                
                Participation.obj[id] = self
                Participation.lst.append(id)
            else:
                print('Podcast ', podcast_id, ' not found')
        else:
            print('Guest', guest_id, ' not found')

    @property
    def id(self):
        return self._id
    
    @property
    def creation_date(self):
        return self._creation_date
   
    @property
    def podcast_id(self):
        return self._podcast_id
    
    @property
    def guest_id(self):
        return self._guest_id
   
    @property
    def amount(self):
        return self._amount