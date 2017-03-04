import os

AZURE_CLIENT_ID=os.getenv('AZURE_CLIENT_ID')
AZURE_CLIENT_SECRET=os.getenv('AZURE_CLIENT_SECRET')
AZURE_TENANT_ID=os.getenv('AZURE_TENANT_ID')
SUBSCRIPTION_ID=os.getenv('SUBSCRIPTION_ID')

VMSS_RESOURCE_GROUP=os.getenv('VMSS_RESOURCE_GROUP')
VMSS_NAME=os.getenv('VMSS_NAME')
VMSS_MIN_CAPACITY=1
VMSS_MAX_CAPACITY=5
VMSS_LOW_THRESHOLD=3
VMSS_HIGH_THRESHOLD=10
VMSS_SCALE_UP_BY=1
VMSS_SCALE_DOWN_BY=1

SB_RESOURCE_GROUP=os.getenv('SB_RESOURCE_GROUP')
SB_NAMESPACE=os.getenv('SB_NAMESPACE')
SB_KEYNAME=os.getenv('SB_KEYNAME')
SB_KEYVAL=os.getenv('SB_KEYVAL')
SB_TOPIC_1=os.getenv('TOPIC1', default='t1')
SB_TOPIC_2=os.getenv('TOPIC2', default='t2')
SB_SUBSCRIPTION_1=os.getenv('SUB1', default='s10')
SB_SUBSCRIPTION_2=os.getenv('SUB2', default='s20')

RUN_ONCE=bool(os.getenv('RUN_ONCE'))
INTERVAL_IN_SEC=float(os.getenv('INTERVAL_IN_SEC', default=300))
