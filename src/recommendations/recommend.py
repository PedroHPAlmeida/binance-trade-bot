from datetime import timedelta

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

from src.apis.custom_dict_loader import DictDocumentLoader
from src.db.price_now_repo import PriceNowRepository
from src.db.statistics_24hr_repo import Statistics24hRepository


class Recommend:
    def __init__(self, price_now_repo: PriceNowRepository, statistics24h_repo: Statistics24hRepository):
        self._price_now_repo = price_now_repo
        self._statistics24h_repo = statistics24h_repo

    def most_valued(self):
        last_30_days = self._price_now_repo.find_by_last_time(timedelta(days=30))
        last_7_days = self._price_now_repo.find_by_last_time(timedelta(days=7))
        last_3_days = self._price_now_repo.find_by_last_time(timedelta(days=3))
        last_24_hours = self._price_now_repo.find_by_last_time(timedelta(hours=24))
        last_1_hour = self._price_now_repo.find_by_last_time(timedelta(hours=1))
        last_5_minutes = self._price_now_repo.find_by_last_time(timedelta(minutes=5))
        prices = {
            'last_30_days_prices': last_30_days,
            'last_7_days_prices': last_7_days,
            'last_3_days_prices': last_3_days,
            'last_24_hours_prices': last_24_hours,
            'last_1_hour_prices': last_1_hour,
            'last_5_minutes_prices': last_5_minutes,
        }

        last_30_days_trades = self._statistics24h_repo.find_by_last_time(timedelta(days=30))
        last_7_days_trades = self._statistics24h_repo.find_by_last_time(timedelta(days=7))
        last_3_days_trades = self._statistics24h_repo.find_by_last_time(timedelta(days=3))
        last_24_hours_trades = self._statistics24h_repo.find_by_last_time(timedelta(hours=24))
        last_1_hour_trades = self._statistics24h_repo.find_by_last_time(timedelta(hours=1))
        last_5_minutes_trades = self._statistics24h_repo.find_by_last_time(timedelta(minutes=5))
        trades = {
            'last_30_days_trades': last_30_days_trades,
            'last_7_days_trades': last_7_days_trades,
            'last_3_days_trades': last_3_days_trades,
            'last_24_hours_trades': last_24_hours_trades,
            'last_1_hour_trades': last_1_hour_trades,
            'last_5_minutes_trades': last_5_minutes_trades,
        }

        loader = DictDocumentLoader({**prices, **trades})
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()
        db = FAISS.from_documents(texts, embeddings)
        retriever = db.as_retriever()

        template = '''Answer the question also based on the context provided:

        {context}

        Question: {question}

        The message must be written entirely in Brazilian Portuguese.
        '''
        prompt = ChatPromptTemplate.from_template(template)
        model = ChatOpenAI()

        def format_docs(docs):
            return '\n\n'.join([d.page_content for d in docs])

        chain = {'context': retriever | format_docs, 'question': RunnablePassthrough()} | prompt | model | StrOutputParser()

        return chain.invoke(
            '''Which currencies have appreciated the most:
            * In the last month?
            * In the last 7 days?
            * In the last 3 days?
            * In the last 24 hours?
            * In the last 1 hour?
            * In the last 5 minutes?
            '''
        )
