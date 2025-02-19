aws s3 ls --no-sign-request s3://noaa-wod-pds/ --recursive --human-readable --summarize
rclone sync --progress --s3-public-url s3://noaa-wod-pds aws:iode-wod-backup
