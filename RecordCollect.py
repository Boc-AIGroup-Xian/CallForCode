# -*- coding: UTF-8 -*-
from ibmdbpy import IdaDataBase, IdaDataFrame

import ibm_db
import ibm_db_dbi

import json

if __name__ == '__main__':
    recordFile = './record.json'
    print 'Collect Trade Records from Device ...'
    print 'Reading Data From File: ' + recordFile
    with open(recordFile,'r') as f :
        records = json.load(f)
        recordcount = records.__len__()
        print str(recordcount) + ' Records Read Completed !!!'
        for r in records:
            print 'From:', r['customer_src'], ' To:', r['customer_dst'], ' Amount:', r['amount']
            print r

    conn_str = 'database=BLUDB;hostname=dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net;Port=50000;PROTOCOL=TCPIP;UID=lwk40497;PWD=w2hb^26z7lvmtz6j'
    ibm_db_conn = ibm_db.connect(conn_str,'','')
    conn = ibm_db_dbi.Connection(ibm_db_conn)
    # print ibm_db.tables(conn,'BOC_XIAN_DATA_TYPE_EXPLAINATION')

    tables = conn.tables('LWK40497')
    print tables.__len__()

    for t in tables:
        print t

    sql = 'SELECT * FROM LWK40497.TRANSACTION WHERE "verified" = TRUE;'
    cur = conn.cursor()
    cur.execute(sql)

    row = cur.fetchall()

    for r in row:
        print r


    conn.close()
