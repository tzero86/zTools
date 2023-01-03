import openai
from libs import Keyring

class Bryce:
    def __init__(self):
        self.api_key = Keyring.Keys.OPEN_AI_KEY
        openai.api_key = Keyring.Keys.OPEN_AI_KEY
        
    def ask(self, question):
        model_engine = "text-davinci-003"
        prompt = (f"{question}\n")

        try:
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )

            if isinstance(completions, str):
                # Return the error message as the response
                return completions
            else:
                # Access the `choices` attribute as before
                message = completions.choices[0].text
                return message
        except Exception as e:
            # Return the error message as the response
            return str(e)

    def test(self):
        return self.ask('A Dog class in python')