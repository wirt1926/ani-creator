import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('203828-ada2')
my_file = open('/home/ec2-user/Files/test4.txt', 'w+')
my_file.write('Here will be my test content, isint it cool?')
my_file.close()

bucket.put_object(
  Key='MyTxtFiles/test4.txt',
  Body=open('/home/ec2-user/Files/test4.txt', 'rb')
)
