#!/usr/bin/env python3
"""
Create a simple icon for the Archive Producer Batch Renamer app
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    # Create a 512x512 image with a music-themed background
    size = 512
    img = Image.new('RGBA', (size, size), (255, 107, 107, 255))  # Red background
    
    draw = ImageDraw.Draw(img)
    
    # Draw a simple music note symbol
    # Note head
    draw.ellipse([200, 300, 280, 380], fill='white', outline='white', width=3)
    
    # Note stem
    draw.rectangle([270, 200, 280, 380], fill='white')
    
    # Note flag
    draw.ellipse([280, 200, 350, 250], fill='white', outline='white', width=3)
    
    # Save as PNG
    img.save('icon.png')
    
    # Create different sizes for different platforms
    sizes = {
        'icon.ico': [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
        'icon.icns': [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256), (512, 512)]
    }
    
    for filename, size_list in sizes.items():
        if filename == 'icon.ico':
            # For Windows ICO
            img.save(filename, format='ICO', sizes=size_list)
        elif filename == 'icon.icns':
            # For macOS ICNS (simplified - just save as PNG for now)
            img.save(filename.replace('.icns', '.png'), format='PNG')

if __name__ == "__main__":
    create_icon()
    print("✅ Icons created successfully!") 