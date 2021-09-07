import os
from multiprocessing import cpu_count

bind = "localhost:{}".format(os.environ.get("SERVER_PORT", "8000"))

