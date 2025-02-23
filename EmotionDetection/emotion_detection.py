''' This file contains a function that calls the Emotion Predict function of the Watson NLP Library to analyze text 
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

    if response.status_code == 400:
        emotions = {'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion':None}
    else:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        #Extract the required dictionary of emotions
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        #find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        #add the dominant emotion to the emotions dictionary
        emotions['dominant_emotion'] = dominant_emotion

    return emotions
