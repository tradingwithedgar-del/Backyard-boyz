# 1. Website Blueprint: Backyard Boyz Window Tinting

> Folder note: this `_redesign/` folder starts with an underscore, so GitHub Pages (Jekyll) does not publish it. It stays in the repo as working notes only.

## The business

| | |
|---|---|
| **Who** | Backyard Boyz Window Tinting (Backyard Boyz Auto LLC). Family-run by brothers Hector and Adrian. |
| **What** | Auto window tint, home and commercial window tint, auto glass replacement, headliners and other interior work. |
| **Where** | Shop in Cypress, TX, or fully mobile across Houston. |
| **Proof on hand** | 4+ years in business, an active Instagram (@backyardd.boyzz) full of finished jobs, a real local phone that takes calls and texts. |
| **Proof missing** | Customer reviews, photos on the site itself, film brand and warranty details. These are the biggest gaps (see the launch checklist). |

## The ideal visitor

**Primary:** a driver in Cypress, Jersey Village, Katy or northwest Houston, usually 20 to 45, who just bought a car or truck, or got a ticket for their tint. They're on their phone, often coming from Instagram or a "window tint near me" search. In the first 10 seconds they want to know three things:
1. Roughly what it costs and how fast they can get a quote.
2. What shade they can legally run in Texas.
3. Whether they have to drive somewhere or someone can come to them.

**Secondary:** a homeowner or small business owner with a west-facing room or storefront that cooks every afternoon. They care about heat, UV and privacy, and about who's showing up to the property.

## Reference sites

You didn't name three sites, so I worked from patterns that keep showing up across the category. **Send me the three sites you admire and I'll adjust the style direction.**

| Pattern | Where it shows up | How we use it |
|---|---|---|
| **Guided quote flow** (pick the service, then the details, then contact info) | National auto glass and tint chains | Kept and tightened. It's already your strongest conversion feature. |
| **Shade visualizer** (see 5% vs 35% before you pick) | Window film manufacturer sites | Rebuilt small as the hero. Tap a shade and the window darkens, with a Texas legal note. Your pick carries into the quote form. |
| **Flaw to beat:** vague "contact us" pages, stock photos of cars that aren't theirs, no word on what's legal | Most small local tint shops | Use your own work only, say plainly how the quote comes back (by text), and answer the legal question up front. |

## The one action

**Request a quote** (a 3-step form, and the quote comes back by text). Calling or texting (832) 859-6786 counts as the same action through a second door. Every section either answers a question that's blocking that action or hands the visitor a button for it.

## Sitemap

```
backyardboyzautollc.com
├── /                Home (one long page, anchored sections)
│   ├── #services
│   ├── #shades      (in the hero)
│   ├── #how
│   ├── #work
│   ├── #faq
│   └── #quote
└── /privacy.html    Privacy Policy (unchanged in this round)
```

The site stays a single page for launch. A small shop gets more from one fast page that does one job than from five thin pages. **Phase 2 (after launch):** split out `/auto-tint`, `/home-tint` and `/auto-glass` pages once real photos and reviews exist to fill them. Each one targets its own Google search.

## Homepage sections, in order

| # | Section | Job | Headline | CTA |
|---|---|---|---|---|
| 0 | **Top nav** (sticky) | Always one tap from calling | Logo · Services · Shades · FAQ | **Call** (desktop and mobile) and **Get a quote** (desktop) |
| 1 | **Hero + shade picker** | Say what you do, where, and let them play with the decision they came to make | *Tint that takes the Houston heat off.* | **Get my quote** (primary) · **Call or text** (secondary) |
| 2 | **Proof strip** | Fast trust using only true facts | (none) | (none) |
| 3 | **Three benefits** | Why you, in three reasons | *Why people around Houston call the Boyz* | (none) |
| 4 | **Services** | What you can book | *What we do* | "Quote this" link on each card |
| 5 | **How it works** | Remove the "what happens next" worry | *Three steps. No runaround.* | (none) |
| 6 | **The work** | Visual proof (their own photos plus Instagram) | *See it on real cars* | **See more on Instagram** |
| 7 | **Testimonials** | Social proof | *What customers say* | (none) |
| 8 | **Quote form** | THE conversion point | *Get your quote by text* | **Send & get my quote** |
| 9 | **FAQ** | Clear the last objections | *Questions we get every week* | Inline call link |
| 10 | **Closing band** | Last push, darkest band | *Ready when you are.* | **Get my quote** · **Call** |
| 11 | **Footer** | Name, address and phone, plus links | (none) | Call · IG · Email |
| — | **Sticky mobile bar** | Thumb-reach CTA on phones | (none) | **Call** · **Quote** |

**CTA placement:** quote/call shows up in the nav, the hero, every service card, the form itself, the FAQ, the closing band and the sticky mobile bar. At no scroll position on a phone is a CTA more than one tap away.

## Style direction (short version; full spec in `02-design-system.md`)

**Concept: the shade card.** Tint shops sell from a swatch card where the film steps from clear to limo black. The page works the same way. It opens light like clear glass, the bands get darker as you scroll, and it closes on a near-black "5%" band. Each band carries a small mono label (`VLT 70%`, `VLT 35%` and so on), the way a real swatch card is labeled.

- **Colors:** cool clear-glass white `#F3F4F2`, haze `#E2E5E3`, smoke `#2B2F31`, limo `#0E0F10`, ink `#141617`. Brand gold `#C9AE6A` is kept for the logo and a few accents only, so the site reads as Backyard Boyz rather than another black-and-gold "luxury" template.
- **Fonts:** **Big Shoulders Display** for headlines (tall, condensed, industrial signage), **Instrument Sans** for body text, **IBM Plex Mono** for shade percentages, labels and specs.
- **Feel:** rugged, exact, neighborly. **Not** corporate, not "luxury", not a franchise.
