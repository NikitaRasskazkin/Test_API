from pymongo.write_concern import WriteConcern


alias = 'main'


class BaseModel:
    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = alias
        final = True

    @classmethod
    def insert_data(cls):
        pass
