class TTTPlayer:
    def __init__(self, name):
        if name != '':
            self._name = name

    def get_name(self):
        return self._name

    _name = 'NO_NAME_ENTERED'
    _mark = 'NO_MARK_CURRENTLY'

