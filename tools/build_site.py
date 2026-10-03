#!/usr/bin/env python3
"""
Static site generator for the Ubuntu Rising Foundation website.

The markup, CSS, JS and component library come from the HTML template that was
supplied as a zip. This script assembles the pages so the shared chrome (head,
header, footer, scripts) only has to be maintained in one place. Run:

    python3 tools/build_site.py

...and the .html files in the repository root are regenerated.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = {
    "name": "Ubuntu Rising Foundation",
    "short": "Ubuntu Rising",
    "tagline": "I am because we are.",
    "email": "hello@ubunturising.org",
    "partnerships_email": "partnerships@ubunturising.org",
    # WhatsApp is the only telephone route exposed on the site. The number
    # itself is never rendered as text, only as a wa.me deep link.
    "wa": "254112272061",
    "wa_link": "https://wa.me/254112272061",
    "wa_link_donate": "https://wa.me/254112272061?text=Hello%20Ubuntu%20Rising%2C%20I%27d%20like%20to%20make%20a%20donation.",
    "wa_link_volunteer": "https://wa.me/254112272061?text=Hello%20Ubuntu%20Rising%2C%20I%27d%20like%20to%20volunteer.",
    "wa_link_partner": "https://wa.me/254112272061?text=Hello%20Ubuntu%20Rising%2C%20I%27d%20like%20to%20discuss%20a%20partnership.",
    "address": "Ubuntu House, 4th Floor, Riverside Drive, Westlands, Nairobi, Kenya",
    "po": "P.O. Box 48230-00100, Nairobi",
    "reg": "Registered NGO No. OP.218/051/23-089/1174",
}

# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------

NAV = [
    ("Home", "index.html", []),
    ("About", "about.html", []),
    ("Programmes", "programmes.html", []),
    ("Our Work", "projects.html", [
        ("Current Projects", "projects.html"),
        ("Impact & Transparency", "impact.html"),
    ]),
    ("Get Involved", "volunteer.html", [
        ("Volunteer", "volunteer.html"),
        ("Corporate Partners", "partners.html"),
    ]),
    ("News", "blog.html", [
        ("Latest News", "blog.html"),
        ("Story Detail", "blog_details.html"),
    ]),
    ("Contact", "contact.html", []),
]


def nav_html(active):
    out = []
    for label, href, children in NAV:
        cls = ' class="active"' if active in ([href] + [c[1] for c in children]) else ""
        if children:
            sub = "".join(
                f'<li><a href="{c_href}">{c_label}</a></li>' for c_label, c_href in children
            )
            out.append(
                f'<li{cls}><a href="{href}">{label}</a><ul class="submenu">{sub}</ul></li>'
            )
        else:
            out.append(f'<li{cls}><a href="{href}">{label}</a></li>')
    return "\n                                                ".join(out)


# ---------------------------------------------------------------------------
# Shared chrome
# ---------------------------------------------------------------------------

HEAD = """<!doctype html>
<html class="no-js" lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="assets/img/hero/h1_hero1.jpg">
    <link rel="shortcut icon" type="image/svg+xml" href="assets/img/logo/mark.svg">

    <!-- CSS here -->
    <link rel="preload" href="assets/fonts/webfonts/plus-jakarta-sans-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="assets/fonts/webfonts/montserrat-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="assets/css/bundle.min.css?v={asset_v}">
</head>

<body>
    <!-- Preloader Start -->
    <div id="preloader-active">
        <div class="preloader d-flex align-items-center justify-content-center">
            <div class="preloader-inner position-relative">
                <div class="preloader-circle"></div>
                <div class="preloader-img pere-text">
                    <img src="assets/img/logo/mark.svg" alt="Ubuntu Rising Foundation">
                </div>
            </div>
        </div>
    </div>
    <!-- Preloader End -->

    <header>
        <div class="header-area">
            <div class="main-header">
                <div class="header-top d-none d-lg-block">
                    <div class="container-fluid">
                        <div class="row align-items-center">
                            <div class="col-lg-7">
                                <div class="header-info-left">
                                    <span><i class="ti-location-pin"></i> {address}</span>
                                    <span class="ml-25"><i class="ti-email"></i> <a href="mailto:{email}">{email}</a></span>
                                    <span class="ml-25"><i class="ti-comment-alt"></i> <a href="{wa_link}" target="_blank" rel="noopener">Chat with us on WhatsApp</a></span>
                                </div>
                            </div>
                            <div class="col-lg-5">
                                <div class="header-info-right text-right">
                                    <span class="urf-tagline">&ldquo;{tagline}&rdquo;</span>
                                    <a href="#" aria-label="Ubuntu Rising on X"><i class="fab fa-twitter"></i></a>
                                    <a href="#" aria-label="Ubuntu Rising on Facebook"><i class="fab fa-facebook-f"></i></a>
                                    <a href="#" aria-label="Ubuntu Rising on Instagram"><i class="fab fa-instagram"></i></a>
                                    <a href="#" aria-label="Ubuntu Rising on LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="header-bottom header-sticky">
                    <div class="container-fluid">
                        <div class="row align-items-center">
                            <div class="col-xl-3 col-lg-3 col-md-6 col-6">
                                <div class="logo">
                                    <a href="index.html"><img src="assets/img/logo/logo.svg" alt="Ubuntu Rising Foundation" width="230" height="50"></a>
                                </div>
                            </div>
                            <div class="col-xl-9 col-lg-9">
                                <div class="menu-wrapper d-flex align-items-center justify-content-end">
                                    <div class="main-menu d-none d-lg-block">
                                        <nav>
                                            <ul id="navigation">
                                                {nav}
                                            </ul>
                                        </nav>
                                    </div>
                                    <div class="header-right-btn d-none d-lg-block ml-20">
                                        <a href="donate.html" class="btn header-btn urf-btn-pulse">Donate <i class="ti-arrow-right"></i></a>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="mobile_menu d-block d-lg-none"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <main>
"""

FOOTER = """    </main>

    <footer>
        <div class="footer-wrapper">
            <div class="footer-area footer-padding">
                <div class="container">
                    <div class="row justify-content-between">
                        <div class="col-xl-4 col-lg-4 col-md-8 col-sm-8">
                            <div class="single-footer-caption mb-50">
                                <div class="single-footer-caption mb-30">
                                    <div class="footer-logo mb-35">
                                        <a href="index.html"><img src="assets/img/logo/logo-white.svg" alt="Ubuntu Rising Foundation" width="235" height="51"></a>
                                    </div>
                                    <div class="footer-tittle">
                                        <div class="footer-pera">
                                            <p>Ubuntu Rising Foundation is a Kenyan-registered non-profit working alongside
                                                communities across East Africa on education, clean water, women&rsquo;s
                                                livelihoods and climate resilience. {reg}.</p>
                                        </div>
                                    </div>
                                    <div class="footer-social">
                                        <a href="#" aria-label="X"><i class="fab fa-twitter"></i></a>
                                        <a href="#" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                                        <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                                        <a href="#" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-xl-2 col-lg-2 col-md-4 col-sm-4">
                            <div class="single-footer-caption mb-50">
                                <div class="footer-tittle">
                                    <h4>Our programmes</h4>
                                    <ul>
                                        <li><a href="programmes.html#education">Education &amp; Scholarships</a></li>
                                        <li><a href="programmes.html#water">Clean Water &amp; Sanitation</a></li>
                                        <li><a href="programmes.html#women">Women&rsquo;s Livelihoods</a></li>
                                        <li><a href="programmes.html#health">Community Health</a></li>
                                        <li><a href="programmes.html#climate">Youth Climate Action</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-xl-2 col-lg-2 col-md-4 col-sm-4">
                            <div class="single-footer-caption mb-50">
                                <div class="footer-tittle">
                                    <h4>Get involved</h4>
                                    <ul>
                                        <li><a href="donate.html">Make a donation</a></li>
                                        <li><a href="volunteer.html">Volunteer with us</a></li>
                                        <li><a href="partners.html">Corporate partnership</a></li>
                                        <li><a href="impact.html">Impact &amp; reports</a></li>
                                        <li><a href="blog.html">News &amp; stories</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-xl-3 col-lg-3 col-md-6 col-sm-4">
                            <div class="single-footer-caption mb-50">
                                <div class="footer-tittle">
                                    <h4>Contact us</h4>
                                    <ul>
                                        <li><a href="mailto:{email}">{email}</a></li>
                                        <li><a href="#">{address}</a></li>
                                        <li><a href="#">{po}</a></li>
                                        <li><a href="{wa_link}" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i> Chat on WhatsApp</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer-bottom-area">
                <div class="container">
                    <div class="footer-border">
                        <div class="row d-flex align-items-center">
                            <div class="col-xl-12">
                                <div class="footer-copy-right text-center">
                                    <p>Copyright &copy;<script>document.write(new Date().getFullYear());</script> Ubuntu Rising Foundation. All rights reserved.
                                        <a href="impact.html">Transparency</a> &middot; <a href="#">Privacy policy</a> &middot; <a href="#">Safeguarding</a></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <!-- Floating WhatsApp -->
    <a class="urf-wa-float" href="{wa_link}" target="_blank" rel="noopener" aria-label="Chat with Ubuntu Rising on WhatsApp">
        <i class="fab fa-whatsapp"></i>
        <span>Chat with us</span>
    </a>

    <div id="back-top">
        <a title="Go to Top" href="#"> <i class="fas fa-level-up-alt"></i></a>
    </div>

    <!-- JS here -->
    <script src="assets/js/bundle.min.js?v={asset_v}" defer></script>
</body>

</html>
"""


def bradcam(title, crumb, bg="bradcam"):
    return f"""        <!-- Page title -->
        <div class="bradcam_area {bg}">
            <div class="container">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="bradcam_text text-center">
                            <h3>{title}</h3>
                            <nav aria-label="breadcrumb">
                                <ol class="breadcrumb justify-content-center">
                                    <li class="breadcrumb-item"><a href="index.html">Home</a></li>
                                    <li class="breadcrumb-item active" aria-current="page">{crumb}</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Page title end -->
"""


CTA_BAND = """        <!-- CTA band -->
        <section class="urf-cta-band">
            <div class="urf-cta-glow" aria-hidden="true"></div>
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-xl-7 col-lg-7">
                        <div class="urf-cta-text">
                            <span class="urf-eyebrow">Support our work</span>
                            <h3>Your giving turns into school terms, boreholes and businesses</h3>
                            <p>KES 2,500 keeps a girl in school for a term. KES 1.8M gives a village a solar borehole
                                that lasts a generation. Every gift is reported back to you within 90 days.</p>
                        </div>
                    </div>
                    <div class="col-xl-5 col-lg-5">
                        <div class="urf-cta-actions">
                            <a href="donate.html" class="btn urf-btn-solid urf-btn-lg">Donate now <i class="ti-arrow-right"></i></a>
                            <a href="{wa_link_donate}" target="_blank" rel="noopener" class="urf-btn-wa">
                                <i class="fab fa-whatsapp"></i> Give via WhatsApp
                            </a>
                            <a href="volunteer.html" class="urf-link-arrow">Or volunteer your skills <i class="ti-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- CTA band end -->
"""


ASSET_V = "1"


def write(path, title, description, active, body):
    html = (
        HEAD.format(
            asset_v=ASSET_V,
            title=title,
            description=description,
            nav=nav_html(active),
            address=SITE["address"],
            email=SITE["email"],
            tagline=SITE["tagline"],
            wa_link=SITE["wa_link"],
        )
        + body
        + FOOTER.format(
            asset_v=ASSET_V,
            email=SITE["email"],
            address=SITE["address"],
            po=SITE["po"],
            wa_link=SITE["wa_link"],
            reg=SITE["reg"],
        )
    )
    html = lazyload_images(html)
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", path)


def lazyload_images(html):
    """Defer off-screen photography.

    Every <img> gets loading="lazy" and decoding="async" except the logo, which
    sits in the header and is needed for the first paint. Saves ~10 blocking
    image requests per page.
    """

    def repl(match):
        tag = match.group(0)
        if "loading=" in tag or "/logo/" in tag:
            return tag
        return tag[:-1].rstrip() + ' loading="lazy" decoding="async">'

    return re.sub(r"<img\b[^>]*>", repl, html)


# ---------------------------------------------------------------------------
# Asset bundling
#
# The template shipped 16 stylesheets and 24 scripts, so every page cost ~40
# round trips before it could render. They are concatenated here, in their
# original order, into one CSS and one JS file. Order is preserved exactly,
# so cascade and jQuery plugin registration behave as before.
# ---------------------------------------------------------------------------

CSS_FILES = ['assets/css/urf-fonts.css', 'assets/css/bootstrap.min.css', 'assets/css/owl.carousel.min.css', 'assets/css/slicknav.css', 'assets/css/flaticon.css', 'assets/css/progressbar_barfiller.css', 'assets/css/gijgo.css', 'assets/css/animate.min.css', 'assets/css/animated-headline.css', 'assets/css/magnific-popup.css', 'assets/css/fontawesome-all.min.css', 'assets/css/themify-icons.css', 'assets/css/slick.css', 'assets/css/nice-select.css', 'assets/css/style.css', 'assets/css/urf.css']

JS_FILES = ['assets/js/vendor/modernizr-3.5.0.min.js', 'assets/js/vendor/jquery-1.12.4.min.js', 'assets/js/popper.min.js', 'assets/js/bootstrap.min.js', 'assets/js/jquery.slicknav.min.js', 'assets/js/owl.carousel.min.js', 'assets/js/slick.min.js', 'assets/js/wow.min.js', 'assets/js/animated.headline.js', 'assets/js/jquery.magnific-popup.js', 'assets/js/jquery.nice-select.min.js', 'assets/js/jquery.sticky.js', 'assets/js/jquery.barfiller.js', 'assets/js/jquery.counterup.min.js', 'assets/js/waypoints.min.js', 'assets/js/hover-direction-snake.min.js', 'assets/js/contact.js', 'assets/js/jquery.form.js', 'assets/js/jquery.validate.min.js', 'assets/js/mail-script.js', 'assets/js/jquery.ajaxchimp.min.js', 'assets/js/plugins.js', 'assets/js/main.js', 'assets/js/urf.js']


def _minify_css(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)       # comments
    text = re.sub(r"\s+", " ", text)                         # runs of whitespace
    text = re.sub(r"\s*([{}:;,>~])\s*", r"\1", text)         # space around punctuation
    text = text.replace(";}", "}")
    return text.strip()


def build_bundles(root):
    import hashlib, os

    css_out = []
    for rel in CSS_FILES:
        with open(os.path.join(root, rel), encoding="utf-8", errors="replace") as fh:
            css_out.append(_minify_css(fh.read()))
    css = "\n".join(css_out)
    with open(os.path.join(root, "assets/css/bundle.min.css"), "w", encoding="utf-8") as fh:
        fh.write(css)

    js_out = []
    for rel in JS_FILES:
        with open(os.path.join(root, rel), encoding="utf-8", errors="replace") as fh:
            # a trailing semicolon and newline keeps files that end mid-expression
            # or without a terminator from swallowing the next file
            js_out.append(fh.read().rstrip() + "\n;\n")
    js = "".join(js_out)
    with open(os.path.join(root, "assets/js/bundle.min.js"), "w", encoding="utf-8") as fh:
        fh.write(js)

    digest = hashlib.sha1((css + js).encode("utf-8")).hexdigest()[:10]
    print("bundled %d css + %d js -> %.0f KB css, %.0f KB js (v=%s)"
          % (len(CSS_FILES), len(JS_FILES), len(css) / 1024, len(js) / 1024, digest))
    return digest
