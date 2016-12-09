import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/schema_name?charset=utf8&use_unicode=0'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_ECHO = False

# CSRF TOKEN KEY
SECRET_KEY = 'tempFlaskProject'

