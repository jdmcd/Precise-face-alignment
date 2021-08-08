import os 

directory = r'images'
image_paths = []
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_paths.append(os.path.join(directory, filename))
    else:
        continue

counter = 0
for image in image_paths:
    counter += 1
    print(f'Processing {image} ({counter} of {len(image_paths)})')
    name = image.split('/')[1]
    output_path = f'output/{name}'
    os.system(f'python3 run.py --mode 1 --path_to_load=\'{image}\' --path_to_save=\'{output_path}\'')