class MTK2:
    def __init__(self):
        self.state = None

        self.numbers = {
            "00011": '-', "11001": '?', "01110": ':', "01001": 'Кто там?',
            "01111": '(', "10010": ')', "11100": '.', "01100": ',',
            "00101": '\'', "11110": '=', "11101": '/', "10001": '+',
            "10110": '0', "10111": '1', "10011": '2', "00001": '3',
            "01010": '4', "10000": '5', "10101": '6', "00111": '7',
            "00110": '8', "11000": '9', "11010": 'Ш', "10100": 'Щ',
            "01101": "Э", "01011": 'Ю'
        }

        self.russian = {
            "00011": 'А', "11001": 'Б', "10011": 'В', "11010": 'Г',
            "01001": 'Д', "00001": 'Е', "11110": 'Ж', "10001": 'З',
            "00110": 'И', "01011": 'Й', "01111": 'К', "10010": 'Л',
            "11100": 'М', "01100": 'Н', "11000": 'О', "10110": 'П',
            "01010": 'Р', "00101": 'С', "10000": 'Т', "00111": 'У',
            "01101": 'Ф', "10100": 'Х', "01110": 'Ц', "10101": 'Ы',
            "11101": 'Ь', "10111": 'Я'
        }

        self.latin = {
            "00011": 'A', "11001": 'B', "01110": 'C', "01001": 'D',
            "00001": 'E', "01101": 'F', "11010": 'G', "10100": 'H',
            "00110": 'I', "01011": 'J', "01111": 'K', "10010": 'L',
            "11100": 'M', "01100": 'N', "11000": 'O', "10110": 'P',
            "10111": 'Q', "01010": 'R', "00101": 'S', "10000": 'T',
            "00111": 'U', "11110": 'V', "10011": 'W', "11101": 'X',
            "10101": 'Y', "10001": 'Z'
        }

        self.control = {
            "01000": '\r',
            "00010": '\n',
            "11111": self.latin,
            "11011": self.numbers,
            "00100": ' ',
            "00000": self.russian,
        }

        self.types = [self.control, self.russian, self.numbers, self.latin]

    def decode(self, bits):
        text = ''
        for i in range(0, len(bits), 5):
            bits5 = bits[i: i + 5]
            if bits5 in self.control and isinstance(self.control.get(bits5, ''), dict):
                self.state = self.control.get(bits5, None)
            elif not self.state:
                text += ''
            else:
                text += self.state.get(bits5, '')
        return text
