#!/usr/bin/env python3
#############################################################################################################
# Project Name:         S3_Manager
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
from http import client
import os
from queue import Empty
import re
from cryptography.fernet import Fernet
from botocore.exceptions import ClientError
import boto3
import boto3.session
import logging
from exceptions import *


# setup the save directory
basePath = r"".join(os.getcwd())  # get the current directory
dataPath = r"".join(os.path.join(basePath, 'data'))
parentPath = r"".join(os.path.dirname(basePath))


#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        08/10/2022
#  *
#  * Description:
#  * 
#############################################################################################################
def main():

    # Try to open a key file. If there is no key file then generate one
    key, access_key, secret_key = open_key("filekey.key")

    fernet = Fernet(key)

    # Open the pdf and read it
    with open('test.pdf', 'rb') as file:
        original = file.read()
        # encrypt the file
        encrypted = fernet.encrypt(original)

    # write the encrypted file to pdf
    with open('test_encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print(access_key)

    upload_file('test_encrypted', 'test-123908471235', access_key, secret_key, 'test_encrypted')


    print("done")

#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        08/12/2022
#  *
#  * Description:
#  * Controls the flow of data process the home page and grabs all of the links related to birds. Then calls
#  * the crawl functions that pull data from the birds page and collects more links to traverse
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
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        08/12/2022
#  *
#  * Description:
#  * Controls the flow of data process the home page and grabs all of the links related to birds. Then calls
#  * the crawl functions that pull data from the birds page and collects more links to traverse
#############################################################################################################
def decrypt_file(fernet):

    with open('test_encrypted', 'rb') as encrypted_file1:
        encrypted = encrypted_file1.read()
        decrypted = fernet.decrypt(encrypted)
        
        with open('decrypted_pdf.pdf', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)


#############################################################################################################
#  * Function:            upload_file
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        08/12/2022
#  *
#  * Description:
#  * Upload files to s3 bucket
#############################################################################################################
def upload_file(file_name, bucket, access_key, secret_key, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    client = boto3.client('s3',
                            aws_access_key_id = str(access_key),
                            aws_secret_access_key = str(secret_key),
                            region_name = 'us-east-1')

    try:
        # Fetch the list of existing buckets
        clientResponse = client.list_buckets()
    
        # Print the bucket names one by one
        print('Printing bucket names...')
        for bucket in clientResponse['Buckets']:
            print(f'Bucket Name: {bucket["Name"]}')

    except ClientError as e:
        logging.error(e)
        return False
    return True


#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        04/01/2022
#  *
#  * Description:
#  * Controls the flow of data process the home page and grabs all of the links related to birds. Then calls
#  * the crawl functions that pull data from the birds page and collects more links to traverse
#############################################################################################################
if __name__ == '__main__':
    main()
