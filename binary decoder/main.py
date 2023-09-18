import sys

class Helper:

    @staticmethod
    def sanitize(binary_string) -> str:
        return ''.join(char for char in binary_string if char in ('0', '1'))

    @staticmethod
    def convert(binary_string) -> int:
        try:
            decimal_data = int(binary_string, 2)
            return decimal_data
        except ValueError:
            return None 

class Decoder:

    def __init__(self, file) -> None:
        self.binary_string = open(file, 'r').read()

    def decode(self) -> str:
        str_data = ''
        helper = Helper()
        # https://www.geeksforgeeks.org/convert-binary-to-string-using-python/
        # used as a reference 
        for i in range(0, len(self.binary_string), 7):
            temp_data = self.binary_string[i:i + 7]
            sanitizeddata = helper.sanitize(temp_data)
            decimal_data = helper.convert(sanitizeddata)
            
            if decimal_data is not None:
                if decimal_data == 7:
                    str_data += '\x07'
                elif decimal_data == 8:
                    str_data += '\x08'
                else:
                    str_data += chr(decimal_data) 

        return str_data

file = sys.argv

for i in file:
    my_file = Decoder(i)
    print(my_file.decode())
