import json
import boto3


def time_mask():
    import datetime
    dt = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H')
    minute_mask = int(datetime.datetime.utcnow().strftime('%M')) // 5
    return f'{dt}_{str(minute_mask)}'


if __name__ == '__main__':
    body = event['body']    
    response = event['body']
    parsed = json.loads(response)
    review_is_positive = parsed['rating'] == 'great'
    
    # is it a positive review? proceed
    if not review_is_positive:
        exit()
    
    cur_time_mask = time_mask()
    obj_name =  f'success_{cur_time_mask}'
    
    
    bucket = boto3.get_service('s3').get_bucket('ak-celebrate')



# example iam policy
{
    "Sid": "Stmt1468366974000",
    "Effect": "Allow",
    "Action": "s3:*",
    "Resource": [
        "arn:aws:s3:::ak-celebrate/*"
    ]
}

{
    'version': '2.0', 'routeKey': 'POST /ak-celebrate-fn', 'rawPath': '/default/ak-celebrate-fn', 'rawQueryString': '',
    'headers':
    {'accept': '*/*', 'accept-encoding': 'gzip, deflate', 'content-length': '0', 'host': '5iqp205sa4.execute-api.us-west-2.amazonaws.com', 'user-agent': 'HTTPie/3.0.2', 'x-amzn-trace-id': 'Root=1-6256243d-5f2f7749651854c7494b7abf', 'x-forwarded-for': '65.129.92.233', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'}, 'requestContext':
    {'accountId': '670059471275', 'apiId': '5iqp205sa4', 'domainName': '5iqp205sa4.execute-api.us-west-2.amazonaws.com', 'domainPrefix': '5iqp205sa4',
       'http': {'method': 'POST', 'path': '/default/ak-celebrate-fn', 'protocol': 'HTTP/1.1', 'sourceIp': '65.129.92.233', 'userAgent': 'HTTPie/3.0.2'},
     'requestId': 'QfqZljQBPHcESrA=', 'routeKey': 'POST /ak-celebrate-fn', 'stage': 'default', 'time': '13/Apr/2022:01:15:41 +0000', 'timeEpoch': 1649812541164},
 'isBase64Encoded': False}
