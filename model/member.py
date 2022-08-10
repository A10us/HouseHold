# MEMBER er som minimum 1 administrator som kan administrere systemet
# is_admin - bool
class Member(object):
    def __init__(self, name, userid, password, is_admin):
        self.name = name
        self.userid = userid
        self.password = password
        self.is_admin = is_admin