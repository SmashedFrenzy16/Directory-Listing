from ftplib import FTP

def get_ftp_connection(host, user, password):
    ftp = FTP(host)
    ftp.login(user, password)
    return ftp

def main():
    
    host = input("Enter in the FTP server name: ")
    user = input("Enter in the FTP server username: ")
    password = input("Enter in the FTP server password: ")
    
    ftp = get_ftp_connection(host, user, password)

    direc = input("Enter in the name of a directory in the server: ")

    ftp.cwd(direc)

    ftp.retrlines('LIST')

main()

