import os
import base64
import uuid
from datetime import datetime


def save_image_from_base64(base64_string, directory):
    try:

        image_data = base64.b64decode(base64_string)

        if not os.path.exists(directory):
            os.makedirs(directory)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{timestamp}_{str(uuid.uuid4())[:8]}.jpg"

        file_path = os.path.join(directory, unique_filename)

        with open(file_path, 'wb') as f:
            f.write(image_data)

        print(f"Изображение сохранено в {file_path}")
        return file_path
    except Exception as e:
        print(f"Ошибка при сохранении изображения: {e}")
        return None