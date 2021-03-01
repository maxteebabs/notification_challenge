from os import environ, path

database_filename = "swvl.db"
project_dir = path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(path.join(project_dir, database_filename))
print('pppp', database_path)

class Default:
    """Default Configuration for the swvl application"""
    DEBUG = True
    #: Define the SQLAlchemy database connection properties
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Default):
    """Development configuration for the swvl application."""
    DEBUG = True

class Testing(Default):
    """Testing configuration for the swvl application."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URI')

class Production(Default):
    """Testing configuration for the swvl application."""
    DEBUG = False

CONFIGS = {
    'Default': Default,
    'Development': Development,
    'Testing': Testing,
    'Production': Production
}