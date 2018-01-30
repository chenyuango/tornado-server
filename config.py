PORT = 9000
PROCESSES = 4

SYS_LOG_LEVEL = "INFO"
SYS_LOG_PATH = '/tmp/sys.log'
DATA_LOG_LEVEL = "INFO"
DATA_LOG_PATH = '/tmp/data.log'

MONGODB_URL = 'mongodb://10.0.1.11:27017,10.0.1.12:27017,10.0.1.27:27017/?replicaSet=gt_server_replSet'

REDIS_URL = 'redis://192.168.3.169:6379'
