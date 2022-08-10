#!/usr/bin/env python3
#############################################################################################################
# Project Name:         S3_Manager
# Author:               Peter Pham (pxp180041)
# Date Started:         08/10/2022
#
# Description:
#
#############################################################################################################

################# I M P O R T S #################
import os
import re
from cryptography.fernet import Fernet


# setup the save directory
basePath = r"".join(os.getcwd())  # get the current directory
dataPath = r"".join(os.path.join(basePath, 'data'))


#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        04/01/2022
#  *
#  * Description:
#  * 
#############################################################################################################
def print_hi(name):
    print(f'Hi, {name}')



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
    print_hi('PyCharm')
