#!/usr/bin/env python


import urllib

def main():
    print urllib.urlencode({"foo":"b/?ar"})
    

if __name__ == "__main__":
    main()