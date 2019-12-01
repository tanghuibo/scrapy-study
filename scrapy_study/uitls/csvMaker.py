import csv


class CsvMaker(object):
    def __init__(self, file_name, headers):
        self.file_name = file_name
        self.headers = headers
        with open(file_name, 'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
        pass
    pass

    def add(self, item):
        row = []
        for header in self.headers:
            row.append(item[header])
        with open(self.file_name, "a+")as f:
            f_csv = csv.writer(f)
            f_csv.writerows([row])
