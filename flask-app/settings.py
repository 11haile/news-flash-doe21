import pydantic

def get_settings():
    
    return Settings()

class Settings(pydantic.BaseSettings):
    api_key:str = pydantic.Field(env='NEWS_API_KEY', min_length=10)
    class Config():
        pass
