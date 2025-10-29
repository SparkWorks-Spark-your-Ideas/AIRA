import logging
logger = logging.getLogger(__name__)

class VectorStore:
    def __init__(self):
        self.initialized = False
    async def initialize(self, *args, **kwargs):
        logger.info("VectorStore stub mode")
        self.initialized = True
    async def search(self, query: str, *args, **kwargs):
        return []
