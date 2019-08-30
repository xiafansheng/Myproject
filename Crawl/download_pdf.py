import  requests
import urllib
def download_pdf(url,name):
    path = name+'.pdf'
    r = requests.get(url)
    print(r.content)
    f = open(r'C:\pycharm project\Crawl\pbc\%s'%path,'wb')
    f.write(r.content)
    f.close()

def download(url,name):
    path = name + '.pdf'
    data = urllib.request.urlopen(url).read()
    print(data)
    f = open(r'C:\pycharm project\Crawl\pbc\%s'% path, 'wb')
    f.write(data)



download_pdf('http://gs.cufe.edu.cn/system/resource/storage/download.jsp?mark=RjhGQzVERDMzQzVDNzBGQTc5N0VEM0Y0OUJERDhBRTYvOUY2NzYxRUYvMTcwRTg=','2')