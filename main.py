import os

def read_vol_file(filename):
    try:
        with open(filename, 'rb') as file:
            # Read the entire file as bytes
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def recover_png(data):
    png_signature = b'\x89PNG\r\n\x1a\n'
    png_files = []
    current_position = 0
    
    while True:
        # Find next PNG signature
        position = data.find(png_signature, current_position)
        if position == -1:
            break
            
        # Find IEND chunk which marks the end of PNG
        current_position = position
        while current_position < len(data):
            if data[current_position:current_position+4] == b'IEND':
                # Add 8 bytes for CRC and chunk length
                current_position += 8
                png_files.append(data[position:current_position])
                break
            current_position += 1
            
        current_position = position + 1
        
    # Save recovered files
    for i, png_data in enumerate(png_files):
        with open(f'recovered_{i}.png', 'wb') as f:
            f.write(png_data)
            
    return len(png_files)

def recover_jpg(data):
    jpg_signature = b'\xff\xd8\xff'
    jpg_end = b'\xff\xd9'
    jpg_files = []
    current_position = 0
    
    while True:
        # Find next JPG signature
        position = data.find(jpg_signature, current_position)
        if position == -1:
            break
            
        # Find end of JPG
        end_position = data.find(jpg_end, position)
        if end_position == -1:
            break
            
        # Add 2 bytes to include the end marker
        jpg_files.append(data[position:end_position + 2])
        current_position = position + 1
        
    # Save recovered files
    for i, jpg_data in enumerate(jpg_files):
        with open(f'recovered_{i}.jpg', 'wb') as f:
            f.write(jpg_data)
            
    return len(jpg_files)

if __name__ == "__main__":
    # Specify the path to your .vol file
    vol_file = "image00.vol"
    
    # Read the file
    vol_data = read_vol_file(vol_file)
    
    if vol_data:
        print(f"Successfully read {len(vol_data)} bytes from {vol_file}")
    # Recover PNG files
    num_png = recover_png(vol_data)
    print(f"Recovered {num_png} PNG files")
    
    # Recover JPG files
    num_jpg = recover_jpg(vol_data)
    print(f"Recovered {num_jpg} JPG files")
    # Create 'img' directory if it doesn't exist
    os.makedirs('img', exist_ok=True)
    
    # Move recovered files to img directory
    for ext in ['png', 'jpg']:
        for i in range(max(num_png, num_jpg)):
            old_path = f'recovered_{i}.{ext}'
            if os.path.exists(old_path):
                new_path = os.path.join('img', f'recovered_{i}.{ext}')
                os.rename(old_path, new_path)
