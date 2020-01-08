import sys
import requests
import urllib.parse

def main(argv):
  url = "http://challenge-server.code-check.io/api/hash?q=" + urllib.parse.quote(argv[0])
  response = requests.request("GET", url)
  result = response.json()
  print(result["hash"])

if __name__ == '__main__':
    main(sys.argv[1:])
