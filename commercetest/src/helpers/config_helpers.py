import os

def get_base_url():
    env = os.environ.get("ENV", "prod")

    if env.lower() == "test":
        return "http://localhost:7888/Commercesite"
    elif env.lower() == "prod":
        return "http://demostore.supersqa.com"
    else:
        raise Exception(f"Unknown envirnment: {env}")