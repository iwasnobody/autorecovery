import boto3

client = boto3.client('cloudwatch',region_name = 'us-east-1')


response = client.put_metric_alarm(
    AlarmName='ec2-autorecover',
    AlarmDescription='ec2-autorecover',
    ActionsEnabled=True,
    AlarmActions=[
        'arn:aws:automate:us-east-1:ec2:recover',
    ],
    MetricName='StatusCheckFailed_System',
    Namespace='AWS/EC2',
    Statistic='Minimum',
    #ExtendedStatistic='string',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'i-03fb97f61687d0588'
        },
    ],
    Period=60,
    #Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
    EvaluationPeriods=3,
    #DatapointsToAlarm=123,
    Threshold=1,
    ComparisonOperator='GreaterThanOrEqualToThreshold'
    #TreatMissingData='string',
    #EvaluateLowSampleCountPercentile='string'
)

print response
