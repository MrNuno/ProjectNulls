from src.adb.client import run_adb_binary_command


def test_screencap():
    resultado = run_adb_binary_command(
        ["exec-out", "screencap", "-p"]
    )

    print("=== OBJETO COMPLETO ===")
    print(resultado)

    print("\n=== TIPO DO STDOUT ===")
    print(type(resultado.stdout))

    print("\n=== TAMANHO DO STDOUT ===")
    print(len(resultado.stdout))

    print("\n=== RETURN CODE ===")
    print(resultado.returncode)

    assert resultado.returncode == 0
    assert isinstance(resultado.stdout, bytes)
    assert len(resultado.stdout) > 0


if __name__ == "__main__":
    test_screencap()