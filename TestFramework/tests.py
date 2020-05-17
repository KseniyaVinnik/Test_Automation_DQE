import glob
from sys import argv
from TestFramework.configurator import Configurator
from TestFramework.connector import Connector
from TestFramework.test_processor import TestProcessor

config = Configurator(argv[1])

database_url = config.get_database_url()
connector = Connector(database_url)
test_data_folder = config.get_test_data_folder()
print([f for f in glob.glob(test_data_folder + '/*.json', recursive=True)])
