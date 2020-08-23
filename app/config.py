class Config(object):
    # We might want to change this secret key later. Generated with:
    #     python -c 'import os; print(os.urandom(16))'
    SECRET_KEY = b'5@r\x04Y\x7f0\x88\xc9\x97\xc6\xb1\x1e\x91Bc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
