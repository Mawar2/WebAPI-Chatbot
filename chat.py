import models, json, random, requests_oauthlib, os, app
import requests

# Twitter API setup
url = "https://api.twitter.com/1.1/search/tweets.json?q=inspirational"

oauth = requests_oauthlib.OAuth1(
        os.getenv("N8GHmjLh4c4ErNnAz0XR8iQ5h"),
        os.getenv("D670rnMTpckt5teCwMkAEuknDVnjVpD9o2uctr44FxOVA4dPy9")
    )

class Chatbot():
    def get_response(self, message):
        if message == '!! help':
            chatbot_message = 'please select: |!! about | |!! weather |!! inspire  |!! temperature.' 
            return chatbot_message
        elif message == '!! about':
            chatbot_message = "My name is Jarvis! This application was created by a famous scientist named Dr. Warren in 2026. You can contact him at mawar2@icloud.com to make sure he did it.. this bot serves as a way to enjoy funny memes while doing homework!"
            return chatbot_message
        elif message == '!! weather':
            
            api_link = 'http://api.openweathermap.org/data/2.5/weather?appid=1b33742104dab9ec6e744eb014181193&q='
            city = input("Your City Name : ")
            url = api_link + city
            json_data = requests.get(url).json()
            formatted_data = json_data['weather'][0]['description']
            temp_data = json_data['main']['temp']

            if 'cloud' in formatted_data:
                return('The forcast is Cloudy: You will be covered!\n' + str(temp_data)+ ' is the temperature right now!')
            elif 'rain' in formatted_data:
                return('Have an umbrella today. You will need it\n'+ str(temp_data) + ' is the temperature right now!')
            elif 'storm' in formatted_data:
                return('Yeah a storm is coming..\n'+ str(temp_data) + ' is the temperature right now!')
            elif 'clear' in formatted_data:
                return('Clear skies right now! \n' + str(temp_data) + ' is the temperature right now!')
            else:
                return(formatted_data + temp_data)
        elif message == '!! temperature':
            api_link = 'http://api.openweathermap.org/data/2.5/weather?appid=1b33742104dab9ec6e744eb014181193&q='
            city = input("Your City Name : ")
            url = api_link + city
            json_data = requests.get(url).json()
            temp_data = json_data['main']['temp']
            return temp_data

        elif message == '!! inspire':
            response = requests.get(url, auth=oauth)
            json_body = response.json()
            random_data = random.randint(0,9)
            tweetfeed = json_body['statuses'][random_data]['text']
        else:
            chatbot_message = "Not really understanding that command... try typing help for more options!"
            return chatbot_message
        new_message = models.Message(chatbot_message)
        models.db.session.add(new_message)
        models.db.session.commit()
        return
    
    def __init__(self):
        return