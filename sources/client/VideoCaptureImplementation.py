import io

from picamera import PiCamera
from sources.client import InitializeCustomLogger


class VideoCaptureImplementation:
    """
    This class is responsible for Video Recording & Streaming. You send in the camera object
    """
    def __init__(self, buffer_class):
        # Setup Camera
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 30
        self.camera.hflip = True

        # Configure Circular-Buffer Size
        self.circular_buffer = buffer_class

        # Setup Logger
        self.logger = InitializeCustomLogger(__class__.__name__)

    def start_recording(self):
        self.logger.info(f'Starting Camera - {self.camera}')
        self.camera.start_recording(self.circular_buffer, format='h264')

    def stop_recording(self):
        self.logger.info(f'Stopping Camera - {self.camera}')
        self.camera.stop_recording()

    def get_current_frames(self):
        return self.circular_buffer.read_frames()

    # def video_stream(self):
    #     # Instantiate Pi-Camera
    #     # Init it here & not in the constructor (Unless you can make the code reuse the same instance).
    #     # self.camera.start_preview()
    #     with PiCamera() as camera:
    #         self.logger.info(f'Starting Camera - {camera}')
    #         camera.resolution = (640, 480)
    #         camera.framerate = 30
    #         camera.hflip = True
    #
    #         # You can choose to ignore this command as this will not have an impact on streaming
    #         camera.start_preview()
    #         try:
    #             stream = io.BytesIO()
    #             for frame in camera.capture_continuous(stream, format='jpeg', use_video_port=True,
    #                                                    resize=camera.resolution):
    #                 stream.seek(0)
    #                 yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n'
    #                 stream.seek(0)
    #                 stream.truncate()
    #         except (TypeError, AttributeError):
    #             raise TypeError
    #         finally:
    #             camera.stop_preview()
