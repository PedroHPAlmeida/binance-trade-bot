import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class LLM:
    def __init__(self, token: str = os.getenv('OPENAI_API_KEY')) -> None:
        self._llm = ChatOpenAI(api_key=token)

    def generate(self, prompt: str | ChatPromptTemplate, **kwargs) -> str:
        if isinstance(prompt, ChatPromptTemplate):
            prompt = prompt.format_messages(**kwargs)
        return self._llm.invoke(prompt)['content']
