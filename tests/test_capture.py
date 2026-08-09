from src.vision.capture import capture_screen


def test_capture_screen():
    resultado = capture_screen()

    print("=== TIPO ===")
    print(type(resultado.stdout))

    print("\n=== TAMANHO ===")
    print(len(resultado.stdout))

    print("\n=== RETURN CODE ===")
    print(resultado.returncode)

    assert resultado.returncode == 0
    assert isinstance(resultado.stdout, bytes)
    assert len(resultado.stdout) > 0


if __name__ == "__main__":
    test_capture_screen()