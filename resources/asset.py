from flask_restful import Resource

class AssetResource(Resource):
  @classmethod
  def get(cls):
    return { 'Asset': 'Thank you for your asset' }
