#!/usr/bin/env python
import csv
from sys import argv


class GoogleTrendAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.table = []
        self.headers = []

        with open(filename, "r") as f:
            self.title = f.readline().strip()
            reader = csv.reader(f)
            f.readline()
            self.headers = reader.__next__()
            for row in reader:
                self.table.append(row)

    def most_popular(self):
        """

        :return:
        :rtype:
        """
        max_col_num = -1
        max_value = float("-inf")
        for row in self.table:
            for col, data in enumerate(row):
            #for col in range(len(row)):
                #data = row[col]
                if col > 0:
                    data_float = float(data)
                    if data_float > max_value:
                        max_value = data_float
                        max_col_num = col
        return self.headers[max_col_num]

    def time_most_popular(self, col_number):
        """
        Returns the date that the search term in column col_number was most
        popular
        :param col_number: a column number in the db, between 1 and number of
        terms, inclusive
        :type col_number:
        :return:
        :rtype:
        """
        pass


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage is stats.py [filename]")
    print(argv)
    analyzer = GoogleTrendAnalyzer(argv[1])
    print(analyzer.most_popular())
