
class CameraBufferImplementation:
    """
    A basic implementation of the Ring-Buffer to store the frames that are yielded by the camera instance
    """
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.index = 0

    def write_frames(self, data):
        self.buffer[self.index] = data
        self.index = (self.index + 1) % self.size

    def read_frames(self):
        return [frame for frame in self.buffer if frame is not None]



