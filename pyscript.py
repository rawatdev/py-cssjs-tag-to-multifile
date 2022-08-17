import os
import glob

from bs4 import BeautifulSoup

# Change path of files inside join
for selectedFile in glob.glob(os.path.join("./project", "*.html")):
  with open(selectedFile, "r") as readFile:
    soup = BeautifulSoup(readFile.read(), 'html.parser')
    # Change the css link (relative to html)
    soup.head.append(BeautifulSoup('<link rel="stylesheet" href="./css/style.css">','html.parser'))
    # Change the script tag (relative to html)
    soup.body.append(BeautifulSoup('<script src="./js/script.js"></script>','html.parser'))
    with open(selectedFile, "wb") as writeFile:
      writeFile.write(soup.prettify("utf-8"))
