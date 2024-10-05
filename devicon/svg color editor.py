import os
import re
import shutil

def is_hex_color(value):
    return re.fullmatch(r'^#([0-9A-Fa-f]{3}){1,2}$', value) is not None

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def process_svg_files(hex_color):
    source_folder = 'sources'
    destination_folder = hex_color

    create_folder_if_not_exists(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith('.svg'):
            with open(os.path.join(source_folder, filename), 'r') as file:
                content = file.read()

            # Replace existing fill attributes
            content = re.sub(r'fill="#[0-9A-Fa-f]{3,6}"', f'fill="{hex_color}"', content)

            # Add fill attribute to <svg> tag if not present
            if 'fill="' not in content:
                content = content.replace('<svg', f'<svg fill="{hex_color}"')

            # Write modified content to new file in the destination folder
            with open(os.path.join(destination_folder, filename), 'w') as file:
                file.write(content)

def clear_and_copy_files(destination_folder):
    static_svg_folder = 'static/svg'

    # Remove all contents inside static/svg/ folder
    if os.path.exists(static_svg_folder):
        shutil.rmtree(static_svg_folder)
    
    # Create static/svg/ folder if it doesn't exist
    os.makedirs(static_svg_folder, exist_ok=True)

    # Copy all files from the destination folder to static/svg/ folder
    for filename in os.listdir(destination_folder):
        shutil.copy(os.path.join(destination_folder, filename), static_svg_folder)

def main():
    hex_color = input("Enter a hexadecimal color (e.g., #1572B6 or #333): ")

    if is_hex_color(hex_color):
        process_svg_files(hex_color)
        clear_and_copy_files(hex_color)
        print(f"SVG files have been processed and saved in the folder '{hex_color}', n\and copied to 'static/svg/'.")
    else:
        print("Invalid hexadecimal color value.")

if __name__ == "__main__":
    main()
