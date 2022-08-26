from app.config import BaseConfig
from app.server import create_app

app = create_app(BaseConfig)

if __name__ == "__main__":
    app.run()