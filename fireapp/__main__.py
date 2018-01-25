import fire


class Maths:
    """Example for firepex"""
    def add(self, num1, num2):
        """Addition"""
        return num1 + num2

    def div(self, num1, num2):
        """Division"""
        return num1 / num2


fire.Fire(Maths)
