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
