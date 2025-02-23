''' This file contains a that function calls the Emotion Predict function of the Watson NLP Library to analyze text 
    for detecting emotions.
'''
# Import libraries
import requests
import json

def emotion_detector(text_to_analyze):
    ''' This function calls the Emotion Predict function of the Watson NLP Library to analyze text 
        for detecting emotions.
    '''
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    #formatted_response = json.loads(response.text)
    return response.text

