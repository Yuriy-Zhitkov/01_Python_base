

class Test:

    def message(self, text):
        self.text = text
        return str(text)


my_text = Test()
my_text.message('qwqw')

print(my_text)
