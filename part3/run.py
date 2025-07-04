import os
from config import DevelopmentConfig, ProductionConfig
from app import create_app

env = os.getenv('FLASK_CONFIG', 'development')

if env == 'production':
    config_class = ProductionConfig
else:
    config_class = DevelopmentConfig

app = create_app(config_class)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
