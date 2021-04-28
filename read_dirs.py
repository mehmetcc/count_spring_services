import os


class DirectoryCrawler:
    def __init__(self, path, keyword, extension):
        self.path = path
        self.keyword = keyword
        self.extension = extension
        self.count = 0
        self.processed = False

    def _walk_file(self):
        for r, d, f in os.walk(self.path):
            for file in f:
                if (file.endswith(self.extension)):
                    file_contents = open(os.path.join(r, file)).read()
                    if self.keyword in file_contents:
                        self.count = self.count + 1
                        self.processed = True

    def _crawl(self):
        self._walk_file()
        return self.count

    def crawl(self):
        if self.processed:
            return self.count
        else:
            return self._crawl()
