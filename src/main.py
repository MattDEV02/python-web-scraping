from utils import *
from winsound import Beep
from notify_run import Notify


notify = Notify(endpoint = ENDPOINT)
checkCond()
product = input('Product:  ')
print('Started at %s' % now())

while True:
   URL = getURL(product)
   html = makeReq(URL)
   anchors = scraping(html)
   link_annunci = getAnnunci(anchors)

   if len(link_annunci) > 0:
      fpath = getFilePath(product)
      f = getFile(fpath)
      if f:
         old_link_annunci = readFileAnnunci(fpath)
         new_link_annunci = []
         for link_annuncio in link_annunci:
            if link_annuncio not in old_link_annunci:
               new_link_annunci.append(link_annuncio)
               f.write('%s\n' % link_annuncio)
               print('%s writed to %s' % (link_annuncio, absPath(fpath)))
         f.close()
         if new_link_annunci:
            num_annunci = str(len(new_link_annunci))
            print('New Results!! opening %s annunci...' % num_annunci)
            Beep(2500, 350)
            msg = '%s nuovi annunci per il prodotto %s !' % (num_annunci, product)
            notify.send(msg, new_link_annunci[-1])
            openLinks(new_link_annunci)
         else:
            print('There are not new Results.')
      else:
         print('File not valid.')
         break
   else:
      print('Zero Results.')





