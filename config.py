import os
from dotenv import load_dotenv
load_dotenv('.env')

database_filename = "swvl.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
# database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
# test_database_path = "sqlite:///{}".format(os.path.join(project_dir, "swvl_test.db"))

database_path = os.environ.get("DATABASE_URI")
test_database_path = os.environ.get("TEST_DATABASE_URI")

class Default:
    """Default Configuration for the swvl application"""
    DEBUG = True
    #: Define the SQLAlchemy database connection properties
    SQLALCHEMY_DATABASE_URI = database_path
    #os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class Development(Default):
    """Development configuration for the swvl application."""
    DEBUG = True

class Testing(Default):
    """Testing configuration for the swvl application."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = test_database_path

class Production(Default):
    """Testing configuration for the swvl application."""
    DEBUG = False

CONFIGS = {
    'Default': Default,
    'Development': Development,
    'Testing': Testing,
    'Production': Production
}