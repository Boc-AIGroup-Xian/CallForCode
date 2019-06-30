# -*- coding: UTF-8 -*-
# from __future__ import print_function
from ibmdbpy import IdaDataBase, IdaDataFrame

import ibm_db
import ibm_db_dbi
import json
import random

recordFile = './record.json'


def verifyRecord(r):
    # verify procedure is omitted, this function is only a sample;
    random.randint(0, 100)
    if random.randint(0, 100) % 2 == 0:
        return True
    else:
        return False


def transfer(conn, src, dst, amount):
    cur = conn.cursor()

    sql = 'update LWK40497.USER_ACCOUNT set "balance" = "balance" - ' \
          + str(amount) + ' where "customer_id" = ' + str(src)
    # print sql
    cur.execute(sql)

    sql = 'update LWK40497.USER_ACCOUNT set "balance" = "balance" + ' \
          + str(amount) + ' where "customer_id" = ' + str(dst)
    # print sql
    cur.execute(sql)


if __name__ == '__main__':
    print '--------------------STAGE 1--------------------'
    print 'Collect Trade Records from Device ...'
    print 'Reading Data From File: ' + recordFile

    conn_str = 'database=BLUDB;hostname=dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net;Port=50000;PROTOCOL=TCPIP;UID=lwk40497;PWD=w2hb^26z7lvmtz6j'
    ibm_db_conn = ibm_db.connect(conn_str, '', '')
    conn = ibm_db_dbi.Connection(ibm_db_conn)

    with open(recordFile, 'r') as f:
        records = json.load(f)
        count = records.__len__()
        print str(count) + ' Records Read Completed !!!'
        for r in records:
            print 'From:', r['customer_src'], ' To:', r['customer_dst'], ' Amount:', r['amount']

            sql = "insert into LWK40497.RECORDS values('%s','%s','%s','%s','%s','%s',%d,'%s', 0);" \
                  % (r['record_id'], r['transaction_id'], r['customer_src'], r['customer_dst'], r['device_src'],
                     r['device_dst'], r['amount'], r['trade_time'])

            cur = conn.cursor()
            if cur.execute(sql):
                print 'Record Collected...'
            else:
                print 'Record Collecting Failed...'

    print '--------------------STAGE 2--------------------'
    print 'Verifying All the Records...'

    sql = 'select * from LWK40497.RECORDS where "verified" = 0'

    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchall()

    print row.__len__(), 'Unverified Records in Database Were Found!!!'

    for r in row:
        if verifyRecord(r):
            # print r[2],r[3],r[6]
            transfer(conn, r[2], r[3], r[6])
            cur = conn.cursor()
            sql = 'update LWK40497.RECORDS set "verified" = 1 where "record_id" = \'' + r[0] + '\''
            # print sql
            cur.execute(sql)
            print 'Record ' + r[0] + ' has been verified! User Account has been refreshed!'
        else:
            print 'Record ' + r[0] + ' is rejected!'

    conn.close()

# (RECORD_ID,TRANSACTION_ID,CUSTOMER_SRC,CUSTOMER_DST,DEVICE_SRC,DEVICE_DST,AMOUNT,TRADE_TIME,VERIFIED)
