-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "user" (
    "id"  SERIAL  NOT NULL,
    "email" VARVHAR(150)   NOT NULL,
    "group_id" bigint   NOT NULL,
    "name" VARCHAR(50)   NOT NULL,
    CONSTRAINT "pk_user" PRIMARY KEY (
        "id"
     ),
    CONSTRAINT "uc_user_email" UNIQUE (
        "email"
    ),
    CONSTRAINT "uc_user_group_id" UNIQUE (
        "group_id"
    )
);

CREATE TABLE "group" (
    "id"  SERIAL  NOT NULL,
    "name" VARCHAR(50)   NOT NULL,
    CONSTRAINT "pk_group" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "mail_piece" (
    "id"  SERIAL  NOT NULL,
    "user_id" bigint   NOT NULL,
    "mailing_id" BIGINT   NOT NULL,
    "pieceId" UUID   NULL,
    "edocMailingGroupId" VARCHAR(50)   NULL,
    "idTag" VARCHAR(50)   NULL,
    "imb" VARCHAR(31)   NOT NULL,
    "mailClassDescription" VARCHAR(50)   NULL,
    "imbMid" VARCHAR(9)   NOT NULL,
    "imbRoutingCode" VARCHAR(11)   NULL,
    "imbTrackingCode" VARCHAR(20)   NOT NULL,
    "expectedDeliveryDate" date   NULL,
    "startTheClockDate" date   NULL,
    "imbSerialNumber" VARCHAR(11)   NULL,
    "imbStid" VARCHAR(3)   NOT NULL,
    "anticipatedDeliveryDate" date   NULL,
    "predictedDeliveryDate" date   NULL,
    "edocSubmitterCrid" VARCHAR(15)   NULL,
    "routingCodeImbMatchingPortion" VARCHAR(11)   NULL,
    "edocJobId" VARCHAR(50)   NULL,
    "recipient" VARCHAR(50)   NULL,
    "title" (VARCHAR(50)   NULL,
    "company" VARCHAR(50)   NULL,
    "address1" VARCHAR(150)   NULL,
    "address2" VARCHAR(150)   NULL,
    "address3" VARCHAR(150)   NULL,
    "city" VARCHAR(150)   NOT NULL,
    "state" VARCHAR(2)   NOT NULL,
    "zip" VARCHAR(9)   NOT NULL,
    CONSTRAINT "pk_mail_piece" PRIMARY KEY (
        "id"
     ),
    CONSTRAINT "uc_mail_piece_pieceId" UNIQUE (
        "pieceId"
    )
);

CREATE TABLE "scan" (
    "id"  SERIAL  NOT NULL,
    "piece_id" bigint   NOT NULL,
    "scanLocaleKey" VARCHAR(10)   NULL,
    "machineName" VARCHAR(10)   NULL,
    "scanFacilityCity" VARCHAR(100)   NULL,
    "scanFacilityState" VARCHAR(2)   NULL,
    "scannerType" VARCHAR(50)   NULL,
    "scanEventCode" int   NULL,
    "scanDatetime" dateTime   NOT NULL,
    "handlingEventTypeDescription" VARCHAR(25)   NULL,
    "scanFacilityZip" VARCHAR(9)   NULL,
    "machineId" VARCHAR(10)   NULL,
    "handlingEventType" VARCHAR(10)   NULL,
    "scanFacilityName" VARCHAR(50)   NULL,
    CONSTRAINT "pk_scan" PRIMARY KEY (
        "id"
     ),
    CONSTRAINT "uc_scan_piece_id" UNIQUE (
        "piece_id"
    )
);

CREATE TABLE "data_message" (
    "id"  SERIAL  NOT NULL,
    "scan_id" bigint   NULL,
    "import_time" dateTime  DEFAULT getutcdate() NULL,
    "msgGrpId" VARCHAR(50)   NULL,
    "msgSerNbr" int   NULL,
    "totMsgCnt" int   NULL,
    "recCnt" int   NULL,
    "totRecCnt" int   NULL,
    CONSTRAINT "pk_data_message" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "mailing" (
    "id" BIGINT   NOT NULL,
    "customer" VARCHAR(100)   NULL,
    "mailing_name" VARVHAR(50)   NULL,
    "mailing_dropoff_date" date   NULL,
    "mailing_type_description" VARCHAR(50)   NULL,
    CONSTRAINT "pk_mailing" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "user" ADD CONSTRAINT "fk_user_group_id" FOREIGN KEY("group_id")
REFERENCES "group" ("id");

ALTER TABLE "mail_piece" ADD CONSTRAINT "fk_mail_piece_id" FOREIGN KEY("id")
REFERENCES "scan" ("piece_id");

ALTER TABLE "mail_piece" ADD CONSTRAINT "fk_mail_piece_user_id" FOREIGN KEY("user_id")
REFERENCES "user" ("id");

ALTER TABLE "mail_piece" ADD CONSTRAINT "fk_mail_piece_mailing_id" FOREIGN KEY("mailing_id")
REFERENCES "mailing" ("id");

ALTER TABLE "scan" ADD CONSTRAINT "fk_scan_id" FOREIGN KEY("id")
REFERENCES "data_message" ("scan_id");

