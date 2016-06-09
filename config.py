import os

basedir = os.path.abspath(os.path.dirname(__file__))

# sqlalchemy configurations
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# form configurations
WTF_CSRF_ENABLED = True
SECRET_KEY = 'uKVD2>P2/Alz}B{1FTv|t6G2zjFI}P'

# openid configurations
OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
