import pandas as pd
import logging
import json
from .models import Mailpiece, Mailing, Scan
import zipfile


#
def handle_uploaded_list(file=False, mailing_pk=False):
    if file:
        mailing = Mailing.objects.get(id=mailing_pk)
        mailing_list = pd.read_csv(file)
        mailing_list = mailing_list.fillna('')
        required_headers = ['fullname', 'title', 'company']
        for required_header in required_headers:
            if required_header not in mailing_list:
                mailing_list[required_header] = " "
        pieces = mailing_list.to_dict('records')

        mailpiece_instances = [Mailpiece(mailing_id=mailing, recipient=piece['fullname'], title=piece['title'],
                                         company=piece['company'], address1=piece['FNL_PRIADR'],
                                         address2=piece['FNL_SECADR'], address_extra=piece['FNL_EXTADR'],
                                         city=piece['FNL_CITY'], state=piece['FNL_STATE'], zip=piece['FNL_ZIP9'],
                                         record_number=piece['RecordId'], oel=piece['PST_OPT_EN'],
                                         imb=piece['PST_IMB'], sort_order=piece['PST_PC_NO'],
                                         bundle_number=piece['PST_PKG_NO'], container_number=piece['PST_CTN_NO'],
                                         manifest_key=piece['manfst_key']) for piece in pieces]
        Mailpiece.objects.bulk_create(mailpiece_instances)

        # sort_order = models.IntegerField(null=True)
        # bundle_number = models.IntegerField(null=True)
        # container_number = models.IntegerField(null=True)
        # manifest_key = models.CharField(max_length=25)

    # mailing_list = mailing_list['recipient', 'title', 'company',
    #                             'address1', 'address2', 'address_extra', 'city', 'state', 'zip',
    #                             'record_number', 'oel', 'imb_numeric', 'imb_alpha', 'sort_order',
    #                             'bundle_number', 'container_number', 'manifest_key']
    # logging.error(x)


def handle_uploaded_scans(file):
    pass
    scans = json.load(file)
    scans_df = pd.DataFrame(scans['events'])
    scan_imbs = scans_df['imb'].unique().tolist()
    for imb in scan_imbs:
        try:
            imb_df = scans_df.loc[scans_df['imb'] == imb]
            scans_imb_dicts = imb_df.to_dict('records')
            # for col in imb_df.columns:
            #     logging.error(col)
            # logging.error(imb_df.head(1))
            piece_cols = [
                'pieceId', 'edocMailingGroupId', 'idTag', 'mailClassDescription', 'imbMid', 'imbRoutingCode',
                'imbTrackingCode', 'expectedDeliveryDate', 'startTheClockDate', 'imbSerialNumber', 'imbStid',
                'anticipatedDeliveryDate', 'predictedDeliveryDate', 'routingCodeImbMatchingPortion', 'edocSubmitterCrid',
                'edocJobId']
            # imb_df.loc[:, piece_cols] = imb_df.loc[:, piece_cols].ffill().bfill()
            piece_df = imb_df[piece_cols].ffill().bfill()
            # logging.error(piece_df.head(1))
            piece_dict = piece_df.head(1).to_dict('records')[0]
            Mailpiece.objects.filter(imb=imb).update(**piece_dict)
            piece = Mailpiece.objects.get(imb=imb)
            scan_instances = [
                Scan(piece_id=piece, scanLocaleKey=scan['scanLocaleKey'], machineName=scan['machineName'],
                     scanFacilityCity=scan['scanFacilityCity'], scanFacilityState=scan['scanFacilityState'],
                     scannerType=scan['scannerType'],
                     scanDatetime=scan['scanDatetime'],
                     handlingEventTypeDescription=scan['handlingEventTypeDescription'],
                     scanFacilityZip=scan['scanFacilityZip'], machineId=scan['machineId'],
                     handlingEventType=scan['handlingEventType'], scanFacilityName=scan['scanFacilityName'])
                for scan in scans_imb_dicts]
            Scan.objects.bulk_create(scan_instances)

        except:
            pass
            # logging.error(f"mailpiece with imb: {imb} does not exist")
    # logging.error("\n"+str(scans_df.head(3)))
    # Mailing.objects.get_or_create(customer="123123", mailing_name="name", mailing_dropoff_date="2021-01-01", mailing_type_description="it's stuff y'all", job_number="0012345")
    # mailing = Mailing.objects.get(id=23)
    # Mailpiece.objects.get_or_create(mailing_id=mailing, imb_numeric="123123")

# def read_headers(file):
#     scans_df = pd.read_csv(file).head(1)
#     logging.error(scans_df.columns)
