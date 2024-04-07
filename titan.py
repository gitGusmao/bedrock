import boto3
import json
brt = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

body = json.dumps({
    "inputText": "Me explique o que é o Angular ?",
    "textGenerationConfig": {
        "maxTokenCount": 100,
        "stopSequences": [],
        "temperature": 0.5,
        "topP": 0.9,
    }
})

modelId = 'amazon.titan-text-express-v1'
accept = 'application/json'
contentType = 'application/json'

response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())

# text
print(response_body.get('results')[0].get('outputText'))