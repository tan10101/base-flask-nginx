from flask_restful import Resource

class CounterResource(Resource):
  @classmethod
  def get(cls):
    return { 'Counter': 'Thank you for your counter' }
