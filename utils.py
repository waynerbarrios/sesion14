from werkzeug.security import generate_password_hash, check_password_hash

def hash_pwd(in_passwd):
    passwd_hashed= generate_password_hash(in_passwd)
    return passwd_hashed

if __name__=='__main__':
    in_passwd='admin2021'
    out_passwd= hash_pwd(in_passwd)
    print(out_passwd)