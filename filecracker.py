import rarfile
import pikepdf
import huepy

"""
It run only on your computer so if you try to use it in sololearn compiler it dos not work


"""
from tqdm import tqdm
wordlist='adminfinder.txt'
rar='help.rar'
words_n=len(list(open(wordlist,'rb')))

def cracker(rar,wordlist,words_n):
    print('Total passwords to use {}'.format(words_n))
    rar=rarfile.RarFile(rar)

    with open(wordlist,'rb') as wlist:
        for word in tqdm(wlist,total=words_n,unit='word'):

            try:
                rar.extractall(pwd=word.strip())
                print('Password Found')

            except Exception as e:
                continue
            else:
                print(huepy.good('Password found: {}'.format(word)))
                exit()

        print(huepy.bad('Password Not found'))

    


passwords=[line.strip() for line in open('adminfinder.txt')]

pdffile='help.pdf'
def pdfcracker(passwords,pdfflie):
    for password in tqdm(passwords,'Decryption pdf '):
        try:
            #open pdf file
            with pikepdf.open(pdfflie,password=password)as pdf:

                print(huepy.good('File cracked successfully {}'.format(password)))
                break
        except pikepdf._qpdf.PasswordError as e:
            continue





print('-'*20+'Extract me'+'-'*20)
print('    Coded by cdead2 github ')
print('Sololearn hussain')
print("""
1> for rar files
2> for pdf files
99> to leave



""")
ch=input('Choose : ')
if ch=='1':
    cracker(rar,wordlist,words_n)
elif ch=='2':
    pdfcracker(passwords,pdffile)
else:
    quit(0)