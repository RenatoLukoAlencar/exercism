class BufferFullException(BufferError):
    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = ["" for _ in range(capacity)]
        self.readIndex = 0
        self.writeIndex = 0

    def read(self):
        if self.buffer[self.readIndex] != "":
            res = self.buffer[self.readIndex]
            self.buffer[self.readIndex] = ""
            self.readIndex = (
                0 if self.readIndex == self.capacity - 1 else self.readIndex + 1
            )
            return res

        else:
            raise BufferEmptyException("Circular buffer is empty")

    def write(self, data):
        if self.buffer[self.writeIndex] == "":
            self.buffer[self.writeIndex] = data
            self.writeIndex = (
                0 if self.writeIndex == self.capacity - 1 else self.writeIndex + 1
            )
        else:
            raise BufferFullException("Circular buffer is full")

    def overwrite(self, data):
        if self.buffer[self.writeIndex] == "":
            self.write(data)
        else:
            self.buffer[self.writeIndex] = data
            self.writeIndex = (
                0 if self.writeIndex == self.capacity - 1 else self.writeIndex + 1
            )
            self.readIndex = (
                0 if self.readIndex == self.capacity - 1 else self.readIndex + 1
            )

    def clear(self):
        self.buffer = ["" for _ in range(self.capacity)]
