import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')
BUCKET = 'ak-celebrate'


def time_mask():
    import datetime
    # don't 0 pad
    dt = datetime.datetime.utcnow().strftime('%Y-%-m-%-d-%-H')
    minute_mask = int(datetime.datetime.utcnow().strftime('%M')) // 5
    return f'{dt}_{str(minute_mask)}'

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    response = event.get('body')
    if not response:
        print('no body found')
    
    parsed = json.loads(response)
    review_is_positive = parsed['rating'] == 'great'
    
    # is it a positive review? proceed
    if not review_is_positive:
        print(f"this review wasn\'t positive: {parsed['rating']}")
        return
    
    cur_time_mask = time_mask()
    obj_name =  f'{cur_time_mask}.html'
    print(f'creating {obj_name} in bucket {BUCKET}')

    try:
        s3.put_object(Bucket=BUCKET,
                      Body=b'',
                      Key=obj_name,
                      ContentType='text/html')
    except Exception as e:
        print(e)
        print(f'Error putting object {obj_name} in bucket {BUCKET}.')
        raise e
