import boto3
import json

def lambda_handler(event, context):
    # Initialize Rekognition client in eu-west-2
    rekognition = boto3.client('rekognition', region_name='eu-west-2')

    # Extract bucket and object key from the event
    s3_info = event['Records'][0]['s3']
    bucket = s3_info['bucket']['name']
    key = s3_info['object']['key']

    # Call Rekognition to detect labels
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=10,
        MinConfidence=75
    )

    # Log results to CloudWatch
    print(f"Detected labels for {key} in bucket {bucket}:")
    for label in response['Labels']:
        print(f"{label['Name']} - Confidence: {label['Confidence']:.2f}%")

    return {
        'statusCode': 200,
        'body': json.dumps('Image analysis complete.')
    }
