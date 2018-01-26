import fire


class Example:
    """Example for firepex"""
    def r_string(self, string):
        return string

    def r_class(self):
        return MoreCommands

class MoreCommands:
    """This will be a subset of commands under r_class"""
    def r_add(self, num1, num2):
        return num1 + num2

    def r_sub(self, num1, num2):
        return num1 - num2


fire.Fire(Example)
