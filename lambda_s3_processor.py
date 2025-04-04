import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Enter bucket name and get the file details from the event
    bucket_name = "dehlive-sales-xxxxxxx-us-east-1"
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Ignore files outside 'inbound/' folder
    if not object_key.startswith("inbound/"):
        print("File is not in the inbound folder, ignoring...")
        return

    # Define source and destination paths
    source_path = object_key
    destination_path = object_key.replace("inbound/", "archive/")
    
    # Read the file content
    response = s3.get_object(Bucket=bucket_name, Key=source_path)
    file_content = response['Body'].read().decode('utf-8')
    
    # Apply transformation (convert text to uppercase)
    transformed_content = file_content.upper()
    
    # Upload transformed file to archive
    s3.put_object(Bucket=bucket_name, Key=destination_path, Body=transformed_content)
    
    # Delete the original file from inbound
    s3.delete_object(Bucket=bucket_name, Key=source_path)

    print(f"Processed file moved to {destination_path} and deleted from inbound")
