from ibmdbpy import IdaDataBase, IdaDataFrame
import pypyodbc

# @hidden_cell
# This connection object is used to access your data and contains your credentials.
# You might want to remove those credentials before you share your notebook.
idadb_7b989244e3e640e0901deaf1fb0f05e3 = IdaDataBase(dsn='DASHDB;Database=BLUDB;Hostname=dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net;Port=50000;PROTOCOL=TCPIP;UID=lwk40497;PWD=w2hb^26z7lvmtz6j')

col = IdaDataFrame(idadb_7b989244e3e640e0901deaf1fb0f05e3, 'LWK40497.BOC_XIAN_DATA_TYPE_EXPLAINATION').as_dataframe()
# col = IdaDataBase()

#
# 'DASHDB;' \
# 'Database=BLUDB;' \
# 'Hostname=dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net;' \
# 'Port=50000;' \
# 'PROTOCOL=TCPIP;' \
# 'UID=lwk40497;' \
# 'PWD=w2hb^26z7lvmtz6j'
#
# credentials = {
#     'username':'DASHDB',
#     'database':'BLUDB',
#     ''
# }