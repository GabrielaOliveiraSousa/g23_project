# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:11:52 2026

@author: axlea
"""

from classes.podcast import Podcast
from classes.gclass import Gclass

class PodcastTheme(Gclass()):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_theme_id','_subject','_podcast_id']

    header = 'Theme'
    des = ['Theme_Id','Subject','Podcast_id']

    def __init__(self, id, subject, podcast_id):
        super().__init__()
        # Object attributes
        # Check the customer referential integrity
        podcast_id =int(podcast_id)
        if podcast_id in Podcast.lst:
            id = PodcastTheme.get_theme_id(id)
            self._theme_id = id
            self._subject = subject
            self._podcast_id = podcast_id
            # Add the new object to the Order list
            PodcastTheme.obj[id] = self
            PodcastTheme.lst.append(id)
        else:
            print('Podcast ', podcast_id, ' not found')

    @property
    def theme_id(self):
        return self._theme_id
    @property
    def subject(self):
        return self._subject
    @subject.setter
    def subject(self, subject):
        self._subject = subject
    @property
    def podcast_id(self):
        return self._podcast_id
    @podcast_id.setter
    def podcast_id(self, podcast_id):
        if podcast_id in Podcast.lst:
            self._podcast_id = podcast_id
        else:
            print('Podcast ', podcast_id, ' not found')    
            
