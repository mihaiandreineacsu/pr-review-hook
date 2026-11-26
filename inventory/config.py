import os

DB_URL = os.environ.get("DB_URL", "postgres://admin:admin123@localhost/inventory")
PAGE_SIZE = 50
DEBUG = True
