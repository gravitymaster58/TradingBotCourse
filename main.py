import tkinter as tk
import logging

from connectors.binance_futures import BinanceFuturesClient


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("d37afda6853b41b7f28f7eda7c6b4c48b90fc5aeaf88a9d6438d5bd1fe7b6733",
                                   "018617dc93e8149c99a14b8ea8cb1ec71142b189c73dc9c5ada55d86eedf6392", True)



    root = tk.Tk()
    root.mainloop()
