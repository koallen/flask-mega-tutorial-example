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
