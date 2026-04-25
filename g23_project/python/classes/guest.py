# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:58:49 2026

@author: GabrielaOliveiraSousa
"""

from classes.gclass import Gclass

class Guest(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id','_name']
    header = 'Guest'
    def __init__(self, id, name):
        super().__init__()
        id = Guest.get_id(id)
        self._id = id
        self._name = name
        Guest.obj[id] = self
        Guest.lst.append(id)
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name

   