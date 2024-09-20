import pyautogui
from PIL import Image
import os


def get_scale_factor(base_height=1440):
    screen_width, screen_height = pyautogui.size()
    if screen_height == base_height:
        return 1
    return screen_height / base_height


def scale_image(image_path, scale_factor):
    image = Image.open(image_path)
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_image = image.resize((new_width, new_height))

    image_name = os.path.basename(image_path)
    image_name, extension = os.path.splitext(image_name)

    resized_image.save(os.path.join(f"../images/{str(pyautogui.size().height)}", f'{image_name}{extension}'))
    return resized_image


def locate_image_on_screen(image_name, scale_factor, confidence=0.7, grayscale=True):
    if scale_factor == 1:
        image_path = os.path.join("images", image_name)
    else:
        image_path = os.path.join("images", str(pyautogui.size().height), image_name)
    return pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=grayscale)


def run_image_scaling():
    scale_factor = get_scale_factor()

    resized_images_path = os.path.join('../images', str(pyautogui.size().height))

    if not os.path.exists(resized_images_path):
        os.mkdir(resized_images_path)

    if scale_factor != 1:
        for image_name in os.listdir('../images'):
            if image_name.endswith('.png'):
                image_path = os.path.join('../images', image_name)
                scale_image(image_path, scale_factor)


if __name__ == '__main__':
    run_image_scaling()
