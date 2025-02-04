import boto3
import json

def upload_to_s3(file_path, bucket_name, object_name):
    """
    Uploads a file to an S3 bucket.
    
    :param file_path: Path to the file to upload
    :param bucket_name: Name of the S3 bucket
    :param object_name: S3 object name (if different from file_path)
    :return: True if file was uploaded, else False
    """
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        return True
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False

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
    IMAGE_PATH = "path/to/your/image.jpg"
    IMAGE_KEY = "your-image.jpg"
    
    if upload_to_s3(IMAGE_PATH, S3_BUCKET, IMAGE_KEY):
        results = classify_image(S3_BUCKET, IMAGE_KEY)
        print(json.dumps(results, indent=4))
