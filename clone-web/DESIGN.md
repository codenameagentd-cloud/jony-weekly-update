# DESIGN.md — olhalazarieva.com Clone Spec

## Tech Stack
- React (CRA build)
- Lenis smooth scroll (`.scroll-container` with `overflow: hidden auto`)
- GSAP (bundled, scroll-triggered animations)
- Single-page app, section-based scroll

## Typography

| Role | Font | Weight | Size | Color |
|------|------|--------|------|-------|
| Primary / Display | Sofia Sans Condensed | 400–700 | Variable (hero ~full-width, section titles ~80px) | `#101010` (light bg), `#F7F7F7` (dark bg) |
| Mono / Nav / Body | Spline Sans Mono | 300–400 | 13–14px (nav), 36px (pull quotes) | `#AAAAAA` (secondary text) |

**Letter spacing:** Nav links use `~0.56px` letter-spacing with each character in its own `<span>` for per-letter animation.

**Nav format:** `[ A B O U T  M E ]` — characters spaced individually inside brackets.

## Color Palette

| Token | Value | Usage |
|-------|-------|-------|
| bg-light | `#F7F7F7` | Page background, light sections |
| bg-dark | `#101010` | About section, Works gallery, dark zones |
| text-primary | `#101010` | Headings on light bg |
| text-inverse | `#F7F7F7` | Text on dark bg |
| text-muted | `#AAAAAA` | Secondary text, quotes on dark bg |
| accent | none | No accent color — purely monochrome |

## Page Structure (top to bottom)

### 1. Header (sticky)
- Left: Name logo "OLHA LAZARIEVA" — Sofia Sans Condensed, bold, stacked two lines
- Center: Nav links in brackets — Spline Sans Mono, 13px
- Right: "CONTACT ME ↗" button
- Background transitions from transparent to solid based on scroll section

### 2. Hero Section (~100vh, light bg)
- **Counter animation**: Number ticker cycling 0–9 with vertical slide, comma-separated — top-left
- **"CREATIVE DESIGNER"**: Full-width display text, Sofia Sans Condensed, black, bold — takes entire width
- **Portrait photo**: B&W, positioned center-right, overlapping the display text
- **Specialties**: Left-aligned under photo — "/ ART DIRECTION", "/ WEB DESIGN (UX/UI)", "/ WEB DEVELOPMENT" — bold mono
- **Tagline**: Centered mono text — "I'M EXPERIENCED WEB AND UX/UI DESIGNER..."
- **"BASED IN UKRAINE"**: Spaced letters, right-aligned
- **Bottom-left**: "AVAILABLE FOR COLLABORATION" + email link with arrow icon
- **Bottom-right**: "RECENT WORK" + project name "MAX MILKIN" in large serif

### 3. About Section (dark bg, `#101010`)
- **Section title**: "ABOUT ME" — spaced letters, large display
- **Stats badge**: Small mono label "2/5 for me dsgn/2" — top-left decorative
- **Portrait**: Same B&W photo, centered
- **"Hello! I'm Olha Lazarieva"**: Centered greeting, mono
- **Sub-sections**: "MY EXPERIENCE ↘", "MY PHILOSOPHY ↘", "MY LIFESTYLE ↘" — each with expanding body text
- **Pull quote**: "IT'S NOT JUST A PROFESSION — IT'S A WAY OF THINKING." — Spline Sans Mono, 36px, weight 300, `#AAAAAA`
- **Scroll-triggered text animation**: Large scattered rotating letters that compose on scroll (the transition screenshot at scroll ~1500)

### 4. Works / Gallery (dark bg, pinned 3D scene)
- **Section title**: "RECENT WORKS" — large display
- **3D gallery room**: Dark room with ceiling lamp, framed project screenshots on wall, cylindrical objects on floor
- **This is the most complex section** — appears to be a Three.js or CSS 3D perspective scene
- **"Swipe slider"** indicator and **"[ VIEW CASE ]"** link at bottom
- **Pinned during scroll** — takes ~3000px of scroll distance while viewport stays fixed

### 5. Services Section (light bg)
- **Section title**: "SERVICES" — spaced letters + "dsgn/4" decorative label
- **5 accordion cards** stacked vertically:
  1. "00-1 Web Design" — hover reveals image + bullet list
  2. "00-2 UX/UI Design"
  3. "00-3 Creative Design"
  4. "00-4 Product and App Design"
  5. "00-5 Development"
- Each card: number prefix, title, "// title" alternate heading, bullet list with "/" prefix, hover image, description paragraph

### 6. Awards Section (light bg)
- **Section title**: "AWARDS" — spaced letters + "dsgn/5"
- **Intro text**: "My expertise is confirmed by many international recognitions"
- **Award list** (horizontal scrolling cards with count badges):
  - Awwwards (7), Muzli (3), CSS Design Award (4), GSAP (2), FWA (1), WD Awards (2), Behance (1)
- **Codrops article mention** at bottom

### 7. Contact Section (light bg)
- **"Let's start the conversation"** — small heading
- **"Great design starts with great collaboration"** — large spaced-letter display
- **Form fields**: Name, Phone, Email, "How can I help you"
- **Budget radio**: `[ 5k-10k ]` `[ 10k-20k ]` `[ more ]` — bracket-wrapped
- **Submit button**: "Discuss the project ↗"

### 8. Footer (light bg)
- **Contact info**: Phone, email
- **Social links**: Instagram, Telegram, Facebook — with arrow icons
- **Nav repeat**: About Me, Services, Works
- **Address**: Physical address
- **Portfolio links**: Dribbble, Behance, LinkedIn — bracket format
- **Large name**: "O L H A  L A Z A R I E V A" — massive spaced display text
- **Timezone**: City + live clock
- **Credits**: "development — MM Max Milkin"
- **Copyright**: 2025

## Motion & Animation Spec

### Global
- **Lenis smooth scroll** — entire page in `.scroll-container`
- **Custom cursor** — likely hidden default, replaced with custom

### Hero
- **Number counter**: Vertical digit slide — numbers 0–9 stacked, translateY animated
- **"CREATIVE DESIGNER"**: Fade/slide in on load
- **Staggered letter reveals**: Each character fades in sequentially

### About Transition
- **Scattered letter composition**: On scroll from hero → about, large letters appear scattered and rotated, then compose into readable text. Uses per-character transforms (rotate, translate, scale) driven by scroll progress. Very dramatic effect.

### Works Gallery
- **3D perspective room**: CSS `perspective` or Three.js scene
- **Parallax layers**: Lamp, frame, floor objects move at different rates
- **Pinned scroll**: Section stays fixed while scroll drives animation progress
- **Swipe interaction**: Horizontal swipe to navigate between projects

### Services
- **Accordion expand**: Smooth height transition on card open
- **Image reveal on hover**: Image slides in from side on card hover

### Nav Links
- **Per-letter flip on hover**: Each character rotates individually on Y-axis

### Section Transitions
- **Background color shift**: Smooth transition from light (#F7F7F7) → dark (#101010) and back

## Spacing Principles
- Large whitespace between sections (~100–200px)
- Generous internal padding (~40–80px)
- Full-width display text with tight leading
- Mono text has relaxed line-height (~1.6)

## Rebuild Priority (for Jarvis)

1. **Header + Nav** — sticky, bracket format, letter animation
2. **Hero** — counter, display text, photo overlay, layout
3. **About** — dark section, scattered letter transition, sub-sections
4. **Services** — accordion with hover images
5. **Awards** — horizontal scroll cards
6. **Contact** — form with budget radio
7. **Footer** — large name, social links
8. **Works 3D Gallery** — most complex, do last

## What to Keep vs Adjust for David

**Keep:**
- Overall structure and section flow
- Monochrome palette
- Typography system (Sofia Sans Condensed + Spline Sans Mono)
- Bracket nav format
- Scattered letter animation concept
- Services accordion pattern

**Adjust:**
- Remove "BASED IN UKRAINE" → David's location
- Replace portrait photo
- Replace project content in Works
- Replace awards with David's credentials
- Update contact info
- Consider whether 3D gallery is worth the complexity — a simpler project showcase might serve better
- Budget radio in contact form may not apply — simplify to just a message form
