from app import db
# Clases
class usuuser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    useruser = db.Column(db.String(30))
    pwduser = db.Column(db.String(30))  
    pwdhashuser = db.Column(db.String(100))

    def __init__(self, id, useruser, pwduser, pwdhashuser):
       self.id= id
       self.useruser= useruser
       self.pwduser= pwduser
       self.pwdhashuser= pwdhashuser
    
    def __init__(self, useruser, pwduser, pwdhashuser):
        self.useruser= useruser
        self.pwduser= pwduser
        self.pwdhashuser= pwdhashuser