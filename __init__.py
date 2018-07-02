from api import run_api
from database import create_database
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-n", "--name", dest="db_name", default="database.db",
            help="change the name of the database file, by default database.db", metavar="FILENAME")
    parser.add_option("-p", "--port", dest="api_port", default="5002",
            help="change the port for the REST API, by default 5002", metavar="PORT")

    (options, args) = parser.parse_args()

    if create_database(options.db_name):
        run_api(options.db_name, options.api_port)
    else:
        print("failed to create database")
