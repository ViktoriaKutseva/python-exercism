class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message 


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data_list = []
        self.count = 0
    def read(self):
        if self.count <= self.capacity:
            returned_data = self.data_list[self.count]
            self.count += 1
            return returned_data
        elif self.count > self.capacity:
            raise BufferFullException("buffer full")
        else:
            raise BufferEmptyException("buffer empty")

    def write(self, data):
        capacity = self.capacity
        if capacity > 0:
            self.data_list.append(data)
            self.capacity -= 1    # def overwrite(self, data):
        
    def overwrite(self, data):
        pass
    def clear(self):
        self.data_list = []

buf = CircularBuffer(5)
print(buf.capacity)
print(buf.write(1))
print(buf.capacity)
print(buf.write(2))
print(buf.clear())
print(buf.read())
