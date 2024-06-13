import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


class LLM:
    def __init__(self, token: str = os.getenv('OPENAI_API_KEY')) -> None:
        self._llm = ChatOpenAI(model='gpt-4o', api_key=token)
        self._str_parser = StrOutputParser()

    def generate(self, prompt: str | ChatPromptTemplate, **kwargs) -> str:
        if isinstance(prompt, ChatPromptTemplate):
            prompt = prompt.format_messages(**kwargs)
        chain = self._llm | self._str_parser
        return chain.invoke(prompt)
