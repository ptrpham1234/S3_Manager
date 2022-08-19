#!/usr/bin/env python3
#############################################################################################################
# Project Name:         S3_Manager
# File Name:            main.py
# Author:               Peter Pham (pxp180041)
# Date Started:         08/10/2022
#
# Description:
# 
# 
# 
# TODO: implement access key and secret key read in
# TODO: implement boto3 upload
# TODO: implement 
#############################################################################################################

################# I M P O R T S #################
import os
import re
from typing import List
from cryptography.fernet import Fernet
from botocore.exceptions import ClientError
import boto3
import boto3.session
import logging
from exceptions import *
from S3 import *


# setup the main directory
S3_Manager_Dir = r"".join(os.getcwd())  # get the current directory




#############################################################################################################
# Function:            main
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# 
#############################################################################################################
def main():

    # Try to open a key file. If there is no key file then generate one
    key, access_key, secret_key = open_key("filekey.key")

    fernet = Fernet(key)

    # Open the pdf and read it
    with open(os.path.join(S3_Manager_Dir, "test.pdf"), 'rb') as file:
        original = file.read()
        # encrypt the file
        encrypted = fernet.encrypt(original)

    # write the encrypted file to pdf
    with open(os.path.join(S3_Manager_Dir, "test_encrypted"), 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print(access_key)

    s3 = S3_Bucket(access_key, secret_key)

    buckets = s3.get_buckets()

    files = s3.get_files(bucket_name=buckets[1])

    split_files = list()
    visited = list()

    for item in files:
        if "/" in item:
            splitted = item.split("/", 1)

            if splitted[0] not in visited:
                visited.append(splitted[0])
            




    print()
    print(files)

    # print()
    # print(split_files)


    print("done")

#############################################################################################################
# Function:            main
# Author:              Peter Pham (pxp180041)
# Date Started:        08/12/2022
#
# Description:
# Controls the flow of data process the home page and grabs all of the links related to birds. Then calls
# the crawl functions that pull data from the birds page and collects more links to traverse
#############################################################################################################
def open_key(file):

    # open the key file
    with open(file, 'rb') as key_file:
        key = key_file.readline().strip()
        access_key = key_file.readline().strip()
        secret_key = key_file.readline().strip()

        # if the key does not contain the access key and secret_key
        if (not access_key) and (not secret_key):
            raise IncorrectKey

        return key, access_key.decode(), secret_key.decode()



#############################################################################################################
# Function:            main
# Author:              Peter Pham (pxp180041)
# Date Started:        08/12/2022
#
# Description:
# Controls the flow of data process the home page and grabs all of the links related to birds. Then calls
# the crawl functions that pull data from the birds page and collects more links to traverse
#############################################################################################################
def decrypt_file(fernet):

    with open('test_encrypted', 'rb') as encrypted_file1:
        encrypted = encrypted_file1.read()
        decrypted = fernet.decrypt(encrypted)
        
        with open('decrypted_pdf.pdf', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

#############################################################################################################
# Function:            main
# Author:              Peter Pham (pxp180041)
# Date Started:        04/01/2022
#
# Description:
# Controls the flow of data process the home page and grabs all of the links related to birds. Then calls
# the crawl functions that pull data from the birds page and collects more links to traverse
#############################################################################################################
if __name__ == '__main__':
    main()
