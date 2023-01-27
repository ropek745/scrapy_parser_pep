from pathlib import Path

BOT_NAME = 'pep_parse'
PEP_DOMAIN = 'peps.python.org'
PEP_URL = f'https://{PEP_DOMAIN}/'
SPIDER_NAME = 'pep'

RESULTS_DIR = 'results'
BASE_DIR = Path(__file__).parent.parent

SPIDER_MODULES = [f'{BOT_NAME}.spiders']
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}
