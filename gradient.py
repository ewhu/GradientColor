from PIL import Image

def generate_gradient(width, height, start_color, end_color):
    # Create a new blank image
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for x in range(width):
        # Calculate the interpolation factor (0 to 1)
        factor = x / (width - 1)
        # Linearly interpolate each RGB channel
        r = int(start_color[0] + (end_color[0] - start_color[0]) * factor)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * factor)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * factor)

        for y in range(height):
            pixels[x, y] = (r, g, b)

    return img

if __name__ == "__main__":
    width, height = 500, 100
    start_color = (255, 0, 0)    # Red
    end_color = (0, 0, 255)      # Blue

    gradient_img = generate_gradient(width, height, start_color, end_color)
    gradient_img.show()  # Displays the gradient image
    # gradient_img.save("gradient.png")  # Optional: save the image to a file
