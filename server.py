''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
#Import libraries
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and their 
        scores along with the dominant emotion for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] == None:
        return "Invalid text! Please try again"

    # Return a formatted string with the sentiment label and score
    return "For the given statement the system response is 'anger':{}, 'disgust':{}, \
'fear':{}, 'joy':{}, and 'sadness':{}. The dominant emotion \
is {} {} {}.".format(emotions['anger'], emotions['disgust'], emotions['fear'], emotions['joy'], \
                                         emotions['sadness'], '<b>', emotions['dominant_emotion'],'</b>')

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

#This if statement executes the flask app and deploys it on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)