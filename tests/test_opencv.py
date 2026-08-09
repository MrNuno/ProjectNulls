import cv2
import numpy as np

from src.vision.capture import capture_screen


def test_opencv_decode():
    resultado = capture_screen()

    imagem = cv2.imdecode(
        np.frombuffer(resultado.stdout, dtype=np.uint8),
        cv2.IMREAD_COLOR,
    )

    print("=== TIPO DA IMAGEM ===")
    print(type(imagem))

    print("\n=== DIMENSÕES ===")
    print(imagem.shape)

    assert resultado.returncode == 0
    assert imagem is not None


if __name__ == "__main__":
    test_opencv_decode()