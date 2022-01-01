import pandas as pd
import logging


#
def handle_uploaded_list(file, mailing_pk):
    mailing_list = pd.read_csv(file)
    logging.error(str(mailing_list.head(3)))
    # mailing_list = mailing_list['recipient', 'title', 'company',
    #                             'address1', 'address2', 'address_extra', 'city', 'state', 'zip',
    #                             'record_number', 'oel', 'imb_numeric', 'imb_alpha', 'sort_order',
    #                             'bundle_number', 'container_number', 'manifest_key']
    # logging.error(x)

def handle_uploaded_scans(file):
    logging.error(file)