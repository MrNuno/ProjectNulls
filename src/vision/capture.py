from src.adb.client import run_adb_binary_command


def capture_screen():
    """
    Captura a tela atual do dispositivo Android.

    Retorna os dados da imagem em bytes.
    """

    return run_adb_binary_command(
        ["exec-out", "screencap", "-p"]
    )