"""
@author: g23
#objective: test g23 podcast classes
"""
from classes.podcast import Podcast
from classes.guest import Guest
from classes.theme import PodcastTheme
from classes.podcastsponsor import PodcastSponsor
from classes.participation import Participation

# Read all classes from DB
Podcast.read('data/DadaBase_Podcast.db')
Guest.read('data/DadaBase_Podcast.db')
PodcastTheme.read('data/DadaBase_Podcast.db')
PodcastSponsor.read('data/DadaBase_Podcast.db')
Participation.read('data/DadaBase_Podcast.db')

# --- PODCAST ---
# Sort podcasts by title and print first 3
print('Podcasts sorted by title:')
Podcast.sort('_title')
for id in Podcast.lst[:3]:
    print(Podcast.obj[id])

# Create podcasts if none exist
if len(Podcast.lst) == 0:
    p1 = Podcast(0, '2024-01-10', 'Technology', 'Tech Talks')
    p2 = Podcast(0, '2024-02-15', 'Science', 'Ciencia Viva')
    Podcast.insert(p1.id)
    Podcast.insert(p2.id)

# --- GUEST ---
# Sort guests by name and print first 3
print('\nGuests sorted by name:')
Guest.sort('_name')
for id in Guest.lst[:3]:
    print(Guest.obj[id])

# Create guests if none exist
if len(Guest.lst) == 0:
    g1 = Guest(0, 'Joaquim Silva')
    g2 = Guest.from_string('0;Maria Santos')
    Guest.insert(g1.id)
    Guest.insert(g2.id)

# --- PODCASTTHEME ---
# Print themes linked to first podcast
first_podcast_id = Podcast.lst[0]
themes = PodcastTheme.getlines('_podcast_id', first_podcast_id)
print('\nTheme codes for podcast', first_podcast_id, ':', themes)
print('Themes for podcast', first_podcast_id, ':')
for id in themes:
    print(PodcastTheme.obj[id])

# Create a theme if none exist
if len(PodcastTheme.lst) == 0:
    t1 = PodcastTheme(0, 'Technology', first_podcast_id)
    PodcastTheme.insert(t1.theme_id)

# --- PODCASTSPONSOR ---
# Print sponsors linked to first podcast
sponsors = PodcastSponsor.getlines('_podcast_id', first_podcast_id)
print('\nSponsor codes for podcast', first_podcast_id, ':', sponsors)
print('Sponsors for podcast', first_podcast_id, ':')
for id in sponsors:
    print(PodcastSponsor.obj[id])

# Create a sponsor if none exist
if len(PodcastSponsor.lst) == 0:
    s1 = PodcastSponsor(0, 'extra info test', first_podcast_id)
    PodcastSponsor.insert(s1.id)

# --- PARTICIPATION ---
# Print participations linked to first podcast
# and show the guest details for each
first_guest_id = Guest.lst[0]
parts = Participation.getlines('_podcast_id', first_podcast_id)
print('\nParticipation codes for podcast', first_podcast_id, ':', parts)
print('Guests participating in podcast', first_podcast_id, ':')
for id in parts:
    guest_id = Participation.obj[id].guest_id
    print(Guest.obj[guest_id])

# Create a participation if none exist
if len(Participation.lst) == 0:
    par1 = Participation(0, '2024-01-10', 500, first_podcast_id, first_guest_id)
    Participation.insert(par1.id)
