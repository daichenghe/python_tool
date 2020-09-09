import os

class AuthSamples(object):
    url = "https://{}.blob.core.windows.net".format(
        os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    )
    oauth_url = "https://{}.blob.core.windows.net".format(
        os.getenv("OAUTH_STORAGE_ACCOUNT_NAME")
    )

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    shared_access_key = os.getenv("AZURE_STORAGE_ACCESS_KEY")
    active_directory_application_id = os.getenv("ACTIVE_DIRECTORY_APPLICATION_ID")
    active_directory_application_secret = os.getenv("ACTIVE_DIRECTORY_APPLICATION_SECRET")
    active_directory_tenant_id = os.getenv("ACTIVE_DIRECTORY_TENANT_ID")

    def auth_connection_string(self):
        # [START auth_from_connection_string]
        from azure.storage.blob import BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        # [END auth_from_connection_string]

        # [START auth_from_connection_string_container]
        from azure.storage.blob import ContainerClient
        container_client = ContainerClient.from_connection_string(
            self.connection_string, container_name="mycontainer")
        # [END auth_from_connection_string_container]

        # [START auth_from_connection_string_blob]
        from azure.storage.blob import BlobClient
        blob_client = BlobClient.from_connection_string(
            self.connection_string, container_name="mycontainer", blob_name="blobname.txt")
        # [END auth_from_connection_string_blob]

        # Get account information for the Blob Service
        account_info = blob_service_client.get_account_information()

    def auth_shared_key(self):
        # [START create_blob_service_client]
        from azure.storage.blob import BlobServiceClient
        blob_service_client = BlobServiceClient(account_url=self.url, credential=self.shared_access_key)
        # [END create_blob_service_client]

        # Get account information for the Blob Service
        account_info = blob_service_client.get_account_information()

    def auth_blob_url(self):
        # [START create_blob_client]
        from azure.storage.blob import BlobClient
        blob_client = BlobClient.from_blob_url(blob_url="https://account.blob.core.windows.net/container/blob-name")
        # [END create_blob_client]

        # [START create_blob_client_sas_url]
        from azure.storage.blob import BlobClient

        sas_url = "https://account.blob.core.windows.net/container/blob-name?sv=2015-04-05&st=2015-04-29T22%3A18%3A26Z&se=2015-04-30T02%3A23%3A26Z&sr=b&sp=rw&sip=168.1.5.60-168.1.5.70&spr=https&sig=Z%2FRHIX5Xcg0Mq2rqI3OlWTjEg2tYkboXr1P9ZUXDtkk%3D"
        blob_client = BlobClient.from_blob_url(sas_url)
        # [END create_blob_client_sas_url]
