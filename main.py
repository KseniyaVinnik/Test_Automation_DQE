import sys
import logging
from Conductor import Conductor

logging.basicConfig(filename='log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    level=logging.INFO)
logging.info("Analysing FB2 files started")

try:
    directory_name = sys.argv[1]
except IndexError as e:
    logging.error(e)
    print("In the parameters specify the folder with fb2 files for analysis")
    sys.exit(e)

Conductor.run(directory_name)

logging.info("Analysing FB2 file finished")
