# photoRecover
.png and .jpg file recover for image00.vol

## Description

```python
def read_vol_file(filename)
```

This function reads a binary volume file:

- Takes a filename as input
- Opens the file in binary read mode ('rb')
- Returns the entire file content as bytes
- Includes error handling for missing files and other exceptions
- Returns None if any errors occur

```python
def recover_png(data)
```
This function recovers PNG files from binary data:

- Searches for PNG signature (\x89PNG\r\n\x1a\n)
- Locates each PNG file's end by finding the 'IEND' chunk
- Extracts complete PNG files including headers and footers
- Saves each recovered PNG with incremental naming (recovered_0.png, etc.)
- Returns the total number of PNG files recovered
```python
def recover_jpg(data)
```
This function recovers JPG files from binary data:

- Looks for JPG signature (\xff\xd8\xff)
- Finds corresponding end markers (\xff\xd9)
- Extracts complete JPG files between markers
- Saves each recovered JPG with incremental naming (recovered_0.jpg, etc.)
- Returns the total number of JPG files recovered

## Main Execution Block
The main execution block:
```python
if __name__ == "__main__":
```
- Reads the volume file (image00.vol)
- Recovers both PNG and JPG files
- Creates an img directory
- Moves all recovered files to the img directory
- Prints status messages about recovery process

This code is designed for digital forensics or file recovery scenarios where image files need to be extracted from a volume file.
