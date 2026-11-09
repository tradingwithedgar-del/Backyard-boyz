"""Builds the four service pages from one template.

Run from the repo root:  python3 _redesign/build_service_pages.py
Edit the copy in PAGES below, then re-run; the .html files are overwritten.
Nav, footer and phone bar are copied from index.html, so change those there first.
Nothing here invents facts: no prices, film brands, warranties or job times
until Hector & Adrian confirm them.
"""
import html
import json
import re

SITE = "https://backyardboyzautollc.com/"
PHONE_TEL = "tel:+18328596786"
PHONE = "(832) 859-6786"

# Service area: shop in Cypress, mobile to the rest. Keep in sync with the homepage "Where we work" section.
CITIES = ["Cypress", "Houston", "Katy", "Jersey Village", "Tomball", "The Woodlands", "Spring", "Pasadena", "Humble", "Kingwood"]
AREA_LIST = ", ".join(CITIES[1:-1]) + " and " + CITIES[-1]

CALL_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" '
             'stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 '
             '2 2z"/></svg>')

REVIEWS = {
    "gerardo": ("If you’re looking for high-quality tint work, look no further. They did an absolute perfectionist job on my car. "
                "The micro-edges are clean, the film laid down smooth with zero bubbles, and the whole vehicle looks elevated.", "Gerardo C."),
    "chris": ("Hector and his team were fast and efficient and have great quality work and affordable service! I Recommend them 100 %", "Chris W."),
    "arturo": ("As someone who hates dealing with anything car related, this business hands down has the best customer service ever! "
               "Got me out of a pinch in no time at all. And when they say open 24 hours a day, they mean it. Thank you! 🙏", "Arturo C."),
    "samantha": ("Hector is quick to respond, service was great!!", "Samantha V."),
}

PAGES = [
    {
        "file": "auto-window-tint.html",
        "key": "tint",
        "nav": "Auto window tint",
        "title": "Car Window Tinting in Cypress & Houston, TX | Backyard Boyz Auto LLC",
        "desc": "Car, truck and SUV window tinting in Cypress and Houston. Texas-legal shades, shop or mobile, from Hector and Adrian. Get your quote by text.",
        "service_type": "Automotive window tinting",
        "eyebrow": "Auto window tint · Cypress & Houston",
        "h1": "Car window tinting in Cypress &amp; Houston",
        "lede": "Cars, trucks and SUVs. Less heat, less glare, more privacy and a cleaner look, done at our Cypress shop or in your driveway. Hector and Adrian do the work themselves and text you your quote.",
        "hero_img": ("work/toyota-rear-window-tint.webp", 905, 1200, "Gray Toyota with dark tint on the rear side windows", "Rear windows tinted on a Toyota"),
        "points_title": "What tint does for your ride",
        "points": [
            ("Cuts the heat.", "Film slows the sun coming through the glass, so seats, the steering wheel and the dash don't bake in a Houston parking lot."),
            ("Kills the glare.", "Easier on your eyes in the afternoon sun and with headlights behind you at night."),
            ("Privacy and a clean look.", "Darker back glass keeps what's in the car out of sight, and the whole vehicle looks finished."),
        ],
        "extra": "law",
        "photos": [("work/broken-door-glass.webp", 774, 1200, "Before: gray Toyota with the rear door glass shattered", "Before: busted door glass", "50% 86%"),
                   ("work/toyota-rear-window-tint.webp", 905, 1200, "After: the same Toyota with new glass, tinted dark", "After: new glass, tinted", "55% 50%")],
        "review": "gerardo",
        "faq": [
            ("How much does car tint cost?", "It depends on the vehicle, how many windows and which film. A coupe and a crew-cab truck aren't the same job. Send the quote form or text us your year, make and model and we'll text you a real number."),
            ("What's the darkest I can go in Texas?", "The front side windows have to let in at least 25% of light. The back side windows and rear glass can go darker if you have side mirrors on both sides. We'll tell you what's legal for your vehicle before we start. This is a summary, not legal advice."),
            ("What do the percentages mean?", "The number is how much light gets through. 70% is barely there, 35% is the classic look, 20% is dark and 5% is limo. Try them on the G-wagon on our homepage."),
            ("When can I roll my windows down?", "Give the film a few days to cure first. We'll tell you exactly how long for your film when we finish."),
            ("Will it bubble or turn purple?", "Bubbling and purple fade usually come from cheap film or a rushed install. Ask us which films we carry and what they cover when we quote."),
            ("Can you come to me?", f"Yes. We're mobile across {AREA_LIST}, or you can bring it to our shop in Cypress."),
        ],
    },
    {
        "file": "home-window-tint.html",
        "key": "home",
        "nav": "Home & commercial tint",
        "title": "Home & Business Window Tinting in Houston | Backyard Boyz Auto LLC",
        "desc": "Home and business window tinting in Houston and Cypress. Cooler rooms, less UV and glare, more privacy. We come to you. Get your quote by text.",
        "service_type": "Residential and commercial window film",
        "eyebrow": "Home & commercial tint · Houston",
        "h1": "Home &amp; commercial window tinting in Houston",
        "lede": "Houses, storefronts and offices across Cypress and Houston. Window film keeps rooms cooler, cuts glare and adds privacy, and we come to you to install it.",
        "hero_img": ("work/home-window-film.webp", 903, 1200, "House window mid-job: bubbled old film on the left panes, clean glass on the right", "Home window, mid-job"),
        "points_title": "Why tint your windows",
        "points": [
            ("Cooler rooms.", "West-facing rooms that cook every afternoon stay a lot more comfortable, and the AC doesn't have to fight as hard."),
            ("Less UV and glare.", "Film cuts the UV that fades floors, furniture and rugs, and the glare on TVs and screens."),
            ("Daytime privacy.", "Neighbors and people walking by see less of what's inside, without blinds closed all day."),
        ],
        "extra": "home_steps",
        "photos": [],
        "review": "chris",
        "faq": [
            ("How much does home tint cost?", "It's priced by the number and size of the windows. Text us a rough count, or a couple of photos, and we'll text a quote back."),
            ("Will it make my rooms dark?", "Not unless you want it to. There are light films that cut heat without looking tinted. We'll show you options before anything goes on the glass."),
            ("Can people see in at night?", "Most privacy films work in daylight. At night, with lights on inside, people outside can see in, so you'll still want blinds after dark."),
            ("My old film is bubbling. Can you fix it?", "Ask us about taking the old film off and putting new film on. Send a photo with your quote request."),
            ("Do you do businesses?", "Yes. Storefronts and offices too. Tell us the address and roughly how many windows."),
        ],
    },
    {
        "file": "auto-glass.html",
        "key": "glass",
        "nav": "Auto glass",
        "title": "Auto Glass Replacement in Cypress & Houston | Backyard Boyz Auto LLC",
        "desc": "Cracked windshield or busted side glass? Auto glass replacement in Cypress and Houston, at our shop or where your car is. Get your quote by text.",
        "service_type": "Windshield and auto glass replacement",
        "eyebrow": "Auto glass · Cypress & Houston",
        "h1": "Auto glass &amp; windshield replacement",
        "lede": "Cracked windshield, a break-in or a rock through the side glass. We replace it at our Cypress shop or come to where the car is, and we can tint the new glass while we're there.",
        "hero_img": ("work/mustang-windshield-install.webp", 701, 1200, "White classic Mustang in the shop with its new windshield taped in place", "Windshield install on a classic Mustang"),
        "points_title": "What we replace",
        "points": [
            ("Windshields.", "Cracked, chipped or starred. Send a photo and we'll tell you what it needs."),
            ("Door and side glass.", "Break-ins and busted windows. Text us the year, make and model and which window."),
            ("New glass, tinted to match.", "Already have tint on the other windows? We can tint the replacement glass so it all matches."),
        ],
        "extra": None,
        "photos": [("work/broken-door-glass.webp", 774, 1200, "Before: gray Toyota with the rear door glass shattered", "Before: busted door glass", "50% 86%"),
                   ("work/toyota-rear-window-tint.webp", 905, 1200, "After: the same Toyota with new glass, tinted dark", "After: new glass, tinted", "55% 50%")],
        "review": "arturo",
        "faq": [
            ("How much does glass replacement cost?", "It depends on the vehicle and which glass. Text us the year, make and model and a photo of the damage and we'll text you a price."),
            ("How soon can you get to me?", "Call or text and we'll tell you how soon we can get there. We're mobile around Houston and have a shop in Cypress."),
            ("Can you tint the new window?", "Yes. Tell us when you request your quote and we'll match it to your other windows."),
            ("Do you do classic cars?", "Yes. The Mustang on this page was done in our shop."),
        ],
    },
    {
        "file": "headliner-repair.html",
        "key": "headliner",
        "nav": "Headliners",
        "title": "Headliner Repair & Replacement in Houston, TX | Backyard Boyz Auto LLC",
        "desc": "Sagging or falling headliner? Headliner repair and replacement in Houston and Cypress, shop or mobile. Get your quote by text.",
        "service_type": "Car headliner repair and replacement",
        "eyebrow": "Headliners · Houston & Cypress",
        "h1": "Headliner repair &amp; replacement in Houston",
        "lede": "Roof fabric sagging onto your head? We pull the headliner board, strip the old fabric and redo it properly, so it stays up.",
        "hero_img": ("work/headliner-removed.webp", 898, 1200, "Worn-out headliner board with the fabric falling apart, pulled out of a car", "Worn-out headliner, pulled for new fabric"),
        "points_title": "Why headliners sag",
        "points": [
            ("The foam gives out.", "There's a thin foam layer between the fabric and the board. Heat and age break it down until it crumbles."),
            ("Glue can't fix it.", "Spray glue or pins on the old fabric don't hold for long, because the foam it's stuck to is what failed."),
            ("The fix is new material.", "The board comes out, gets stripped down, and gets new fabric bonded to it."),
        ],
        "extra": "headliner_steps",
        "photos": [],
        "review": "samantha",
        "faq": [
            ("How much does a headliner cost?", "It depends on the vehicle and whether it has a sunroof. Text us the year, make and model and we'll text you a quote."),
            ("Can I pick the fabric color?", "Tell us what you want and we'll tell you what we can get for your car."),
            ("How long does it take?", "We'll give you a time with your quote so you can plan around it."),
            ("Can you come to me?", f"Ask when you request your quote. We're mobile across {AREA_LIST}, and our shop is in Cypress."),
        ],
    },
]

EXTRAS = {
    "law": """
<section class="band band--haze" aria-labelledby="lawTitle">
  <div class="wrap">
    <div class="sec-head">
      <span class="mono eyebrow">Texas tint law</span>
      <h2 id="lawTitle">What's legal in Texas</h2>
      <p>The percentage is how much light the window lets through. Lower means darker.</p>
    </div>
    <div class="table-scroll">
      <table class="law">
        <thead><tr><th scope="col">Window</th><th scope="col">Texas rule</th></tr></thead>
        <tbody>
          <tr><th scope="row">Windshield</th><td>Only a strip across the top</td></tr>
          <tr><th scope="row">Front side windows</th><td>25% or lighter</td></tr>
          <tr><th scope="row">Back side windows</th><td>Any shade, with side mirrors on both sides</td></tr>
          <tr><th scope="row">Rear window</th><td>Any shade, with side mirrors on both sides</td></tr>
        </tbody>
      </table>
    </div>
    <p class="note">A summary, not legal advice. We'll tell you what's legal for your vehicle before we start. <a class="link" href="index.html#shades">Try the shades on our G-wagon →</a></p>
  </div>
</section>
""",
    "home_steps": """
<section class="band band--haze" aria-labelledby="stepsTitle">
  <div class="wrap">
    <div class="sec-head">
      <span class="mono eyebrow">How it works</span>
      <h2 id="stepsTitle">How a home job goes</h2>
    </div>
    <ol class="steps steps--light">
      <li class="step"><span class="n" aria-hidden="true">1</span><div><h3>Send the windows.</h3><p>A rough count and a couple of photos is plenty to start.</p></div></li>
      <li class="step"><span class="n" aria-hidden="true">2</span><div><h3>Get your quote by text.</h3><p>We text a price and the film options that fit what you want.</p></div></li>
      <li class="step"><span class="n" aria-hidden="true">3</span><div><h3>We come out.</h3><p>We clean the glass and install the film at your home or business.</p></div></li>
    </ol>
  </div>
</section>
""",
    "headliner_steps": """
<section class="band band--haze" aria-labelledby="stepsTitle">
  <div class="wrap">
    <div class="sec-head">
      <span class="mono eyebrow">The process</span>
      <h2 id="stepsTitle">How a headliner job usually goes</h2>
    </div>
    <ol class="steps steps--light">
      <li class="step"><span class="n" aria-hidden="true">1</span><div><h3>Board comes out.</h3><p>Trim, lights and handles come off and the headliner board slides out of the car.</p></div></li>
      <li class="step"><span class="n" aria-hidden="true">2</span><div><h3>Stripped and recovered.</h3><p>The old fabric and crumbling foam come off, and new fabric is bonded to the clean board.</p></div></li>
      <li class="step"><span class="n" aria-hidden="true">3</span><div><h3>Back in, tight.</h3><p>The board goes back in and everything gets reinstalled.</p></div></li>
    </ol>
  </div>
</section>
""",
}


def shared_parts():
    s = open("index.html", encoding="utf-8").read()

    def grab(a, b):
        i = s.index(a)
        return s[i:s.index(b, i) + len(b)]

    head = grab('<meta http-equiv="Content-Security-Policy"', ">")
    fonts = grab('<link rel="preconnect" href="https://fonts.googleapis.com">', 'display=swap" rel="stylesheet">')
    header = grab('<header class="nav">', "</header>")
    footer = grab("<footer>", "</footer>")
    mobar = grab('<div class="mobar">', "</div>")
    # anchors on the homepage become links back to it
    header = header.replace('href="#top"', 'href="index.html"').replace('aria-label="Backyard Boyz Auto LLC, back to top"', 'aria-label="Backyard Boyz Auto LLC, home"')
    header = re.sub(r'href="#(\w+)"', r'href="index.html#\1"', header)
    mobar = re.sub(r'href="#(\w+)"', r'href="index.html#\1"', mobar)
    footer = re.sub(r'href="#(\w+)"', r'href="index.html#\1"', footer)
    for p in PAGES:  # footer service list links to the pages
        footer = footer.replace(f'<li><a href="index.html#services">{html.escape(p["nav"])}</a></li>',
                                f'<li><a href="{p["file"]}">{html.escape(p["nav"])}</a></li>')
    return head, fonts, header, footer, mobar


def shot(img, cls="shot"):
    src, w, h, alt, cap, *pos = img
    style = f' style="object-position:{pos[0]}"' if pos else ""
    return (f'<figure class="{cls}">\n        <img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy"{style}>\n'
            f'        <figcaption>{cap}</figcaption>\n      </figure>')


def build(page, parts):
    head, fonts, header, footer, mobar = parts
    url = SITE + page["file"]
    quote = f'index.html?service={page["key"]}#quote'
    header = header.replace('href="index.html#quote"', f'href="{quote}"')
    mobar = mobar.replace('href="index.html#quote"', f'href="{quote}"')
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "@id": url + "#service", "name": html.unescape(page["h1"]),
             "serviceType": page["service_type"], "url": url,
             "provider": {"@id": SITE + "#business"},
             "areaServed": [{"@type": "City", "name": f"{c}, TX"} for c in CITIES]},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
                {"@type": "ListItem", "position": 2, "name": page["nav"], "item": url}]},
        ],
    }
    points = "\n".join(f'      <div class="benefit">\n        <h3>{t}</h3>\n        <p>{d}</p>\n      </div>' for t, d in page["points"])
    photos = ""
    if page["photos"]:
        photos = f"""
<section class="band band--clear" aria-labelledby="photosTitle">
  <div class="wrap">
    <div class="sec-head">
      <span class="mono eyebrow">The work</span>
      <h2 id="photosTitle">Before &amp; after</h2>
    </div>
    <div class="pair">
      {shot(page["photos"][0])}
      {shot(page["photos"][1])}
    </div>
  </div>
</section>
"""
    q, who = REVIEWS[page["review"]]
    faq = "\n".join(f'      <details>\n        <summary>{qq}</summary>\n        <div class="a"><p>{aa}</p></div>\n      </details>' for qq, aa in page["faq"])
    others = "\n".join(f'      <a class="btn btn--line" href="{p["file"]}">{html.escape(p["nav"])}</a>' for p in PAGES if p is not page)
    extra = EXTRAS.get(page["extra"], "") if page["extra"] else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light">
{head}
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{html.escape(page["title"])}</title>
<meta name="description" content="{html.escape(page["desc"])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#F3F4F2">
<link rel="icon" type="image/webp" href="favicon.webp">
<link rel="apple-touch-icon" href="logo.webp">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(page["title"])}">
<meta property="og:description" content="{html.escape(page["desc"])}">
<meta property="og:site_name" content="Backyard Boyz Auto LLC">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
{fonts}
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">
{json.dumps(schema, indent=2, ensure_ascii=False)}
</script>
</head>
<body>
<a class="sr-only skip" href="{quote}">Skip to the quote form</a>

{header}

<main id="top">

<section class="band band--clear page-hero" aria-labelledby="pageTitle">
  <div class="wrap">
    <div class="hero-copy">
      <nav class="crumbs mono" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">{html.escape(page["nav"])}</span></nav>
      <span class="mono eyebrow">{page["eyebrow"]}</span>
      <h1 id="pageTitle">{page["h1"]}</h1>
      <p class="lede">{page["lede"]}</p>
      <div class="cta-row">
        <a class="btn btn--ink" href="{quote}">Get my quote</a>
        <a class="btn btn--line" href="{PHONE_TEL}">{CALL_ICON}Call or text {PHONE}</a>
      </div>
    </div>
    {shot(page["hero_img"], "shot page-shot")}
  </div>
</section>

<section class="band band--clear" aria-labelledby="pointsTitle" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <h2 id="pointsTitle">{page["points_title"]}</h2>
    </div>
    <div class="benefits">
{points}
    </div>
  </div>
</section>
{extra}{photos}
<section class="band band--haze" aria-labelledby="revTitle">
  <div class="wrap">
    <figure class="quote-card quote-solo">
      <span class="stars" aria-label="5 out of 5 stars">★★★★★</span>
      <blockquote><p>{q}</p></blockquote>
      <figcaption class="mono">{who} · Google review</figcaption>
    </figure>
    <a class="btn btn--line reviews-more" href="https://www.google.com/search?q=backyard+boyz+auto+llc+reviews" target="_blank" rel="noopener">View more reviews on Google</a>
  </div>
</section>

<section class="band band--smoke" aria-labelledby="faqTitle">
  <div class="wrap faq-wrap">
    <div class="sec-head">
      <span class="mono eyebrow">FAQ</span>
      <h2 id="faqTitle">Common questions</h2>
    </div>
    <div class="faq">
{faq}
    </div>
  </div>
</section>

<section class="band band--limo closing" aria-labelledby="closeTitle">
  <div class="wrap">
    <h2 id="closeTitle">Ready when you are.</h2>
    <p>Tell us what you've got and we'll text you a quote.</p>
    <div class="cta-row">
      <a class="btn btn--gold" href="{quote}">Get my quote</a>
      <a class="btn btn--line" href="{PHONE_TEL}">Call {PHONE}</a>
    </div>
    <span class="mono eyebrow" style="margin-top:var(--s-6)">Other services</span>
    <div class="cta-row">
{others}
    </div>
  </div>
</section>

</main>

{footer}

{mobar}

<script>document.getElementById('yr').textContent = new Date().getFullYear();</script>
</body>
</html>
"""


if __name__ == "__main__":
    parts = shared_parts()
    for p in PAGES:
        open(p["file"], "w", encoding="utf-8").write(build(p, parts))
        print("wrote", p["file"])
