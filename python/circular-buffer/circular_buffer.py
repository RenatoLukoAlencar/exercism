class BufferFullException(BufferError):
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def read(self):
        return self.buffer[-1]

    def write(self, data):
        self.buffer.append(data)
        return self.read()

    def overwrite(self, data):
        pass

    def clear(self):
        pass
