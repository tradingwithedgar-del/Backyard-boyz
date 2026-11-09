# 2. Design System: Backyard Boyz Window Tinting

A developer should be able to build any new section from this page without guessing. Every value here is a CSS custom property in `index.html` (`:root`).

## Brand read

| | |
|---|---|
| **Personality** | Two brothers who are good with their hands and straight with people. Street-credible, not flashy. |
| **Audience** | Local drivers on phones (mostly from Instagram), plus homeowners. They decide fast and want a straight answer. |
| **Industry costume to avoid** | Black background, gold script, chrome glare: every tint shop looks like a nightclub flyer. We keep the gold only because it's in the real logo. |
| **Feeling on exit** | "These guys know tint, they'll tell me what's legal, and they'll text me back today." |
| **If it were an object** | A tint shade card: a strip of film swatches going clear → limo, each labeled with a percentage. |

## Color

| Token | Hex | Use | Contrast (WCAG, computed) |
|---|---|---|---|
| `--clear` | `#F3F4F2` | Page background, hero ("70%" band) | (none) |
| `--haze` | `#E2E5E3` | Alternate light band, input fields | (none) |
| `--smoke` | `#2B2F31` | Dark band ("20%"), quote section | (none) |
| `--limo` | `#0E0F10` | Darkest band ("5%"): closing CTA and footer | (none) |
| `--ink` | `#141617` | Body text and headlines on light | 16.5:1 on `--clear` |
| `--ink-2` | `#4B5256` | Secondary text on light | 7.2:1 on `--clear`, 6.3:1 on `--haze` |
| `--paper` | `#F3F4F2` | Text on dark bands | 12.3:1 on `--smoke` |
| `--paper-2` | `#B4BBBE` | Secondary text on dark | 7.0:1 on `--smoke`, 9.9:1 on `--limo` |
| `--gold` | `#C9AE6A` | Brand accent **on dark only**: primary button, focus ring | 8.4:1 ink-on-gold, 6.3:1 gold on `--smoke` |
| `--gold-ink` | `#7A5E1C` | Gold used **as text on light** (eyebrows, links) | 5.5:1 on `--clear`, 4.8:1 on `--haze` |
| `--line` | `rgba(20,22,23,.14)` / `rgba(243,244,242,.14)` | 1px rules on light / dark | (none) |
| `--ok` | `#256B41` | "Legal on front windows" tag | 5.1:1 on `--haze` |
| `--warn` | `#9A4A12` | "Back windows only" tag, placeholder flags | 4.9:1 on `--haze` |

**Rules**
- Gold appears in at most three places per screen. It is never a background on a light band.
- Bands get darker going down the page: clear → haze → smoke → limo. Never put a light band below a darker one, except the white form card that sits inside the smoke band.
- Never use pure black `#000` or pure white `#FFF`.

## Typography

| Role | Font | Weights | Notes |
|---|---|---|---|
| Display | **Big Shoulders Display** | 800, 900 | Headlines, all caps, `letter-spacing: .005em`, `line-height: .92` |
| Body | **Instrument Sans** | 400, 500, 600 | Paragraphs, buttons, form text |
| Utility | **IBM Plex Mono** | 500 | Shade %, band labels, eyebrows, step numbers. Uppercase, `letter-spacing: .12em` |

Loaded from Google Fonts with `display=swap`. Fallbacks: `Impact, "Arial Narrow", sans-serif` / `system-ui, sans-serif` / `ui-monospace, monospace`.

**Type scale** (mobile → desktop, using `clamp()`)

| Token | Size | Use |
|---|---|---|
| `--t-hero` | 48 → 96px | H1 only |
| `--t-h2` | 36 → 60px | Section headlines |
| `--t-h3` | 22 → 26px | Card titles (display face) |
| `--t-lede` | 18 → 20px | Hero subheadline, section intros |
| `--t-body` | 16px | Paragraphs (line-height 1.6, max 62ch) |
| `--t-small` | 14px | Captions, form notes |
| `--t-label` | 12px | Mono labels |

## Spacing scale (4px base)

`--s-1: 4px` · `--s-2: 8px` · `--s-3: 12px` · `--s-4: 16px` · `--s-5: 24px` · `--s-6: 32px` · `--s-7: 48px` · `--s-8: 64px` · `--s-9: 96px`

- Section padding: `--s-8` mobile, `--s-9` desktop (top and bottom).
- Side gutter: 20px mobile, centered `max-width: 1160px` container.
- Spacing between siblings comes from `gap` on flex or grid, not per-element margins.

## Corners and edges

One rule everywhere: **4px radius** (`--r`). It's tight, like a cut sheet of film. Pills (999px) are allowed **only** for shade chips. No drop shadows on cards. Separation comes from 1px lines and band color.

## Buttons

| Variant | Look | Where |
|---|---|---|
| **Primary (light band)** | `--ink` fill, `--clear` text | Hero "Get my quote" |
| **Primary (dark band)** | `--gold` fill, `--ink` text | Quote submit, closing band |
| **Secondary** | Transparent, 1.5px border in current text color | "Call or text" |
| **Text link** | `--gold-ink` underlined, 2px offset | Inline "Quote this" |

Specs: min height **48px** (tap target), padding `14px 22px`, Instrument Sans 600 at 16px, sentence case, icon 18px at left. Hover lifts the button `translateY(-1px)` and darkens or lightens the fill by one step. Active pushes it down 1px. Focus shows a **3px gold outline with 3px offset** in every variant.

## Cards

- **Service card:** light band, `--clear` fill, 1px `--line` border, 4px radius, padding `--s-5`. Top row has a mono label (`AUTO`, `HOME`, `GLASS`, `INTERIOR`). On hover the border turns `--ink` and a 4px gold rule grows along the bottom edge. No icons, no shadow.
- **Testimonial card:** no box. A big display quote mark in gold-ink, the quote in body 18px, and the name and car in mono below.
- **Form card:** the one raised object. `--clear` card inside the smoke band, 4px radius, padding `--s-6`.

## Icons

- **Line icons only**, 24px grid, 1.75px stroke, round caps, `currentColor`.
- Used **only where they mean an action**: phone, text bubble, Instagram, email, map pin, check, arrow. Never as decoration in front of a benefit or service. Labels do that job.
- Inline SVG, no icon font, no emoji as icons.

## Photo rules

1. **Your own work only.** No stock photos, no Google Images, no photos from other shops. Every photo should be a car, home or storefront the Boyz actually did.
2. **Shoot the glass, not the car.** Side profile at a 3/4 angle so the tinted windows read. Best light is late afternoon with the sun behind the camera.
3. **One crop:** 4:3 for the work grid, 3:2 if you add a hero photo. Same height across a row.
4. **Clean backgrounds:** a driveway or the shop bay, no trash cans or other cars cutting through the frame.
5. **No plates and no faces** unless the customer said OK. Blur plates.
6. **Export:** WebP, 1200px on the long side, under 200 KB each. Name files descriptively (`tahoe-20-percent-side.webp`).
7. **Alt text:** say what it is and the shade, e.g. *"Black Tahoe with 20% tint on the back windows and 35% on the fronts."*
8. Before/after pairs are the strongest proof you can post. Shoot both from the same spot.

## Motion

One moment only: **the shade picker.** When a shade is tapped, the window glass fades to that darkness over 400ms. Everything else is a hover state (150ms). With `prefers-reduced-motion`, all transitions are off.
