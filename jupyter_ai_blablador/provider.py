from os import getenv

from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings

from jupyter_ai import EnvAuthStrategy, Field
from jupyter_ai_magics import BaseProvider, BaseEmbeddingsProvider, Persona

# Difference between OpenAI and ChatOpenAI:
#   https://stackoverflow.com/questions/76950609/what-is-the-difference-between-openai-and-chatopenai-in-langchain

class BlabladorProvider(BaseProvider, OpenAI):
    id = "blablador"
    name = "Blablador"
    models = [
        "alias-code",
        "alias-fast",
        "alias-large",
    ]
    help = "Click here for more details on [Blablador](https://helmholtz-blablador.fz-juelich.de)"
    model_id_key = "model_name"
    model_id_label = "Model ID"
    # registry = False
    pypi_package_deps = ["langchain_openai"]
    auth_strategy =  EnvAuthStrategy(
        name="BLABLADOR_API_KEY", keyword_param="openai_api_key",
    )
    # openai_api_key = getenv("BLABLADOR_API_KEY", '')
    openai_api_base = getenv("BLABLADOR_API_BASE", 'https://helmholtz-blablador.fz-juelich.de:8000/v1')
    openai_organization = "Helmholtz Federation"
    persona = Persona(name="Blablador", avatar_route="api/ai/static/jupyternaut.svg")

    @classmethod
    def is_api_key_exc(cls, e: Exception):
        """
        Determine if the exception is an Blablador API key error.
        """
        import openai

        if isinstance(e, openai.AuthenticationError):
            error_details = e.json_body.get("error", {})
            return error_details.get("code") == "invalid_api_key"
        return False


class ChatBlabladorProvider(BaseProvider, ChatOpenAI):
    id = "blablador-chat"
    name = "Blablador"
    models = [
        "alias-code",
        "alias-fast",
        "alias-large",
    ]
    help = "Click here for more details on [Blablador](https://helmholtz-blablador.fz-juelich.de)"
    model_id_key = "model_name"
    model_id_label = "Model ID"
    # registry = False
    pypi_package_deps = ["langchain_openai"]
    auth_strategy =  EnvAuthStrategy(
        name="BLABLADOR_API_KEY", keyword_param="openai_api_key",
    )
    # openai_api_key = getenv("BLABLADOR_API_KEY", '')
    openai_api_base = getenv("BLABLADOR_API_BASE", 'https://helmholtz-blablador.fz-juelich.de:8000/v1')
    openai_organization = "Helmholtz Federation"
    persona = Persona(name="Blablador", avatar_route="api/ai/static/jupyternaut.svg")

    @classmethod
    def is_api_key_exc(cls, e: Exception):
        """
        Determine if the exception is an Blablador API key error.
        """
        import openai

        if isinstance(e, openai.AuthenticationError):
            error_details = e.json_body.get("error", {})
            return error_details.get("code") == "invalid_api_key"
        return False


class BlabladorEmbeddingsProvider(BaseEmbeddingsProvider, OpenAIEmbeddings):
    id = "blablador-embeddings"
    name = "Blablador"
    models = [
        "alias-embeddings",
    ]
    help = "Click here for more details on [Blablador](https://helmholtz-blablador.fz-juelich.de)"
    model_id_key = "model_name"
    model_id_label = "Model ID"
    # registry = False
    pypi_package_deps = ["langchain_openai"]
    auth_strategy =  EnvAuthStrategy(
        name="BLABLADOR_API_KEY", keyword_param="openai_api_key",
    )
    # openai_api_key = getenv("BLABLADOR_API_KEY", '')
    openai_api_base = getenv("BLABLADOR_API_BASE", 'https://helmholtz-blablador.fz-juelich.de:8000/v1')
    openai_organization = "Helmholtz Federation"
    persona = Persona(name="Blablador", avatar_route="api/ai/static/jupyternaut.svg")
