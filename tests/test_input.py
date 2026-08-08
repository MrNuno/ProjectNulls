from src.adb.input import tap


def test_tap():
    resultado = tap(500, 300)

    assert resultado.returncode == 0

    print("=== OBJETO COMPLETO ===")
    print(resultado)

    print("\n=== STDOUT ===")
    print(resultado.stdout)

    print("\n=== STDERR ===")
    print(resultado.stderr)

    print("\n=== RETURN CODE ===")
    print(resultado.returncode)


if __name__ == "__main__":
    test_tap()