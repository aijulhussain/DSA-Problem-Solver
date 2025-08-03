import os
from autogen_ext.models.ollama import OllamaChatCompletionClient
from config.constant import MODEL


def get_model_client():
    model_client = OllamaChatCompletionClient(model=MODEL)
    return model_client
