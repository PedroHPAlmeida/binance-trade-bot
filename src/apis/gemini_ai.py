import os
import textwrap

import google.generativeai as genai
from markdown import markdown


class GeminiAI:
    def __init__(self, token: str = os.getenv('GOOGLE_API_KEY')) -> None:
        self._api_key = token
        genai.configure(api_key=self._api_key)
        self._model = genai.GenerativeModel('gemini-pro')

    def generate(self, prompt: str) -> str:
        response = self._model.generate_content(prompt)
        return self.to_markdown(response.text)

    def to_markdown(self, text: str) -> str:
        text = text.replace('•', '  *')
        return markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
