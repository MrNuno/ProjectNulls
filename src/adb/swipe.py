from src.adb.client import run_adb_command


def swipe(x1: int, y1: int, x2: int, y2: int):
    """
    Desliza o dedo na tela do Android.

    Começa em (x1, y1) e termina em (x2, y2).
    """

    return run_adb_command(
        [
            "shell",
            "input",
            "swipe",
            str(x1),
            str(y1),
            str(x2),
            str(y2),
        ]
    )