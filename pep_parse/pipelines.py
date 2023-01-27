import csv
from collections import defaultdict
import datetime as dt

from pep_parse.items import PepParseItem
from pep_parse.settings import BASE_DIR, RESULTS_DIR

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = f'status_summary_{dt.datetime.now().strftime(DATETIME_FORMAT)}.csv'

HEAD_OF_TABLE = ['status', 'count']
TOTAL_ROW = 'Total'


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.summary_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.summary_statuses[PepParseItem(item)['status']] += 1
        return item

    def close_spider(self, spider):
        with open(self.results_dir / FILE_NAME, 'w') as csv_file:
            writer = csv.writer(csv_file, csv.unix_dialect)
            writer.writerow(HEAD_OF_TABLE)
            for status, count in self.summary_statuses.items():
                writer.writerow([status, count])
            writer.writerow([TOTAL_ROW, sum(self.summary_statuses.values())])
