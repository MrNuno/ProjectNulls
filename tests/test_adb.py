from src.adb.client import run_adb_command


def test_adb_devices():
    resultado = run_adb_command(["devices"])

    print("=== OBJETO COMPLETO ===")
    print(resultado)

    print("\n=== STDOUT ===")
    print(resultado.stdout)

    print("\n=== STDERR ===")
    print(resultado.stderr)

    print("\n=== RETURN CODE ===")
    print(resultado.returncode)


if __name__ == "__main__":
    test_adb_devices()