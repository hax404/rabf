#!/usr/bin/python3
import argparse
import hashlib

parser = argparse.ArgumentParser(description='Generate and verify Address')
parser.add_argument('--verify')
args = parser.parse_args()

def verify_addr(addr):
  euser = addr[0:2]
  edomain = addr.split("@")[1]
  ecsum = addr[2:4]
  eitext = ''.join((euser, addr.split("@")[0][4:]))
  gencsum = hashlib.sha512(eitext.encode('utf-8')).hexdigest()[41:43]

  print(euser, edomain, ecsum, eitext, gencsum)
  print(hashlib.sha512(eitext.encode('utf-8')).hexdigest())

  if (ecsum == gencsum):
    print ("Checksum of address", addr, "is right")
  else:
    print ("Checksums differ:\nextracted Checksum:", ecsum, "\ngenerated Checksum:", gencsum)

def main():
  verify_addr(args.verify)

if __name__ == "__main__":
  main()


