"""
Purpose:
This script demonstrates a controlled brute-force technique used during
malware analysis and incident response investigations.

Context:
Developed as part of the AIG "Shields Up" threat analysis project to
illustrate how analysts may recover encrypted artifacts during forensic
analysis.

Authorized Use Only:
This script is intended strictly for educational and defensive security
purposes on systems and files you own or have explicit permission to analyze.
"""

import zipfile

# Path to the encrypted zip file and password dictionary
zip_file_path = '/mnt/data/enc.zip'
password_file_path = '/mnt/data/rockyou.txt'

def brute_force_zip(zip_file_path, password_file_path):
   try:
       # Open the zip file in read mode
       zip_file = zipfile.ZipFile(zip_file_path)
       
       # Open the password file and try each password
       with open(password_file_path, 'r', encoding='latin-1') as password_file:
           for password in password_file:
               password = password.strip()  # Remove any leading/trailing spaces/newlines
               try:
                   # Try to extract the zip file using the current password
                   zip_file.extractall(pwd=password.encode('utf-8'))
                   print(f'Success! The password is: {password}')
                   return True
               except (RuntimeError, zipfile.BadZipFile):
                   # RuntimeError is raised for incorrect passwords
                   print(f'Trying password: {password}... Failed.')
       print('Brute force failed. No valid password found.')
       return False
   except zipfile.BadZipFile:
       print("The file is not a zip file or it is corrupted.")
       return False

# Run the brute force attack
brute_force_zip(zip_file_path, password_file_path)
