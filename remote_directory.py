from ftplib import FTP

def main():

  address = input("Enter in the ftp server address: ")

  path = input("Enter in the path of the directory inside the FTP server: ")

  server = FTP(address)

  server.login()

  ftp.cwd(path)
