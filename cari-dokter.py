from requests import Session
from bs4 import BeautifulSoup as s
import os, inquirer

class alodoc:
    def __init__(self, spesialis, kota):
        self.u = f'https://www.alodokter.com/cari-dokter/dokter-{spesialis}/{kota}'.lower().replace(" ","-")        
        self.r = Session().get(self.u).text
        
    def result_data(self):
        soup = s(self.r, 'html.parser')
        find = soup.findAll("card-list-doctor-procedure")
        data = [datas for datas in find]
        for mydata in data:
            city = mydata.get('district-detail')
            rating = mydata.get('doctor-rating')
            spesialis = mydata.get('doctor-procedure')
            rumkit = mydata.get('hospital-name')
            name_dr = mydata.get('name-doctor')
            price = mydata.get('price')
            p_url = mydata.get('url-detail')
            b_url = mydata.get('url-reservation')
            ulasan = mydata.get('total-review')
            print(f'''
{"+" *50}                        
Nama dokter      : {name_dr}
spesialis        : {spesialis}
Rumah sakit      : {rumkit}
Lokasi/kota v    : {city}
Biaya Konsultasi : {price}
Dokter Rating    : {rating}
Ulasan           : {ulasan}
{"+" *50}\n''')

os.system('clear')
question = [inquirer.List('search',
                 message="cari dokter spesialis?",
                 choices=["Penyakit dalam","Anak","Saraf","Kulit","Bedah","THT","Kandungan","Psikiater","Dokter gigi"]
                 )
           ]
answer = inquirer.prompt(question)
question = [inquirer.Text('loc',message='Kamu ingin mencari di lokasi mana')]
answers = inquirer.prompt(question)
alodoc(answer["search"],answers["loc"]).result_data()
input()