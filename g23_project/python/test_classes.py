"""
@author: g23
#objective: test g23 podcast classes
"""
from classes.podcast import Podcast
from classes.guest import Guest
from classes.theme import Theme
from classes.sponsor import Sponsor
from classes.participation import Participation

# ========================
# READ DATABASE
# ========================
Podcast.read('data/DadaBase_Podcast.db')
Guest.read('data/DadaBase_Podcast.db')
Theme.read('data/DadaBase_Podcast.db')
Sponsor.read('data/DadaBase_Podcast.db')
Participation.read('data/DadaBase_Podcast.db')

# ========================
# PODCAST
# ========================
print('Podcasts sorted by title:')
Podcast.sort('_title')

for id in Podcast.lst[:3]:
    print(Podcast.obj[id])

if len(Podcast.lst) == 0:
    p1 = Podcast(0, 'Tech Talks', 'Technology', '2024-01-10')
    p2 = Podcast(0, 'Ciencia Viva', 'Science', '2024-02-15')
    Podcast.insert(p1.id)
    Podcast.insert(p2.id)

# ========================
# GUEST
# ========================
print('\nGuests sorted by name:')
Guest.sort('_name')

for id in Guest.lst[:3]:
    print(Guest.obj[id])

if len(Guest.lst) == 0:
    g1 = Guest(0, 'Joaquim Silva')
    g2 = Guest.from_string('0;Maria Santos')
    Guest.insert(g1.id)
    Guest.insert(g2.id)

# ========================
# THEME
# ========================
first_podcast_id = Podcast.lst[0]

themes = Theme.getlines('_podcast_id', first_podcast_id)

print('\nTheme codes for podcast', first_podcast_id, ':', themes)
print('Themes for podcast', first_podcast_id, ':')

for id in themes:
    print(Theme.obj[id])

if len(Theme.lst) == 0:
    t1 = Theme(first_podcast_id, 'Technology', 0)
    Theme.insert(t1.id)

# ========================
# SPONSOR
# ========================
sponsors = Sponsor.getlines('_podcast_id', first_podcast_id)

print('\nSponsor codes for podcast', first_podcast_id, ':', sponsors)
print('Sponsors for podcast', first_podcast_id, ':')

for id in sponsors:
    print(Sponsor.obj[id])

if len(Sponsor.lst) == 0:
    s1 = Sponsor(0, first_podcast_id, 'extra info test')
    Sponsor.insert(s1.id)

# ========================
# PARTICIPATION
# ========================
first_guest_id = Guest.lst[0]

parts = Participation.getlines('_podcast_id', first_podcast_id)

print('\nParticipation codes for podcast', first_podcast_id, ':', parts)
print('Guests participating in podcast', first_podcast_id, ':')

for id in parts:
    guest_id = Participation.obj[id].guest_id
    print(Guest.obj[guest_id])

if len(Participation.lst) == 0:
    par1 = Participation(first_guest_id, first_podcast_id, '10/01/2024', 500)
    Participation.insert(par1.id)
