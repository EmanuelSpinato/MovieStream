import boto3

# Crie uma sessão com suas credenciais AWS
session = boto3.Session(
    aws_access_key_id='AKIA3M7ACWECQRHFPRSZ',
    aws_secret_access_key='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',
)

# Crie um recurso S3
s3 = session.resource('s3')

# Envie o arquivo para o S3
s3.meta.client.upload_file(Filename='index.html', Bucket='bucket.emanuel', Key='index.html')