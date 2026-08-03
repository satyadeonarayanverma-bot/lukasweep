import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def draw_cartoon_rose(draw, cx, cy, radius, main_color=(255, 51, 102), light_color=(255, 128, 160), dark_color=(204, 0, 68), outline_color=(153, 0, 51)):
    # Draw leaves around rose
    leaf_color = (74, 222, 128)
    leaf_outline = (22, 101, 52)
    
    # 3 leaves at angles 45, 160, 260
    for leaf_angle in [40, 150, 250]:
        rad = math.radians(leaf_angle)
        lx = cx + math.cos(rad) * (radius * 1.1)
        ly = cy + math.sin(rad) * (radius * 1.1)
        
        # Leaf points
        p1 = (cx + math.cos(rad - 0.4) * (radius * 0.5), cy + math.sin(rad - 0.4) * (radius * 0.5))
        p2 = (cx + math.cos(rad) * (radius * 1.7), cy + math.sin(rad) * (radius * 1.7))
        p3 = (cx + math.cos(rad + 0.4) * (radius * 0.5), cy + math.sin(rad + 0.4) * (radius * 0.5))
        
        draw.polygon([p1, p2, p3], fill=leaf_color, outline=leaf_outline, width=max(2, int(radius * 0.08)))

    # Outer petal circles for cartoon rose look
    for i, angle in enumerate([0, 72, 144, 216, 288]):
        rad = math.radians(angle)
        px = cx + math.cos(rad) * (radius * 0.5)
        py = cy + math.sin(rad) * (radius * 0.5)
        pr = radius * 0.65
        draw.ellipse([px - pr, py - pr, px + pr, py + pr], fill=light_color, outline=outline_color, width=max(2, int(radius * 0.07)))

    # Middle petals
    for i, angle in enumerate([36, 108, 180, 252, 324]):
        rad = math.radians(angle)
        px = cx + math.cos(rad) * (radius * 0.35)
        py = cy + math.sin(rad) * (radius * 0.35)
        pr = radius * 0.5
        draw.ellipse([px - pr, py - pr, px + pr, py + pr], fill=main_color, outline=outline_color, width=max(2, int(radius * 0.07)))

    # Inner core spiral / concentric arches
    draw.ellipse([cx - radius*0.35, cy - radius*0.35, cx + radius*0.35, cy + radius*0.35], fill=dark_color, outline=outline_color, width=max(2, int(radius * 0.07)))
    
    # Swirl accent inside center
    draw.arc([cx - radius*0.22, cy - radius*0.22, cx + radius*0.22, cy + radius*0.22], start=0, end=240, fill=(255, 255, 255), width=max(2, int(radius * 0.08)))
    draw.arc([cx - radius*0.12, cy - radius*0.12, cx + radius*0.12, cy + radius*0.12], start=120, end=360, fill=light_color, width=max(2, int(radius * 0.07)))

def main():
    img_path = 'WhatsApp Image 2026-07-26 at 17.02.03.jpeg'
    if not os.path.exists(img_path):
        print(f"Error: {img_path} not found")
        return

    photo = Image.open(img_path).convert('RGBA')
    pw, ph = photo.size

    # Canvas dimensions
    canvas_w = max(1600, pw + 400)
    canvas_h = max(1200, ph + 400)

    # Pink background
    canvas = Image.new('RGBA', (canvas_w, canvas_h), (255, 194, 209, 255))
    
    # Draw Pink Gradient background
    gradient = Image.new('RGBA', (canvas_w, canvas_h))
    draw_g = ImageDraw.Draw(gradient)
    for y in range(canvas_h):
        r = int(255 - (y / canvas_h) * 20)
        g = int(180 - (y / canvas_h) * 40)
        b = int(205 - (y / canvas_h) * 30)
        draw_g.line([(0, y), (canvas_w, y)], fill=(r, g, b, 255))
    
    canvas = Image.alpha_composite(canvas, gradient)

    # Watermark overlay layer
    watermark_layer = Image.new('RGBA', (canvas_w * 2, canvas_h * 2), (0, 0, 0, 0))
    wm_draw = ImageDraw.Draw(watermark_layer)

    # Try loading a nice font, fallback to default if not available
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()

    text = "aqsa aqsa  🌸  aqsa  💖  "
    step_x = 280
    step_y = 70

    for y_idx, y in enumerate(range(0, canvas_h * 2, step_y)):
        offset = (y_idx % 2) * 120
        for x in range(-200, canvas_w * 2, step_x):
            wm_draw.text((x + offset, y), text, font=font, fill=(180, 20, 90, 45))

    # Rotate watermark layer
    rotated_wm = watermark_layer.rotate(20, resample=Image.BICUBIC, expand=False)
    # Crop to canvas size
    crop_x = (watermark_layer.width - canvas_w) // 2
    crop_y = (watermark_layer.height - canvas_h) // 2
    rotated_wm_cropped = rotated_wm.crop((crop_x, crop_y, crop_x + canvas_w, crop_y + canvas_h))

    canvas = Image.alpha_composite(canvas, rotated_wm_cropped)

    # Position for photo frame (centered)
    frame_padding = 24
    border_width = 8
    
    frame_w = pw + (frame_padding + border_width) * 2
    frame_h = ph + (frame_padding + border_width) * 2
    
    fx = (canvas_w - frame_w) // 2
    fy = (canvas_h - frame_h) // 2

    # Drop shadow for frame
    shadow = Image.new('RGBA', (canvas_w, canvas_h), (0,0,0,0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([fx + 10, fy + 12, fx + frame_w + 10, fy + frame_h + 12], radius=30, fill=(120, 0, 40, 70))
    shadow = shadow.filter(ImageFilter.GaussianBlur(15))
    canvas = Image.alpha_composite(canvas, shadow)

    # Main Frame rectangle
    frame_img = Image.new('RGBA', (canvas_w, canvas_h), (0,0,0,0))
    f_draw = ImageDraw.Draw(frame_img)
    
    # Outer white/cream frame
    f_draw.rounded_rectangle([fx, fy, fx + frame_w, fy + frame_h], radius=28, fill=(255, 255, 255, 245), outline=(255, 105, 180, 200), width=4)
    # Inner pink border
    f_draw.rounded_rectangle([fx + frame_padding, fy + frame_padding, fx + frame_w - frame_padding, fy + frame_h - frame_padding], radius=18, outline=(230, 50, 120, 180), width=3)

    canvas = Image.alpha_composite(canvas, frame_img)

    # Paste photo inside frame
    px = fx + frame_padding + border_width
    py = fy + frame_padding + border_width
    canvas.paste(photo, (px, py), photo)

    # Draw Cartoon Roses on Frame Corners and Sides
    overlay_draw = ImageDraw.Draw(canvas)

    # Corner 1: Top-Left
    draw_cartoon_rose(overlay_draw, fx + 15, fy + 15, radius=45, main_color=(255, 51, 119))
    draw_cartoon_rose(overlay_draw, fx + 65, fy - 10, radius=32, main_color=(255, 102, 153))
    draw_cartoon_rose(overlay_draw, fx - 10, fy + 65, radius=30, main_color=(230, 40, 90))

    # Corner 2: Top-Right
    draw_cartoon_rose(overlay_draw, fx + frame_w - 15, fy + 15, radius=45, main_color=(255, 51, 119))
    draw_cartoon_rose(overlay_draw, fx + frame_w - 65, fy - 10, radius=32, main_color=(255, 120, 170))
    draw_cartoon_rose(overlay_draw, fx + frame_w + 10, fy + 65, radius=30, main_color=(230, 40, 90))

    # Corner 3: Bottom-Left
    draw_cartoon_rose(overlay_draw, fx + 15, fy + frame_h - 15, radius=45, main_color=(255, 51, 119))
    draw_cartoon_rose(overlay_draw, fx + 65, fy + frame_h + 10, radius=32, main_color=(255, 102, 153))
    draw_cartoon_rose(overlay_draw, fx - 10, fy + frame_h - 65, radius=30, main_color=(230, 40, 90))

    # Corner 4: Bottom-Right
    draw_cartoon_rose(overlay_draw, fx + frame_w - 15, fy + frame_h - 15, radius=45, main_color=(255, 51, 119))
    draw_cartoon_rose(overlay_draw, fx + frame_w - 65, fy + frame_h + 10, radius=32, main_color=(255, 120, 170))
    draw_cartoon_rose(overlay_draw, fx + frame_w + 10, fy + frame_h - 65, radius=30, main_color=(230, 40, 90))

    # Top Center Rose Accent
    draw_cartoon_rose(overlay_draw, fx + frame_w // 2, fy - 15, radius=38, main_color=(255, 20, 100))

    # Save output image
    output_filename = "aqsa_framed_watermark.png"
    canvas.convert('RGB').save(output_filename, "PNG")
    print(f"Successfully generated {output_filename}")

if __name__ == '__main__':
    main()
