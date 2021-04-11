from utils import *
    

while True:
    product = input('Product: ')
    if product == '0':
        break
    url = getURL(product)

    html = makeReq(url)
    anchors = scraping(html)
    link_annunci = getAnnunci(anchors)
    num_annunci = len(link_annunci)

    if num_annunci > 0:
        fpath = getFilePath(product)
        f = open(fpath, 'a')
        old_link_annunci = readFileAnnunci(fpath)
        new_link_annunci = []
        for link_annuncio in link_annunci:
            if link_annuncio not in old_link_annunci:
                new_link_annunci.append(link_annuncio)
                f.write('%s\n' % link_annuncio)
        f.close()

        if(new_link_annunci):
            print('New Results!! Opening...')
            openLinks(new_link_annunci)
        else:
            print('There are not new Results.')

    else:
        print('Zero Results')


print('Finish.')

