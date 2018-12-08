from flask_restful import Resource

class LandingResource(Resource):
  @classmethod
  def get(cls):
    return { 'Hellow': 'Thank you for visiting' }
