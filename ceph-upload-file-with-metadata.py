#! /usr/bin/env python3


import os
import sys
from argparse import ArgumentParser
import json

import boto3


with open('credentials.json', 'r') as fd:
    credentials = json.loads(fd.read())


def main():

    parser = ArgumentParser(description='Creates a bucket')
    parser.add_argument('--bucket-name',
                        dest='bucket_name',
                        action='store',
                        required=True,
                        help='the name of the bucket to create')
    parser.add_argument('--key-name',
                        dest='key_name',
                        action='store',
                        required=True,
                        help='the objects key name')
    parser.add_argument('--file-name',
                        dest='file_name',
                        action='store',
                        required=True,
                        help='the file to upload')
    args = parser.parse_args()

    s3 = boto3.resource('s3',
                        endpoint_url=credentials['endpoint_url'],
                        aws_access_key_id=credentials['access_key'],
                        aws_secret_access_key=credentials['secret_key'])

    bucket = s3.Bucket(args.bucket_name)

    bucket.upload_file(
        Filename=args.file_name,
        Key=args.key_name,
        ExtraArgs={
            "Metadata": {
                "language":"Python",
                "version":"3.8",
                "type":"requirement",
                "project":"S3Demo",
            }
        }
    )


if __name__ == '__main__':
    main()
