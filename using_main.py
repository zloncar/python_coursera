#!/usr/bin/python
import sys

def main():
  try:
    sys.argv[1]
    print 'hi', sys.argv[1]

  except:
    print 'supply at least one argument'

if __name__ == '__main__':
  main()
