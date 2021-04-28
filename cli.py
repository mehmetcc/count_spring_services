import argparse

from globals import *
from read_dirs import DirectoryCrawler

# Initial declr.
parser = argparse.ArgumentParser(description=ENTRY_TEXT)

# Arguments
parser.add_argument("--path", "-p", help="Set the search path")
parser.add_argument("--keyword", "-k", help="Set the keyword")
parser.add_argument("--extension", "-e", help="Set the extension")

# RUN FFS
args = parser.parse_args()

# i am already bored with this but anyways
path  = args.path if args.path is not None else PATH_FLAG
keyword = args.keyword if args.keyword is not None else KEYWORD_FLAG
extension = args.extension if args.extension is not None else EXTENSION_FLAG

crawler = DirectoryCrawler(path, keyword, extension)
print("Number of references to keyword {} is {}".format(keyword, crawler.crawl()))




