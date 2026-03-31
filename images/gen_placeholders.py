"""
Generates dummy JPG placeholder images for Puneri Wada website.
Replace any file here with your actual image - same filename.
"""

import struct, zlib, os

def make_png(width, height, r, g, b, label):
    """Create a minimal PNG with a solid color and label baked in as raw pixels."""
    # We'll create a simple solid-color PNG (no text, pure color block)
    # For labeled placeholders we use a simple approach: solid color PNG
    def png_chunk(chunk_type, data):
        c = chunk_type + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

    # IHDR
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr = png_chunk(b'IHDR', ihdr_data)

    # Image data: solid color rows
    raw_rows = b''
    row = b'\x00' + bytes([r, g, b] * width)
    raw_rows = row * height
    compressed = zlib.compress(raw_rows)
    idat = png_chunk(b'IDAT', compressed)

    iend = png_chunk(b'IEND', b'')

    signature = b'\x89PNG\r\n\x1a\n'
    return signature + ihdr + idat + iend


def make_placeholder_jpg(path, width, height, label):
    """
    Creates a placeholder image as PNG saved with .jpg extension.
    Uses a warm earthy tone matching Puneri Wada theme.
    Browsers accept PNG data regardless of .jpg extension for <img> tags.
    """
    # Warm earthy brown/tan color
    r, g, b = 200, 184, 154
    data = make_png(width, height, r, g, b, label)
    with open(path, 'wb') as f:
        f.write(data)


images = [
    # Hero slides
    ('hero-1.jpg',              'Hero Slide 1',              1200, 600),
    ('hero-2.jpg',              'Traditional Chowk',         1200, 600),
    ('hero-3.jpg',              'Pre-wedding Location',      1200, 600),
    # Index
    ('wada-main.jpg',           'Wada Main Building',        800,  500),
    ('gallery-1.jpg',           'Traditional Courtyard',     600,  400),
    ('gallery-2.jpg',           'Wooden Architecture',       600,  400),
    ('gallery-3.jpg',           'Pre-Wedding Shoot',         600,  400),
    ('gallery-4.jpg',           'Rural Surroundings',        600,  400),
    # About
    ('about-header.jpg',        'About Header',              1200, 400),
    ('about-wada.jpg',          'Wada Architecture',         600,  450),
    ('about-location.jpg',      'Sinhagad Location',         600,  450),
    ('about-shoots.jpg',        'Shooting Location',         600,  450),
    # Gallery page
    ('gallery-header.jpg',      'Gallery Header',            1200, 400),
    ('gallery-arch-1.jpg',      'Wooden Pillars',            600,  400),
    ('gallery-arch-2.jpg',      'Carved Doors',              600,  400),
    ('gallery-arch-3.jpg',      'Stone Walls',               600,  400),
    ('gallery-arch-4.jpg',      'Wooden Beams',              600,  400),
    ('gallery-arch-5.jpg',      'Traditional Entrance',      600,  400),
    ('gallery-court-1.jpg',     'Central Chowk',             600,  400),
    ('gallery-court-2.jpg',     'Courtyard Above',           600,  400),
    ('gallery-court-3.jpg',     'Evening Courtyard',         600,  400),
    ('gallery-court-4.jpg',     'Courtyard Details',         600,  400),
    ('gallery-shoot-1.jpg',     'Pre-Wedding Photography',   600,  400),
    ('gallery-shoot-2.jpg',     'Advertisement Shoot',       600,  400),
    ('gallery-shoot-3.jpg',     'Fashion Photography',       600,  400),
    ('gallery-shoot-4.jpg',     'Video Production',          600,  400),
    ('gallery-surr-1.jpg',      'Rural Landscape',           600,  400),
    ('gallery-surr-2.jpg',      'Sinhagad Fort View',        600,  400),
    ('gallery-surr-3.jpg',      'Surrounding Farmland',      600,  400),
    # Facilities
    ('facilities-header.jpg',   'Facilities Header',         1200, 400),
    ('facility-courtyard.jpg',  'Traditional Courtyard',     600,  400),
    ('facility-wooden.jpg',     'Wooden Architecture',       600,  400),
    ('facility-rooms.jpg',      'Interior Spaces',           600,  400),
    ('facility-outdoor.jpg',    'Outdoor Areas',             600,  400),
    ('facility-terrace.jpg',    'Terrace Views',             600,  400),
    ('facility-parking.jpg',    'Parking Area',              600,  400),
    # Contact
    ('contact-header.jpg',      'Contact Header',            1200, 400),
    # Projects
    ('project-header.jpg',      'Projects Header',           1200, 400),
    ('project-1.jpg',           'Pre-Wedding Shoot',         600,  400),
    ('project-2.jpg',           'Advertisement Film',        600,  400),
    ('project-3.jpg',           'Fashion Shoot',             600,  400),
    ('project-4.jpg',           'Music Video',               600,  400),
    ('project-5.jpg',           'Social Media Content',      600,  400),
    ('project-6.jpg',           'Short Film',                600,  400),
]

out_dir = os.path.dirname(os.path.abspath(__file__))
created = 0

for filename, label, w, h in images:
    path = os.path.join(out_dir, filename)
    make_placeholder_jpg(path, w, h, label)
    print(f'  created: {filename}  ({w}x{h})')
    created += 1

print(f'\nDone. {created} placeholder images created in: {out_dir}')
print('Replace any file with your actual image using the SAME filename.')
