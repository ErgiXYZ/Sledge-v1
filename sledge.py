_1lO0O0lOOlIll = __import__('hashlib')
_1I0O1I0l1l0111OOO = 'https://pyobfuscate.com'
_II0011OO1O100001 = _1lO0O0lOOlIll.sha256(_1I0O1I0l1l0111OOO.encode('utf-8')).digest()

def _0OOlIlOO0IlIIl0I(_11l01O0O001l0l0I1O, _OO0lOII0l1O1lOO):
    _I1I0IOIlOIl1 = bytearray()
    _00010101IO = 0
    while len(_I1I0IOIlOIl1) < _11l01O0O001l0l0I1O:
        _I1I0IOIlOIl1 += _1lO0O0lOOlIll.sha256(_OO0lOII0l1O1lOO + _00010101IO.to_bytes(8, 'big')).digest()
        _00010101IO += 1
    return bytes(_I1I0IOIlOIl1[:_11l01O0O001l0l0I1O])
_1OlO01IOlOO0 = {}

def _I1OO1Oll101101(_O1I11OIlIl0, _0lIIO1O01I1):
    _lOl0lO1lI0I1l011O = (_O1I11OIlIl0, _0lIIO1O01I1)
    if _lOl0lO1lI0I1l011O in _1OlO01IOlOO0:
        return _1OlO01IOlOO0[_lOl0lO1lI0I1l011O]
    _1lOlOI10I0 = bytes((_IO0IOOOII1OI1lOII ^ _000lO1IlOII0 for _IO0IOOOII1OI1lOII, _000lO1IlOII0 in zip(_O1I11OIlIl0, _0OOlIlOO0IlIIl0I(len(_O1I11OIlIl0), _II0011OO1O100001 + _0lIIO1O01I1)))).decode('utf-8', 'surrogatepass')
    _1OlO01IOlOO0[_lOl0lO1lI0I1l011O] = _1lOlOI10I0
    return _1lOlOI10I0

def _l0l01l1000ll(_10IIOl000l0, _l1lIOOlll1IO11):
    _II1ll1lI00I11OO011 = (_10IIOl000l0, _l1lIOOlll1IO11)
    if _II1ll1lI00I11OO011 in _1OlO01IOlOO0:
        return _1OlO01IOlOO0[_II1ll1lI00I11OO011]
    _lOIO1I0OOIlIl1 = bytes((_0lII10O1O10llO1 ^ _I1IOl01lO01I1I0 for _0lII10O1O10llO1, _I1IOl01lO01I1I0 in zip(_10IIOl000l0, _0OOlIlOO0IlIIl0I(len(_10IIOl000l0), _II0011OO1O100001[::-1] + _l1lIOOlll1IO11)))).decode('utf-8', 'surrogatepass')
    _1OlO01IOlOO0[_II1ll1lI00I11OO011] = _lOIO1I0OOIlIl1
    return _lOIO1I0OOIlIl1

def _l00O1IOIlIl(_0OO0OI0OOOl00O, _O0O1OIIllOOOI0O):
    _0O1l01llIIIlOl011O = (_0OO0OI0OOOl00O, _O0O1OIIllOOOI0O)
    if _0O1l01llIIIlOl011O in _1OlO01IOlOO0:
        return _1OlO01IOlOO0[_0O1l01llIIIlOl011O]
    _Il0O0l0O01OO1O = bytes((_lI0I10lOO0I0101II ^ _00IIl01IO1lO for _lI0I10lOO0I0101II, _00IIl01IO1lO in zip(_0OO0OI0OOOl00O, _0OOlIlOO0IlIIl0I(len(_0OO0OI0OOOl00O), _1lO0O0lOOlIll.sha256(_II0011OO1O100001 + _O0O1OIIllOOOI0O).digest())))).decode('utf-8', 'surrogatepass')
    _1OlO01IOlOO0[_0O1l01llIIIlOl011O] = _Il0O0l0O01OO1O
    return _Il0O0l0O01OO1O
import requests as _O1lIIl00O1I01ll1lO
print(_l0l01l1000ll(b'`-+4\x19\xcd\xae\xfbNz.\x8b\x9cZj\x06\xabU\x05py\x87T\xc0\x03', b'\xc0\t\xe0\xb8'))
print(_l00O1IOIlIl(b'n\xa2\xdc\xc3D\x86\x7f\x87\xf5qXT8\x15\xeb.\x18\x84J\xa34\xda\xa1\xb0\x82', b'u\x87\xef,'))
print(_l00O1IOIlIl(b'\xefTN\xb2~\xa6=d\x1fX\xf7\x04S\\\xbf\x11\xa3\xe7\x8eZ}|\xb1', b'\xef\x83l\xd9'))
print(_l0l01l1000ll(b'O\xf934\x02\xdf\xd8\xca\n\x9a\xc2De\xef\x02\xb9n2\x8aC\x0f\xb9\x1c\xae', b'%\x8b\x92_'))
print(_l0l01l1000ll(b"F\xe9\x7f\x86;E1\xc2y\x17P\x93\xb0\xfef6\x9e\xc5\xc7'\xd0Y\xc7\x07", b'G3\xb2\xdd'))
print(_l0l01l1000ll(b'\xae0\x1e\xdbP\x06zH\xe3\xb8\xb2}\xd3&o3^Z\x08\xdb\xdd6\xf9=', b'.\xf7\xc4\n'))
print(_I1OO1Oll101101(b'\xb0\xce\xa5G\xa3\x8e\x1fN\xe5\x19\xe8G\xc65@\x0eV\xc3j\x04W\xe5\xfb>i', b'\xf3$%\xb5'))
print(_l00O1IOIlIl(b'vL\xe9d\xe4k\x86\x84\x00\xc9\xdc\x89\xe0\x7f\xa6Y\x1d\x8e(w\xbdn\xd8\xe2\x01>\xaf\xad9\x9e&\x02k\xca|', b'F\xccg\xdb'))
while True:
    _010l0IllII01llIlI0 = input(_l0l01l1000ll(b'\xb5U\x17\xe0*\xe6z4\xcc\xc3\x08e', b'AZ*\x1f'))
    _l00lOIOOIlIlI = int(input(_l0l01l1000ll(b'@\xc3\x0b\x8c\xaa]\x95,(\x16\xa8^I\xcfKb\xf20\x16\xdb\xd8\xd0GP$|\xb67\x83L\n|\xab\t\xc9\xa7\xc1\xc3\x1b\x9d\xb8\x8f4', b')L\xe4\xd6')))
    if _l00lOIOOIlIlI > 164989772 ^ 164989766:
        print(_l00O1IOIlIl(b'.\xfa-\x90\x927\xa8', b'/\xce\xc8S'))
        print(_I1OO1Oll101101(b"O\x19\x1c\x17\x97e\x98'\xa5\xce\xf8e\xcd\x0f\x9e*\xcd\xfb[\xa4{\xc5\x95\xe3\x9c\xc1k\x94\xf0", b'\\\xb9\xc6\xa7'))
        break
    for _00011OllO0OOI0II1 in range(_l00lOIOOIlIlI):
        _O0OI00O10lI = _O1lIIl00O1I01ll1lO.get(_010l0IllII01llIlI0)
        if _O0OI00O10lI.status_code == 88429947 ^ 88430003:
            print(_l00O1IOIlIl(b'\xfb\xbebR\xfb7G\xed\x98\x91{r\xc7r],\x9eJ\xf1{-', b'\xd3v\xd4`'))
        elif _O0OI00O10lI.status_code == 1644707941 ^ 1644708341:
            print(_l00O1IOIlIl(b"\x90\xad'\xf2\xe5\r\xe6y?\xc0\x82\xddg\x16\x10\xa9A\xc8\xdd\xc0", b'\xcd\xe2\x9c\x9d'))
        else:
            print(_I1OO1Oll101101(b'Z\x16\xff\xccDu\x87O\x87+c\xb5\xe2y\x9b\x83|"', b'\x15\xd1\xedp'))
    break