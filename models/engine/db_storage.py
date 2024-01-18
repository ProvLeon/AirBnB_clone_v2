#!/usr/bin/python3
"""Creating a Storage database"""
"""imported modules"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """The DB Storage class"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """initializing"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        db_url = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.drop_all(bind=self.__engine)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

    def all(self, cls=None):
        """All stored data"""
        if cls is not None:
            data = self.__session.query(cls)
        else:
            classes = [State, City, User, Place, Review]
            data = []
            for itter in classes:
                data.extend(self.__session.query(itter).all())
        obj_datas = {}
        for obj in data:
            classname = type(obj).__name__
            id = obj.id
            key = f"{classname}.{id}"
            obj_datas[key] = obj
        for value in obj_datas.values():
            print(value)
        return obj_datas

    def new(self, obj):
        """The new method"""
        self.__session.add(obj)

    def save(self):
        """ The save method"""
        self.__session.commit()

    def delete(self, obj=None):
        """The delete method"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """The reload method"""
        from models.user import User, Base
        from models.city import City, Base
        from models.place import Place, Base
        from models.state import State, Base
        from models.amenity import Amenity
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
