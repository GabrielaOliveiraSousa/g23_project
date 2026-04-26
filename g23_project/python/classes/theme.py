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

    att = ['_podcast_id', '_subject', '_id']

    header = 'Theme'
    des = ['Podcast_id', 'Subject', 'Theme_Id']

    def __init__(self, podcast_id, subject, id):
        super().__init__()

        podcast_id = int(podcast_id)

        if podcast_id in Podcast.lst:
            id = Theme.get_id(id)

            self._id = id
            self._subject = subject
            self._podcast_id = podcast_id

            if id not in Theme.obj:
                Theme.obj[id] = self
                Theme.lst.append(id)
        else:
            print('Podcast', podcast_id, 'not found')

    @property
    def id(self):
        return self._id

    @property
    def subject(self):
        return self._subject

    @property
    def podcast_id(self):
        return self._podcast_id
