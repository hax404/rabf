#!/usr/bin/python3
import Milter
import time

class haxRAbF(Milter.Base):

  def envrcpt(self, to, *str):
    a = 23
    b = 42
    addr = to
    euser = addr[0:2]
    edomain = addr.split("@")[1]
    ecsum = addr[2:4]
    eitext = addr.split("@")[0][4:]
    genitext = ''.join((euser, eitext))
    gencsum = hashlib.sha512(genitext.encode('utf-8')).hexdigest()
    posa = int(a)-1
    posb = int(b)-1
    csuma = str(gencsum[posa:posa+1])
    csumb = str(gencsum[posb:posb+1])

    if (ecsum == "".join((csuma,csumb))):
      print ("Checksum of address", addr, "is right")
    else:
      print ("Checksums differ:\nextracted Checksum:", ecsum, "\ngenerated Checksum:", "".join((csuma,csumb)))

  def log(self,*msg):
    logq.put((msg,self.id,time.time()))

  def background():
    while True:
      t = logq.get()
      if not t: break
      msg,id,ts = t
      print ("%s [%d]" % (time.strftime('%Y%b%d %H:%M:%S',time.localtime(ts)),id),)
      # 2005Oct13 02:34:11 [1] msg1 msg2 msg3 ...
      for i in msg: print (i),
      print ()

def main():
  bt = Thread(target=background)
  bt.start()
  socketname = "/tmp/haxrabf"
  timeout = 600
  Milter.factory = haxRAbF
  print ("%s milter startup" % time.strftime('%Y%b%d %H:%M:%S'))
  sys.stdout.flush()
  Milter.runmilter("pythonfilter",socketname,timeout)
  logq.put(None)
  bt.join()
  print ("%s bms milter shutdown" % time.strftime('%Y%b%d %H:%M:%S'))

if __name__ == "__main__":
  main()
