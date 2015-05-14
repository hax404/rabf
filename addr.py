#!/usr/bin/python3
import argparse
import hashlib

parser = argparse.ArgumentParser(description='Generate and verify Address')
parser.add_argument('--verify')
parser.add_argument('--generate')
args = parser.parse_args()

def verify_addr(addr):
  euser = addr[0:2]
  edomain = addr.split("@")[1]
  ecsum = addr[2:4]
  eitext = addr.split("@")[0][4:]
  genitext = ''.join((euser, eitext))
  gencsum = hashlib.sha512(genitext.encode('utf-8')).hexdigest()[41:43]

  if (ecsum == gencsum):
    print ("Checksum of address", addr, "is right")
  else:
    print ("Checksums differ:\nextracted Checksum:", ecsum, "\ngenerated Checksum:", gencsum)

def gen_addr(addr):
  euser = addr[0:2]
  edomain = addr.split("@")[1]
  eitext = addr.split("@")[0][2:]
  genitext = ''.join((euser, eitext))
  gencsum = hashlib.sha512(genitext.encode('utf-8')).hexdigest()[41:43]

  print ("Generated Checksum:", gencsum)
  print ("Generated Address:", "".join((euser,gencsum,eitext,"@",edomain)))

def main():
  if args.verify:
    verify_addr(args.verify)
  elif args.generate:
    gen_addr(args.generate)

if __name__ == "__main__":
  main()


