from bs4 import BeautifulSoup
import webbrowser as broswer
import requests as req


baseUrl = 'https://www.subito.it/'
path = 'annunci-italia/vendita/usato/?q='


def getURL(product):
   URL = (
      baseUrl +
      path +
      product +
      '/'
   )
   URL = URL.replace(' ', '+')
   print('Opening %s ...' % URL)
   return URL

def makeReq(url):
   res = req.get(url)
   res.raise_for_status()
   return res.text

def scraping(html):
   html_parsed = BeautifulSoup(html, 'html.parser')
   div_annunci = html_parsed.find('div', class_ = 'visible')
   return div_annunci.find_all('a')

def getAnnunci(anchors):
   link_annunci = []
   for anchor in anchors:
      link_annuncio = str(anchor.get('href'))
      link_annunci.append(link_annuncio)
   return link_annunci

def getFilePath(product):
  return 'out/%s.txt' % product

def readFileAnnunci(fpath):
   return [
      row.rstrip('\n')
      for row in open(fpath)
    ]

def openLinks(links):
   for link in links:
      broswer.open(link)
      

"""
       info = 'Number: %s ;\n \n' % str(num_annunci)
        print(info)
        f.write(info)
"""
