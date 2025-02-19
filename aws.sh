#!/bin/bash

# aws s3 ls --no-sign-request s3://noaa-wod-pds/ --recursive --human-readable --summarize
aws s3api put-bucket-lifecycle-configuration --bucket iode-wod-backup --lifecycle-configuration file://lifecycle.json
rclone sync --ignore-deletes --progress --min-size 1b noaa:noaa-wod-pds s3:iode-wod-backup
