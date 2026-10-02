# -*- coding: utf-8 -*-
"""Rebuilds blog, blog details, contact and style-guide pages on the shared layout."""
import io, re, itertools
import build_site as B

SRC = "/tmp/x/environmentalorganization-main/%s"


def main_of(fn):
    s = io.open(SRC % fn, encoding="utf-8").read()
    return s.split("<main>", 1)[1].rsplit("</main>", 1)[0]


def seq(pattern, items, text, flags=0):
    it = itertools.cycle(items)
    return re.sub(pattern, lambda m: next(it), text, flags=flags)


POSTS = [
    ("Twelve boreholes later: what Turkana taught us about handover",
     "Three years after the first solar pump went in at Lokiriama, the committee has replaced two pumps "
     "without calling us once. Here is the maintenance model we now use everywhere.",
     "Water &amp; Sanitation", "14", "Sep"),
    ("Why we pay school fees termly, not annually",
     "A small change in how our scholarship fund disburses money cut drop-outs by a fifth. "
     "Our education team explains the data behind the decision.",
     "Education", "02", "Sep"),
    ("Nine savings groups, one year: what the numbers say",
     "Average household income in the Kisumu Mama Biashara cohort rose 38% in twelve months. "
     "We break down who gained, who did not, and why.",
     "Livelihoods", "19", "Aug"),
    ("How 40 volunteers packed 1,800 hygiene kits in a weekend",
     "Our Nairobi volunteer chapter turned a warehouse in Industrial Area into a production line "
     "for families displaced by the April floods.",
     "Volunteering", "05", "Aug"),
    ("Community health promoters are the cheapest health system we have",
     "A review of 90 promoters in Karamoja found each one reached 240 households a quarter "
     "for less than the cost of a single clinic visit.",
     "Community Health", "22", "Jul"),
]

RECENT = [
    ("Turkana borehole no. 12 is flowing", "28 September 2026"),
    ("Scholarship applications open for 2027", "16 September 2026"),
    ("Flood response fund reaches 61%", "04 September 2026"),
    ("Audited 2025 accounts published", "21 August 2026"),
]

TAGS = ["clean water", "education", "volunteering", "livelihoods",
        "community health", "climate", "Nairobi", "transparency"]

CATS = [("Water &amp; sanitation", "18"), ("Education", "24"), ("Community health", "15"),
        ("Livelihoods", "11"), ("Climate resilience", "09"), ("Volunteer stories", "21")]

# ------------------------------------------------------------------ blog.html
m = main_of("blog.html")
m = m.replace("<h2>Blog</h2>", "<h2>News &amp; stories</h2>")
m = m.replace('<li class="breadcrumb-item"><a href="#">Blog</a></li>',
              '<li class="breadcrumb-item"><a href="#">News</a></li>')
m = seq(r'<h2 class="blog-head" style="color: #2d2d2d;">[^<]*</h2>',
        ['<h2 class="blog-head" style="color: #2d2d2d;">%s</h2>' % p[0] for p in POSTS], m)
m = seq(r"<p>That dominion stars lights dominion divide years for fourth have don't stars is that\s+he earth it first without heaven in place seed it second morning saying\.</p>",
        ["<p>%s</p>" % p[1] for p in POSTS], m)
m = seq(r'<i class="fa fa-user"></i> Travel, Lifestyle',
        ['<i class="fa fa-user"></i> %s' % p[2] for p in POSTS], m)
m = seq(r'<i class="fa fa-comments"></i> 03 Comments',
        ['<i class="fa fa-comments"></i> %02d Comments' % n for n in (7, 4, 11, 3, 6)], m)
m = seq(r'<h3>15</h3>\s*<p>Jan</p>',
        ['<h3>%s</h3>\n                                        <p>%s</p>' % (p[3], p[4]) for p in POSTS], m)
# sidebar
m = m.replace("Search Posts", "Search stories")
m = seq(r'<h3 style="color: #2d2d2d;">(From life was you fish\.\.\.|The Amazing Hubble|Astronomy Or Astrology|Asteroids telescope)</h3>',
        ['<h3 style="color: #2d2d2d;">%s</h3>' % r[0] for r in RECENT], m)
m = seq(r'<p>(January 12, 2019|0\d Hours ago)</p>', ['<p>%s</p>' % r[1] for r in RECENT], m)
m = seq(r'<a href="#">(project|love|technology|travel|restaurant|life style|design|illustration)</a>',
        ['<a href="#">%s</a>' % t for t in TAGS], m)
m = m.replace("Instagram Feeds", "From the field")
m = m.replace("Newsletter", "Stay in touch")
m = re.sub(r'<p>Travel</p>|<p>Lifestyle</p>', '', m)
B.page("blog.html", "News &amp; stories",
       "Field notes, impact data and community voices from Ubuntu Rising Foundation's programmes in Kenya, Uganda, Tanzania and Rwanda.",
       m)

# ---------------------------------------------------------- blog_details.html
d = main_of("blog_details.html")
d = d.replace("<h2>Blog Details</h2>", "<h2>Story</h2>")
d = d.replace('<li class="breadcrumb-item"><a href="#">Blog Details</a></li>',
              '<li class="breadcrumb-item"><a href="blog.html">News</a></li>')
d = re.sub(r'<h2>[^<]*35-storey office[^<]*</h2>',
           '<h2>Twelve boreholes later: what Turkana taught us about handover</h2>', d)
d = re.sub(r'<h2 class="blog-head"[^>]*>[^<]*</h2>',
           '<h2 class="blog-head" style="color: #2d2d2d;">Twelve boreholes later: what Turkana taught us about handover</h2>', d)
BODY1 = ("<p class=\"excert\">When we drilled the first solar-powered borehole at Lokiriama in 2023, we assumed the hard "
         "part was the geology. It was not. The hard part was the twenty-fourth month, the day we handed over the keys, "
         "the spares cabinet and the bank account to a committee of nine people elected by their neighbours.</p>")
BODY2 = ("<p>Three years on, that committee has replaced two pump controllers and a solar regulator without calling our "
         "Lodwar office once. They charge households five shillings a jerrican, bank it on the first Monday of the month, "
         "and publish the balance on a chalkboard outside the water kiosk. The fund has never dropped below KES 60,000.</p>")
BODY3 = ("<p>We now build that model into every water project before the drill rig arrives: an elected committee, two "
         "trained technicians on a retainer, a tariff the community sets itself, and a spares list priced in the nearest "
         "market town rather than in Nairobi. It costs about 9% more up front. It has cut our five-year failure rate from "
         "31% to 4%.</p>")
BODY4 = ("<p>The committee keeps a simple rule we did not invent and would not have thought of: anyone who misses "
         "two monthly meetings is replaced at the next assembly. Attendance has never dropped below seven of nine. "
         "Governance, it turns out, is a maintenance task like any other.</p>")
QUOTE = ("We did not want a donated pump. We wanted a pump that is ours, that we can fix on a Tuesday "
         "without waiting for anybody to drive from Nairobi.")

d = re.sub(r'<h2 style="color: #2d2d2d;">.*?</h2>',
           '<h2 style="color: #2d2d2d;">Twelve boreholes later: what Turkana taught us about handover</h2>',
           d, count=1, flags=re.S)
d = re.sub(r'<p class="excert">.*?</p>', BODY1, d, count=1, flags=re.S)
d = re.sub(r'<div class="quotes">.*?</div>',
           '<div class="quotes">%s<br><br>&mdash; Esther Ekiru, chair of the Lokiriama water committee</div>' % QUOTE,
           d, count=1, flags=re.S)
_bodies = itertools.cycle([BODY2, BODY3, BODY4])
d = re.sub(r'<p>\s*MCSE boot camps.*?</p>', lambda m: next(_bodies), d, flags=re.S)
d = re.sub(r'<p class="comment">.*?</p>', lambda m, c=itertools.cycle([
    "We used this handover model for our school tank in Siaya and the difference is night and day. "
    "Could you publish the committee constitution template?",
    "Brilliant piece. The 9% extra cost up front is the number every funder needs to see next to the "
    "31% to 4% failure rate.",
    "Proud to have been on the Lokiriama build weekend in 2023. Seeing it still running three years "
    "later is everything."]): '<p class="comment">%s</p>' % next(c), d, flags=re.S)
d = re.sub(r'<h4 style="color: #2d2d2d;">Space The Final Frontier</h4>',
           '<h4 style="color: #2d2d2d;">Why we pay school fees termly</h4>', d)
d = re.sub(r'<h4 style="color: #2d2d2d;">Telescopes 101</h4>',
           '<h4 style="color: #2d2d2d;">Nine savings groups, one year</h4>', d)
d = re.sub(r'<p class="like-info">.*?</p>',
           '<p class="like-info"><span class="align-middle"><i class="fa fa-heart"></i></span> Grace and 42 people like this</p>',
           d, flags=re.S)
d = d.replace("Travel, Lifestyle", "Water &amp; Sanitation")
d = d.replace("<h4>Harvard milan</h4>", "<h4>Daniel Mwangi Kariuki, Director of Programmes</h4>")
for old, new in (("Emilly Blunt", "Winnie Achieng"), ("Elsie Cunningham", "Peter Odhiambo"),
                 ("Annie Davis", "Sarah Mutiso"), ("Maria Luna", "Brian Kiptoo")):
    d = d.replace(old, new)
d = re.sub(r'<p class="date">[^<]*</p>', lambda m, c=itertools.cycle([
    "16 September 2026 at 9:12 am", "17 September 2026 at 2:40 pm",
    "19 September 2026 at 8:05 am"]): '<p class="date">%s</p>' % next(c), d)
d = seq(r'<a href="#">(project|love|technology|travel|restaurant|life style|design|illustration)</a>',
        ['<a href="#">%s</a>' % t for t in TAGS], d)
d = d.replace("Instagram Feeds", "From the field").replace("Newsletter", "Stay in touch")
d = d.replace("Search Posts", "Search stories")
B.page("blog_details.html", "Twelve boreholes later",
       "What three years of community handovers in Turkana taught Ubuntu Rising Foundation about building water points that keep working.",
       d)

# -------------------------------------------------------------- contact.html
MAP = """                <div class="mb-5 pb-4 d-none d-sm-block">
                    <iframe title="Ubuntu Rising Foundation, Riverside Drive, Nairobi"
                        src="https://www.openstreetmap.org/export/embed.html?bbox=36.7800%2C-1.2800%2C36.8200%2C-1.2550&amp;layer=mapnik&amp;marker=-1.2675%2C36.8000"
                        style="border:0;width:100%;height:420px" loading="lazy"></iframe>
                </div>
"""
c = main_of("contact.html")
c = c.replace("<h2>Contact</h2>", "<h2>Contact us</h2>")
c = re.sub(r'<div class="d-none d-sm-block mb-5 pb-4">.*?</script>\s*</div>', MAP, c, flags=re.S)
c = re.sub(r'<script src="https://maps\.googleapis\.com.*?</script>', '', c, flags=re.S)
c = c.replace("<h2 class=\"contact-title\">Get in Touch</h2>",
              "<h2 class=\"contact-title\">Get in touch</h2>")
c = c.replace("<h3>Buttonwood, California.</h3>\n                            <p>Rosemead, CA 91770</p>",
              "<h3>Ubuntu House, Nairobi</h3>\n                            <p>4th Floor, Riverside Drive, Nairobi, Kenya</p>")
c = c.replace("<h3>+1 253 565 2365</h3>\n                            <p>Mon to Fri 9am to 6pm</p>",
              "<h3>%s</h3>\n                            <p>Mon to Fri, 8.30am to 5pm EAT</p>" % B.PHONE)
c = c.replace("<h3>support@colorlib.com</h3>\n                            <p>Send us your query anytime!</p>",
              "<h3>%s</h3>\n                            <p>We reply within two working days</p>" % B.EMAIL)
EXTRA = """        <section class="section-padding30 pt-0">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-heart"></i></span><h4>Donations &amp; receipts</h4>
                        <p>donations@ubunturising.org<br>M-PESA Paybill 400200, account URF</p></div></div>
                    <div class="col-lg-4 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-briefcase"></i></span><h4>Partnerships &amp; grants</h4>
                        <p>partnerships@ubunturising.org<br>Capability statement on request</p></div></div>
                    <div class="col-lg-4 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-shield"></i></span><h4>Safeguarding concerns</h4>
                        <p>safeguarding@ubunturising.org<br>Reports go straight to our board lead</p></div></div>
                </div>
            </div>
        </section>
"""
c = c + EXTRA + B.CTA_BAND
B.page("contact.html", "Contact us",
       "Contact Ubuntu Rising Foundation in Nairobi: donations, partnerships, volunteering and safeguarding enquiries.",
       c)

# ------------------------------------------------------------- elements.html
e = main_of("elements.html")
e = e.replace("<h2>Elements</h2>", "<h2>Style guide</h2>")
e = e.replace('<li class="breadcrumb-item"><a href="#">Element</a></li>',
              '<li class="breadcrumb-item"><a href="#">Style guide</a></li>')
B.page("elements.html", "Style guide",
       "Typography, buttons and form components used across the Ubuntu Rising Foundation website.", e)
print("pages2 done")
