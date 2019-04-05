from __future__ import print_function
import oci
import sys

"""""
SAMPLE to perform STOP/START action
"""""


config = oci.config.from_file(
    '_PATH_TO_CONFIG_FILE_',
    'DEFAULT'
)

search_client = oci.resource_search.ResourceSearchClient(config)
compute = oci.core.ComputeClient(config)


def search_cloud_resources(tagkey, tagval):
    """""
    Search all resources with TAG value and KEY
    """""
    structured_search = oci.resource_search.models.StructuredSearchDetails(
        query="query instance resources where (freeformTags.key = '{}' && freeformTags.value = '{}')".format(
            tagkey, tagval),
        type='Structured',
        matching_context_type=oci.resource_search.models.SearchDetails.MATCHING_CONTEXT_TYPE_NONE)
    resources_result = search_client.search_resources(structured_search)
    return resources_result


action = str(sys.argv.pop()).upper()
print(action)

my_instances = []
find_resources = search_cloud_resources('SAS', 'GFS')
for res in find_resources.data.items:
    print(action, 'ACTION Resource ID: {}'.format(res.identifier))
    my_instances.append(res.identifier)

for instance in my_instances:
    compute.instance_action(instance, action)
