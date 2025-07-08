#!/usr/bin/env python3
"""
Create a background image for the DMG installer
"""

from PIL import Image, ImageDraw, ImageFont

def create_background():
    # Create a 540x380 background (DMG window size)
    width, height = 540, 380
    img = Image.new('RGBA', (width, height), (240, 242, 246, 255))  # Light gray background
    
    draw = ImageDraw.Draw(img)
    
    # Draw a simple design
    # Header
    draw.rectangle([0, 0, width, 80], fill=(255, 107, 107, 255))
    
    # Title text
    try:
        # Try to use a system font
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    except:
        font = ImageFont.load_default()
    
    draw.text((width//2, 40), "Archive Producer", fill='white', anchor='mm', font=font)
    draw.text((width//2, 65), "Batch Renamer", fill='white', anchor='mm', font=font)
    
    # Instructions
    instruction_font = ImageFont.load_default()
    instructions = [
        "Drag the Archive Producer Batch Renamer",
        "to your Applications folder to install."
    ]
    
    y_pos = 120
    for instruction in instructions:
        draw.text((width//2, y_pos), instruction, fill='black', anchor='mm', font=instruction_font)
        y_pos += 25
    
    # Save the background
    img.save('background.png')
    print("✅ Background image created successfully!")

if __name__ == "__main__":
    create_background() 