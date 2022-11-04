from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

endpoint = "https://undertandspeech.cognitiveservices.azure.com/"
credential = AzureKeyCredential('a7bcdc417a9540a183fc362f2a99db3b')
client = ConversationAnalysisClient(endpoint, credential)
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations.authoring import ConversationAuthoringClient
def calculate_intent(speech):
    client = ConversationAnalysisClient(endpoint, credential)
    with client:
        query = speech
        result = client.analyze_conversation(
        task={
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "participantId": "1",
                    "id": "1",
                    "modality": "text",
                    "language": "en",
                    "text": query
                },
                "isLoggingEnabled": False
            },
            "parameters": {
                "projectName": 'basicintent',
                "deploymentName": 'calculate4',
                "verbose": True
            }
        }
    )
    return(result['result']['prediction']['intents'][0]['confidenceScore'])

print(calculate_intent("he is a cat"))