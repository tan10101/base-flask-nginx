class Config:
  def init_app(self):
    pass

class TestingConfig(Config):
  TESTING = True

config = {
  'testing': TestingConfig,
  'default': TestingConfig
}

