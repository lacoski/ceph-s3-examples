# ceph-s3-examples

## Bucket 

```
## Create Bucket
python ceph-create-bucket.py --bucket-name thanhdemo

## List Bucket
python ceph-list-buckets.py

## Delete Bucket
python ceph-delete-bucket.py --bucket-name thanhdemo
```

## Object
```
## List Object
python ceph-list-objects.py --bucket-name thanhdemo

## Create Bucket
python ceph-download-file.py --bucket-name thanhdemo --key-name documents.txt --file-name documents.txt

## Upload file
python ceph-upload-file.py --bucket-name thanhdemo --key-name requirements.txt --file-name requirements.txt

## Download Object
python ceph-download-file.py --bucket-name thanhdemo --key-name documents.txt --file-name downloads/documents.txt
python ceph-download-file.py --bucket-name thanhdemo --key-name requirements.txt --file-name downloads/requirements.txt
python ceph-download-file-2.py --bucket-name thanhdemo --key-name requirements.txt --file-name downloads/requirements-2.txt

## Delete
python ceph-delete-object.py --bucket-name thanhdemo --key-name documents.txt
python ceph-delete-object.py --bucket-name thanhdemo --key-name documents.txt
```
