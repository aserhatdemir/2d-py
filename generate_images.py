from PIL import Image, ImageDraw

def create_rock_image():
    img = Image.new('RGBA', (40, 40), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse((5, 5, 35, 35), fill=(128, 128, 128))  # Gray circle
    img.save('assets/rock.png')

def create_paper_image():
    img = Image.new('RGBA', (40, 40), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle((10, 5, 30, 35), fill=(255, 255, 0))  # Yellow rectangle
    img.save('assets/paper.png')

def create_scissors_image():
    img = Image.new('RGBA', (40, 40), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # Draw an 'X' shape to represent scissors
    draw.line((10, 10, 30, 30), fill=(255, 0, 0), width=3)
    draw.line((30, 10, 10, 30), fill=(255, 0, 0), width=3)
    img.save('assets/scissors.png')

if __name__ == "__main__":
    create_rock_image()
    create_paper_image()
    create_scissors_image()
    print("Images have been created in the 'assets' directory.")