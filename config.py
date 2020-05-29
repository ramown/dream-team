"""."""


class Config:
    """Commom configurations."""

    DEBUG = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dream_team.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development configurations."""

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """Production configurations."""

    TESTING = False


class TestingConfig(Config):
    """onfigurations for Testing, with a separate test databse."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_db.db"
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
