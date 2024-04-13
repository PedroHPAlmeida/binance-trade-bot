import os

import google.generativeai as genai


class GeminiAI:
    def __init__(self, token: str = os.getenv('GOOGLE_API_KEY')) -> None:
        self._api_key = token
        genai.configure(api_key=self._api_key)
        self._model = genai.GenerativeModel('gemini-pro')

    def generate(self, prompt: str) -> str:
        response = self._model.generate_content(prompt)
        return response.text
