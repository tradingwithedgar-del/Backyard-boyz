# 6. SEO Plan: Getting Backyard Boyz Found on Google

## What Search Console is telling us (28 days, Nov 2026)

| Query | Clicks | What it means |
|---|---|---|
| window tinting near me | 1 | Google **does** index the site and shows it, just rarely and low down. |
| window tinting · car window tinting near me | 0 | Shown a few times, not clicked. These are the money searches. |
| auto repair near me | 0 | Google files the site as "auto repair" because of the old schema type. |
| tint boyz window tinting · backyard tint | 0 | People half-remember the name. The site should own those searches. |

Total: 6 queries and a handful of impressions. The site is **indexed** but has almost no visibility. That's normal for a domain that started in Aug 2026 with one page and no links pointing at it.

## Why it isn't showing up

1. **"Near me" searches are won by the Google Business Profile (the map pack), not the website.** Proximity, reviews and profile completeness decide the top 3 map results. The website mostly *backs up* the profile.
2. **The business name didn't match.** The Google profile is **Backyard Boyz Auto LLC** and the site said **Backyard Boyz Window Tinting**. Google cross-checks name, address and phone. *Fixed on the branch.*
3. **The redesign isn't live yet.** Google is still reading the old page, which has a capital-B canonical URL and the wrong name. None of the fixes count until the PR is merged.
4. **One page, little text.** "Window tinting Cypress" and "windshield replacement Houston" each want a page about that thing.
5. **No other sites link to it or list it.** Directories (Yelp, Bing, Apple Maps, Facebook) are the easy first links.

## Done on the branch (ships when the PR merges)

- [x] Service area on every page (footer, homepage "Where we work", FAQ answers, structured data `areaServed`): Cypress, Houston, Katy, Jersey Village, Tomball, The Woodlands, Spring, Pasadena, Humble, Kingwood.

- [x] Name is **Backyard Boyz Auto LLC** everywhere: title, nav, footer, social cards, privacy page, structured data.
- [x] Title is now **"Window Tinting in Cypress & Houston, TX | Backyard Boyz Auto LLC"**, with the main keyword first and the city named.
- [x] H1 now starts with **"Window tint…"**.
- [x] Meta description names the services and both cities.
- [x] Structured data rebuilt: business type is `AutoRepair` + `HomeAndConstructionBusiness` (they do homes too), the official name plus the old name as `alternateName`, service catalog, service area, logo, a work photo, and a `WebSite` entry.
- [x] Lowercase canonical URL (the old site used `Backyardboyzautollc.com`).
- [x] Real job photos with descriptive alt text, and real Google reviews with a "View more reviews on Google" link.
- [x] `sitemap.xml` lastmod updated.
- [x] Homepage dropped from 209 KB to about 50 KB. Speed is a ranking factor on phones.
- Review stars are **not** in the structured data on purpose: Google ignores self-posted review stars for local businesses and can treat them as spam.

## Do right after the merge (about 15 minutes, in Search Console)

- [ ] **URL Inspection** → `https://backyardboyzautollc.com/` → **Request indexing**.
- [ ] **Sitemaps** → submit `sitemap.xml` (or resubmit).
- [ ] **Pages** report: check for "Duplicate, Google chose different canonical" from the old capital-B URL. It should clear within a couple of weeks.
- [ ] Test the page at search.google.com/test/rich-results. It should detect a LocalBusiness.

## Google Business Profile (the biggest lever for "near me")

- [ ] **Primary category: "Window tinting service".** Secondary: "Auto glass shop", "Car accessories store" or "Auto upholsterer" (headliners). If the primary is "Auto repair shop", that explains the "auto repair near me" match.
- [ ] **Website field:** `https://backyardboyzautollc.com/`, exactly.
- [ ] **Name:** "Backyard Boyz Auto LLC", exactly as on the site. Don't add keywords to the name; Google suspends profiles for that.
- [ ] **Service area:** set the same list as the website: Cypress, Houston, Katy, Jersey Village, Tomball, The Woodlands, Spring, Pasadena, Humble, Kingwood.
- [ ] **Hours:** if they really are 24 hours (a review says so), set it. If not, set real hours.
- [ ] **Services list:** add each service with a one-line description.
- [ ] **Photos:** upload the same job photos, plus new ones every week. Profiles with fresh photos get more clicks.
- [ ] **Reviews:** keep asking every customer, and **reply to every review** (Google weighs owner replies). Use the direct review link from the profile's "Ask for reviews" button.
- [ ] **Posts:** one post a week (a finished job plus a line of text).

## Citations: list the business with the same name, phone and website

Same exact **name / phone / website** on each: Bing Places (imports from Google), Apple Business Connect (Apple Maps), Yelp, Facebook page, Nextdoor, BBB, Yellow Pages. Also link the site from the Instagram bio.

## Service pages: built (Nov 2026)

`auto-window-tint.html`, `home-window-tint.html`, `auto-glass.html`, `headliner-repair.html`, each with its own title, H1, description, Service + Breadcrumb structured data, a real photo, a real Google review, an FAQ and quote buttons that preselect the service on the homepage form. Generated by `_redesign/build_service_pages.py` (edit the copy there, then re-run). All four are in `sitemap.xml`.

**To make them stronger** (more text and proof = better ranking), send from Hector & Adrian: film brands and warranty, typical times, "starting at" prices, which cities they drive to, and 3–6 more photos per service. Each answer replaces a vague line with a specific one.

### Original plan

One page per service, each with its own title, H1, 300–600 words of real detail, 3–6 photos of that service, an FAQ, and a quote button:

| Page | Target search |
|---|---|
| `/auto-window-tint` | car window tinting Cypress / Houston, ceramic tint, Texas tint laws |
| `/home-window-tint` | home window tinting Houston, residential window film |
| `/auto-glass` | windshield replacement Cypress, auto glass Houston |
| `/headliner-repair` | headliner repair Houston, sagging headliner |

To write these without making things up, I need from Hector & Adrian: film brands and warranty, typical times and price ranges (or "starting at"), which cities they drive to, and more photos per service.

## How to tell it's working

Check Search Console → Performance every 2 weeks: impressions should climb first, then clicks. In the Google Business Profile → Performance, watch calls, website clicks and direction requests. Realistic timeline for a new local site: **4–12 weeks** after the profile and citations are cleaned up.
