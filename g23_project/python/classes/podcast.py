"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Podcast(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_podcast_id','_date','_category','_title']
    # Class header title
    header = 'Podcasts'
    # field description for use in, for example, input form
    des = ['Podcast_Id','Date','Category','Title']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, date, category, title):
        super().__init__()
        # Object attributes
        id = Podcast.get_id(id)
        self._podcast_id = id
        self._category = category
        self._date = datetime.date.fromisoformat(date)
        self._title = title
        # Add the new object to the dictionary of objects
        Podcast.obj[id] = self
        # Add the id to the list of object ids
        Podcast.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._podcast_id
    @id.setter
    def id(self, id):
        self._podcast_id = id
    # name property getter method
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    # dob property getter method
    @property
    def date(self):
        return self._date
    # dob property setter method
    @date.setter
    def date(self, date):
        self._date = date
    # salary property getter method
    @property
    def category(self):
        return self._category
    # salary property setter method
    @category.setter
    def category(self, category):
        self._category = category