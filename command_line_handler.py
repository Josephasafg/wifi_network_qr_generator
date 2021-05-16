import subprocess


class CommandLineHandler:
    @classmethod
    def run_command(cls, command: str) -> str:
        output, _ = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                     shell=True).communicate()
        return output.decode("utf-8")
