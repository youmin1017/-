import random

class game:

    def __init__(self):
        self.passwd = random.sample('0123456789', 4)

    def __is_unique(self, input: str):
        char_seen = []
        for char in input:
            if char in char_seen:
                return False
            char_seen.append(char)
        return True

    def play(self, input: str) -> str:
        input = input.replace(' ', '')
        if len(input) != 4 or not input.isnumeric() or not self.__is_unique(input):
            return "請輸入正確的輸入。e.g. 1234"
        A, B = 0, 0
        for i, c in enumerate(input):
            if self.passwd[i] == c:
                A += 1
            elif c in self.passwd:
                B += 1
        return f"{A}A{B}B" if A != 4 else "WIN"

