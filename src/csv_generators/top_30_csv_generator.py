import csv
import os
from definitions import *

class Top30CSVGenerator:

    def generate_top_30_csv(self, top_30_array, csv_file_location=OUTPUT_LOC, file_name='ItJobsWatchTop30.csv', headers_array=None):
        with open(f'{csv_file_location}{file_name}', 'w+') as top30csv:
            writer = csv.writer(top30csv)
            if headers_array is not None:
                writer.writerow(headers_array)
            writer.writerows(top_30_array)


if __name__ == '__main__':
    print()
