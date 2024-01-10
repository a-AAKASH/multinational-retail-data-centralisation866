#### This file will work as a utility class
#### It will be creating methods that help extract data from different data sources
#### The methods contained will be fit to extract data from a particular data source - 
#### These sources can include CSV files, an API and an S3 bucket
from database_utils import DatabaseConnector
from sqlalchemy import MetaData


class DataExtractor():
    def __init__(self, database_connector_instance):
        self.database_connector_instance = database_connector_instance

    def list_db_tables(self):
        try:
            db_engine = self.database_connector_instance.init_db_engine()

            with db_engine.connect() as connection:
                metadata = MetaData()
                metadata.reflect(bind=connection)

                table_names = metadata.tables.keys()
                return list(table_names)
        except Exception as e:
            print(f"Error: Unable to list the database tables. \n{e}")
            return []
            # Configure the logging as an alternative, good stuff when you don't want errors showing
            #logging.basicConfig(filename='data_extraction.log', level=logging.ERROR)
            #logging.error(f"Unable to list the database tables. Error: {e}")
            #return []


if __name__ == "__main__":
    my_database_connector = DatabaseConnector()
    data_extractor = DataExtractor(database_connector_instance=my_database_connector)
    tables = data_extractor.list_db_tables()
    print("Tables in the database:", tables)