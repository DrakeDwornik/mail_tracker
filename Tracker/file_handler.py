import pandas as pd
import logging


def handle_uploaded_file(file, mailing_id):
    mailing_list = pd.read_csv(file)
    logging.error(mailing_list.head())
