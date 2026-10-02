# Ubuntu Rising Foundation — website

Static marketing site for Ubuntu Rising Foundation, a Nairobi-based NGO working on water,
education, health, livelihoods and climate resilience across East Africa.

Primary goals of the site: **online donations**, **volunteer sign-ups** and
**corporate partnership leads**.

## Pages

| File | Purpose |
|---|---|
| `index.html` | Home — hero slider, impact counters, mission, programmes, live appeals, ways to give, partners, news |
| `about.html` | Story, values, team, governance & accountability |
| `what-do.html` | The six programmes and our four-step method |
| `projects.html` | Live projects with budgets, locations and funding progress |
| `donate.html` | Donation form (once/monthly, amount tiers, designation) plus M-PESA & bank details |
| `volunteer.html` | Volunteer roles and sign-up form |
| `partners.html` | Corporate/CSR partnership offer and lead capture form |
| `blog.html`, `blog_details.html` | News & field stories |
| `contact.html` | Contact details, map and enquiry form |
| `elements.html` | Template style guide |

## Running locally

```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

## How the pages are built

The HTML is generated from two small scripts so the header, footer and shared sections stay
identical across every page:

```bash
python3 build_site.py     # index, about, what-do, projects, donate, volunteer, partners
python3 build_pages2.py   # blog, blog_details, contact, elements (re-skins the original template pages)
```

Edit the scripts, re-run them, and the `.html` files are rewritten. (`build_pages2.py` reads the
original Colorlib markup from the extracted template, so keep the zip/extract around if you need
to regenerate those four pages from scratch.)

## Custom assets

* `assets/css/ubuntu.css` — all bespoke styling (impact counters, ways-to-give cards, programme
  cards, donation form, project cards, donate band). The original template CSS is untouched.
* `assets/js/ubuntu.js` — counters plus the donation amount/frequency picker.

## Forms

All forms post to `contact_process.php` (from the original template). Wire these up to your real
donation processor (card gateway + M-PESA Daraja) and CRM before going live.

## Photography

Real photographs from Pexels — see `CREDITS.md`. No AI-generated imagery is used.
