import os
from PIL import Image

def convert_images_to_jpg(directory):
    # Loop through all files in the given directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip if it's not a file
        if not os.path.isfile(filepath):
            continue

        try:
            with Image.open(filepath) as img:
                # Build new filename with .jpg extension
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_filepath = os.path.join(directory, new_filename)

                # Convert and save as JPG
                rgb_img = img.convert("RGB")
                rgb_img.save(new_filepath, "JPEG")

                print(f"Converted: {filename} -> {new_filename}")

            # Delete the original file after successful conversion
            os.remove(filepath)
            print(f"Deleted original: {filename}")

        except Exception as e:
            print(f"Skipping {filename}: {e}")

if __name__ == "__main__":
    # Change '.' to your target directory path
    target_directory = "."
    convert_images_to_jpg(target_directory)
