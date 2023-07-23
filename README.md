# gpt-caller
OpenAI APIを使ってGPTをコールするAPI
# PRD
- Lambda
  - IAMロールでAPI Gatewayからしか実行できないようにする
- API Gateway
  - APIキーを発行して実行制限をかける
  - APIキーはフロントがAPI叩く時に指定する

# Deploy
## Docker(ECR)
```
docker build -t my-lambda-image .
docker tag my-lambda-image:latest <account-id>.dkr.ecr.<region>.amazonaws.com/my-lambda-repo:latest

aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/my-lambda-repo:latest
```

## Lambda
作成
```
aws lambda create-function --function-name my-function \
--package-type Image \
--code ImageUri=<account-id>.dkr.ecr.<region>.amazonaws.com/my-lambda-repo:latest \
--role arn:aws:iam::<account-id>:role/<role-name> \
--region <region>
```

更新
```
aws lambda update-function-code \
--function-name my-function \
--image-uri <account-id>.dkr.ecr.<region>.amazonaws.com/my-lambda-repo:latest \
--region <region>
--architectures arm64
```