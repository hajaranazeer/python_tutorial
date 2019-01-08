class score:
    def mark(self):
        print("first class")


class sheet (score):
    def mark(self):
        print("second class")


m = sheet()
m.mark()
