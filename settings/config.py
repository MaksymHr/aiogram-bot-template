from pydantic import SecretStr, BaseSettings


class BotConfig(BaseSettings):
    """
    Class for main bot variables which are loaded from .env file.\n
    For some of important variables using Secret String from pydantic, so you'll should to "unsecret" it,
    using variable.get_secret_value().
    """

    BOT_TOKEN: SecretStr

    class Config:

        # fields = {
        #     "BOT_TOKEN": {
        #         'env': "BOT_TOKEN"
        #     }
        # }

        # if you move .env file you should rewrite path below.
        env_file = "settings\\.env"
        encoding = "utf-8"
