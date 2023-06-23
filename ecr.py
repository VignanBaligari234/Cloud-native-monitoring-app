import boto3

ecr_client = boto3.client('ecr')

repository_name = "my-cloud-native-flask-app-repo"

response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
uri = repository_uri
print(uri)
