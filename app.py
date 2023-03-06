from flask import Flask, render_template, jsonify, request
import boto3, json
from botocore.client import Config
import uuid
from dotenv import load_dotenv
import dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


  
#file_name = request.args.get('file_name')
#file_type = request.args.get('file_type')

@app.route('/get-presigned-post', methods=['POST'])
def get_presigned_post():
    if request.method == 'POST':
        prefix = 'FlaskS3Test'
        key = str(uuid.uuid4())
        S3_BUCKET = 'mmgapp'
        s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_ACCESS_SECRET'),
        )
    post = s3.generate_presigned_post(
        Bucket = S3_BUCKET,
        Key="{}/{}".format(prefix, key),
    
        ExpiresIn = 3600
        )
    return jsonify(post)

if __name__ == '__main__':
    app.run(debug=True)
