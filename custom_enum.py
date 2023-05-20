class StringEnum:
    def __init__(self, *args, start_index=0):
        self._string_to_index = {}
        self._index_to_string = {}
        for idx, value in enumerate(args, start=start_index):
            self._string_to_index[value] = idx
            self._index_to_string[idx] = value

    def name_to_index(self, name):
        return self._string_to_index[name]

    def index_to_name(self, index):
        return self._index_to_string[index]

    def __getattr__(self, name):
        return self.name_to_index(name)

    def __getitem__(self, index):
        return self.index_to_name(index)

    def __repr__(self):
        return str(self._index_to_string)


# Example usage:
Color = StringEnum("<PAD>","RED", "GREEN", "BLUE")
print(Color[0])           # Output: 1
print(Color.name_to_index("GREEN"))  # Output: 2
print(Color[2])            # Output: 'GREEN'
print(Color.index_to_name(3))        # Output: 'BLUE'
