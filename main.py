import logging
from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient
from interface.root_component import Root


logger = logging.getLogger()


logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("info.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == "__main__":

    binance = BinanceClient("4311d1426594789e1b9f1806f926ffbb52e9a4bfd07895c3a30be448cb050118",
                        "56cd89bbb19cf2fa9df97491519da46a4160b21a8f09e1763c6d7214e74c25cd",
                            True, True)

    bitmex = BitmexClient("19vKQqm7Ui7tFyZ19WxIGahN", "uVimV3TJ0Hmxm-89CaBb6tZ655yPiSx2DXJIkExIMlkXuqAk", True)

    root = Root(binance, bitmex)
    root.mainloop()
