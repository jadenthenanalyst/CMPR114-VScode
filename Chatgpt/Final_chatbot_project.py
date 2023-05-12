import openai

class Chatbot:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.messages = []
        
    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})
        
    def run_chatbot(self):
        try:
            system_msg = input("What type of chatbot would you like to create?\n")
            self.add_message("system", system_msg)
            print("Your new assistant is ready!")

            while True:
                message = input()
                if message == "quit()":
                    break
                self.add_message("user", message)
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=self.messages)
                reply = response["choices"][0]["message"]["content"]
                self.add_message("assistant", reply)
                print("\n" + reply + "\n")
        except Exception as e:
            print("An error occurred:", str(e))



api_key = "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"  
chatbot = Chatbot(api_key)
chatbot.run_chatbot()
