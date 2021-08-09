from bs4 import BeautifulSoup
import webbrowser as broswer
import requests as req
import datetime
from os import remove, mkdir
from glob import glob
from sys import argv


baseUrl = 'https://www.subito.it/'

regione = 'italia'
categoria = 'usato'
num_args = len(argv)

if num_args == 2:
   regione = argv[1]
elif num_args > 2:
   regione = argv[1]
   categoria = argv[2]

path = 'annunci-%s/vendita/%s/?q=' % (regione, categoria)

ENDPOINT = 'https://notify.run/XMGH1KBh8dD3ks6X'


def checkCond():
   cond = input('Clear all? y/n [n]:  ')
   cond = cond.lower()
   if cond == 'y' or cond == 'yes' or cond == '1' or cond == 'ok':
      files = glob('../out/*')
      num_files = len(files)
      for file in files:
         remove(file)
      print('Removed %s files.' % str(num_files))
   else:
      print('Nothig removed.')

def now():
   return str(datetime.datetime.now())

def getURL(product):
   URL = (
           baseUrl +
           path +
           product +
           '&from=top-bar'
   )
   URL = URL.replace(' ', '+')
   print('[ %s ] Searching in %s ...' % (now(), URL))
   return URL

def makeReq(url):
   res = req.get(url)
   res.raise_for_status()
   return res.text

def scraping(html):
   html_parsed = BeautifulSoup(html, 'html.parser')
   div_annunci = html_parsed.find('div', class_='visible')
   return div_annunci.find_all('a')

def getAnnunci(anchors):
   link_annunci = []
   for anchor in anchors:
      link_annuncio = str(anchor.get('href'))
      link_annunci.append(link_annuncio)
   return link_annunci

def getFilePath(product):
   return '../out/%s.log' % product

def getFile(fpath):
   f = None
   mode = 'a+'
   try:
      f = open(fpath, mode)
   except FileNotFoundError:
      mkdir('../out')
      f = open(fpath, mode)
   return f

def readFileAnnunci(fpath):
   print('Cheching old annunci in %s ...' % fpath)
   return [
      row.rstrip('\n')
      for row in open(fpath)
   ]

def openLinks(links):
   for i, link in enumerate(reversed(links)):
      print('Opening link number %s = %s ...' % (str(i), link) )
      broswer.open(link)

