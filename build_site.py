# -*- coding: utf-8 -*-
"""Builds the Ubuntu Rising Foundation static site from the shared layout.
Run:  python3 build_site.py
"""
import io, os

ORG = "Ubuntu Rising Foundation"
EMAIL = "hello@ubunturising.org"
PHONE = "+254 20 460 8800"
ADDR = "Ubuntu House, 4th Floor, Riverside Drive, Nairobi, Kenya"

HEAD = """<!doctype html>
<html class="no-js" lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>{title} | Ubuntu Rising Foundation</title>
    <meta name="description" content="{desc}">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="manifest" href="site.webmanifest">
    <link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.ico">

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
    <link rel="stylesheet" href="assets/css/ubuntu.css">
</head>

<body>
    <!-- Preloader Start -->
    <div id="preloader-active">
        <div class="preloader d-flex align-items-center justify-content-center">
            <div class="preloader-inner position-relative">
                <div class="preloader-circle"></div>
                <div class="preloader-img pere-text">
                    <img src="assets/img/logo/loder.png" alt="Ubuntu Rising Foundation">
                </div>
            </div>
        </div>
    </div>
    <!-- Preloader End -->
    <header>
        <!-- Header Start -->
        <div class="header-area">
            <div class="main-header ">
                <div class="header-bottom  header-sticky">
                    <div class="container-fluid">
                        <div class="row align-items-center">
                            <!-- Logo -->
                            <div class="col-xl-2 col-lg-2">
                                <div class="logo">
                                    <a href="index.html"><img src="assets/img/logo/logo.png" alt="Ubuntu Rising Foundation"></a>
                                </div>
                            </div>
                            <div class="col-xl-10 col-lg-10">
                                <div class="menu-wrapper  d-flex align-items-center justify-content-end">
                                    <!-- Main-menu -->
                                    <div class="main-menu d-none d-lg-block">
                                        <nav>
                                            <ul id="navigation">
                                                <li><a href="index.html">Home</a></li>
                                                <li><a href="about.html">About</a></li>
                                                <li><a href="what-do.html">What we Do</a></li>
                                                <li><a href="projects.html">Projects</a></li>
                                                <li><a href="volunteer.html">Get Involved</a>
                                                    <ul class="submenu">
                                                        <li><a href="volunteer.html">Volunteer</a></li>
                                                        <li><a href="partners.html">Corporate Partners</a></li>
                                                        <li><a href="donate.html">Donate</a></li>
                                                    </ul>
                                                </li>
                                                <li><a href="blog.html">News</a>
                                                    <ul class="submenu">
                                                        <li><a href="blog.html">Latest Stories</a></li>
                                                        <li><a href="blog_details.html">Story Details</a></li>
                                                        <li><a href="elements.html">Style Guide</a></li>
                                                    </ul>
                                                </li>
                                                <li><a href="contact.html">Contact</a></li>
                                            </ul>
                                        </nav>
                                    </div>
                                    <!-- Header-btn -->
                                    <div class="header-right-btn d-none d-lg-block ml-20">
                                        <a href="donate.html" class="btn header-btn">Donate Now</a>
                                    </div>
                                </div>
                            </div>
                            <!-- Mobile Menu -->
                            <div class="col-12">
                                <div class="mobile_menu d-block d-lg-none"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Header End -->
    </header>
    <main>
"""

FOOT = """    </main>
    <footer>
        <div class="footer-wrapper">
           <!-- Footer Start-->
           <div class="footer-area footer-padding">
               <div class="container ">
                   <div class="row justify-content-between">
                       <div class="col-xl-4 col-lg-3 col-md-8 col-sm-8">
                           <div class="single-footer-caption mb-50">
                               <div class="single-footer-caption mb-30">
                                   <!-- logo -->
                                   <div class="footer-logo mb-35">
                                       <a href="index.html"><img src="assets/img/logo/logo2_footer.png" alt="Ubuntu Rising Foundation"></a>
                                   </div>
                                   <div class="footer-tittle">
                                       <div class="footer-pera">
                                           <p>Ubuntu Rising Foundation is a Kenyan non-profit working with communities
                                           across East Africa on water, education, health and livelihoods. Registered
                                           in Nairobi, NGO Co-ordination Board No. OP/218/051/24-0117.</p>
                                       </div>
                                   </div>
                                   <!-- social -->
                                   <div class="footer-social">
                                       <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                                       <a href="#" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                                       <a href="#" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                                   </div>
                               </div>
                           </div>
                       </div>
                       <div class="col-xl-2 col-lg-3 col-md-4 col-sm-4">
                           <div class="single-footer-caption mb-50">
                               <div class="footer-tittle">
                                   <h4>Our programmes</h4>
                                   <ul>
                                       <li><a href="what-do.html">Water &amp; sanitation</a></li>
                                       <li><a href="what-do.html">Education &amp; scholarships</a></li>
                                       <li><a href="what-do.html">Community health</a></li>
                                       <li><a href="what-do.html">Women's livelihoods</a></li>
                                       <li><a href="what-do.html">Climate resilience</a></li>
                                   </ul>
                               </div>
                           </div>
                       </div>
                       <div class="col-xl-2 col-lg-2 col-md-4 col-sm-4">
                           <div class="single-footer-caption mb-50">
                               <div class="footer-tittle">
                                   <h4>Get involved</h4>
                                   <ul>
                                       <li><a href="donate.html">Donate</a></li>
                                       <li><a href="volunteer.html">Volunteer</a></li>
                                       <li><a href="partners.html">Corporate partners</a></li>
                                       <li><a href="about.html">Annual reports</a></li>
                                   </ul>
                               </div>
                           </div>
                       </div>
                       <div class="col-xl-3 col-lg-4 col-md-6 col-sm-4">
                           <div class="single-footer-caption mb-50">
                               <div class="footer-tittle">
                                   <h4>Contact us</h4>
                                   <ul>
                                       <li><a href="mailto:%EMAIL%">%EMAIL%</a></li>
                                       <li><a href="contact.html">%ADDR%</a></li>
                                       <li><a href="contact.html">Privacy &amp; safeguarding policy</a></li>
                                       <li class="number"><a href="tel:+254204608800">%PHONE%</a></li>
                                   </ul>
                               </div>
                           </div>
                       </div>
                   </div>
               </div>
           </div>
           <!-- footer-bottom area -->
           <div class="footer-bottom-area">
               <div class="container">
                   <div class="footer-border">
                       <div class="row d-flex align-items-center">
                           <div class="col-xl-12 ">
                               <div class="footer-copy-right text-center">
                                   <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                                      Copyright &copy;<script>document.write(new Date().getFullYear());</script> Ubuntu Rising Foundation. All rights reserved | This template is made with <i class="fa fa-heart" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
                                      <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
              <!-- Footer End-->
          </div>
      </footer>
      <!-- Scroll Up -->
      <div id="back-top" >
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
    <script src="./assets/js/gijgo.min.js"></script>
    <script src="./assets/js/jquery.nice-select.min.js"></script>
    <script src="./assets/js/jquery.sticky.js"></script>
    <script src="./assets/js/jquery.barfiller.js"></script>
    <script src="./assets/js/jquery.counterup.min.js"></script>
    <script src="./assets/js/waypoints.min.js"></script>
    <script src="./assets/js/jquery.countdown.min.js"></script>
    <script src="./assets/js/hover-direction-snake.min.js"></script>
    <script src="./assets/js/contact.js"></script>
    <script src="./assets/js/jquery.form.js"></script>
    <script src="./assets/js/jquery.validate.min.js"></script>
    <script src="./assets/js/mail-script.js"></script>
    <script src="./assets/js/jquery.ajaxchimp.min.js"></script>
    <script src="./assets/js/plugins.js"></script>
    <script src="./assets/js/main.js"></script>
    <script src="./assets/js/ubuntu.js"></script>
</body>
</html>
""".replace("%EMAIL%", EMAIL).replace("%PHONE%", PHONE).replace("%ADDR%", ADDR)


def banner(title, crumb):
    return """        <!-- Hero Start -->
        <div class="slider-area2">
            <div class="slider-height2 d-flex align-items-center">
                <div class="container">
                    <div class="row">
                        <div class="col-xl-12">
                            <div class="hero-cap hero-cap2 pt-70">
                                <h2>%s</h2>
                                <nav aria-label="breadcrumb">
                                    <ol class="breadcrumb">
                                        <li class="breadcrumb-item"><a href="index.html">Home</a></li>
                                        <li class="breadcrumb-item"><a href="#">%s</a></li>
                                    </ol>
                                </nav>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Hero End -->
""" % (title, crumb)


# ---------------------------------------------------------------- shared blocks
PILLARS = """        <!-- Programme pillars Start -->
        <div class="service-area section-padding30">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-11">
                        <div class="single-cat text-center mb-30">
                            <div class="cat-icon">
                                <img src="assets/img/gallery/services1.png" alt="A community water point in rural Kenya">
                            </div>
                            <div class="cat-cap">
                                <h5><a href="what-do.html">Water &amp; Sanitation</a></h5>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-11">
                        <div class="single-cat active text-center mb-30">
                            <div class="cat-icon">
                                <img src="assets/img/gallery/services2.png" alt="Learners sharing a laptop in a community digital lab">
                            </div>
                            <div class="cat-cap">
                                <h5><a href="what-do.html">Education &amp; Skills</a></h5>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-11">
                        <div class="single-cat text-center mb-30">
                            <div class="cat-icon">
                                <img src="assets/img/gallery/services3.png" alt="Community health workers in a training session">
                            </div>
                            <div class="cat-cap">
                                <h5><a href="what-do.html">Community Health</a></h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Programme pillars End -->
"""

MISSION = """        <!-- Mission Start -->
        <div class="visit-tailor-area fix">
            <div class="tailor-offers"></div>
            <div class="tailor-details">
                <span>Our Mission</span>
                <h2>Dignity first, delivered with the community</h2>
                <p>Ubuntu Rising Foundation exists so that no household in East Africa is held back by
                    a lack of safe water, a missed school term or an unaffordable clinic visit.
                    Every project we run is designed with a community committee, delivered by local
                    artisans and technicians, and handed over with a maintenance fund already in place.</p>
                <p class="pera-bottom">&ldquo;I am because we are&rdquo; is not a slogan for us &ndash; it is a budget line.
                    Eighty-seven cents of every shilling we receive reaches programmes in Kenya, Uganda,
                    Tanzania and Rwanda, and our audited accounts are published every February.</p>
                <div class="footer-tittles">
                    <p>Executive Director, Ubuntu Rising Foundation</p>
                    <h2>Amina Wanjiru Otieno</h2>
                </div>
            </div>
        </div>
        <!-- Mission End -->
"""


def support(cta_href="volunteer.html", cta="Join Us Today", extra=""):
    return """        <!-- Why join us Start -->
        <section class="support-company-area fix pt-10%s">
            <div class="support-wrapper align-items-center">
                <div class="left-content">
                    <div class="section-tittle section-tittle2 mb-30">
                        <span>Why you should join us</span>
                        <h2>Local teams, measured results, open books</h2>
                    </div>
                    <div class="support-caption">
                        <p class="pera-top">Ninety-four per cent of our staff and volunteers are East African.
                            We publish the cost per beneficiary of every programme, we survey the
                            households we serve twice a year, and we never start a project we cannot
                            hand over to the community within 24 months.</p>
                        <a href="%s" class="border-btn">%s</a>
                    </div>
                </div>
                <div class="right-content">
                    <div class="right-img">
                        <img src="assets/img/gallery/safe_in.png" alt="Volunteers packing relief and hygiene kits">
                    </div>
                    <div class="support-img-cap text-center d-flex">
                        <div class="single-one">
                            <span>128</span>
                            <p>Projects delivered</p>
                        </div>
                        <div class="single-two">
                            <span>2,400</span>
                            <p>Active volunteers</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Why join us End -->
""" % (extra, cta_href, cta)


APPEALS = """        <!-- Appeals Start -->
        <div class="our-cases-area section-padding30">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-10 col-lg-10 ">
                        <div class="section-tittle text-center mb-80">
                            <h2>Three appeals that need you this quarter</h2>
                            <p class="pl-20 pr-20">Each appeal is costed line by line and reported on monthly.
                            Choose the one closest to your heart, or let us direct your gift to where the
                            need is greatest today.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="single-cases mb-40">
                            <div class="cases-img">
                                <img src="assets/img/gallery/case1.png" alt="A girl drawing water from a village borehole">
                            </div>
                            <div class="cases-caption">
                                <h3><a href="donate.html">Turkana Borehole Appeal</a></h3>
                                <p>Twelve solar-powered boreholes for drought-hit villages in Turkana
                                    County, each serving about 900 people.</p>
                                <div class="single-skill mb-15">
                                    <div class="bar-progress">
                                        <div id="bar1" class="barfiller">
                                            <div class="tipWrap"><span class="tip"></span></div>
                                            <span class="fill" data-percentage="72"></span>
                                        </div>
                                    </div>
                                </div>
                                <div class="prices">
                                    <p><span>KES 5,420,000 of 7,500,000</span></p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="single-cases mb-40">
                            <div class="cases-img">
                                <img src="assets/img/gallery/case2.png" alt="A trainer leading a classroom session with students">
                            </div>
                            <div class="cases-caption">
                                <h3><a href="donate.html">Kibera Scholarship Fund</a></h3>
                                <p>Four-year secondary school scholarships, mentoring and exam
                                    support for 250 students from Nairobi's informal settlements.</p>
                                <div class="single-skill mb-15">
                                    <div class="bar-progress">
                                        <div id="bar2" class="barfiller">
                                            <div class="tipWrap"><span class="tip"></span></div>
                                            <span class="fill" data-percentage="45"></span>
                                        </div>
                                    </div>
                                </div>
                                <div class="prices">
                                    <p><span>KES 3,150,000 of 7,000,000</span></p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="single-cases">
                            <div class="cases-img">
                                <img src="assets/img/gallery/case3.png" alt="A young tailor working in a community workshop">
                            </div>
                            <div class="cases-caption">
                                <h3><a href="donate.html">Mama Biashara Grants</a></h3>
                                <p>Start-up grants, tools and twelve weeks of business coaching for
                                    600 women traders in Kisumu, Mwanza and Kampala.</p>
                                <div class="single-skill mb-15">
                                    <div class="bar-progress">
                                        <div id="bar3" class="barfiller">
                                            <div class="tipWrap"><span class="tip"></span></div>
                                            <span class="fill" data-percentage="58"></span>
                                        </div>
                                    </div>
                                </div>
                                <div class="prices">
                                    <p><span>KES 2,900,000 of 5,000,000</span></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Appeals End -->
"""

STATS = """        <!-- Impact counters Start -->
        <div class="impact-area">
            <div class="container">
                <div class="row">
                    <div class="col-lg-3 col-md-6"><div class="single-impact text-center">
                        <span class="counter">214000</span><p>People reached since 2012</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-impact text-center">
                        <span class="counter">186</span><p>Water points built &amp; maintained</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-impact text-center">
                        <span class="counter">3120</span><p>Scholarships awarded</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-impact text-center">
                        <span class="counter">87</span><p>Pence in every pound to programmes</p></div></div>
                </div>
            </div>
        </div>
        <!-- Impact counters End -->
"""

WAYS = """        <!-- Ways to give Start -->
        <div class="ways-area section-padding30">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-9">
                        <div class="section-tittle text-center mb-70">
                            <h2>Three ways to rise with us</h2>
                            <p>Whether you give, give time, or bring your company along, your support turns
                            into boreholes, classrooms and clinics managed by the people who use them.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6">
                        <div class="single-way mb-30">
                            <span class="way-icon"><i class="ti-heart"></i></span>
                            <h4>Donate</h4>
                            <p>Give once or monthly by card, M-PESA Paybill or bank transfer. KES 2,500 a
                            month keeps a village water point serviced all year.</p>
                            <a href="donate.html" class="way-link">Make a donation <i class="ti-arrow-right"></i></a>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="single-way mb-30">
                            <span class="way-icon"><i class="ti-user"></i></span>
                            <h4>Volunteer</h4>
                            <p>Join a Saturday build in Nairobi, mentor a scholarship student online, or
                            lend professional skills in finance, water engineering or design.</p>
                            <a href="volunteer.html" class="way-link">Sign up to volunteer <i class="ti-arrow-right"></i></a>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="single-way mb-30">
                            <span class="way-icon"><i class="ti-briefcase"></i></span>
                            <h4>Partner</h4>
                            <p>CSR programmes, employee giving, payroll matching and co-funded county
                            projects with quarterly impact reporting your board can use.</p>
                            <a href="partners.html" class="way-link">Talk to our partnerships team <i class="ti-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Ways to give End -->
"""

PARTNERS_STRIP = """        <!-- Partner logos Start -->
        <div class="partner-strip">
            <div class="container">
                <p class="text-center">Trusted by funders and corporate partners across the region</p>
                <ul class="partner-list">
                    <li>Safari Telecom Foundation</li>
                    <li>East Africa Trust</li>
                    <li>Mazingira Fund</li>
                    <li>Rift Valley Bank</li>
                    <li>Jua Kali Logistics</li>
                    <li>Nile Insurance Group</li>
                </ul>
            </div>
        </div>
        <!-- Partner logos End -->
"""

NEWS = """        <!-- Latest stories Start -->
        <section class="home-blog-area pb-padding">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8 col-lg-9 col-md-11">
                        <div class="section-tittle text-center mb-90">
                            <h2>Latest from the field</h2>
                            <p>Field notes, impact data and the voices of the people we work with &ndash;
                            published every fortnight by our programme teams.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-xl-6 col-lg-6 col-md-6">
                        <div class="home-blog-single mb-30">
                            <div class="blog-img-cap">
                                <div class="blog-img">
                                    <img src="assets/img/gallery/home-blog1.png" alt="Volunteers sorting donated supplies">
                                </div>
                                <div class="blog-cap">
                                    <h3><a href="blog_details.html">How 40 volunteers packed 1,800 hygiene kits in a weekend</a></h3>
                                    <p>Our Nairobi volunteer chapter turned a warehouse in Industrial Area into
                                    a production line for families displaced by the April floods.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-6 col-lg-6 col-md-6">
                        <div class="home-blog-single mb-30">
                            <div class="blog-img-cap">
                                <div class="blog-img">
                                    <img src="assets/img/gallery/home-blog2.png" alt="Women of a village savings group meeting outdoors">
                                </div>
                                <div class="blog-cap">
                                    <h3><a href="blog_details.html">Nine savings groups, one year: what the numbers say</a></h3>
                                    <p>Average household income in our Kisumu cohort rose 38% after twelve
                                    months of grants, coaching and group savings.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Latest stories End -->
"""

CTA_BAND = """        <!-- Donate band Start -->
        <div class="donate-band">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-8">
                        <h2>KES 1,500 gives one family safe water for a year.</h2>
                        <p>Give today and we will send you the GPS location and photographs of the water point your gift helps build.</p>
                    </div>
                    <div class="col-lg-4 text-lg-right">
                        <a href="donate.html" class="btn header-btn">Donate now</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Donate band End -->
"""


def page(fn, title, desc, body):
    html = HEAD.format(title=title, desc=desc) + body + FOOT
    with io.open(fn, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fn, len(html))


# ---------------------------------------------------------------- index
slides = [
    ("slider-bg1", "Ubuntu Rising",
     "Communities across East Africa rising together &ndash;<br> with water, schooling, health and work.",
     "donate.html", "Donate Now"),
    ("slider-bg2", "Safe water, close to home",
     "186 water points built with the villages that now<br> own and maintain every one of them.",
     "projects.html", "See our projects"),
    ("slider-bg3", "Stand with us",
     "2,400 volunteers and 40 corporate partners<br> make this work possible. Add your name.",
     "volunteer.html", "Get involved"),
]
slider = """        <!-- slider Area Start-->
        <div class="slider-area position-relative">
            <div class="slider-active dot-style">
"""
for cls, h1, p, href, label in slides:
    slider += """                <!-- Single Slider -->
                <div class="single-slider hero-overly slider-height %s d-flex align-items-center">
                    <div class="container">
                        <div class="row">
                            <div class="col-xl-8 col-lg-8 col-md-8 col-sm-10">
                                <div class="hero__caption">
                                    <h1 data-animation="fadeInUp" data-delay=".2s">%s</h1>
                                    <P data-animation="fadeInUp" data-delay=".4s">%s</P>
                                    <div class="hero__btn">
                                        <a href="%s" class="hero-btn mb-10"  data-animation="fadeInUp" data-delay=".8s">%s</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
""" % (cls, h1, p, href, label)
slider += """            </div>
        </div>
        <!-- slider Area End-->
"""

page("index.html", "Water, schools and livelihoods across East Africa",
     "Ubuntu Rising Foundation is a Nairobi-based NGO delivering clean water, education, health and livelihood programmes across East Africa. Donate, volunteer or partner with us.",
     slider + STATS + MISSION + PILLARS + support() + APPEALS + WAYS + PARTNERS_STRIP + NEWS + CTA_BAND)

# ---------------------------------------------------------------- about
about_story = """        <!-- Story Start -->
        <section class="about-story section-padding30">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6">
                        <div class="section-tittle mb-30">
                            <span>Our story</span>
                            <h2>From one water tank in Mathare to four countries</h2>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <p>Ubuntu Rising Foundation began in 2012 when a group of teachers, nurses and
                        engineers in Mathare, Nairobi, pooled KES 180,000 to install a single 10,000-litre
                        water tank for a school that had gone three terms without running water.</p>
                        <p>Thirteen years later we work in 27 counties and districts across Kenya, Uganda,
                        Tanzania and Rwanda, with 64 full-time staff, 2,400 registered volunteers and a
                        single rule that has never changed: the community decides, we deliver with them,
                        and we hand it over.</p>
                    </div>
                </div>
                <div class="row mt-50">
                    <div class="col-lg-4 col-md-6">
                        <div class="single-value mb-30">
                            <h4>Ubuntu</h4>
                            <p>We are because our neighbours are. Communities lead the design and own the
                            asset &ndash; we are the partner, never the owner.</p>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="single-value mb-30">
                            <h4>Open books</h4>
                            <p>Audited accounts, project budgets and cost-per-beneficiary figures are
                            published every February on this website.</p>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="single-value mb-30">
                            <h4>Safeguarding</h4>
                            <p>Every staff member and volunteer is vetted and trained. Our safeguarding
                            lead reports directly to the board.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Story End -->
"""

about_team = """        <!-- Team Start -->
        <section class="team-area section-padding30 gray-bg">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8">
                        <div class="section-tittle text-center mb-70">
                            <h2>The people behind the work</h2>
                            <p>Our leadership team is based in Nairobi, with country coordinators in
                            Kampala, Mwanza and Kigali.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-3 col-md-6"><div class="single-team text-center mb-30">
                        <img src="assets/img/blog/comment_1.png" alt="Amina Wanjiru Otieno">
                        <h4>Amina Wanjiru Otieno</h4><p>Executive Director</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-team text-center mb-30">
                        <img src="assets/img/blog/comment_2.png" alt="Daniel Mwangi Kariuki">
                        <h4>Daniel Mwangi Kariuki</h4><p>Director of Programmes</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-team text-center mb-30">
                        <img src="assets/img/blog/comment_3.png" alt="Grace Nakato">
                        <h4>Grace Nakato</h4><p>Head of Partnerships, Uganda</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-team text-center mb-30">
                        <img src="assets/img/blog/author.png" alt="Joseph Lekuraiyo">
                        <h4>Joseph Lekuraiyo</h4><p>Finance &amp; Compliance Lead</p></div></div>
                </div>
            </div>
        </section>
        <!-- Team End -->
"""

about_gov = """        <!-- Governance Start -->
        <section class="section-padding30">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8">
                        <div class="section-tittle text-center mb-50">
                            <h2>Accountability &amp; governance</h2>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-6">
                        <ul class="tick-list">
                            <li>Registered with the Kenya NGO Co-ordination Board, No. OP/218/051/24-0117</li>
                            <li>Independently audited by Mwende &amp; Associates, Nairobi</li>
                            <li>Board of nine trustees, six of them from the communities we serve</li>
                            <li>Signatory to the Core Humanitarian Standard</li>
                        </ul>
                    </div>
                    <div class="col-lg-6">
                        <ul class="tick-list">
                            <li>Annual report and full financial statements published each February</li>
                            <li>Child protection and PSEA policies reviewed every two years</li>
                            <li>Anti-bribery, data protection and whistle-blowing policies in force</li>
                            <li>Donor data handled under the Kenya Data Protection Act, 2019</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        <!-- Governance End -->
"""

page("about.html", "About us",
     "Learn about Ubuntu Rising Foundation: our story from Mathare to four East African countries, our team, values and governance.",
     banner("About us", "About") + MISSION + about_story + about_team + about_gov + support() + CTA_BAND)

# ---------------------------------------------------------------- what we do
programmes = [
    ("Water &amp; sanitation", "assets/img/gallery/case1.png",
     "Solar-powered boreholes, rainwater harvesting at schools, latrine blocks and hygiene training. "
     "Every water point is handed to a community water committee with a serviced maintenance fund and "
     "two trained local technicians."),
    ("Education &amp; scholarships", "assets/img/gallery/case2.png",
     "Four-year secondary scholarships, digital learning labs, teacher coaching and holiday catch-up "
     "camps. 91% of our scholars complete Form 4 and 64% go on to college or a trade."),
    ("Community health", "assets/img/gallery/services3.png",
     "We train and equip community health promoters, run maternal health outreach clinics and supply "
     "county dispensaries with essential medicines through a transparent procurement partnership."),
    ("Women's livelihoods", "assets/img/gallery/case3.png",
     "Mama Biashara start-up grants, tools, bookkeeping and twelve weeks of coaching, delivered through "
     "village savings and loan associations that keep running long after we leave."),
    ("Climate resilience", "assets/img/gallery/services1.png",
     "Drought-tolerant seed, agroforestry, 1.2 million trees planted with schools, and county-level "
     "early warning systems for pastoralist communities in Turkana and Karamoja."),
    ("Emergency response", "assets/img/gallery/home-blog1.png",
     "Rapid hygiene kits, cash transfers and safe water trucking when floods or drought hit, delivered "
     "within 72 hours through our volunteer chapters and county partners."),
]
blocks = ""
for i, (t, img, txt) in enumerate(programmes):
    blocks += """                    <div class="col-lg-4 col-md-6">
                        <div class="single-programme mb-30">
                            <img src="%s" alt="%s">
                            <div class="programme-cap">
                                <h3>%s</h3>
                                <p>%s</p>
                                <a href="donate.html" class="way-link">Support this work <i class="ti-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>
""" % (img, t.replace("&amp;", "and"), t, txt)

approach = """        <!-- Approach Start -->
        <section class="section-padding30 gray-bg">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8">
                        <div class="section-tittle text-center mb-70">
                            <h2>How we work</h2>
                            <p>A four-step method we apply to every project, from a single school tank to a
                            county-wide water scheme.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-3 col-md-6"><div class="single-step mb-30"><span>01</span>
                        <h4>Listen</h4><p>A community assembly ranks its own priorities before a single budget line is written.</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-step mb-30"><span>02</span>
                        <h4>Co-design</h4><p>Local engineers, county officials and the community committee agree the design and the costs.</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-step mb-30"><span>03</span>
                        <h4>Build together</h4><p>We hire locally, train two technicians per site and publish spending as it happens.</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-step mb-30"><span>04</span>
                        <h4>Hand over</h4><p>Ownership, tools and a maintenance fund transfer to the community within 24 months.</p></div></div>
                </div>
            </div>
        </section>
        <!-- Approach End -->
"""

page("what-do.html", "What we do",
     "Our six programmes: water and sanitation, education, community health, women's livelihoods, climate resilience and emergency response across East Africa.",
     banner("What we do", "What we do") + PILLARS +
     """        <section class="section-padding30 pt-0">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-9">
                        <div class="section-tittle text-center mb-70">
                            <h2>Six programmes, one promise</h2>
                            <p>We only work where a community has asked us to, and we only stay until the
                            community can run the service itself.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
""" + blocks + """                </div>
            </div>
        </section>
""" + approach + support() + CTA_BAND)

# ---------------------------------------------------------------- projects
project_rows = [
    ("Turkana Solar Borehole Programme", "Turkana County, Kenya", "In progress",
     "assets/img/gallery/case1.png",
     "Twelve solar-powered boreholes and 24 trained technicians serving 10,800 people in Lodwar and Kakuma wards.",
     72, "KES 5,420,000 of 7,500,000"),
    ("Kibera Secondary Scholarships", "Nairobi, Kenya", "Recruiting",
     "assets/img/gallery/case2.png",
     "250 four-year scholarships with mentoring, exam coaching and a laptop lab at the Olympic community centre.",
     45, "KES 3,150,000 of 7,000,000"),
    ("Mama Biashara Grants", "Kisumu, Mwanza &amp; Kampala", "In progress",
     "assets/img/gallery/case3.png",
     "600 women traders receive a start-up grant, a toolkit and twelve weeks of business coaching.",
     58, "KES 2,900,000 of 5,000,000"),
    ("Karamoja Maternal Health Outreach", "Karamoja, Uganda", "In progress",
     "assets/img/gallery/services3.png",
     "Mobile antenatal clinics and 90 community health promoters covering 42 villages.",
     34, "KES 1,700,000 of 5,000,000"),
    ("Nyanza Green Schools", "Kisumu &amp; Siaya, Kenya", "Funded",
     "assets/img/gallery/services2.png",
     "Rainwater harvesting, 60,000 trees and digital labs in 34 primary schools.",
     100, "Fully funded &ndash; completing March 2026"),
    ("Flood Response Fund", "Tana River &amp; Mwanza", "Open",
     "assets/img/gallery/home-blog1.png",
     "Standing fund so our teams can move hygiene kits, cash and safe water within 72 hours.",
     61, "KES 1,830,000 of 3,000,000"),
]
rows = ""
for i, (t, loc, status, img, txt, pct, amt) in enumerate(project_rows):
    rows += """                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="single-cases mb-40">
                            <div class="cases-img">
                                <img src="%s" alt="%s">
                                <span class="case-status">%s</span>
                            </div>
                            <div class="cases-caption">
                                <span class="case-loc"><i class="ti-location-pin"></i> %s</span>
                                <h3><a href="donate.html">%s</a></h3>
                                <p>%s</p>
                                <div class="single-skill mb-15">
                                    <div class="bar-progress">
                                        <div id="bar%d" class="barfiller">
                                            <div class="tipWrap"><span class="tip"></span></div>
                                            <span class="fill" data-percentage="%d"></span>
                                        </div>
                                    </div>
                                </div>
                                <div class="prices"><p><span>%s</span></p></div>
                            </div>
                        </div>
                    </div>
""" % (img, t.replace("&amp;", "and"), status, loc, t, txt, i + 1, pct, amt)

page("projects.html", "Projects",
     "Live projects from Ubuntu Rising Foundation across Kenya, Uganda, Tanzania and Rwanda, with budgets and progress against each appeal.",
     banner("Projects", "Projects") +
     """        <div class="our-cases-area section-padding30">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-10 col-lg-10 ">
                        <div class="section-tittle text-center mb-80">
                            <h2>Where your money is working right now</h2>
                            <p class="pl-20 pr-20">Every project below has a published budget, a named
                            community committee and a monthly progress report. Figures updated 1 October 2026.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
""" + rows + """                </div>
            </div>
        </div>
""" + STATS + support() + PILLARS + CTA_BAND)

# ---------------------------------------------------------------- donate
donate_body = banner("Donate", "Donate") + """        <!-- Donate Start -->
        <section class="contact-section section-padding30">
            <div class="container">
                <div class="row">
                    <div class="col-lg-7">
                        <h2 class="contact-title">Make a donation</h2>
                        <p>Choose an amount, or enter your own. Card, M-PESA and bank transfers are all
                        processed in Kenyan shillings; international cards are accepted.</p>
                        <form class="form-contact contact_form donate-form" action="contact_process.php" method="post" id="donateForm" novalidate="novalidate">
                            <div class="give-toggle mb-30">
                                <button type="button" class="give-tab active" data-freq="once">Give once</button>
                                <button type="button" class="give-tab" data-freq="monthly">Give monthly</button>
                            </div>
                            <input type="hidden" name="frequency" id="frequency" value="once">
                            <div class="amount-grid mb-20">
                                <button type="button" class="amount-option" data-amount="1500">KES 1,500</button>
                                <button type="button" class="amount-option active" data-amount="2500">KES 2,500</button>
                                <button type="button" class="amount-option" data-amount="5000">KES 5,000</button>
                                <button type="button" class="amount-option" data-amount="10000">KES 10,000</button>
                                <button type="button" class="amount-option" data-amount="25000">KES 25,000</button>
                            </div>
                            <div class="row">
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="amount" id="amount" type="number" value="2500" placeholder="Other amount (KES)"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <select class="form-control" name="designation" id="designation">
                                        <option value="greatest-need">Where the need is greatest</option>
                                        <option value="turkana-water">Turkana Borehole Appeal</option>
                                        <option value="kibera-scholarships">Kibera Scholarship Fund</option>
                                        <option value="mama-biashara">Mama Biashara Grants</option>
                                        <option value="flood-response">Flood Response Fund</option>
                                    </select></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="name" id="name" type="text" placeholder="Full name"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="email" id="email" type="email" placeholder="Email address"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="phone" id="phone" type="text" placeholder="Phone (for M-PESA receipt)"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="country" id="country" type="text" placeholder="Country"></div></div>
                                <div class="col-12"><div class="form-group">
                                    <textarea class="form-control w-100" name="message" id="message" cols="30" rows="4" placeholder="Dedicate this gift or tell us anything we should know (optional)"></textarea></div></div>
                            </div>
                            <div class="form-group form-check-line">
                                <label><input type="checkbox" name="updates" checked> Email me programme updates (unsubscribe any time)</label>
                            </div>
                            <div class="form-group mt-3">
                                <button type="submit" class="button button-contactForm boxed-btn">Give <span id="give-summary">KES 2,500 once</span></button>
                            </div>
                        </form>
                    </div>
                    <div class="col-lg-4 offset-lg-1">
                        <div class="give-card mb-30">
                            <h4>Other ways to give</h4>
                            <p><strong>M-PESA Paybill</strong><br>Business no. 400200<br>Account: URF + your name</p>
                            <p><strong>Bank transfer</strong><br>Ubuntu Rising Foundation<br>Rift Valley Bank, Westlands branch<br>Acc. 0110 2298 4471<br>SWIFT RVBKKENA</p>
                            <p><strong>Cheques</strong><br>Payable to Ubuntu Rising Foundation, posted to Ubuntu House, Riverside Drive, Nairobi.</p>
                        </div>
                        <div class="give-card">
                            <h4>What your gift buys</h4>
                            <ul class="tick-list">
                                <li>KES 1,500 &ndash; safe water for one family for a year</li>
                                <li>KES 2,500/month &ndash; a village water point serviced all year</li>
                                <li>KES 10,000 &ndash; one term of secondary school, books included</li>
                                <li>KES 25,000 &ndash; a Mama Biashara start-up grant and toolkit</li>
                            </ul>
                            <p class="small-note">Ubuntu Rising Foundation is a registered Kenyan NGO. Donations from
                            the UK and EU can be gift-aided through our fiscal sponsor &ndash; email
                            <a href="mailto:%EMAIL%">%EMAIL%</a>.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Donate End -->
""".replace("%EMAIL%", EMAIL) + STATS + APPEALS

page("donate.html", "Donate", "Donate to Ubuntu Rising Foundation by card, M-PESA or bank transfer and fund clean water, schooling, health and livelihoods in East Africa.", donate_body)

# ---------------------------------------------------------------- volunteer
vol_body = banner("Volunteer", "Volunteer") + """        <section class="section-padding30">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-9">
                        <div class="section-tittle text-center mb-70">
                            <h2>Give your time, your skills or your Saturdays</h2>
                            <p>We place around 400 new volunteers every year. Most roles are in Nairobi,
                            Kisumu, Kampala and Mwanza; mentoring and professional roles can be done remotely.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-hummer"></i></span><h4>Field build days</h4>
                        <p>One-day water point, latrine or classroom builds, roughly two Saturdays a month.</p></div></div>
                    <div class="col-lg-4 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-comments"></i></span><h4>Scholar mentoring</h4>
                        <p>One hour a fortnight by phone or video with a secondary school scholar.</p></div></div>
                    <div class="col-lg-4 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-ruler-pencil"></i></span><h4>Pro-bono skills</h4>
                        <p>Water engineering, audit, legal, design, data and M&amp;E support for our programme teams.</p></div></div>
                </div>
            </div>
        </section>
        <section class="contact-section pb-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <h2 class="contact-title">Volunteer sign-up</h2>
                        <form class="form-contact contact_form" action="contact_process.php" method="post" id="volunteerForm" novalidate="novalidate">
                            <div class="row">
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="name" type="text" placeholder="Full name"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="email" type="email" placeholder="Email address"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="phone" type="text" placeholder="Phone number"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <select class="form-control" name="location">
                                        <option>Nairobi, Kenya</option><option>Kisumu, Kenya</option>
                                        <option>Mombasa, Kenya</option><option>Kampala, Uganda</option>
                                        <option>Mwanza, Tanzania</option><option>Kigali, Rwanda</option>
                                        <option>Remote / international</option>
                                    </select></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <select class="form-control" name="role">
                                        <option>Field build days</option><option>Scholar mentoring</option>
                                        <option>Pro-bono professional skills</option><option>Events &amp; fundraising</option>
                                        <option>Emergency response roster</option>
                                    </select></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <select class="form-control" name="availability">
                                        <option>A few hours a month</option><option>One day a month</option>
                                        <option>Weekly</option><option>Full-time placement</option>
                                    </select></div></div>
                                <div class="col-12"><div class="form-group">
                                    <textarea class="form-control w-100" name="message" cols="30" rows="6" placeholder="Tell us about your skills, languages and what you would like to do"></textarea></div></div>
                            </div>
                            <div class="form-group form-check-line">
                                <label><input type="checkbox" name="safeguarding"> I understand all volunteers complete a safeguarding check and induction.</label>
                            </div>
                            <div class="form-group mt-3">
                                <button type="submit" class="button button-contactForm boxed-btn">Submit application</button>
                            </div>
                        </form>
                    </div>
                    <div class="col-lg-3 offset-lg-1">
                        <div class="give-card">
                            <h4>What happens next</h4>
                            <ul class="tick-list">
                                <li>We reply within five working days</li>
                                <li>A 30-minute call with a volunteer coordinator</li>
                                <li>Safeguarding check and online induction</li>
                                <li>Your first placement, usually within a month</li>
                            </ul>
                            <p class="small-note">Volunteers must be 18 or over. Students aged 16&ndash;17 can join
                            our schools programme with guardian consent.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""" + support("donate.html", "Donate instead") + CTA_BAND

page("volunteer.html", "Volunteer", "Volunteer with Ubuntu Rising Foundation in Nairobi, Kisumu, Kampala, Mwanza or remotely. Field builds, mentoring and pro-bono professional roles.", vol_body)

# ---------------------------------------------------------------- partners
part_body = banner("Corporate partners", "Partners") + """        <section class="section-padding30">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-9">
                        <div class="section-tittle text-center mb-70">
                            <h2>Partnerships your board can report on</h2>
                            <p>We work with 40 companies and nine institutional funders. Every partnership
                            comes with a named account lead, quarterly impact data and photography and
                            case studies you are free to use.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-3 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-package"></i></span><h4>Project funding</h4>
                        <p>Fund a named borehole, school lab or health outreach, from KES 750,000.</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-user"></i></span><h4>Employee giving</h4>
                        <p>Payroll giving with matched contributions and a live staff impact dashboard.</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-hummer"></i></span><h4>Team volunteering</h4>
                        <p>Build days and skills-based placements for teams of 10 to 120 people.</p></div></div>
                    <div class="col-lg-3 col-md-6"><div class="single-way mb-30">
                        <span class="way-icon"><i class="ti-stats-up"></i></span><h4>Grant partnerships</h4>
                        <p>Multi-year, logframe-based programmes with independent evaluation.</p></div></div>
                </div>
            </div>
        </section>
""" + PARTNERS_STRIP + """        <section class="contact-section section-padding30">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <h2 class="contact-title">Start a partnership conversation</h2>
                        <form class="form-contact contact_form" action="contact_process.php" method="post" id="partnerForm" novalidate="novalidate">
                            <div class="row">
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="company" type="text" placeholder="Organisation name"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="name" type="text" placeholder="Contact person"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="email" type="email" placeholder="Work email"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <input class="form-control" name="phone" type="text" placeholder="Phone number"></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <select class="form-control" name="interest">
                                        <option>Project funding</option><option>Employee giving &amp; matching</option>
                                        <option>Team volunteering</option><option>Grant partnership</option>
                                        <option>Gifts in kind</option>
                                    </select></div></div>
                                <div class="col-sm-6"><div class="form-group">
                                    <select class="form-control" name="budget">
                                        <option>Budget not yet set</option><option>Under KES 750,000</option>
                                        <option>KES 750,000 &ndash; 3m</option><option>KES 3m &ndash; 10m</option>
                                        <option>Over KES 10m</option>
                                    </select></div></div>
                                <div class="col-12"><div class="form-group">
                                    <textarea class="form-control w-100" name="message" cols="30" rows="6" placeholder="What are you hoping to achieve, and by when?"></textarea></div></div>
                            </div>
                            <div class="form-group mt-3">
                                <button type="submit" class="button button-contactForm boxed-btn">Request a call</button>
                            </div>
                        </form>
                    </div>
                    <div class="col-lg-3 offset-lg-1">
                        <div class="give-card">
                            <h4>Partnerships team</h4>
                            <p>Grace Nakato<br>Head of Partnerships<br><a href="mailto:partnerships@ubunturising.org">partnerships@ubunturising.org</a><br>%PHONE%</p>
                            <p class="small-note">We reply to partnership enquiries within two working days and can
                            share our capability statement, due diligence pack and latest audited accounts on request.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""".replace("%PHONE%", PHONE) + STATS + CTA_BAND

page("partners.html", "Corporate partners", "Partner with Ubuntu Rising Foundation: project funding, employee giving, team volunteering and multi-year grant partnerships across East Africa.", part_body)

print("done")
