# openai-python-example
- Lambda
  - IAMロールでAPI Gatewayからしか実行できないようにする
- API Gateway
  - APIキーを発行して実行制限をかける
  - APIキーはフロントがAPI叩く時に指定する

# SAM
```
sam build
sam package --output-template-file packaged.yaml --s3-bucket gpt-caller-artifact
```

```
sam deploy --template-file packaged.yaml --region ap-northeast-1 --capabilities CAPABILITY_IAM --stack-name GPTCaller
```