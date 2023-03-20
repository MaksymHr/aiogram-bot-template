from pydantic import SecretStr, BaseSettings


class BotConfig(BaseSettings):
    """
    Class for main bot variables which are loaded from .env file.\n
    For some of important variables using Secret String from pydantic, so you'll should to "unsecret" it,
    using variable.get_secret_value().
    """

    bot_token: SecretStr

    class AdditionalConfig:
        env_file = ".env"
        encoding = "utf-8"
