import os
from google.cloud import vision

class ImageTextDetector:
    def __init__(self, credential_path):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path
        self.vision_client = vision.ImageAnnotatorClient()

    def detect_text(self, image_path):
        with open(image_path, 'rb') as file:
            image_content = file.read()
        image = vision.Image(content=image_content)
        response = self.vision_client.text_detection(image=image)
        if response.error.message:
            raise Exception(f'{response.error.message}')
        if response.text_annotations:
            return response.text_annotations[0].description
        return ''
