from flask import Flask, Blueprint
from flask_restful import Api
from config import config
from resources import *

def create_app(config_name):
  app = Flask(__name__)

  config_target = config[config_name]
  app.config.from_object(config_target)
  config_target.init_app(app)

  api_bp = Blueprint('api', __name__, url_prefix='/api')
  api = Api(api_bp)

  api.add_resource(LandingResource, '/')
  api.add_resource(HomeResource, '/home')
  api.add_resource(CounterResource, '/counter')
  api.add_resource(AssetResource, '/asset')

  app.register_blueprint(api_bp)

  return app

config_name = 'testing'
app = create_app(config_name)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
