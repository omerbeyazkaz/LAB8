from abc import ABC, abstractmethod

class FileProcessor(ABC):
    address = ""

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(FileProcessor):
    def calculateFreqs(self):
        frequencies = [0] * 26

        with open(self.address, 'r') as file:
            text = file.read().lower()

            for char in text:
                if char.isalpha():
                    index = ord(char) - ord('a')
                    frequencies[index] += 1

        for i in range(26):
            letter = chr(i + ord('a'))
            frequency = frequencies[i]
            print(f"{letter} = {frequency}")


class DictCount(FileProcessor):
    def calculateFreqs(self):
        frequencies = {}

        with open(self.address, 'r') as file:
            text = file.read().lower()

            for char in text:
                if char.isalpha():
                    frequencies[char] = frequencies.get(char, 0) + 1

        for letter, frequency in frequencies.items():
            print(f"{letter} = {frequency}")



list_counter = ListCount("weirdWords.txt")
list_counter.calculateFreqs()

print("----------")

dict_counter = DictCount("weirdWords.txt")
dict_counter.calculateFreqs()

