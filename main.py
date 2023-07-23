from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import DVD
from modules.cd import CD
from modules.catalog import Catalog
import json

book1 = Book(
    'How to live without',
    None,
    'Psychology',
    '9876-9080-09',
    'Kim Mingyu',
    '00909076'
)

book2 = Book(
    'Forever with you',
    None,
    'Fiction',
    '9876-9080-06',
    'Jeon Wonwoo',
    '0000006'
)

book3 = Book(
    'Menjadi Pemimpin',
    None,
    'Leadership',
    '9876-9080-01',
    'SCOUPS',
    '0000001'
)

magazine1 = Magazine(
    'VOGUE',
    None,
    'Edisi 22 Juli',
    'XXII',
    '-'
)

magazine2 = Magazine(
    'BAZAAR',
    None,
    'Edisi 15 Juni',
    'XV',
    '-'
)

magazine3 = Magazine(
    'SPOTLIGHT',
    None,
    'Edisi 4 Oktober',
    'IV',
    '-'
)

dvd1 = DVD(
    'Power of Love',
    None,
    'Concet DVD',
    'Seventeen',
    'Kim Mingyu & Jeon Wonwoo',
    'Musical'
)

dvd2 = DVD(
    'THE BEST DAY',
    None,
    'K-Pop',
    'DAY6',
    'Park Sungjin',
    'Biography'
)

dvd3 = DVD(
    'Caratland',
    None,
    'Fanmeeting',
    'Seventeen',
    'Kim Mingyu',
    'Documenter'
)

cd1 = CD(
    'Remember Us',
    None,
    '-',
    'DAY6'
)

cd2 = CD(
    'DYE',
    None,
    '-',
    'GOT7'
)

cd3 = CD(
    'Attacca',
    None,
    '-',
    'SEVENTEEN'
)

#collect data per jenis
book = [book1, book2, book3]
magazine = [magazine1, magazine2, magazine3]
dvd = [dvd1, dvd2, dvd3]
cd = [cd1, cd2, cd3]

#get data from json
f = open('files/catalog.json')
data_json = json.load(f)

#create object from data json
for item in data_json:
    if item['source'] == 'book':
        book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            isbn=item['isbn'],
            authors=item['authors'],
            dds_number=item['dds_number'],
        ))
    elif item['source'] == 'magazine':
        magazine.append(Magazine(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume=item['volume'],
            issue=item['issue'],
        ))
    elif item['source'] == 'dvd':
        dvd.append(DVD(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            actors=item['actors'],
            director=item['director'],
            genre=item['genre'],
        ))
    elif item['source'] == 'cd':
        cd.append(CD(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            artist=item['artist'],
        ))

# collect all data
catalog_all = [book, magazine, dvd, cd]

#input search
input_search = 'caratland'
results = Catalog(catalog_all).search(input_search)
if results:
    for index, result in enumerate(results):
        print(f'Result ke -{index+1} | {result}')
else:
    print('NO RESULT')