#!/usr/bin/env python3
#############################################################################################################
# Project Name:         S3_Manager
# File Name:            S3.py
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
from queue import Empty
import boto3
import boto3.session
import logging
from exceptions import *
from botocore.exceptions import ClientError


class S3_Bucket():

    #############################################################################################################
    # Function:            __init__
    # Author:              Peter Pham (pxp180041)
    # Date Started:        08/12/2022
    #
    # Description:
    # initialize the client session
    #  
    #############################################################################################################
    def __init__(self, access_key, secret_key) -> None:

        # create a client
        self.client = boto3.client('s3',
                                aws_access_key_id = str(access_key),
                                aws_secret_access_key = str(secret_key),
                                region_name = 'us-east-1')

        self.buckets = list()

    
    #############################################################################################################
    # Function:            upload_file
    # Author:              Peter Pham (pxp180041)
    # Date Started:        08/12/2022
    #
    # Description:
    # Upload files to s3 bucket
    #############################################################################################################
    def get_buckets(self):

        buckets = list()

        # if there's bucket names
        if self.buckets:
            return self.buckets

        else:
            try:
                # Fetch the list of existing buckets
                clientResponse = self.client.list_buckets()

                # Print the bucket names one by one
                for bucket_name in clientResponse['Buckets']:
                    buckets.append(bucket_name['Name'])

                self.buckets = buckets
                return self.buckets


            except ClientError as e:
                logging.error(e)
                return False

    
    #############################################################################################################
    # Function:            upload_file
    # Author:              Peter Pham (pxp180041)
    # Date Started:        08/12/2022
    #
    # Description:
    # Upload files to s3 bucket
    #############################################################################################################
    def get_files(self, bucket_name):

        file = list()
        clientResponse = self.client.list_objects_v2(Bucket=bucket_name)

        for file_name in clientResponse['Contents']:
                    file.append(file_name['Key'])

        return file