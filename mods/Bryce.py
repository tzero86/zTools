import openai

API_key = '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'

class Bryce:
    def __init__(self, api_key: API_key):
        self.api_key = api_key
        openai.api_key = api_key
        
    def ask(self, question):
        model_engine = "text-davinci-003"
        prompt = (f"{question}\n")

        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        return message

askBryce = Bryce(API_key)
response = askBryce.ask("Create a Python Script that uses Text User Interface using the following pip library 'textual[dev]'")
print(response)
