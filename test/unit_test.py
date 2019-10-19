import unittest
import chat_bot
import responses


class ChatBotUnitTestCases(unittest.TestCase):
    def test_invalid_command(self):
        result = random_functions.response('!!')
        self.assertEquals(result, 'Not a valid command')
    def test_valid_help(self):
        result = chat_bot.ChatBot().get_response("!! help")
        self.assertEquals(result)
    
    def test_invalid_help(self):
        result = chat_bot.ChatBot().get_response("Help")
        self.assertEquals(result, 'Try typing !! about')

    def test_valid_about(self):
        result = ChatBot().get_response("!! about")
        self.assertEquals(result)
    
     def test_valid_weather(self):
        result = ChatBot().get_response("!! weather")
        self.assertEquals(result)
    
    def test_invalid_weather(self):
        result = ChatBot().get_response("!! weather")
        self.assertEquals(result, "Choose a Valid City in the United States!")
    
    def test_valid_quote(self):
        result = ChatBot().get_response("!! inspire")
        self.assertEquals(result)

    def test_valid_temp(self):
        result = ChatBot().get_response("!! temperature")
        self.assertEquals(result)
    def test_invalid_temp(self):
        result = ChatBot().get_response("!! temperature")
        self.assertEquals(result, "Choose a Valid City in the United States!")
    
     def test_valid_string(self):
        result = ChatBot().get_response("Not really understanding that command... try typing !! help for more options!")
        self.assertEquals(result)
    