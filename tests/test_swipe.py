from src.adb.swipe import swipe


def test_swipe():
    resultado = swipe(300, 500, 700, 500)

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
    test_swipe()