# Ubuntu Rising Foundation — website

Static marketing site for **Ubuntu Rising Foundation**, a Nairobi-registered NGO running
education, clean water, women's livelihoods, community health and youth climate programmes
across Kenya, Uganda, Tanzania and Rwanda.

The site is built for three conversion goals, in order: **online donations**,
**volunteer sign-ups**, and **corporate partnership leads**.

## Running it

Any static file server will do:

```bash
python3 -m http.server 3000
# then open http://localhost:3000
```

## Pages

| File | Purpose | Primary CTA |
| --- | --- | --- |
| `index.html` | Homepage — hero, three doors, mission, programmes, impact, live appeals, voices, news | Donate |
| `about.html` | Story, values, timeline, leadership | Donate / Volunteer |
| `programmes.html` | The five programmes in full, with unit costs | Support a programme |
| `projects.html` | Six open appeals with progress bars; where we work | Fund an appeal |
| `impact.html` | Audited spend breakdown, documents, "what did not work" | Donate / due diligence |
| `donate.html` | Donation form (currency switch, amount tiers, M-PESA/card/bank/PayPal) | **Donate** |
| `volunteer.html` | Open roles and the volunteer application form | **Volunteer sign-up** |
| `partners.html` | Partnership models and the corporate enquiry form | **Partnership lead** |
| `blog.html` / `blog_details.html` | News and field stories | Donate (sidebar) |
| `contact.html` | Map, contact form, safeguarding route | Contact |

## Structure

```
assets/
  css/style.css      compiled template stylesheet (from the supplied theme)
  css/urf.css        Ubuntu Rising brand layer + overrides  ← edit this, not style.css
  js/main.js         template behaviours (one documented patch, see below)
  js/urf.js          donation form interactions
  img/               photography, logos, breadcrumb banners
  img/src/           full-size masters — re-crop derivatives from these, never upscale
  scss/              source SCSS for style.css (from the supplied theme)
tools/
  build_site.py      shared head / header / footer / page writer
  pages.py           page content — run this to regenerate the HTML
```

### Regenerating the HTML

Header, footer, navigation and `<head>` live in one place. After editing
`tools/build_site.py` or `tools/pages.py`:

```bash
cd tools && python3 pages.py
```

This rewrites every `.html` file in the repository root. Do not hand-edit the generated
HTML unless you also fold the change back into `tools/`.

## Design system

Inherited unchanged from the supplied template:

| Token | Value | Use |
| --- | --- | --- |
| Primary green | `#09cc7f` | Links, accents, CTAs |
| Gradient | `#46C0BE → #6DD56F → #46C0BE` | Buttons, progress bars, stat bars |
| Deep navy | `#10285d` / `#0a1b3f` | Body copy, footer, CTA bands |
| Heading ink | `#425140` | Headings |
| Mint | `#EEFFFA` | Soft section backgrounds |
| Display typeface | Plus Jakarta Sans 500–800 | All headings |
| Body typeface | Montserrat 200–700 | Body copy, UI, labels |

Brand tokens are exposed as CSS custom properties at the top of `assets/css/urf.css`.

## Notes for the next developer

- **Payments are not wired up.** `donate.html` runs entirely client-side and shows a
  confirmation dialog on submit. Point `#donateForm` at your payment provider
  (M-PESA Daraja / Flutterwave / Stripe) before launch. The currency conversion rates in
  `assets/js/urf.js` are indicative and hard-coded — replace them with a live rate feed.
- **Forms** post to `contact_process.php`, which needs a mail-capable host. Swap in your
  CRM endpoint if you use one.
- **Content is illustrative.** Figures, names, registration numbers, bank details and the
  partner list are plausible placeholders written for this build. Replace them with the
  real ones before going live.
- **Motion** lives in `assets/css/urf.css` (hero Ken Burns drift behind Slick's crossfade,
  animated CTA glow, shimmering spend meters, pulsing donate/WhatsApp buttons, scroll cue)
  and `assets/js/urf.js` (IntersectionObserver scroll reveal). All of it is disabled under
  `prefers-reduced-motion`.
- **Imagery is AI-generated** for layout purposes. Substitute real, consented photography
  from the field — and check it against your safeguarding policy before publishing images
  of children.
- `assets/js/main.js` carries one deliberate change from the stock template: the Nice Select
  initialiser now skips `.urf-select` so the custom form controls keep their styling. It is
  marked with a `URF:` comment.
- `environmentalorganization-main.zip` is the original supplied theme, kept for reference.

## Contact routing

The site exposes **no telephone number as text**. The number `+254 112 272 061` is wired
only into `wa.me` deep links (floating button, top bar, footer, and inline CTAs on the
donate, volunteer, partner and blog pages), so it is never scraped off the page or shown
to visitors. The links live in one place — `SITE["wa_link*"]` in `tools/build_site.py`.

## Credits and licensing

Built on the Colorlib "Environmental Organization" HTML template.

> **Please read:** the template ships under CC BY 3.0, and Colorlib's terms require the
> footer attribution link to remain unless a licence is purchased. That credit has been
> **removed at the client's request**. Before this site goes live you should either buy a
> Colorlib licence (https://colorlib.com/wp/licence/) or restore the attribution, otherwise
> you are using the template outside its licence terms.
