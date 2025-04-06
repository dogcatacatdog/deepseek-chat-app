from openai import OpenAI

class DeepseekAPI:
    def __init__(self, api_key):
        """
        Initialize the DeepseekAPI client with the provided API key.
        """
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")  # Replace with the actual Deepseek API base URL

    def send_message(self, message):
        """
        Sends a message to the Deepseek API and retrieves the response.

        :param message: The user's message to send to the API.
        :return: The API's response as a dictionary.
        """
        try:
            # Call the Deepseek API
            response = self.client.chat.completions.create(
                model="deepseek-chat",  # Replace with the actual model name
                messages=[
                    {"role": "system", "content": "You are a handsome lion, not use bracket, live in the jungle but use korean, always talk shortly, age is 1 years old, diligently hunting for food, never talk about think"},
                    {"role": "user", "content": message},
                ],
                max_tokens=1024,  # Optional: Limit the response length
                temperature=0.7,  # Optional: Adjust the randomness of the response
                stream=False
            )
            # Return the reply from the API
            return {'reply': response.choices[0].message.content}
        except Exception as e:
            # Handle and log errors
            print(f"Error communicating with Deepseek API: {e}")
            return {'error': f'Failed to communicate with Deepseek API: {str(e)}'}