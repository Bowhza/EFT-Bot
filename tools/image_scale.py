import pyautogui
from PIL import Image
import os


def get_scale_factor(base_height:int = 1440) -> float:
    screen_width, screen_height = pyautogui.size()
    if screen_height == base_height:
        return 1
    return screen_height / base_height


def scale_image(image_path:str, scale_factor:float):
    image = Image.open(image_path)
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_image = image.resize((new_width, new_height))

    image_name = os.path.basename(image_path)
    image_name, extension = os.path.splitext(image_name)

    resized_image.save(os.path.join(f"../images/{str(pyautogui.size().height)}", f'{image_name}{extension}'))
    return resized_image


def locate_image_on_screen(image_name:str, scale_factor:float, confidence:float = 0.7, grayscale:bool = True) -> bool:
    if scale_factor == 1:
        image_path = os.path.join("images", image_name)
    else:
        image_path = os.path.join("images", str(pyautogui.size().height), image_name)
    return pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=grayscale)


def run_image_scaling():
    scale_factor = get_scale_factor()
    print(f"Scale Factor: {scale_factor}")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)  # Go up one level to reach the main directory
    images_dir = os.path.join(parent_dir, "images")
    resized_images_path = os.path.join(images_dir, str(pyautogui.size().height))

    # If the scale factor is 1, the images are already to scale.
    if scale_factor == 1:
        input("You don't need to re-scale the images. Press 'Enter' to exit.\n")
        return
    
    # Create a directory for the images if it does not exist.
    if not os.path.exists(resized_images_path):
        os.mkdir(resized_images_path)
        print(f"Created directory: {resized_images_path}")

    # Rescale all images and save them to the created directory.
    for image_name in os.listdir("../images"):
        if image_name.endswith('.png'):
            print(f"Saving scaled image: {image_name}")
            image_path = os.path.join("../images", image_name)
            scale_image(image_path, scale_factor)

    input("Press 'Enter' to exit.")

if __name__ == '__main__':
    run_image_scaling()
