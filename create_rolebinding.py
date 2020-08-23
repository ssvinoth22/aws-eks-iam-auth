from __future__ import print_function
from kubernetes import client, config
import time
import json
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
# configuration = kubernetes.client.Configuration()
# configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'
config.load_kube_config()
# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1Api(kubernetes.client.ApiClient())
# namespace = 'spark' # str | object name and auth scope, such as for teams and projects
# body = kubernetes.client.V1RoleBinding() # V1RoleBinding | 
# pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
# dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
# field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

role_binding = kubernetes.client.V1RoleBinding(
        metadata=kubernetes.client.V1ObjectMeta(namespace="spark",
                                                name="spark-developer-role-binding"),
        subjects=[kubernetes.client.V1Subject(name="fazle", kind="User", api_group="rbac.authorization.k8s.io")],
        role_ref=kubernetes.client.V1RoleRef(kind="Role", api_group="rbac.authorization.k8s.io",
                                             name="developer"))
patch_role_binding = kubernetes.client.V1RoleBinding(
        # metadata=kubernetes.client.V1ObjectMeta(namespace="spark",
        #                                         name="spark-developer-role-binding"),
        subjects=[kubernetes.client.V1Subject(name="vinoth", kind="User", api_group="rbac.authorization.k8s.io")],
        role_ref=kubernetes.client.V1RoleRef(kind="Role", api_group="rbac.authorization.k8s.io",
                                             name="developer"))
#rbac = kubernetes.client.RbacAuthorizationV1Api()
#rbac.create_namespaced_role_binding(namespace="spark",
#                                       body=role_binding)

try:
    dev_response = api_instance.list_namespaced_role_binding("spark", field_selector="metadata.name=spark-developer-role-binding")
    #pprint(dev_response.items)
    if dev_response.items:
        print(dev_response.items[0].metadata.name)
        api_response = api_instance.patch_namespaced_role_binding(name="spark-developer-role-binding", namespace="spark", body=patch_role_binding)
        pprint(api_response)
    else:
        print("Role binding doesnot exist")
        api_response = api_instance.create_namespaced_role_binding(namespace="spark",
                                            body=role_binding)
        pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1Api->create_namespaced_role_binding: %s\n" % e)