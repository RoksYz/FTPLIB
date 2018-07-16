from ftplib import FTP
ftp = FTP("DOMAINNAME.COM")
ftp.login(user='username',passwd='password')

ftp.cwd('/specificdomain-or-location/')

def grabFile():
    fileName = 'FileName.txt'
    localfile = open(fileName,'wb')
    ftp.retrbinary("RETR"+fileName,localfile.write,1024)
    ftp.quit()
    localfile.close()


    def placeFile():
        filename = 'Filename.txt'
        ftp.storbinary('STOR'+filename, open(filename,'rb'))
        ftp.quit()
    """"
    REZ
    """"