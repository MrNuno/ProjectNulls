import subprocess


def run_adb_command(command: list[str]) -> subprocess.CompletedProcess:
    """
    Executa um comando ADB e retorna o resultado.

    Exemplo:
        run_adb_command(["devices"])
    """

    return subprocess.run(
        ["adb"] + command,
        capture_output=True,
        text=True,
    )

def run_adb_binary_command(command: list[str]) -> subprocess.CompletedProcess:
    """
    Executa um comando ADB que retorna dados binários.

    Exemplo:
        run_adb_binary_command(["exec-out", "screencap", "-p"])
    """

    return subprocess.run(
        ["adb"] + command,
        capture_output=True,
    )