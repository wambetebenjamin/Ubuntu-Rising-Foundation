#!/usr/bin/env python3
"""
Static site generator for the Ubuntu Rising Foundation website.

The markup, CSS, JS and component library come from the original Colorlib
"Environmental Organization" template that was supplied as a zip. This script
assembles the pages so the shared chrome (head, header, footer, scripts) only
has to be maintained in one place. Run:

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
    "phone": "+254 20 790 4120",
    "phone_href": "+254207904120",
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
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/owl.carousel.min.css">
    <link rel="stylesheet" href="assets/css/slicknav.css">
    <link rel="stylesheet" href="assets/css/flaticon.css">
    <link rel="stylesheet" href="assets/css/progressbar_barfiller.css">
    <link rel="stylesheet" href="assets/css/gijgo.css">
    <link rel="stylesheet" href="assets/css/animate.min.css">
    <link rel="stylesheet" href="assets/css/animated-headline.css">
    <link rel="stylesheet" href="assets/css/magnific-popup.css">
    <link rel="stylesheet" href="assets/css/fontawesome-all.min.css">
    <link rel="stylesheet" href="assets/css/themify-icons.css">
    <link rel="stylesheet" href="assets/css/slick.css">
    <link rel="stylesheet" href="assets/css/nice-select.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/urf.css">
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
                                        <a href="donate.html" class="btn header-btn">Donate Now</a>
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
                                        <li class="number"><a href="tel:{phone_href}">{phone}</a></li>
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
                                    <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                                        Copyright &copy;<script>document.write(new Date().getFullYear());</script> Ubuntu Rising Foundation. All rights reserved | Template by <a href="https://colorlib.com" target="_blank" rel="noopener">Colorlib</a>
                                        <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <div id="back-top">
        <a title="Go to Top" href="#"> <i class="fas fa-level-up-alt"></i></a>
    </div>

    <!-- JS here -->
    <script src="./assets/js/vendor/modernizr-3.5.0.min.js"></script>
    <script src="./assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="./assets/js/popper.min.js"></script>
    <script src="./assets/js/bootstrap.min.js"></script>
    <script src="./assets/js/jquery.slicknav.min.js"></script>
    <script src="./assets/js/owl.carousel.min.js"></script>
    <script src="./assets/js/slick.min.js"></script>
    <script src="./assets/js/wow.min.js"></script>
    <script src="./assets/js/animated.headline.js"></script>
    <script src="./assets/js/jquery.magnific-popup.js"></script>
    <script src="./assets/js/jquery.nice-select.min.js"></script>
    <script src="./assets/js/jquery.sticky.js"></script>
    <script src="./assets/js/jquery.barfiller.js"></script>
    <script src="./assets/js/jquery.counterup.min.js"></script>
    <script src="./assets/js/waypoints.min.js"></script>
    <script src="./assets/js/hover-direction-snake.min.js"></script>
    <script src="./assets/js/contact.js"></script>
    <script src="./assets/js/jquery.form.js"></script>
    <script src="./assets/js/jquery.validate.min.js"></script>
    <script src="./assets/js/mail-script.js"></script>
    <script src="./assets/js/jquery.ajaxchimp.min.js"></script>
    <script src="./assets/js/plugins.js"></script>
    <script src="./assets/js/main.js"></script>
    <script src="./assets/js/urf.js"></script>
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
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-xl-8 col-lg-8">
                        <div class="urf-cta-text">
                            <h3>Ubuntu means none of us rises alone.</h3>
                            <p>KES 2,500 keeps a girl in school for a term. KES 180,000 gives a village a borehole that
                                lasts a generation. Whatever you give, you will see exactly where it lands.</p>
                        </div>
                    </div>
                    <div class="col-xl-4 col-lg-4 text-lg-right">
                        <a href="donate.html" class="btn urf-btn-solid">Donate now</a>
                        <a href="volunteer.html" class="urf-link-arrow">Or volunteer <i class="ti-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </section>
        <!-- CTA band end -->
"""


def write(path, title, description, active, body):
    html = (
        HEAD.format(
            title=title,
            description=description,
            nav=nav_html(active),
            address=SITE["address"],
            email=SITE["email"],
            tagline=SITE["tagline"],
        )
        + body
        + FOOTER.format(
            email=SITE["email"],
            address=SITE["address"],
            po=SITE["po"],
            phone=SITE["phone"],
            phone_href=SITE["phone_href"],
            reg=SITE["reg"],
        )
    )
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", path)
