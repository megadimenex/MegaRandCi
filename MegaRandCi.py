
# Attention:
# All ciphers generated in this program are temporary and this program does not store any information.
# The ciphers generated in this program are completely random and can not be returned, so if you use\
# this code to register in a special software or sites, be sure to save the relevant cipher in a safe place.

# Features:
# This code is a parameter-based (System Time, System Date and MAC Address) cipher generation program.\
# You can adjust it according to your needs the conditions in below are adjustable:
# Generate one cipher with a length between 4 to 20 characters.
# Generate one cipher with random length.
# Generate cipher in a period of 1 to 120 seconds with a length of 4 to 20 characters.
# Generate cipher at random period with random length.

import random
import string
import secrets
from datetime import datetime
import getmac
import time


def start():
    qtime = int(input('How many seconds to generate a new cipher (between 1 and 120 sec)?\
 OR for generate just "one cipher" press "0": '))
    qlength = int(input('Please choose length cipher (between 4 and 20 character)\
 OR for random length cipher press "0": '))

    if (qlength == 0 or 4 <= qlength <= 20) and (qtime == 0 or 1 <= qtime <= 120):
        cond(qlength, qtime)
    else:
        myprint('Error(1000) = ', 'Please enter a correct number')
    return


def cond(lncipher, signal):
    if lncipher != 0 and signal == 0:
        genrand(lncipher)
    elif lncipher != 0 and signal != 0:
        genrand(lncipher)
        cycle(lncipher, signal, 0)
    elif lncipher == 0 and signal != 0:
        ln = random.randint(4, 20)
        genrand(ln)
        cycle(lncipher, signal, 1)
    elif lncipher == 0 and signal == 0:
        ln = random.randint(4, 20)
        genrand(ln)
    else:
        myprint('Error Code = ', '5000')
        return
    return


def genrand(lengthcipher):
    gsysdata = sysdata()
    chars = string.ascii_letters + string.digits + string.punctuation + gsysdata
    charslist = list(chars)
    shuffle(charslist)
    cip = ''.join(secrets.choice(charslist) for x in range(lengthcipher))
    myprint("Cipher ======> ", str(cip))
    return str(cip)


def cycle(lengthcipher, sec, r):
    if r == 1:
        myprint("Wait:", f"{sec} sec")
        ln = random.randint(4, 20)
        time.sleep(sec)
        genrand(ln)
        cycle(ln, sec, r)
    elif r == 0:
        myprint("Please wait:", f"{sec} sec")
        time.sleep(sec)
        genrand(lengthcipher)
        cycle(lengthcipher, sec, r)
    else:
        myprint('Error = ', 'Signal is not correct')

    return


def sysdata():
    gtime = int(datetime.now().strftime("%H%M%S"))
    gtime = bin(gtime).replace('0b', '')
    gdate = int(datetime.today().strftime('%Y%m%d'))
    gdate = bin(gdate).replace('0b', '')
    gmac = getmac.get_mac_address().replace(':', '')
    gmac = "{0:08b}".format(int(gmac, 16))
    gxor = bin(int(gtime, 2) ^ int(gdate, 2) ^ int(gmac, 2)).replace('0b', '')
    dec = int(gxor, 2)
    hexadec = hex(dec).replace('0x', '')
    return hexadec


def shuffle(chlist):
    n = 200
    for chl in range(n):
        random.shuffle(chlist)
        return
    return


def myprint(name, value):
    print(f'{name}', value)
    return


start()





