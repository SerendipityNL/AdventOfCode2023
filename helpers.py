class Input:

    def get(self, file):
        lines = open(file, "r")
        return self.clean_lines(lines)

    def clean_lines(self, lines):
        return [line.strip() for line in lines.readlines()]


def get_input(day):
    path = "../input/day_" + str(day)
    return Input().get(path)


def get_test_input(day, part=1):
    path = "../test_input/day_" + str(day) + "_" + str(part)
    return Input().get(path)