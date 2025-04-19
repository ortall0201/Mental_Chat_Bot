from crewai import tools
from textblob import TextBlob
from crewai import Agent

#Defining the tool for detection emotions
#Function to detect emotions using 
def detect_mood(text:str)->dict:
    """
    Detects the mood of the user based on the text input.
    """
    
    #create textblonb object
    analysis=TextBlob(text)
    #get the sentiment of the text
    sentiment=analysis.sentiment
    #get the polarity of the text           
    polarity=sentiment.polarity

    if polarity>0: 
        mood="happy"
    elif polarity<0:
        mood="sad"          
    else:                   
        mood="neutral"
    #return the mood    
    return {"mood": mood, "polarity": polarity}


#Defining the tool for providing suggestions   
mood_tool=Tool(
    name="mood_detector",
    description="Detects the mood of the user based on the text input:",
    function=detect_mood
)             