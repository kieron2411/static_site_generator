import os
import shutil
import sys

from copy_static import copy_recursive
from generate_page import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    copy_recursive("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()