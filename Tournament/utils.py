from fractions import Fraction as ratio


class Person:
    def __init__(self, name, username='', program='OTHER'):
        assert isinstance(name, str) and name != '' and name is not None
        if username is not '':
            if username[0] == '@':
                self.username = username
            else:
                self.username = '@' + username
        else:
            self.username = '@DUMMYNAME'
        if program == '' or program is None:
            program = 'OTHER'
        assert program in {'DS', 'iOS', 'FSW', 'Android', None, 'OTHER'}
        self.name = name
        self.program = program

    def show(self):
        return self.name


def show(s):
    if isinstance(s, Person):
        return s.show()
    elif isinstance(s, (str, int, float)):
        return s
    elif isinstance(s, ratio):
        return ':'.join([str(s.numerator), str(s.denominator)])
    else:
        return None
