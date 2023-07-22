import base64
import openai
from dotenv import load_dotenv
import boto3
import json
from botocore.exceptions import BotoCoreError, ClientError

def lambda_handler(event, context):
    load_dotenv()

    # openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = get_key_from_secret_mng()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "OpenAI APIについて20字以内で教えて下さい"}],
    )

    print(response.choices[0].message['content'])

    return {
        'statusCode': 200,
        'body': response.choices[0].message['content']
    }

def get_key_from_secret_mng():
    secret_name = "OPENAI_API_KEY"

    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name="ap-northeast-1"
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise Exception("Couldn't retrieve the secret") from e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            secret = base64.b64decode(get_secret_value_response['SecretBinary'])
        
        # シークレットはJSON文字列として保存されているため、辞書に変換します
        secret_dict = json.loads(secret)
        return secret_dict[secret_name]