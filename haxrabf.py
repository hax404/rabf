#!/usr/bin/python3
import Milter

class haxRAbF(Milter.Base):

  def envrcpt(self, to, *str):


    address = 'ghXXebay@reg.hax404.de'
    # extracted user with two chars at the start
    euser = address[0:2]
    # extracted domain
    edomain = address.split("@")[1]
    # extracted checksum
    ecsum = address[3:4]
    # extracted individual text
    eitext = euser, eaddress.split("@")[0][4:]
    # generated checksum; i think two chars of checksum should be enough
    gencsum = hashlib.sha512(itext.encode('utf-8')).hexdigest()[42:44]
