# MEMBER er som minimum 1 administrator som kan administrere systemet

class Member(object):
    def __init__(self, name, userid, password, is_admin=False):
        self.name = name
        self.userid = userid
        self.password = password
        self.is_admin = is_admin
