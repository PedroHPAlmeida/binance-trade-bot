from typing import Any, Dict, Iterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document


class DictDocumentLoader(BaseLoader):
    def __init__(self, dictionary: Dict[str, Any]) -> None:
        self.dictionary = dictionary

    def lazy_load(self) -> Iterator[Document]:
        for key, value in self.dictionary.items():
            yield Document(
                page_content=str(value),
                metadata={'key': key},
            )
