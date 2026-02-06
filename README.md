# Puneri Wada – Sinhagad Paytha Farm House

A professional static website for Puneri Wada, an authentic heritage farmhouse near Sinhagad Fort, Pune. The property serves as a premium shooting location for pre-wedding photography, advertisement films, social media content, and creative productions.

## Design Philosophy

The website design incorporates **Maratha heritage aesthetics** with modern functionality, featuring:
- **Saffron & Gold Palette**: Traditional Maratha colors (#FF9933 saffron, #C9A961 gold)
- **Decorative Diamond Motifs**: ◆ symbols throughout representing heritage elements
- **Elegant Typography**: Forum (headings) and Lora (body) serif fonts
- **Heritage Borders**: Saffron accent lines and traditional border patterns
- **Gradient Effects**: Saffron-to-gold gradients on headings and accents
- **Subtle Patterns**: Decorative overlays and corner embellishments
- **Sophisticated Animations**: Smooth transitions with heritage-inspired hover effects

## Maratha Heritage Design Elements

### Visual Identity
- **Saffron (#FF9933)**: Primary accent color representing valor and heritage
- **Maratha Gold (#C9A961)**: Secondary color for elegance and tradition
- **Earth Tones**: Browns and terracotta reflecting fort architecture
- **Diamond Motifs (◆)**: Decorative elements throughout the design
- **Gradient Overlays**: Saffron-to-gold transitions on text and borders

### Decorative Features
- Heritage corner decorations with diamond symbols
- Saffron accent borders on cards and sections
- Traditional border patterns with gradient effects
- Decorative dividers with centered diamond motifs
- Subtle background patterns inspired by traditional textiles

### Interactive Elements
- Saffron glow effects on hover
- Border animations revealing heritage colors
- Smooth scale and translate transitions
- Gradient text effects on headings
- Shadow effects with saffron tones

## About the Property

Puneri Wada is an authentic old Maharashtrian farmhouse featuring:
- Traditional Puneri architecture with wooden pillars and carved doors
- Central chowk (courtyard) with traditional stone flooring
- Multiple interior and exterior shooting locations
- Scenic rural surroundings with views of Sinhagad Fort
- Versatile spaces suitable for various types of creative productions

## Website Features

- **Responsive Design**: Fully responsive across all devices (desktop, tablet, mobile)
- **Modern UI/UX**: Heritage-inspired design with contemporary functionality
- **Smooth Animations**: Scroll-reveal effects, hover transitions, and interactive elements
- **Multiple Pages**:
  - **Home** - Hero slider with elegant overlay and call-to-action
  - **About Puneri Wada** - Heritage story and location details
  - **Our Old Project** - Portfolio of past shoots and productions
  - **Facilities** - Detailed information about shooting spaces and amenities
  - **Gallery** - Photo collection with category filtering
  - **Contact Us** - Contact form and location information

## Design Features

### Color Scheme (Maratha Heritage)
- **Saffron**: `#FF9933` (Primary accent - valor and heritage)
- **Deep Saffron**: `#D97706` (Primary color)
- **Maratha Gold**: `#C9A961` (Secondary accent - elegance)
- **Royal Gold**: `#B8860B` (Secondary color)
- **Fort Stone**: `#8B7355` (Neutral tone)
- **Earth Brown**: `#6B4423` (Heritage brown)
- **Dark Wood**: `#3E2723` (Deep brown)
- **Terracotta**: `#C1440E` (Accent red-orange)
- **Cream Background**: `#FAF8F3` (Light background)

### Maratha Design Patterns
- **Diamond Motifs (◆)**: Used throughout as decorative elements
- **Saffron Borders**: 3-4px accent lines on cards and sections
- **Gradient Effects**: Saffron-to-gold transitions
- **Heritage Corners**: Decorative diamond symbols in corners
- **Traditional Dividers**: Gradient lines with centered diamonds

### Typography
- **Headings**: Forum (serif) - Elegant, uppercase with letter-spacing
- **Body**: Lora (serif) - Readable, classic serif font
- **Font Sizes**: Responsive using clamp() for fluid typography

### Layout Principles
- Maximum width: 1320px with responsive breakpoints
- Generous spacing using CSS custom properties
- Grid-based layouts for flexibility
- Consistent padding and margins throughout

### Interactive Elements
- Hover effects with smooth transitions
- Scroll-reveal animations for content
- Image zoom effects on hover
- Sticky header with scroll detection
- Mobile-friendly hamburger menu

## Technology Stack

- **HTML5**: Semantic markup with accessibility in mind
- **CSS3**: Modern features including:
  - CSS Custom Properties (variables)
  - CSS Grid and Flexbox
  - Smooth animations and transitions
  - Responsive design with media queries
- **JavaScript**: Vanilla JS for:
  - Hero slider functionality
  - Mobile menu toggle
  - Gallery filtering
  - Scroll animations
  - Form handling

## File Structure

```
puneri-wada/
├── index.html          # Home page
├── about.html          # About page
├── project.html        # Projects portfolio
├── facilities.html     # Facilities information
├── gallery.html        # Photo gallery
├── contact.html        # Contact page
├── css/
│   └── style.css       # Main stylesheet (refined heritage design)
├── js/
│   └── script.js       # Main JavaScript file
├── images/             # Image assets (to be added)
└── README.md           # This file
```

## Setup Instructions

1. **Clone or download** this repository
2. **Add images** to the `images/` folder with the following naming convention:
   - Hero images: `hero-1.jpg`, `hero-2.jpg`, `hero-3.jpg`
   - Page headers: `about-header.jpg`, `facilities-header.jpg`, etc.
   - Gallery images: `gallery-1.jpg`, `gallery-2.jpg`, etc.
   - Project images: `project-1.jpg`, `project-2.jpg`, etc.
   - Facility images: `facility-courtyard.jpg`, `facility-wooden.jpg`, etc.
3. **Update contact information** in `contact.html`:
   - Replace `[PHONE_NUMBER]` with actual phone number
   - Replace `[EMAIL]` with actual email address
4. **Open `index.html`** in a web browser to view the website

## Image Requirements

For best results, use images with the following specifications:
- **Hero images**: 1920x1080px (16:9 landscape)
- **Page headers**: 1920x600px (wide landscape)
- **Gallery images**: 800x600px (4:3 aspect ratio)
- **Project images**: 800x600px (4:3 aspect ratio)
- **Facility images**: 800x600px (4:3 aspect ratio)

All images should be optimized for web (compressed to reduce file size while maintaining quality).

### Image Optimization Tips
- Use JPEG format for photographs
- Compress images to under 200KB each
- Maintain aspect ratios for consistent layout
- Use descriptive alt text for accessibility

## Customization

### Colors
Edit CSS variables in `css/style.css` to customize the Maratha heritage theme:
```css
:root {
    /* Maratha-inspired Colors */
    --saffron: #FF9933;
    --deep-saffron: #D97706;
    --maratha-gold: #C9A961;
    --royal-gold: #B8860B;
    --fort-stone: #8B7355;
    --earth-brown: #6B4423;
    --dark-wood: #3E2723;
    --terracotta: #C1440E;
    /* ... */
}
```

### Maratha Design Elements
The design includes several utility classes for Maratha heritage styling:
- `.maratha-gold-text` - Gradient text effect
- `.heritage-corner` - Corner diamond decorations
- `.traditional-border` - Heritage border pattern
- `.saffron-glow` - Saffron shadow effect
- `.heritage-divider` - Decorative section divider
- `.maratha-card` - Heritage-styled card component

### Fonts
The website uses Google Fonts (Forum and Lora). To change fonts:
1. Update the Google Fonts link in HTML files
2. Modify CSS variables:
```css
:root {
    --font-primary: 'Your-Heading-Font', serif;
    --font-secondary: 'Your-Body-Font', serif;
}
```

### Spacing
Adjust spacing throughout the site using CSS custom properties:
```css
:root {
    --spacing-xs: 8px;
    --spacing-sm: 16px;
    --spacing-md: 24px;
    --spacing-lg: 40px;
    --spacing-xl: 60px;
    --spacing-xxl: 80px;
}
```

### Content
All text content can be edited directly in the HTML files. Each page is well-structured with semantic HTML for easy content updates.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Optimization

- Minify CSS and JavaScript for production
- Optimize and compress all images
- Enable browser caching
- Consider using a CDN for assets
- Implement lazy loading for images below the fold

## Accessibility Features

- Semantic HTML5 elements
- ARIA labels for interactive elements
- Keyboard navigation support
- Sufficient color contrast ratios
- Responsive text sizing
- Alt text for images (to be added)

## Contact Information

**Puneri Wada Sinhagad Paytha Farm House**  
Sinhagad Fort Paytha Yaa, Golewadi  
Ghera Sinhagad, Pune – 411025  
Maharashtra, India

## License

© 2026 Puneri Wada. All rights reserved.

---

## Development Notes

### Design Inspiration
The UI design incorporates **Maratha heritage elements**, featuring:
- **Saffron & Gold**: Traditional Maratha colors throughout
- **Diamond Motifs (◆)**: Decorative symbols representing heritage
- **Elegant serif typography**: Classic and timeless
- **Heritage borders**: Saffron accent lines and traditional patterns
- **Gradient effects**: Smooth saffron-to-gold transitions
- **Subtle animations**: Respectful of heritage while modern
- **Clean aesthetic**: Heritage touches without overwhelming

### Maratha Heritage Features
- **Color Symbolism**: Saffron represents valor, gold represents prosperity
- **Decorative Patterns**: Diamond motifs used as traditional embellishments
- **Border Styles**: Saffron accent borders inspired by fort architecture
- **Typography**: Uppercase headings with letter-spacing for regal appearance
- **Gradients**: Saffron-to-gold transitions on headings and interactive elements
- **Hover Effects**: Saffron glow and border animations
- **Corner Decorations**: Diamond symbols in strategic positions

### Future Enhancements
- Add backend integration for contact form
- Implement image lightbox/gallery viewer
- Add booking calendar system
- Integrate Google Maps for location
- Add testimonials carousel
- Implement SEO optimization
- Add social media integration

**Note**: This is a static website. For dynamic features like form submissions, you'll need to integrate with a backend service or use third-party form handling services like Formspree, Netlify Forms, or similar.
