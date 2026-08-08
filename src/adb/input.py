from src.adb.client import run_adb_command


def tap(x: int, y: int):
    """
    Toca na tela do Android na posição x,y.
    """

    return run_adb_command(
        ["shell", "input", "tap", str(x), str(y)]
    )