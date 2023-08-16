
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    
        
        city = (tracker.latest_message)['text']
    
        api_address = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="+city)
        if (api_address.json()['cod'] == 200):
            format_add = api_address.json()['main'] 
            k = format_add['temp']
            
            k1 = k-273
            k2 = round(k1, 1)
            dispatcher.utter_message(text="temperature"'\t'+str(k2))
        else:
            dispatcher.utter_message(text="city not found")




        return []

       
