
# GradientColor

A simple Python utility to **generate color gradients** using the Python Imaging Library (PIL).

---

## Features

- Create smooth linear color gradients between two colors
- Output the gradient as an image (PNG, JPEG, etc.)
- Easily customizable gradient size and colors
- Lightweight and minimal dependencies (Pillow)

---

## Installation

Make sure you have Python installed (version 3.x).

Install the required dependency Pillow:

```
pip install pillow
```

---

## Usage

The main script uses PIL to create a horizontal gradient image from a start color to an end color.

Example usage:

```
from PIL import Image

def generate_gradient(width, height, start_color, end_color):
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for x in range(width):
        factor = x / (width - 1)
        r = int(start_color + (end_color - start_color) * factor)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * factor)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * factor)
        for y in range(height):
            pixels[x, y] = (r, g, b)

    return img

if __name__ == "__main__":
    width, height = 500, 100
    start_color = (255, 0, 0)  # Red
    end_color = (0, 0, 255)    # Blue

    gradient_image = generate_gradient(width, height, start_color, end_color)
    gradient_image.show()  # Display the generated gradient
    # gradient_image.save("gradient.png")  # Optionally save to file
```

---

## How to Contribute

Feel free to open issues or submit pull requests. Suggestions for adding vertical gradients, radial gradients, or supporting more color formats are welcome.

---

## License

This project is licensed under the MIT License.

---

