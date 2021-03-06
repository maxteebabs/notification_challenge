import unittest
from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from app import create_app
from extensions import db

manager = Manager(create_app)

## COMMANDS & OPTIONS ########################################################
"""This is used to switch between Development, Testing and Production mode"""
manager.add_option(
    '-m',
    '--mode',
    dest='mode',
    required=False, )

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host="127.0.0.1", port=7000))

@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover("tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

######### START THE APP #######################
if __name__ == '__main__':
    manager.run()
