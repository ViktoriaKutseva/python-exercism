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

    def read(self):
        if self.data_list:
            data_list_instance = self.data_list
            return data_list_instance.pop(0)
        else:
            raise BufferEmptyException("Circular buffer is empty")

    def write(self, data):
        if len(self.data_list) < self.capacity:
            self.data_list.append(data)
            print(len(self.data_list))
        else:
            raise BufferFullException("Circular buffer is full")

    def overwrite(self, data):
        if len(self.data_list) == self.capacity:
            self.data_list.pop(0)
            self.data_list.append(data)
        else:
            self.data_list.append(data)

    def clear(self):
        self.data_list = []