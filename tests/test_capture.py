from src.vision.capture import capture_screen


def test_capture_screen():
    imagem = capture_screen()

    print("=== TIPO ===")
    print(type(imagem))

    print("\n=== DIMENSÕES ===")
    print(imagem.shape)

    assert imagem is not None
    assert imagem.shape == (2400, 1080, 3)


if __name__ == "__main__":
    test_capture_screen()