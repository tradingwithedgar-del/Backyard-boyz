# 5. Launch Checklist: backyardboyzautollc.com

**Status:** the redesign lives on branch `claude/charming-cannon-6l1s0m` only. `main` (the live site) is untouched. Nothing below goes live until you approve the pull request.

## What I analyzed

| Area | Finding |
|---|---|
| **Pages** | `index.html` (redesigned), `privacy.html` (unchanged, still the old dark style). |
| **Page weight** | Old homepage was **209 KB** because the logo was pasted into the HTML 4 times as text. The new homepage is **50 KB** (14 KB gzipped), plus the logo as one cached **32 KB** file. |
| **Images** | Only the logo and favicon so far (pulled out into `logo.webp` and `favicon.webp`). **No work photos yet:** 6 photo slots are waiting. `og-image.jpg` (1200×630) is unchanged. |
| **Forms** | One quote form → Web3Forms → shop email, with hCaptcha and a honeypot. Now also sends the **shade** they picked. Errors show inline (the old version used pop-up alerts). |
| **Domain** | `CNAME` = `backyardboyzautollc.com` on GitHub Pages. The canonical and OG URLs used to say `Backyardboyzautollc.com` (capital B); they're now all lowercase. I couldn't reach the live domain from this sandbox, so the DNS/HTTPS checks below need doing by hand. |
| **Tracking** | None. The privacy policy says there's no analytics. **If you add analytics, the policy has to change too** (step 7). |

---

## 🚫 Must fix before launch (blocking)

- [ ] **Reviews section:** paste 3 real reviews word for word with each customer's OK, and delete the orange "Placeholder" flags. **If you don't have them, delete the whole Reviews `<section>`.** Fake or sample reviews can't go live.
- [ ] **Photo slots:** replace all 6 `.ph` boxes with the brothers' own job photos (rules in `02-design-system.md`). If you only have 3, delete the other 3 so the grid stays even. No stock and no photos from other shops.
- [ ] **Confirm with Hector & Adrian:**
  - [ ] "4+ years" is still accurate.
  - [ ] They're OK with "Hector or Adrian will text your quote" (it promises a text reply).
  - [ ] The Texas tint rule as written (front side 25%, back darker with dual mirrors, windshield strip only). It's on the page twice.
  - [ ] FAQ "How long does it take?": swap in real typical times.
  - [ ] FAQ "Will it bubble?": add film brands and warranty **only if real**.

## 1. Page speed

- [ ] Run **PageSpeed Insights** (pagespeed.web.dev) on the branch preview and again after launch. Target **90+ mobile performance**, LCP under 2.5s.
- [ ] Every work photo is WebP, ≤1200px wide, **under 200 KB**, with `width`/`height` set and `loading="lazy"`.
- [ ] Google Fonts loads 3 families. If PageSpeed flags render-blocking fonts, drop the IBM Plex Mono weight or self-host the fonts.
- [ ] hCaptcha script is `async`, so it doesn't block the first paint. Leave it that way.

## 2. Mobile checks (do these on a real phone, iPhone and Android)

- [ ] No sideways scrolling anywhere (tested at 390px in this build ✅, recheck after photos go in).
- [ ] Sticky bottom bar shows **Call now / Get a quote** and doesn't cover the form's submit button.
- [ ] **Tap "Call now"** → phone dialer opens with (832) 859-6786.
- [ ] **Tap "Call or text"** in the hero → same.
- [ ] Shade picker: tap each shade, the window darkens, and the tag flips to "Back windows only" at 20% and 5%.
- [ ] "Quote me on 20%" jumps to the form with 20% already picked.
- [ ] Form inputs don't zoom the page when tapped (they're 16px, so they shouldn't).
- [ ] FAQ items open and close with one tap.

## 3. Broken links

- [ ] Every nav link scrolls to its section: Services, Shades, How it works, FAQ.
- [ ] Instagram links open **@backyardd.boyzz** in a new tab (3 places).
- [ ] `mailto:llcbackyardboyz@gmail.com` opens mail (2 places).
- [ ] `privacy.html` loads from the footer and from the form note.
- [ ] `grandnashstudio.com` credit link resolves.
- [ ] Optional: run the live URL through a free link checker (e.g. deadlinkchecker.com).

## 4. Search titles and descriptions

| Page | Title | Description |
|---|---|---|
| `/` | Window Tint Cypress & Houston, TX \| Backyard Boyz Window Tinting (64 chars) | Auto and home window tint, auto glass and headliners in Cypress and Houston. Shop or mobile, from brothers Hector and Adrian. Get your quote by text. (152 chars) |
| `/privacy.html` | Keep current | Keep current |

- [ ] One `<h1>` on the homepage ✅
- [ ] LocalBusiness (AutoRepair) schema has the correct name, phone and city. Validate it at search.google.com/test/rich-results.
- [ ] Update `sitemap.xml` `<lastmod>` to the launch date.
- [ ] **Google Business Profile:** make sure the website field points to `https://backyardboyzautollc.com/` and the phone matches.
- [ ] Submit the sitemap in **Google Search Console** (verify the domain first if it isn't verified yet).
- [ ] Share the link in a DM to yourself to check the OG preview card shows the logo image and title.

## 5. Contact form test (do this on the live site after launch)

- [ ] Submit one test for **each** service: auto tint (with a shade), home tint, glass, headliner.
- [ ] Each one arrives at **llcbackyardboyz@gmail.com** within a minute, with Service, Shade, Vehicle/property, Name and Phone filled in. Check spam the first time.
- [ ] Hector or Adrian confirms they actually saw it on their phone (the whole point is a fast text back).
- [ ] Leave name blank → inline error. Enter a 7-digit phone → "looks short" error. Skip the hCaptcha → "Tick the box" error.
- [ ] Turn on **hCaptcha** in the Web3Forms dashboard if it isn't on already.
- [ ] Turn Wi-Fi off and submit → you should see the "call or text us" fallback message, not a fake success.

## 6. Domain and HTTPS

- [ ] GitHub repo → Settings → Pages: custom domain `backyardboyzautollc.com`, **Enforce HTTPS ✅**.
- [ ] `http://` redirects to `https://`.
- [ ] `www.backyardboyzautollc.com` redirects to the bare domain (needs a `CNAME www → <user>.github.io` DNS record).
- [ ] The padlock shows on phone and desktop. No mixed-content warnings in the browser console.

## 7. Analytics setup

Pick one. My recommendation is the first.

- **Cloudflare Web Analytics** or **GoatCounter** (free, no cookies, no consent banner needed). Or:
- **Google Analytics 4** (free, more detail, sets cookies).

Whichever you pick:
- [ ] Add its script domain to the page's **Content-Security-Policy** `script-src` and `connect-src`, or it will be silently blocked.
- [ ] Track these clicks as events: **Call** taps (`tel:` links), **Quote submitted** (step 3 shown), **Instagram** clicks, **Shade picked**.
- [ ] **Update `privacy.html`**: it currently says "We do not run advertising trackers or analytics." Change that line and name the tool, or the policy becomes untrue on day one.

## 8. Rollout

1. You review the preview → approve the draft PR.
2. Merge to `main` → GitHub Pages redeploys in 1–2 minutes.
3. Hard-refresh the live site on a phone, then run sections 2, 3 and 5 above.
4. If anything's wrong: **revert the merge commit** on `main` and the old site is back in about 2 minutes.

---

## First three updates in the week after launch

1. **Day 1–2: Get proof on the page.** Ask the last 5–10 happy customers for a Google review (send them the direct review link from Google Business Profile). Put the best 3 in the Reviews section, plus 6 fresh job photos, and get at least one **before/after** pair.
2. **Day 3–4: Check where people drop off.** In analytics, compare **quote form starts vs. submissions** and **call taps**. If people start but don't finish, cut the shade field or the vehicle field and test again. Ask the brothers how many quote texts they sent this week.
3. **Day 5–7: Match the site to Instagram and Google.** Put the site link in the Instagram bio and in Google Business Profile. Restyle `privacy.html` to match the new design. Then plan Phase 2: separate **Auto tint**, **Home tint** and **Auto glass** pages for "window tint Cypress TX"-type searches.

---

## Risk scan (pre-launch, on this branch)

**Verdict: Fix 2 items first** (the review placeholders and photo slots). Everything else is clear.

| Severity | Area | Evidence | Fix |
|---|---|---|---|
| Blocking | Social proof | `Placeholder, add real review` ×3 | Real reviews or delete the section |
| High | Photos / credibility | `Photo slot 1`–`6` | Own job photos or remove the slots |
| Medium | Legal claim | "Texas lets you run 25% or lighter on the front side windows" | Brothers confirm wording. It's a law summary, not legal advice. |
| Medium | Claims | "4+ years", "Hector or Adrian will text your quote" | Confirm still true |
| Low | Privacy policy | Says no analytics; Google Fonts loads from Google | Update when analytics is added |

Clean: no license, insurance, warranty, rating or "best in Houston" claims. No card fields. Form only collects name, phone and job details, with a plain-language notice. All `target="_blank"` links have `rel="noopener"`. No third-party images.
