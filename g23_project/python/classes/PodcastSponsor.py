from classes.podcast import Podcast
from classes.gclass import Gclass

class PodcastSponsor(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_sponsor_id','_extra_info','_podcast_id']
    header = 'CustomerOrder'
    des = ['Sponsor_id','Extra_info','Podcast_id']
    def __init__(self, id, extra_info, podcast_id):
        super().__init__()
        podcast_id =int(podcast_id)
        if podcast_id in Podcast.lst:
            id = PodcastSponsor.get_id(id)
            self._id = id
            self._extra_info=extra_info
            self._podcast_id = podcast_id

            PodcastSponsor.obj[id] = self
            PodcastSponsor.lst.append(id)
        else:
            print('Customer ', podcast_id, ' not found')
    @property
    def id(self):
        return self._id
    @property
    def extra_info(self):
        return self._extra_info
    @property
    def podcast_id(self):
        return self._podcast_id
            
