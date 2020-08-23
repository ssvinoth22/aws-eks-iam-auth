import boto3
import re
#iam = boto3.client('iam')
# test
access_key = 'test'
secret_key = 'test'
mydict={}
group=[]
iam=boto3.resource('iam',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)
group_list=iam.groups.all()

for k in group_list:
    group_name=(str(k).split("='")[1]).split("'")[0]
    group.append(group_name)
my_list=list(filter(lambda x: 'eks' in x, group))
print(my_list)
for k in my_list:
    users=[]
    group_users=iam.Group(k).users.all()
    for l in group_users:
        user=(str(l).split("='")[1]).split("'")[0]
        users.append(user)
    mydict[k]=users
print(mydict)