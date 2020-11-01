# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "Landon": "UTC+1:00",
    "German": "UTC+3:00",
    "Mumbai": "UTC+5:30",
}

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_timezone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        timezone = timezone.get(city)

        if timezone is None:
            output = "could not find the timezone of {}".format(city)
        else :
            output = "timezone of {} is {}".format(city,timezone)

        dispatcher.utter_message(text=output)

        return []
