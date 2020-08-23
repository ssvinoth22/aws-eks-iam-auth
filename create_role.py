from kubernetes import client, config
from kubernetes.client.rest import ApiException
from pprint import pprint

config.load_kube_config()

metadata = client.V1ObjectMeta(name='developer', namespace='spark')
rule = client.V1PolicyRule(api_groups=['*'], resources=['*'], verbs=['get'])
rules = []
rules.append(rule)
body = client.V1Role(metadata=metadata, rules=rules)


api_instance = client.RbacAuthorizationV1Api()

try:
    api_response = api_instance.create_namespaced_role('spark', body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1Api->create_namespaced_role: %s\n" % e)