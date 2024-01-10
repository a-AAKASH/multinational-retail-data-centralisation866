#### DatabaseConnector class used to connect with and upload the data to the db


import yaml
from sqlalchemy import create_engine


class DatabaseConnector():
    def __init__(self):
        pass

    def read_db_creds(self, file_path='db_creds.yaml'):
        try:
            with open(file_path, 'r') as file:
                db_credentials = yaml.safe_load(file)
            return db_credentials.get('database', {})
        except FileNotFoundError:
            print(f"Error: File not found!")
        except yaml.YAMLError as e:
            print(f"Error: Unable to load YAML file.\n{e}")
        except Exception as e:
            print(f"Error: {e}")


    def init_db_engine(self, file_path='db_creds.yaml'):
        db_credentials = self.read_db_creds(file_path)
        if not db_credentials:
            return ValueError("Error: Database credentials are empty or invalid!")
        
        db_url = f"postgresql://{db_credentials['user']}:{db_credentials['password']}@{db_credentials['host']}:{db_credentials['port']}/{db_credentials['name']}"
        engine = create_engine(db_url)

        return engine
# db_utils = DatabaseConnector()
# db_creds = db_utils.read_db_creds('db_creds.yaml')
# print(db_creds)
   