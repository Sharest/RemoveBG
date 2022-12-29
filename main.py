from rembg import remove
from PIL import Image
from pathlib import Path


def remove_bg():
    list_of_extensions = ['*.png','*.jpg']
    all_files = []

    for ext in list_of_extensions:
        all_files.extend(Path('D:\ReposVSCode\Python\RemoveBG\in_img').glob(ext))

    # print(all_files)

    for item in all_files:
        input_path = Path(item)
        file_name = input_path.stem

        output_path = f'D:\ReposVSCode\Python\RemoveBG\out_img\{file_name}_output.png'

        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)


def main():
    remove_bg()

if __name__ == '__main__':
    main()
