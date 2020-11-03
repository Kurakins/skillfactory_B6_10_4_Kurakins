class Volunteer:
    def __init__(self, name, second_name, town, status):
        self.name = name
        self.second_name = second_name
        self.town = town
        self.status = status

    def __str__(self):
        return '{} {}, г. {}, статус "{}"'.format(self.name, self.second_name, self.town, self.status)

class VolunteersList(list):

    def __str__(self):
        list = ''
        for empl in self:
            list += str(empl) + '\n'
        return list
