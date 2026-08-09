import cv2
import numpy as np

from src.adb.client import run_adb_binary_command


def capture_screen() -> np.ndarray:
    """
    Captura a tela atual do dispositivo Android.

    Retorna:
        Uma imagem OpenCV como numpy.ndarray.

    Levanta:
        RuntimeError se a captura ou decodificação falhar.
    """

    resultado = run_adb_binary_command(
        ["exec-out", "screencap", "-p"]
    )

    if resultado.returncode != 0:
        raise RuntimeError(
            f"Falha ao capturar a tela: {resultado.stderr}"
        )

    imagem = cv2.imdecode(
        np.frombuffer(resultado.stdout, dtype=np.uint8),
        cv2.IMREAD_COLOR,
    )

    if imagem is None:
        raise RuntimeError(
            "O ADB retornou dados, mas o OpenCV não conseguiu "
            "decodificar a imagem."
        )

    return imagem