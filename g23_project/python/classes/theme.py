# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:11:52 2026

@author: axlea
"""
from classes.gclass import Gclass
from classes.podcast import Podcast

class Theme(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    table = 'Theme'
    name = 'Theme'

    att = ['_id', '_subject', '_podcast_id']

    header = 'Theme'
    des = ['Theme_Id', 'Subject', 'Podcast_id']

    def _init_(self, id, subject, podcast_id):
        super()._init_()

        podcast_id = int(podcast_id)

        if podcast_id not in Podcast.lst:
            return

        id = Theme.get_id(id)

        self._id = id
        self._subject = subject
        self._podcast_id = podcast_id

        Theme.obj[id] = self
        Theme.lst.append(id)

    @property
    def id(self):
        return self._id

    @property
    def subject(self):
        return self._subject

    @property
    def podcast_id(self):
        return self._podcast_id
        else:
            print('Podcast', podcast_id, 'not found')
