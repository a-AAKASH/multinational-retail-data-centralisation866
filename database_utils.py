#### DatabaseConnector class used to connect with and upload the data to the db


import yaml


class DatabaseConnector():
    def __init__(self):
        pass

    def read_db_creds(self, file_path='db_creds.yaml'):
        try:
            with open(file_path, 'r') as file:
                creds = yaml.safe_load(file)
            return creds.get('database', {})
        except FileNotFoundError:
            print(f"Error: File not found!")
        except yaml.YAMLError as e:
            print(f"Error: Unable to load YAML file.\n{e}")
        except Exception as e:
            print(f"Error: {e}")

# db_utils = DatabaseConnector()
# db_creds = db_utils.read_db_creds('db_creds.yaml')
# print(db_creds)
   