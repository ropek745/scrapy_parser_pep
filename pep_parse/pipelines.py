import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, RESULT_DIR

HEADERS_PEP_TABLE = ('Статус', 'Количество')
TIME_FORMAT = '%Y-%m-%dT%H-%M-%S'
TOTAL_STATUSES = 'Итого'
FILE_NAME = 'status_summary_{datetime}.csv'


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULT_DIR
        results_dir.mkdir(exist_ok=True)
        with open(
            results_dir / FILE_NAME.format(
                datetime=dt.now().strftime(TIME_FORMAT)
            ),
            mode='w',
            encoding='utf-8'
        ) as file:
            csv.writer(file, dialect=csv.unix_dialect).writerows([
                HEADERS_PEP_TABLE,
                *(self.status_count.items()),
                [TOTAL_STATUSES, sum(self.status_count.values())]
            ])
