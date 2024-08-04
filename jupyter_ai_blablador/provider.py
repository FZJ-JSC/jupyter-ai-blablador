from typing import ClassVar, List

from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings

from jupyter_ai import AuthStrategy, EnvAuthStrategy, Field
from jupyter_ai_magics import BaseProvider, BaseEmbeddingsProvider

# Difference between OpenAI and ChatOpenAI:
#   https://stackoverflow.com/questions/76950609/what-is-the-difference-between-openai-and-chatopenai-in-langchain

class BlabladorProvider(BaseProvider, OpenAI):
    id: ClassVar[str] = "blablador"
    name: ClassVar[str] = "Blablador"
    models: ClassVar[List[str]] = [
        "alias-code",
        "alias-fast",
        "alias-large",
    ]
    # help: ClassVar[str] = None
    model_id_key: ClassVar[str] = "model_name"
    model_id_label: ClassVar[str] = "Model ID"
    pypi_package_deps: ClassVar[List[str]] = ["langchain_openai"]
    auth_strategy: ClassVar[AuthStrategy] = EnvAuthStrategy(name="OPENAI_API_KEY")
    # registry: ClassVar[bool] = False
    openai_api_base: ClassVar[str] = "https://helmholtz-blablador.fz-juelich.de:8000/v1" 
    # openai_api_key: 
    # openai_organization:

    @classmethod
    def is_api_key_exc(cls, e: Exception):
        """
        Determine if the exception is an OpenAI API key error.
        """
        import openai

        if isinstance(e, openai.AuthenticationError):
            error_details = e.json_body.get("error", {})
            return error_details.get("code") == "invalid_api_key"
        return False


class ChatBlabladorProvider(BaseProvider, ChatOpenAI):
    id: ClassVar[str] = "blablador-chat"
    name: ClassVar[str] = "Blablador"
    models: ClassVar[List[str]] = [
        "alias-code",
        "alias-fast",
        "alias-large",
    ]
    # help: ClassVar[str] = None
    model_id_key: ClassVar[str] = "model_name"
    model_id_label: ClassVar[str] = "Model ID"
    pypi_package_deps: ClassVar[List[str]] = ["langchain_openai"]
    auth_strategy: ClassVar[AuthStrategy] = EnvAuthStrategy(name="OPENAI_API_KEY")
    # registry: ClassVar[bool] = False
    openai_api_base: ClassVar[str] = "https://helmholtz-blablador.fz-juelich.de:8000/v1"
    # openai_api_key:
    # openai_organization:

    @classmethod
    def is_api_key_exc(cls, e: Exception):
        """
        Determine if the exception is an OpenAI API key error.
        """
        import openai

        if isinstance(e, openai.AuthenticationError):
            error_details = e.json_body.get("error", {})
            return error_details.get("code") == "invalid_api_key"
        return False


class BlabladorEmbeddingsProvider(BaseEmbeddingsProvider, OpenAIEmbeddings):
    id: ClassVar[str] = "blablador-embeddings"
    name: ClassVar[str] = "Blablador"
    models: ClassVar[List[str]] = [
        "alias-embeddings",
    ]
    model_id_key = "model"
    pypi_package_deps = ["langchain_openai"]
    auth_strategy = EnvAuthStrategy(name="OPENAI_API_KEY")
    openai_api_base: ClassVar[str] = "https://helmholtz-blablador.fz-juelich.de:8000/v1"
