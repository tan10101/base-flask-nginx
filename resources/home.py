from flask_restful import Resource

class HomeResource(Resource):
  @classmethod
  def get(cls):
    return { 'ok': 'Welcome Hello' }

