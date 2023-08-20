import boto3

ecr_client = boto3.client('ecr')
repository_name = "my_cloud_native_monitoring_app_image"

try:
    response = ecr_client.create_repository(repositoryName=repository_name)
    print(f"Repository '{repository_name}' created successfully.")
except ecr_client.exceptions.RepositoryAlreadyExistsException:
    print(f"Repository '{repository_name}' already exists.")

repository_uri = response['repository']['repositoryUri']
print(f"Repository URI: {repository_uri}")
