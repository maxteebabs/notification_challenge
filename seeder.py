from flask import current_app
from models.User import User, TYPE
from models.Group import Group, UserGroup
from extensions import db

class Seeder:
    def seed(self):
        self.seedCustomer()
        self.seedGroup()
    
    def seedCustomer(self):
        user = User.query.first()
        if not user:
            user = User(id=1, name="Mark Dean", mobile="23480000000523", type = TYPE.CUSTOMER)
            stat = user.save()
            # current_app.logger.info(f'seeding user {user.name}')
            
            user = User(id=2, name="Angela Prisca", mobile="23480000000127", type = TYPE.CUSTOMER)
            stat = user.save()
            # current_app.logger.info(f'seeding rider {user.name}')
        
            user = User(id=3, name="Jack Robison", mobile="23480000000355", type = TYPE.CUSTOMER)
            stat = user.save()
            # current_app.logger.info(f'seeding rider {user.name}')

            # seed rider
            user = User(id=4, name="Emmanuel Hanks", mobile="23480000000675", type = TYPE.RIDER)
            stat = user.save()
            # current_app.logger.info(f'seeding rider {user.name}')

            user = User(id=5, name="John Richard", mobile="23480063800355", type = TYPE.RIDER)
            stat = user.save()
            # current_app.logger.info(f'seeding rider {user.name}')
    
    def seedGroup(self):
        group = Group.query.first()
        if not group:
            group = Group(name="Nigeria Division")
            stat = group.save()
            # current_app.logger.info(f'seeding Group {group.name}')

            # attach user to Nigeria division group
            user = User.query.filter_by(name='Angela Prisca').first()
            user_group = UserGroup(group_id=group.id, user_id= user.id) 
            user_group.save()
            # current_app.logger.info(f'seeding UserGroup:: \
                # group id: {user_group.id}:user id: {user_group.user_id}')

            # attach user to Nigeria division group
            user = User.query.filter_by(name='Jack Robison').first()
            user_group = UserGroup(group_id=group.id, user_id= user.id) 
            user_group.save()
            # current_app.logger.info(f'seeding UserGroup:: \
                # group id: {user_group.id}:user id: {user_group.user_id}')

            group = Group(name="London Division")
            stat = group.save()
            # current_app.logger.info(f'seeding Group {group.name}')

            group = Group(name="Rider Group")
            stat = group.save()
            # current_app.logger.info(f'seeding Group {group.name}')
            
            # attach user to Rider group
            user = User.query.filter_by(name='John Richard').first()
            user_group = UserGroup(group_id=group.id, user_id= user.id) 
            user_group.save()
            # current_app.logger.info(f'seeding UserGroup:: \
                # group id: {user_group.id}:user id: {user_group.user_id}')