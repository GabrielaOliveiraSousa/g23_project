"""
@author: g23
#objective: test g23 podcast classes
"""
from classes.podcast import Podcast
from classes.guest import Guest
from classes.participation import Participation
from classes.theme import Theme
from classes.sponsor import Sponsor

# Reads the classes info
Podcast.read('data/DadaBase_Podcast.db')
Guest.read('data/DadaBase_Podcast.db')
Participation.read('data/DadaBase_Podcast.db')
Theme.read('data/DadaBase_Podcast.db')
Sponsor.read('data/DadaBase_Podcast.db')

# Creates three products
if len(Podcast.lst) == 0:
    p1 = Podcast(0, 'Technology', 'Tech Talks', '10/01/2024')
    p2 = Podcast.from_string('0;Science;Ciencia Viva;15/02/2024')
    p3 = Podcast(0, 'Entertainment', 'Movie Talks', '20/03/2024')
    Podcast.insert(p1.id)
    Podcast.insert(p2.id)
    Podcast.insert(p3.id)

# Sort products in price ascending order
print('Products sorted by price:')
Podcast.sort('_title')

for id in Podcast.lst:
    print(Podcast.obj[id])

# Creates a customer
if len(Guest.lst) == 0:
    c1 = Guest(0, 'Joaquim Silva')
    Guest.insert(c1.id)

# Creates two orders
if len(Theme.lst) == 0:
    o1 = Theme(0, 'Technology', 1)
    o2 = Theme(0, 'Science', 1)
    Theme.insert(o1.id)
    Theme.insert(o2.id)

# Creates sponsors
if len(Sponsor.lst) == 0:
    s1 = Sponsor(0, 'extra info test', 1)
    s2 = Sponsor(0, 'new sponsor', 2)

    Sponsor.insert(s1.id)
    Sponsor.insert(s2.id)

# Creates product orders for order 1 and 2
if len(Participation.lst) == 0:
    op1 = Participation(0, '10/01/2024', 500, 1, 1)
    op2 = Participation(0, '11/01/2024', 300, 1, 1)
    op3 = Participation(0, '12/01/2024', 200, 2, 1)

    print(op1._id, op1._date, op1._views, op1._podcast_id, op1._guest_id)

    Participation.insert(op1.id)
    Participation.insert(op2.id)
    Participation.insert(op3.id)

# Select the products ordered in order 1
order = Participation.getlines('_podcast_id',1)

print('\nOrderProduct codes for order 1:', order)
print('Ordered products in order 1:')

for id in order:
    guest_id = Participation.obj[id].guest_id
    print(Guest.obj[guest_id])

# Select sponsors in podcast 1
sponsors = Sponsor.getlines('_podcast_id',1)

print('\nSponsor codes for podcast 1:', sponsors)
print('Sponsors in podcast 1:')

for id in sponsors:
    print(Sponsor.obj[id])
