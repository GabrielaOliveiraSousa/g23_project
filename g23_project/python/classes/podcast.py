from classes.gclass import Gclass
import datetime
class Podcast(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_podcast_id','_date','_category','_title']
    header = 'Podcasts'
    des = ['Podcast_Id','Date','Category','Title']
    def __init__(self, id, date, category, title): 
        super().__init__()
        id = Podcast.get_id(id)
        self._podcast_id = id
        self._date = datetime.date.fromisoformat(date) 
        self._category = category
        self._title = title
        Podcast.obj[id] = self
        Podcast.lst.append(id)
    @property
    def id(self):
        return self._podcast_id
    @id.setter
    def id(self, id):
        self._podcast_id = id
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        self._date = date
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        self._category = category
