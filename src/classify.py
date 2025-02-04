import boto3
import json

def classify_image(s3_bucket, image_key):
    """
    Uses AWS Rekognition to classify objects in an image stored in S3.
    
    :param s3_bucket: Name of the S3 bucket
    :param image_key: Image file path in S3
    :return: List of detected labels with confidence scores
    """
    client = boto3.client('rekognition')
    
    response = client.detect_labels(
        Image={'S3Object': {'Bucket': s3_bucket, 'Name': image_key}},
        MaxLabels=10,
        MinConfidence=75
    )
    
    labels = response['Labels']
    return [{"Label": label['Name'], "Confidence": label['Confidence']} for label in labels]

if __name__ == "__main__":
    S3_BUCKET = "your-s3-bucket-name"
    IMAGE_KEY = "path/to/your/image.jpg"
    
    results = classify_image(S3_BUCKET, IMAGE_KEY)
    print(json.dumps(results, indent=4))
