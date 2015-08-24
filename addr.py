#!/usr/bin/python3
import argparse
import hashlib

parser = argparse.ArgumentParser(description='Generate and verify Address')
parser.add_argument('--verify')
parser.add_argument('--generate')
parser.add_argument('a')
parser.add_argument('b')
args = parser.parse_args()

def verify_addr(addr,a,b):
  euser = addr[0:2]
  edomain = addr.split("@")[1]
  ecsum = addr[2:4]
  eitext = addr.split("@")[0][4:]
  genitext = ''.join((euser, eitext, edomain))
  gencsum = hashlib.sha512(genitext.encode('utf-8')).hexdigest()
  posa = int(a)-1
  posb = int(b)-1
  csuma = str(gencsum[posa:posa+1])
  csumb = str(gencsum[posb:posb+1])

  if (ecsum == "".join((csuma,csumb))):
    print ("Checksum of address", addr, "is right")
  else:
    print ("Checksums differ:\nextracted Checksum:", ecsum, "\ngenerated Checksum:", "".join((csuma,csumb)))

def gen_addr(addr,a,b):
  euser = addr[0:2]
  edomain = addr.split("@")[1]
  eitext = addr.split("@")[0][2:]
  genitext = ''.join((euser, eitext, edomain))
  posa = int(a)-1
  posb = int(b)-1
  gencsum = hashlib.sha512(genitext.encode('utf-8')).hexdigest()
  csuma = str(gencsum[posa:posa+1])
  csumb = str(gencsum[posb:posb+1])

  print ("Generated Checksum:", "".join((csuma,csumb)))
  print ("Generated Address:", "".join((euser,"".join((csuma,csumb)),eitext,"@",edomain)))

def main():
  if args.verify:
    verify_addr(args.verify,args.a,args.b)
  elif args.generate:
    gen_addr(args.generate,args.a,args.b)

if __name__ == "__main__":
  main()


