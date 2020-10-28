from typing import List
from Resources.JsonWrapper import Content


class KnowledgeGraphInfo:
    sentences: List[list]
    content: Content

    def __init__(self, _sentences, _content):
        self.sentences = _sentences
        self.content = _content
