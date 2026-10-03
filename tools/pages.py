#!/usr/bin/env python3
"""Page bodies for the Ubuntu Rising Foundation website."""

import build_site
from build_site import write, bradcam, CTA_BAND, SITE

# ---------------------------------------------------------------------------
# Re-usable fragments
# ---------------------------------------------------------------------------

PARTNERS_STRIP = """        <!-- Partner logos -->
        <section class="urf-partners-strip">
            <div class="container">
                <p class="urf-partners-label">Trusted by funders, companies and county governments</p>
                <div class="urf-partner-logos">
                    <span>Safaricom Foundation</span>
                    <span>Mastercard Foundation</span>
                    <span>UNICEF Kenya</span>
                    <span>Equity Group</span>
                    <span>Kakamega County</span>
                    <span>Segal Family Trust</span>
                </div>
            </div>
        </section>
        <!-- Partner logos end -->
"""

NEWSLETTER = """        <!-- Newsletter -->
        <section class="urf-newsletter">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-xl-5 col-lg-5">
                        <h3>Quarterly updates from the field</h3>
                        <p>Clear, concise reporting from the communities we work with, four emails a year.</p>
                    </div>
                    <div class="col-xl-7 col-lg-7">
                        <form class="urf-newsletter-form" action="#" method="post">
                            <label class="sr-only" for="nl-email">Email address</label>
                            <input id="nl-email" type="email" name="email" placeholder="your@email.com" required>
                            <button type="submit" class="btn">Subscribe</button>
                        </form>
                        <small>Four emails a year. Unsubscribe in one click.</small>
                    </div>
                </div>
            </div>
        </section>
        <!-- Newsletter end -->
"""


def impact_counters(extra_class=""):
    return f"""        <!-- Impact numbers -->
        <section class="urf-stats {extra_class}">
            <div class="container">
                <div class="row">
                    <div class="col-lg-3 col-md-6 col-6">
                        <div class="urf-stat">
                            <span class="counter">42</span>
                            <p>Communities partnered<br>since 2013</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-6">
                        <div class="urf-stat">
                            <span class="counter">18400</span><span class="urf-stat-plus">+</span>
                            <p>Learners supported<br>through school</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-6">
                        <div class="urf-stat">
                            <span class="counter">96</span>
                            <p>Boreholes and water<br>points maintained</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-6">
                        <div class="urf-stat">
                            <span class="counter">2300</span><span class="urf-stat-plus">+</span>
                            <p>Women trading through<br>our savings groups</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Impact numbers end -->
"""


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------

HOME = """        <!-- Hero slider -->
        <div class="slider-area position-relative">
            <div class="slider-active dot-style">
                <div class="single-slider hero-overly slider-height d-flex align-items-center">
                    <div class="urf-kb slider-bg1" aria-hidden="true"></div>
                    <div class="container">
                        <div class="row">
                            <div class="col-xl-8 col-lg-8 col-md-9 col-sm-11">
                                <div class="hero__caption">
                                    <span class="urf-eyebrow" data-animation="fadeInUp" data-delay=".1s">Nairobi, Kenya &middot; working across East Africa</span>
                                    <h1>Lasting change,<br>led by communities</h1>
                                    <p data-animation="fadeInUp" data-delay=".4s">We work with 42 communities across Kenya, Uganda, Tanzania and Rwanda,
                                        funding education, clean water, livelihoods and climate programmes that each
                                        community chooses for itself.</p>
                                    <div class="hero__btn">
                                        <a href="donate.html" class="hero-btn mb-10" data-animation="fadeInUp" data-delay=".8s">Donate now</a>
                                        <a href="programmes.html" class="hero-btn hero-btn-ghost mb-10" data-animation="fadeInUp" data-delay="1s">Explore our programmes</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="single-slider hero-overly slider-height d-flex align-items-center">
                    <div class="urf-kb slider-bg2" aria-hidden="true"></div>
                    <div class="container">
                        <div class="row">
                            <div class="col-xl-8 col-lg-8 col-md-9 col-sm-11">
                                <div class="hero__caption">
                                    <span class="urf-eyebrow" data-animation="fadeInUp" data-delay=".1s">Clean water &amp; sanitation</span>
                                    <h1>Clean water,<br>within reach</h1>
                                    <p data-animation="fadeInUp" data-delay=".4s">Ninety-six solar boreholes, each handed to a trained community water
                                        committee with three years of funded maintenance built into the budget.</p>
                                    <div class="hero__btn">
                                        <a href="projects.html" class="hero-btn mb-10" data-animation="fadeInUp" data-delay=".8s">Fund a water point</a>
                                        <a href="programmes.html#water" class="hero-btn hero-btn-ghost mb-10" data-animation="fadeInUp" data-delay="1s">How it works</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="single-slider hero-overly slider-height d-flex align-items-center">
                    <div class="urf-kb slider-bg3" aria-hidden="true"></div>
                    <div class="container">
                        <div class="row">
                            <div class="col-xl-8 col-lg-8 col-md-9 col-sm-11">
                                <div class="hero__caption">
                                    <span class="urf-eyebrow" data-animation="fadeInUp" data-delay=".1s">Volunteer &amp; partner with us</span>
                                    <h1>Put your skills<br>to work</h1>
                                    <p data-animation="fadeInUp" data-delay=".4s">More than 1,150 teachers, engineers, accountants, designers and
                                        clinicians give their time each year, most of them remotely, from wherever they live.</p>
                                    <div class="hero__btn">
                                        <a href="volunteer.html" class="hero-btn mb-10" data-animation="fadeInUp" data-delay=".8s">Become a volunteer</a>
                                        <a href="partners.html" class="hero-btn hero-btn-ghost mb-10" data-animation="fadeInUp" data-delay="1s">Partner with us</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="urf-scroll-cue" aria-hidden="true">
                <span class="urf-scroll-track"><span class="urf-scroll-dot"></span></span>
                <em>Scroll</em>
            </div>
        </div>
        <!-- Hero slider end -->

        <!-- Three doors -->
        <section class="urf-doors">
            <div class="container">
                <div class="row no-gutters">
                    <div class="col-lg-4 col-md-4">
                        <a class="urf-door" href="donate.html">
                            <i class="ti-heart"></i>
                            <h4>Give</h4>
                            <p>Give once or monthly by M-PESA, card or bank transfer, in KES, USD, GBP or EUR.</p>
                            <span class="urf-link-arrow">Donate now <i class="ti-arrow-right"></i></span>
                        </a>
                    </div>
                    <div class="col-lg-4 col-md-4">
                        <a class="urf-door urf-door-mid" href="volunteer.html">
                            <i class="ti-user"></i>
                            <h4>Volunteer</h4>
                            <p>Give four hours a month remotely, or join a funded field placement in Kenya or Uganda.</p>
                            <span class="urf-link-arrow">See open roles <i class="ti-arrow-right"></i></span>
                        </a>
                    </div>
                    <div class="col-lg-4 col-md-4">
                        <a class="urf-door" href="partners.html">
                            <i class="ti-briefcase"></i>
                            <h4>Partner</h4>
                            <p>CSR programmes, payroll giving, staff volunteering and co-funded county projects.</p>
                            <span class="urf-link-arrow">Start a conversation <i class="ti-arrow-right"></i></span>
                        </a>
                    </div>
                </div>
            </div>
        </section>
        <!-- Three doors end -->

        <!-- Mission -->
        <div class="visit-tailor-area fix">
            <div class="tailor-offers"></div>
            <div class="tailor-details">
                <span>Who we are</span>
                <h2>Community-led, locally delivered, independently audited</h2>
                <p>Ubuntu Rising Foundation was founded in 2013 by six Kenyan teachers and a retired
                    hydrologist. Our model is simple: an elected community committee defines the priority, we raise the
                    funding alongside them, and we commit to a minimum of five years so that the work holds.</p>
                <p class="pera-bottom">Eighty-four per cent of our staff come from the counties and districts where
                    we work. Every shilling is tracked against a published budget, and our annual accounts are
                    externally audited and published in full on this website.</p>
                <div class="footer-tittles">
                    <p>Executive Director, Ubuntu Rising Foundation</p>
                    <h2>Amara Nyambura Okello</h2>
                </div>
            </div>
        </div>
        <!-- Mission end -->

        <!-- Programme cards -->
        <div class="service-area section-padding30">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-9 col-lg-10">
                        <div class="section-tittle text-center mb-80">
                            <span class="urf-eyebrow-dark">What we do</span>
                            <h2>Five programmes, one approach</h2>
                            <p class="pl-20 pr-20">Each programme is run by an East African team, governed by a local
                                committee, and measured against published unit costs and targets.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-11">
                        <div class="single-cat text-center mb-30">
                            <div class="cat-icon">
                                <img src="assets/img/gallery/services1.jpg" alt="A pupil with his exercise book in a rural classroom">
                            </div>
                            <div class="cat-cap">
                                <h5><a href="programmes.html#education">Education &amp; Scholarships</a></h5>
                                <p>Fees, uniforms, sanitary care and mentoring for 18,400 learners, and salaries for
                                    112 community teachers.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-11">
                        <div class="single-cat active text-center mb-30">
                            <div class="cat-icon">
                                <img src="assets/img/gallery/services2.jpg" alt="Clean water from a village hand pump">
                            </div>
                            <div class="cat-cap">
                                <h5><a href="programmes.html#water">Clean Water &amp; Sanitation</a></h5>
                                <p>Solar boreholes, rainwater harvesting and household latrines, with funded maintenance
                                    for three years after handover.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-11">
                        <div class="single-cat text-center mb-30">
                            <div class="cat-icon">
                                <img src="assets/img/gallery/services3.jpg" alt="A woman training on a sewing machine">
                            </div>
                            <div class="cat-cap">
                                <h5><a href="programmes.html#women">Women&rsquo;s Livelihoods</a></h5>
                                <p>Village savings groups, vocational training and start-up grants for 2,300 women
                                    running their own businesses.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-center">
                    <div class="col-auto">
                        <a href="programmes.html" class="btn urf-btn-solid mt-20">Explore all five programmes <i class="ti-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Programme cards end -->

        <!-- Why join -->
        <section class="support-company-area fix pt-10">
            <div class="support-wrapper align-items-center">
                <div class="left-content">
                    <div class="section-tittle section-tittle2 mb-30">
                        <span>Why give through Ubuntu Rising</span>
                        <h2>87% of every shilling reaches the field</h2>
                    </div>
                    <div class="support-caption">
                        <p class="pera-top">We publish our full accounts, our salary bands and the unit cost of every
                            intervention. Nine per cent of income covers administration and four per cent covers
                            fundraising; the remaining 87 per cent goes directly to programmes. Our books are audited
                            annually by PKF Eastern Africa and filed with the NGO Co-ordination Board.</p>
                        <p class="pera-top">You can restrict your gift to a single project, and we will send you that
                            project&rsquo;s budget, progress photographs and an honest account of what worked.</p>
                        <div class="urf-btn-row">
                            <a href="impact.html" class="btn urf-btn-solid">Read our impact report <i class="ti-arrow-right"></i></a>
                            <a href="donate.html" class="urf-link-arrow">Or give today <i class="ti-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
                <div class="right-content">
                    <div class="right-img">
                        <img src="assets/img/gallery/safe_in.jpg" alt="A mentor teaching two teenage girls at a community learning centre">
                    </div>
                    <div class="support-img-cap text-center d-flex">
                        <div class="single-one">
                            <span>87%</span>
                            <p>Straight to programmes</p>
                        </div>
                        <div class="single-two">
                            <span>1,150</span>
                            <p>Active volunteers</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Why join end -->

""" + impact_counters() + """
        <!-- Live appeals -->
        <div class="our-cases-area section-padding30">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-10 col-lg-10">
                        <div class="section-tittle text-center mb-80">
                            <span class="urf-eyebrow-dark">Open appeals</span>
                            <h2>Appeals we are raising for now</h2>
                            <p class="pl-20 pr-20">Every appeal has a published budget and a named field lead. Once an
                                appeal reaches its target we close it rather than keep collecting against it.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="single-cases mb-40">
                            <div class="cases-img">
                                <img src="assets/img/gallery/case1.jpg" alt="Girls reading in a classroom in Kakamega">
                            </div>
                            <div class="cases-caption">
                                <span class="urf-pill">Kakamega County, Kenya</span>
                                <h3><a href="projects.html">Return 400 girls to secondary school</a></h3>
                                <p>Full fees, boarding and sanitary care for 400 girls who dropped out during the 2024
                                    drought. Led by Beatrice Ayuma.</p>
                                <div class="single-skill mb-15">
                                    <div class="bar-progress">
                                        <div id="bar1" class="barfiller">
                                            <div class="tipWrap"><span class="tip"></span></div>
                                            <span class="fill" data-percentage="72"></span>
                                        </div>
                                    </div>
                                </div>
                                <div class="prices">
                                    <p><span>KES 8.6M raised of KES 12M</span></p>
                                </div>
                                <a href="donate.html" class="urf-link-arrow">Fund this appeal <i class="ti-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="single-cases mb-40">
                            <div class="cases-img">
                                <img src="assets/img/gallery/case2.jpg" alt="Water flowing from a new borehole hand pump">
                            </div>
                            <div class="cases-caption">
                                <span class="urf-pill">Turkana County, Kenya</span>
                                <h3><a href="projects.html">Six solar boreholes for Turkana</a></h3>
                                <p>Drilling, solar pumps, storage tanks and a trained water committee for six settlements
                                    now walking 7km for water.</p>
                                <div class="single-skill mb-15">
                                    <div class="bar-progress">
                                        <div id="bar2" class="barfiller">
                                            <div class="tipWrap"><span class="tip"></span></div>
                                            <span class="fill" data-percentage="38"></span>
                                        </div>
                                    </div>
                                </div>
                                <div class="prices">
                                    <p><span>KES 4.1M raised of KES 10.8M</span></p>
                                </div>
                                <a href="donate.html" class="urf-link-arrow">Fund this appeal <i class="ti-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="single-cases mb-40">
                            <div class="cases-img">
                                <img src="assets/img/gallery/case3.jpg" alt="A woman entrepreneur at her market stall">
                            </div>
                            <div class="cases-caption">
                                <span class="urf-pill">Mbale, Uganda</span>
                                <h3><a href="projects.html">Start-up grants for 150 women traders</a></h3>
                                <p>Twelve weeks of business training plus a UGX 900,000 grant for women leaving our
                                    savings groups to trade full time.</p>
                                <div class="single-skill mb-15">
                                    <div class="bar-progress">
                                        <div id="bar3" class="barfiller">
                                            <div class="tipWrap"><span class="tip"></span></div>
                                            <span class="fill" data-percentage="91"></span>
                                        </div>
                                    </div>
                                </div>
                                <div class="prices">
                                    <p><span>KES 6.4M raised of KES 7M</span></p>
                                </div>
                                <a href="donate.html" class="urf-link-arrow">Fund this appeal <i class="ti-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Live appeals end -->

""" + CTA_BAND + """
        <!-- Voices -->
        <section class="urf-voices">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8 col-lg-9">
                        <div class="section-tittle text-center mb-80">
                            <span class="urf-eyebrow-dark">Voices</span>
                            <h2>What our communities and partners say</h2>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6">
                        <blockquote class="urf-quote">
                            <p>&ldquo;They asked us what we wanted before they told us what they had. That had never
                                happened here before. We said a secondary school, and four years later my daughter
                                sits her exams in it.&rdquo;</p>
                            <cite><strong>Josephine Wanjiku</strong><span>Chair, Nyandarua community committee</span></cite>
                        </blockquote>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <blockquote class="urf-quote">
                            <p>&ldquo;We fund a lot of NGOs. Ubuntu Rising is the only one that sends us the things that
                                went wrong in the same report as the things that went right.&rdquo;</p>
                            <cite><strong>Daniel Mwangi</strong><span>Head of Sustainability, Equity Group</span></cite>
                        </blockquote>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <blockquote class="urf-quote">
                            <p>&ldquo;I volunteer four hours a month from Berlin doing their monthly bookkeeping. It costs
                                me an evening and it saves them a salary.&rdquo;</p>
                            <cite><strong>Lena Hoffmann</strong><span>Volunteer finance associate</span></cite>
                        </blockquote>
                    </div>
                </div>
            </div>
        </section>
        <!-- Voices end -->

""" + PARTNERS_STRIP + """
        <!-- Latest news -->
        <section class="home-blog-area pb-padding">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8 col-lg-9 col-md-11">
                        <div class="section-tittle text-center mb-90">
                            <span class="urf-eyebrow-dark">News &amp; stories</span>
                            <h2>Latest from the field</h2>
                            <p>Updates and results from our teams in Kenya, Uganda, Tanzania and Rwanda.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-xl-6 col-lg-6 col-md-6">
                        <div class="home-blog-single mb-30">
                            <div class="blog-img-cap">
                                <div class="blog-img">
                                    <img src="assets/img/gallery/home-blog1.jpg" alt="A mobile health clinic in a rural village">
                                </div>
                                <div class="blog-cap">
                                    <span class="urf-pill">18 September 2026 &middot; Health</span>
                                    <h3><a href="blog_details.html">How eleven mobile clinics reached 9,700 people</a></h3>
                                    <p>Immunisation coverage in the villages we serve has risen from 51% to 88%. The
                                        decisive factor was not the medicine, but arriving on the same day every month.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-6 col-lg-6 col-md-6">
                        <div class="home-blog-single mb-30">
                            <div class="blog-img-cap">
                                <div class="blog-img">
                                    <img src="assets/img/gallery/home-blog2.jpg" alt="Young volunteers planting tree seedlings">
                                </div>
                                <div class="blog-cap">
                                    <span class="urf-pill">2 September 2026 &middot; Climate</span>
                                    <h3><a href="blog_details.html">What we learned from planting 60,000 seedlings</a></h3>
                                    <p>Seedling survival has risen from 34% to 71% after we changed species selection,
                                        planting season and funded two years of aftercare.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-center">
                    <div class="col-auto">
                        <a href="blog.html" class="btn urf-btn-solid mt-30">Read all updates <i class="ti-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </section>
        <!-- Latest news end -->

""" + NEWSLETTER


# ---------------------------------------------------------------------------
# About
# ---------------------------------------------------------------------------

ABOUT = bradcam("About Ubuntu Rising", "About") + """
        <!-- Intro -->
        <section class="urf-section">
            <div class="container">
                <div class="row">
                    <div class="col-lg-5">
                        <div class="section-tittle">
                            <span class="urf-eyebrow-dark">Since 2013</span>
                            <h2>Community-led development since 2013</h2>
                        </div>
                    </div>
                    <div class="col-lg-7">
                        <p class="urf-lead">&ldquo;Umuntu ngumuntu ngabantu&rdquo;: a person is a person through
                            other people. Ubuntu Rising Foundation was established on a simple principle: the
                            communities affected by a programme should be the ones who design it.</p>
                        <p>We began with one bursary fund for 24 girls. Thirteen years later we work in 42 communities
                            across Kenya, Uganda, Tanzania and Rwanda, with an annual programme budget of KES 412 million
                            and a staff of 68, of whom 57 were born in the counties and districts where they work.</p>
                        <p>We are registered with Kenya&rsquo;s NGO Co-ordination Board, hold a Public Fundraising Appeals
                            licence, and file audited accounts every year. {reg}.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- Intro end -->

        <!-- Mission block -->
        <div class="visit-tailor-area fix">
            <div class="tailor-offers"></div>
            <div class="tailor-details">
                <span>Mission &amp; values</span>
                <h2>Our mission and values</h2>
                <p><strong>Community mandate.</strong> No project starts without a signed resolution from an elected
                    community committee. They set the priority; we raise against it.</p>
                <p><strong>Long horizons.</strong> Our minimum commitment to a community is five years. Our water
                    programme carries a three-year maintenance budget before handover is considered complete.</p>
                <p><strong>Full transparency.</strong> We publish unit costs, salary bands, audited accounts and an
                    honest assessment of the programmes that underperformed.</p>
                <p class="pera-bottom"><strong>Local leadership.</strong> Eighty-four per cent of our staff and 100 per
                    cent of our country leads are East African. We hire from the communities first.</p>
                <div class="footer-tittles">
                    <p>Co-founder &amp; Chair of Trustees</p>
                    <h2>Dr. Samuel Odhiambo</h2>
                </div>
            </div>
        </div>
        <!-- Mission block end -->

""" + impact_counters() + """
        <!-- Story timeline -->
        <section class="urf-section urf-bg-soft">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8 col-lg-9">
                        <div class="section-tittle text-center mb-80">
                            <span class="urf-eyebrow-dark">Our story</span>
                            <h2>Our journey so far</h2>
                        </div>
                    </div>
                </div>
                <div class="urf-timeline">
                    <div class="urf-tl-item">
                        <span class="urf-tl-year">2013</span>
                        <h4>A bursary fund for 24 girls</h4>
                        <p>Founded in a borrowed classroom in Nairobi with KES 340,000 raised among friends and family.</p>
                    </div>
                    <div class="urf-tl-item">
                        <span class="urf-tl-year">2016</span>
                        <h4>A lesson that reshaped the water programme</h4>
                        <p>Our first Siaya borehole failed within nine months because maintenance had not been budgeted.
                            Every water project since carries three years of funded repairs.</p>
                    </div>
                    <div class="urf-tl-item">
                        <span class="urf-tl-year">2019</span>
                        <h4>Across the border</h4>
                        <p>Savings-group programme opens in Mbale, Uganda, then Mwanza, Tanzania in 2021 and Musanze,
                            Rwanda in 2023.</p>
                    </div>
                    <div class="urf-tl-item">
                        <span class="urf-tl-year">2022</span>
                        <h4>Corporate partnerships formalised</h4>
                        <p>Safaricom Foundation and Equity Group become multi-year co-funders; payroll giving launches
                            with eleven Nairobi employers.</p>
                    </div>
                    <div class="urf-tl-item">
                        <span class="urf-tl-year">2024</span>
                        <h4>Drought response</h4>
                        <p>Emergency schooling and water trucking for 7,400 people across Turkana and Marsabit, run
                            entirely by local staff.</p>
                    </div>
                    <div class="urf-tl-item">
                        <span class="urf-tl-year">2026</span>
                        <h4>42 communities, five programmes</h4>
                        <p>An annual programme budget of KES 412 million and a five-year plan to reach 60 communities
                            without growing head office.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- Story timeline end -->

        <!-- Leadership -->
        <section class="urf-section">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8 col-lg-9">
                        <div class="section-tittle text-center mb-80">
                            <span class="urf-eyebrow-dark">Leadership</span>
                            <h2>Our leadership team</h2>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-person">
                            <div class="urf-person-photo"><img src="assets/img/gallery/team1.jpg" alt="Portrait of Amara Nyambura Okello" loading="lazy" width="560" height="640"></div>
                            <h4>Amara Nyambura Okello</h4>
                            <span>Executive Director</span>
                            <p>Former head teacher in Kibera. Co-founded the foundation in 2013 and has led it since 2018.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-person">
                            <div class="urf-person-photo"><img src="assets/img/gallery/team2.jpg" alt="Portrait of Beatrice Ayuma" loading="lazy" width="560" height="640"></div>
                            <h4>Beatrice Ayuma</h4>
                            <span>Director of Programmes</span>
                            <p>Fifteen years in girls&rsquo; education across western Kenya. Leads our Kakamega scholarship work.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-person">
                            <div class="urf-person-photo"><img src="assets/img/gallery/team3.jpg" alt="Portrait of Tendai Mukasa" loading="lazy" width="560" height="640"></div>
                            <h4>Tendai Mukasa</h4>
                            <span>Country Lead, Uganda</span>
                            <p>Microfinance specialist. Built our Mbale savings-group model from eleven groups to 190.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-person">
                            <div class="urf-person-photo"><img src="assets/img/gallery/team4.jpg" alt="Portrait of Grace Wairimu, CPA" loading="lazy" width="560" height="640"></div>
                            <h4>Grace Wairimu, CPA</h4>
                            <span>Director of Finance</span>
                            <p>Fifteen years in audit at PKF. Owns the published accounts and the unit-cost model.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Leadership end -->

""" + CTA_BAND + PARTNERS_STRIP


# ---------------------------------------------------------------------------
# Programmes
# ---------------------------------------------------------------------------

def programme_block(anchor, eyebrow, title, img, alt, body, bullets, stat, reverse=False):
    order_text = "order-lg-2" if reverse else ""
    order_img = "order-lg-1" if reverse else ""
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""        <section class="urf-programme" id="{anchor}">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6 {order_text}">
                        <div class="urf-programme-text">
                            <span class="urf-eyebrow-dark">{eyebrow}</span>
                            <h2>{title}</h2>
                            {body}
                            <ul class="urf-ticks">{lis}</ul>
                            <div class="urf-programme-stat">{stat}</div>
                            <div class="urf-btn-row">
                                <a href="donate.html" class="btn urf-btn-solid">Fund this programme <i class="ti-arrow-right"></i></a>
                                <a href="{{wa_link}}" target="_blank" rel="noopener" class="urf-btn-wa"><i class="fab fa-whatsapp"></i> Ask a question</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 {order_img}">
                        <div class="urf-programme-img">
                            <img src="{img}" alt="{alt}">
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""


PROGRAMMES = bradcam("Our Programmes", "Programmes", "bradcam2") + """
        <section class="urf-section pb-0">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-9 col-lg-10">
                        <div class="section-tittle text-center mb-60">
                            <span class="urf-eyebrow-dark">What we do</span>
                            <h2>Five programmes, built to be sustained</h2>
                            <p>Every programme has a published unit cost, an East African lead, an accountable
                                community committee and a clear handover plan.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

""" + programme_block(
    "education", "Programme 01", "Education &amp; Scholarships",
    "assets/img/gallery/prog-education.jpg", "Girls reading at desks in a rural classroom",
    """<p>We pay school fees, buy uniforms and books, fund sanitary care, and employ 112 community teachers in schools
        that the government has not been able to staff. Scholars are selected by a community panel, not by us, against
        published criteria.</p>
       <p>Each scholar is matched with a local mentor who sees them monthly. Our secondary completion rate for sponsored
        girls is 91 per cent, against a regional average of 58 per cent.</p>""",
    ["Full secondary scholarship: KES 48,000 per girl per year",
     "One term of school for a girl: KES 2,500",
     "112 community teachers on our payroll across 31 schools",
     "18,400 learners supported since 2013"],
    "<strong>91%</strong> of sponsored girls complete secondary school",
) + programme_block(
    "water", "Programme 02", "Clean Water &amp; Sanitation",
    "assets/img/gallery/prog-water.jpg", "Clean water pouring from a village hand pump",
    """<p>Solar-powered boreholes, spring protection, rainwater harvesting at schools and household latrine subsidies.
        Every installation is handed to an elected water committee that collects a small monthly tariff and holds a
        maintenance account we seed for three years.</p>
       <p>This came from experience: our first borehole in Siaya failed within nine months because no one owned the
        repairs. Of the 96 water points built since, 94 are still functioning.</p>""",
    ["A complete solar borehole with handover: KES 1.8M",
     "A school rainwater harvesting system: KES 340,000",
     "Three years of funded maintenance built into every project",
     "Average walk to water in our communities cut from 74 to 9 minutes"],
    "<strong>94 of 96</strong> water points still running",
    reverse=True,
) + programme_block(
    "women", "Programme 03", "Women&rsquo;s Economic Empowerment",
    "assets/img/gallery/prog-women.jpg", "A woman entrepreneur at her market stall",
    """<p>Village savings and loan associations, twelve-week business training, and start-up grants for members ready to
        trade full time. Groups are run entirely by their members; our staff train the first cohort and then step back.</p>
       <p>Across 190 groups in Kenya, Uganda and Tanzania, members have saved the equivalent of KES 61 million of their
        own money, roughly four times what we have put in.</p>""",
    ["Start-up grant for a graduating trader: KES 32,000",
     "Training one savings group of 25 women: KES 95,000",
     "190 active savings groups, 2,300 women trading",
     "Member savings of KES 61M, 4x our own investment"],
    "<strong>KES 61M</strong> saved by members themselves",
) + programme_block(
    "health", "Programme 04", "Community Health",
    "assets/img/gallery/prog-health.jpg", "Community health volunteers running a mobile clinic",
    """<p>Eleven mobile clinics running fixed monthly routes, staffed by trained community health volunteers and a
        visiting clinical officer. Antenatal care, immunisation, growth monitoring, malaria testing and referral.</p>
       <p>The clinical work is routine. What makes it effective is arriving on the same day of the month, without
        fail, year after year.</p>""",
    ["One mobile clinic day serving ~140 people: KES 68,000",
     "Training and kitting a community health volunteer: KES 24,000",
     "9,700 people seen last quarter across 11 routes",
     "Immunisation coverage in served villages up from 51% to 88%"],
    "<strong>9,700</strong> people seen last quarter",
    reverse=True,
) + programme_block(
    "climate", "Programme 05", "Youth Climate Action",
    "assets/img/gallery/prog-climate.jpg", "Young volunteers planting tree seedlings on a hillside",
    """<p>Paid six-month fellowships for 240 young East Africans running reforestation, soil restoration and clean
        cookstove projects in their own districts. Fellows design the project; we fund it and hold them to the numbers.</p>
       <p>Our first cohort achieved 34 per cent seedling survival. After changing species selection, moving planting to
        the long rains and funding two years of aftercare, survival now stands at 71 per cent.</p>""",
    ["One six-month youth fellowship: KES 180,000",
     "1,000 indigenous seedlings with two years of care: KES 145,000",
     "240 fellows across four countries",
     "71% seedling survival at 24 months"],
    "<strong>71%</strong> seedling survival at two years",
) + CTA_BAND + NEWSLETTER


# ---------------------------------------------------------------------------
# Projects
# ---------------------------------------------------------------------------

def appeal_card(img, alt, pill, title, text, pct, raised, bar_id):
    return f"""                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="single-cases mb-40">
                            <div class="cases-img">
                                <img src="{img}" alt="{alt}">
                            </div>
                            <div class="cases-caption">
                                <span class="urf-pill">{pill}</span>
                                <h3><a href="donate.html">{title}</a></h3>
                                <p>{text}</p>
                                <div class="single-skill mb-15">
                                    <div class="bar-progress">
                                        <div id="{bar_id}" class="barfiller">
                                            <div class="tipWrap"><span class="tip"></span></div>
                                            <span class="fill" data-percentage="{pct}"></span>
                                        </div>
                                    </div>
                                </div>
                                <div class="prices"><p><span>{raised}</span></p></div>
                                <a href="donate.html" class="urf-link-arrow">Fund this appeal <i class="ti-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>
"""


PROJECTS = bradcam("Current Projects", "Our Work", "bradcam3") + """
        <div class="our-cases-area section-padding30">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-10 col-lg-10">
                        <div class="section-tittle text-center mb-80">
                            <span class="urf-eyebrow-dark">Open appeals</span>
                            <h2>Six projects open for funding</h2>
                            <p class="pl-20 pr-20">Each has a published budget, a named field lead and a community
                                committee resolution behind it. Once a target is met, we close the appeal.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
""" + appeal_card(
    "assets/img/gallery/case1.jpg", "Girls reading in a Kakamega classroom", "Kakamega County, Kenya",
    "Return 400 girls to secondary school",
    "Full fees, boarding and sanitary care for 400 girls who dropped out during the 2024 drought. Field lead: Beatrice Ayuma.",
    72, "KES 8.6M raised of KES 12M", "bar1",
) + appeal_card(
    "assets/img/gallery/case2.jpg", "Water from a new borehole", "Turkana County, Kenya",
    "Six solar boreholes for Turkana",
    "Drilling, solar pumps, storage and trained water committees for six settlements currently walking 7km for water.",
    38, "KES 4.1M raised of KES 10.8M", "bar2",
) + appeal_card(
    "assets/img/gallery/case3.jpg", "A woman trader at her stall", "Mbale, Uganda",
    "Start-up grants for 150 women traders",
    "Twelve weeks of business training plus a UGX 900,000 grant for women graduating from our savings groups.",
    91, "KES 6.4M raised of KES 7M", "bar3",
) + """                </div>
                <div class="row">
""" + appeal_card(
    "assets/img/gallery/case4.jpg", "Mobile health clinic under a tent", "Mwanza, Tanzania",
    "Three new mobile clinic routes",
    "Vehicles, kits and twelve months of staffing to extend monthly health routes to 23 villages around Lake Victoria.",
    54, "KES 5.9M raised of KES 11M", "bar4",
) + appeal_card(
    "assets/img/gallery/case5.jpg", "Youth fellows planting trees", "Musanze, Rwanda",
    "40 youth climate fellowships",
    "Six-month paid fellowships for 40 young Rwandans restoring degraded hillside farmland above Musanze.",
    27, "KES 1.9M raised of KES 7.2M", "bar5",
) + appeal_card(
    "assets/img/gallery/case6.jpg", "A mentor working with teenage girls", "Nairobi, Kenya",
    "Ubuntu Digital Skills Centre",
    "Equipping and running a 40-seat coding and digital work centre for school leavers in Mathare for two years.",
    63, "KES 7.6M raised of KES 12M", "bar6",
) + """                </div>
            </div>
        </div>

""" + impact_counters("urf-stats-dark") + """
        <!-- Where we work -->
        <section class="urf-section">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8 col-lg-9">
                        <div class="section-tittle text-center mb-60">
                            <span class="urf-eyebrow-dark">Where we work</span>
                            <h2>42 communities, four countries</h2>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-region">
                            <h4>Kenya</h4>
                            <span>26 communities</span>
                            <p>Kakamega, Turkana, Marsabit, Siaya, Nyandarua, Kilifi, Nairobi (Mathare &amp; Kibera)</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-region">
                            <h4>Uganda</h4>
                            <span>8 communities</span>
                            <p>Mbale, Soroti and Gulu: savings groups, vocational training and school water</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-region">
                            <h4>Tanzania</h4>
                            <span>5 communities</span>
                            <p>Mwanza and Shinyanga: mobile health routes and women&rsquo;s livelihoods</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-region">
                            <h4>Rwanda</h4>
                            <span>3 communities</span>
                            <p>Musanze: youth climate fellowships and hillside soil restoration</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Where we work end -->

""" + CTA_BAND


# ---------------------------------------------------------------------------
# Impact & transparency
# ---------------------------------------------------------------------------

IMPACT = bradcam("Impact &amp; Transparency", "Impact") + """
        <section class="urf-section">
            <div class="container">
                <div class="row">
                    <div class="col-lg-5">
                        <div class="section-tittle">
                            <span class="urf-eyebrow-dark">2025 annual results</span>
                            <h2>Our 2025 results in full</h2>
                        </div>
                    </div>
                    <div class="col-lg-7">
                        <p class="urf-lead">Total income in the year to 31 December 2025 was KES 471.3 million.
                            Programme spend was KES 410.0 million. Our accounts were audited without qualification by
                            PKF Eastern Africa and filed with the NGO Co-ordination Board in March 2026.</p>
                        <p>We publish the unit cost of every intervention so our arithmetic can be checked, and we
                            report the programmes that underperformed alongside those that succeeded. If anything here
                            does not add up, email <a href="mailto:{email}">{email}</a> and we will answer it.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Spend breakdown -->
        <section class="urf-section urf-bg-soft pt-0">
            <div class="container">
                <div class="row">
                    <div class="col-lg-7">
                        <div class="urf-spend">
                            <h3>How every KES 100 was spent</h3>
                            <div class="urf-spend-row">
                                <div class="urf-spend-label"><span>Programmes in the field</span><strong>87%</strong></div>
                                <div class="urf-meter"><i style="width:87%"></i></div>
                            </div>
                            <div class="urf-spend-row">
                                <div class="urf-spend-label"><span>Administration &amp; governance</span><strong>9%</strong></div>
                                <div class="urf-meter"><i style="width:9%"></i></div>
                            </div>
                            <div class="urf-spend-row">
                                <div class="urf-spend-label"><span>Fundraising</span><strong>4%</strong></div>
                                <div class="urf-meter"><i style="width:4%"></i></div>
                            </div>
                            <h3 class="mt-50">Programme spend by area</h3>
                            <div class="urf-spend-row">
                                <div class="urf-spend-label"><span>Education &amp; scholarships</span><strong>KES 148.1M</strong></div>
                                <div class="urf-meter"><i style="width:36%"></i></div>
                            </div>
                            <div class="urf-spend-row">
                                <div class="urf-spend-label"><span>Clean water &amp; sanitation</span><strong>KES 110.7M</strong></div>
                                <div class="urf-meter"><i style="width:27%"></i></div>
                            </div>
                            <div class="urf-spend-row">
                                <div class="urf-spend-label"><span>Women&rsquo;s livelihoods</span><strong>KES 73.8M</strong></div>
                                <div class="urf-meter"><i style="width:18%"></i></div>
                            </div>
                            <div class="urf-spend-row">
                                <div class="urf-spend-label"><span>Community health</span><strong>KES 49.2M</strong></div>
                                <div class="urf-meter"><i style="width:12%"></i></div>
                            </div>
                            <div class="urf-spend-row">
                                <div class="urf-spend-label"><span>Youth climate action</span><strong>KES 28.2M</strong></div>
                                <div class="urf-meter"><i style="width:7%"></i></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-5">
                        <div class="urf-downloads">
                            <h3>Documents</h3>
                            <ul>
                                <li><a href="#"><i class="ti-file"></i> Annual Report 2025 <span>PDF &middot; 4.1 MB</span></a></li>
                                <li><a href="#"><i class="ti-file"></i> Audited Financial Statements 2025 <span>PDF &middot; 1.3 MB</span></a></li>
                                <li><a href="#"><i class="ti-file"></i> Unit Cost Schedule 2026 <span>PDF &middot; 290 KB</span></a></li>
                                <li><a href="#"><i class="ti-file"></i> Safeguarding Policy <span>PDF &middot; 410 KB</span></a></li>
                                <li><a href="#"><i class="ti-file"></i> Anti-Fraud &amp; Whistleblowing Policy <span>PDF &middot; 265 KB</span></a></li>
                                <li><a href="#"><i class="ti-file"></i> Five-Year Strategy 2026-2030 <span>PDF &middot; 2.8 MB</span></a></li>
                            </ul>
                            <div class="urf-reg-box">
                                <h4>Registration</h4>
                                <p>{reg}<br>
                                   Public Fundraising Appeals licence PFA/2026/0417<br>
                                   KRA PIN P051884402C<br>
                                   Auditor: PKF Eastern Africa, Nairobi</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Spend breakdown end -->

        <!-- What didn't work -->
        <section class="urf-section">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8 col-lg-9">
                        <div class="section-tittle text-center mb-60">
                            <span class="urf-eyebrow-dark">Lessons learned</span>
                            <h2>What we are improving in 2026</h2>
                            <p>Three areas that underperformed last year, and the corrective action we have taken.</p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6">
                        <div class="urf-learn-card">
                            <span>01</span>
                            <h4>Shinyanga savings groups underperformed</h4>
                            <p>Nine of the 22 groups we started in Shinyanga had collapsed within a year. We had trained
                                in Swahili but the trading language was Sukuma. We have rehired locally and restarted six.</p>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="urf-learn-card">
                            <span>02</span>
                            <h4>Two Marsabit boreholes ran dry</h4>
                            <p>Our hydrological survey underestimated seasonal draw-down. Both sites now need deepening
                                at a cost of KES 1.1M, which we are funding from reserves rather than new appeals.</p>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="urf-learn-card">
                            <span>03</span>
                            <h4>Digital mentoring attendance dropped</h4>
                            <p>Remote mentoring sessions for scholars dropped to 41% attendance once data bundles ran out.
                                We now budget airtime into the scholarship itself.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- What didn't work end -->

""" + CTA_BAND + PARTNERS_STRIP


# ---------------------------------------------------------------------------
# Donate
# ---------------------------------------------------------------------------

DONATE = bradcam("Make a Donation", "Donate", "bradcam2") + """
        <section class="urf-section">
            <div class="container">
                <div class="row">
                    <div class="col-xl-7 col-lg-7">
                        <div class="urf-donate-card">
                            <h2>Give to Ubuntu Rising</h2>
                            <p class="urf-donate-sub">87% of your gift reaches the field. You receive a receipt
                                immediately and a report on exactly where it went within 90 days.</p>

                            <form action="#" method="post" class="urf-donate-form" id="donateForm">
                                <div class="urf-toggle" role="tablist">
                                    <button type="button" class="urf-toggle-btn active" data-freq="once">Give once</button>
                                    <button type="button" class="urf-toggle-btn" data-freq="monthly">Give monthly</button>
                                </div>

                                <div class="urf-field">
                                    <label for="currency">Currency</label>
                                    <select id="currency" name="currency" class="urf-select">
                                        <option value="KES" data-symbol="KES">Kenyan Shilling (KES)</option>
                                        <option value="USD" data-symbol="$">US Dollar (USD)</option>
                                        <option value="GBP" data-symbol="&pound;">Pound Sterling (GBP)</option>
                                        <option value="EUR" data-symbol="&euro;">Euro (EUR)</option>
                                    </select>
                                </div>

                                <div class="urf-field">
                                    <label>Choose an amount</label>
                                    <div class="urf-amounts">
                                        <button type="button" class="urf-amount" data-amount="2500">
                                            <strong><span class="urf-cur">KES</span> 2,500</strong>
                                            <span>One term of school for a girl</span>
                                        </button>
                                        <button type="button" class="urf-amount active" data-amount="7500">
                                            <strong><span class="urf-cur">KES</span> 7,500</strong>
                                            <span>A health volunteer&rsquo;s kit and training</span>
                                        </button>
                                        <button type="button" class="urf-amount" data-amount="32000">
                                            <strong><span class="urf-cur">KES</span> 32,000</strong>
                                            <span>A start-up grant for one woman trader</span>
                                        </button>
                                        <button type="button" class="urf-amount" data-amount="48000">
                                            <strong><span class="urf-cur">KES</span> 48,000</strong>
                                            <span>A full year of secondary school</span>
                                        </button>
                                    </div>
                                    <div class="urf-custom-amount">
                                        <span class="urf-cur-prefix">KES</span>
                                        <input type="number" min="100" step="100" name="amount" id="customAmount"
                                               placeholder="Other amount" aria-label="Other amount">
                                    </div>
                                </div>

                                <div class="urf-field">
                                    <label for="designation">Send my gift to</label>
                                    <select id="designation" name="designation" class="urf-select">
                                        <option>Where it is needed most</option>
                                        <option>Education &amp; scholarships</option>
                                        <option>Clean water &amp; sanitation</option>
                                        <option>Women&rsquo;s livelihoods</option>
                                        <option>Community health</option>
                                        <option>Youth climate action</option>
                                    </select>
                                </div>

                                <div class="row">
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="donor-name">Full name</label>
                                            <input type="text" id="donor-name" name="name" placeholder="Your name" required>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="donor-email">Email</label>
                                            <input type="email" id="donor-email" name="email" placeholder="your@email.com" required>
                                        </div>
                                    </div>
                                </div>

                                <div class="urf-field">
                                    <label>Pay by</label>
                                    <div class="urf-pay-methods">
                                        <label class="urf-pay"><input type="radio" name="method" value="mpesa" checked><span>M-PESA</span></label>
                                        <label class="urf-pay"><input type="radio" name="method" value="card"><span>Card</span></label>
                                        <label class="urf-pay"><input type="radio" name="method" value="bank"><span>Bank transfer</span></label>
                                        <label class="urf-pay"><input type="radio" name="method" value="paypal"><span>PayPal</span></label>
                                    </div>
                                </div>

                                <div class="urf-checkline">
                                    <input type="checkbox" id="giftaid" name="giftaid">
                                    <label for="giftaid">I am a UK taxpayer. Add Gift Aid and make my gift worth 25% more.</label>
                                </div>

                                <button type="submit" class="btn urf-btn-solid urf-btn-block">
                                    Donate <span class="urf-cur">KES</span> <span id="summaryAmount">7,500</span> <span id="summaryFreq"></span>
                                </button>
                                <p class="urf-donate-foot"><i class="ti-lock"></i> Payments are processed securely. Ubuntu
                                    Rising Foundation never stores your card details.</p>
                            </form>
                        </div>
                    </div>

                    <div class="col-xl-5 col-lg-5">
                        <div class="urf-side-card">
                            <h3>Other ways to give</h3>
                            <div class="urf-give-way">
                                <h4><i class="ti-mobile"></i> M-PESA Paybill</h4>
                                <p>Paybill <strong>880 440</strong>, account <strong>UBUNTU</strong> followed by your
                                    initials. Your SMS receipt is a valid tax receipt in Kenya.</p>
                                <a href="{wa_link_donate}" target="_blank" rel="noopener" class="urf-btn-wa mt-10">
                                    <i class="fab fa-whatsapp"></i> Get help on WhatsApp</a>
                            </div>
                            <div class="urf-give-way">
                                <h4><i class="ti-wallet"></i> Bank transfer</h4>
                                <p>Ubuntu Rising Foundation<br>
                                   Equity Bank Kenya, Westlands branch<br>
                                   KES account 0170 2951 8847 &middot; SWIFT EQBLKENA<br>
                                   USD account 0170 2951 8848</p>
                            </div>
                            <div class="urf-give-way">
                                <h4><i class="ti-gift"></i> Leave a gift in your will</h4>
                                <p>Legacies funded eleven boreholes last year. Email
                                   <a href="mailto:{email}">{email}</a> to request our legacy pack.</p>
                            </div>
                            <div class="urf-give-way">
                                <h4><i class="ti-briefcase"></i> Payroll giving</h4>
                                <p>Eleven Nairobi employers match staff donations through our payroll scheme.
                                   <a href="partners.html">Set it up at your company</a>.</p>
                            </div>
                        </div>

                        <div class="urf-side-card urf-side-card-dark">
                            <h3>What your money buys</h3>
                            <ul class="urf-ticks urf-ticks-light">
                                <li>KES 2,500: one term of school for a girl</li>
                                <li>KES 7,500: a health volunteer&rsquo;s kit and training</li>
                                <li>KES 32,000: a start-up grant for a woman trader</li>
                                <li>KES 48,000: a full year of secondary school</li>
                                <li>KES 180,000: a six-month youth climate fellowship</li>
                                <li>KES 1.8M: a solar borehole, handed over and maintained</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>

""" + impact_counters("urf-stats-dark") + PARTNERS_STRIP


# ---------------------------------------------------------------------------
# Volunteer
# ---------------------------------------------------------------------------

VOLUNTEER = bradcam("Volunteer With Us", "Volunteer", "bradcam3") + """
        <section class="urf-section">
            <div class="container">
                <div class="row">
                    <div class="col-lg-5">
                        <div class="section-tittle">
                            <span class="urf-eyebrow-dark">1,150 volunteers</span>
                            <h2>Skilled volunteers, wherever you are</h2>
                        </div>
                    </div>
                    <div class="col-lg-7">
                        <p class="urf-lead">We do not run volunteer tourism. What we need is skilled professionals giving a
                            few focused hours a month: bookkeeping, translation, grant writing, hydrology review,
                            teacher training and design.</p>
                        <p>If you are in East Africa, we also run community roles: mentoring scholars, supporting savings
                            groups and helping at mobile clinics. Field placements exist but are limited to professionals
                            filling a skills gap our local teams have identified, and they are never shorter than eight weeks.</p>
                        <p>Every volunteer completes safeguarding training and a reference check before starting. This
                            process is never shortened.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Roles -->
        <section class="urf-section urf-bg-soft pt-0">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8"><div class="section-tittle text-center mb-60">
                        <span class="urf-eyebrow-dark">Open roles</span>
                        <h2>Roles open right now</h2>
                    </div></div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6">
                        <div class="urf-role">
                            <span class="urf-pill">Remote &middot; 4 hrs/month</span>
                            <h4>Finance associate</h4>
                            <p>Help our country teams reconcile monthly ledgers. Qualified or part-qualified accountants.</p>
                            <small><i class="ti-time"></i> Minimum 12-month commitment</small>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="urf-role">
                            <span class="urf-pill">Remote &middot; 6 hrs/month</span>
                            <h4>Grant writer</h4>
                            <p>Draft and edit trust and foundation applications with our programmes team.</p>
                            <small><i class="ti-time"></i> Minimum 6-month commitment</small>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="urf-role">
                            <span class="urf-pill">Nairobi &middot; 1 day/month</span>
                            <h4>Scholar mentor</h4>
                            <p>Meet two sponsored students a month in Mathare or Kibera. Training provided.</p>
                            <small><i class="ti-time"></i> Minimum 2-year commitment</small>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="urf-role">
                            <span class="urf-pill">Remote &middot; project based</span>
                            <h4>Hydrology reviewer</h4>
                            <p>Second-opinion review of borehole siting surveys before we commit drilling funds.</p>
                            <small><i class="ti-time"></i> 2-3 reviews per year</small>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="urf-role">
                            <span class="urf-pill">Kakamega &middot; 8-12 weeks</span>
                            <h4>Teacher trainer (field)</h4>
                            <p>In-service training for 112 community teachers. Qualified secondary teachers only.</p>
                            <small><i class="ti-time"></i> Travel and accommodation covered</small>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="urf-role">
                            <span class="urf-pill">Remote &middot; 3 hrs/month</span>
                            <h4>Swahili / Luganda translator</h4>
                            <p>Translate training materials and community reports. Native speakers preferred.</p>
                            <small><i class="ti-time"></i> Minimum 6-month commitment</small>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Roles end -->

        <!-- Sign up -->
        <section class="urf-section">
            <div class="container">
                <div class="row">
                    <div class="col-lg-7">
                        <div class="urf-form-card">
                            <h2>Volunteer sign-up</h2>
                            <p>Tell us what you can do and how much time you have. A real person replies within five
                                working days.</p>
                            <form class="form-contact" action="contact_process.php" method="post" id="volunteerForm">
                                <input type="hidden" name="subject" value="Volunteer application">
                                <div class="row">
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="v-name">Full name</label>
                                            <input type="text" id="v-name" name="name" placeholder="Your name" required>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="v-email">Email</label>
                                            <input type="email" id="v-email" name="email" placeholder="your@email.com" required>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="v-location">Where are you based?</label>
                                            <input type="text" id="v-location" name="location" placeholder="City and country">
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="v-role">Role you are interested in</label>
                                            <select id="v-role" name="role" class="urf-select">
                                                <option>Finance associate</option>
                                                <option>Grant writer</option>
                                                <option>Scholar mentor</option>
                                                <option>Hydrology reviewer</option>
                                                <option>Teacher trainer (field)</option>
                                                <option>Translator</option>
                                                <option>Something else, I&rsquo;ll explain below</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="v-hours">Hours you can give each month</label>
                                            <select id="v-hours" name="hours" class="urf-select">
                                                <option>1-4 hours</option>
                                                <option>5-10 hours</option>
                                                <option>10-20 hours</option>
                                                <option>Full-time field placement</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="v-start">Earliest start</label>
                                            <input type="text" id="v-start" name="start" placeholder="e.g. November 2026">
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="urf-field">
                                            <label for="v-message">Your skills and experience</label>
                                            <textarea id="v-message" name="message" rows="6"
                                                placeholder="Tell us what you do professionally and why this work interests you."></textarea>
                                        </div>
                                    </div>
                                </div>
                                <div class="urf-checkline">
                                    <input type="checkbox" id="v-safeguard" name="safeguarding" required>
                                    <label for="v-safeguard">I understand that all volunteers complete safeguarding
                                        training and a reference check before starting.</label>
                                </div>
                                <div class="urf-btn-row">
                                    <button type="submit" class="btn urf-btn-solid">Send my application <i class="ti-arrow-right"></i></button>
                                    <a href="{wa_link_volunteer}" target="_blank" rel="noopener" class="urf-btn-wa"><i class="fab fa-whatsapp"></i> Ask about a role</a>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="col-lg-5">
                        <div class="urf-side-card">
                            <h3>What happens next</h3>
                            <ol class="urf-steps">
                                <li><strong>Within 5 days</strong>: a programme coordinator emails you.</li>
                                <li><strong>Week 2</strong>: a 30-minute video call about fit and availability.</li>
                                <li><strong>Week 3</strong>: two references and a safeguarding check.</li>
                                <li><strong>Week 4</strong>: two hours of online induction and you start.</li>
                            </ol>
                        </div>
                        <div class="urf-side-card urf-side-card-dark">
                            <h3>Short on time?</h3>
                            <p>A volunteer finance associate saves us roughly KES 420,000 a year. If you cannot give
                                time, a donation of the same value has exactly the same effect.</p>
                            <a href="donate.html" class="btn urf-btn-solid">Donate instead <i class="ti-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Sign up end -->
"""


# ---------------------------------------------------------------------------
# Partners
# ---------------------------------------------------------------------------

PARTNERS = bradcam("Corporate Partnerships", "Partners") + """
        <section class="urf-section">
            <div class="container">
                <div class="row">
                    <div class="col-lg-5">
                        <div class="section-tittle">
                            <span class="urf-eyebrow-dark">For companies &amp; grant makers</span>
                            <h2>Long-term partnerships with measurable outcomes</h2>
                        </div>
                    </div>
                    <div class="col-lg-7">
                        <p class="urf-lead">We seek three-year commitments rather than logo placements. In return you
                            receive a named relationship lead, quarterly reporting against agreed indicators, field
                            access for your staff and board, and audited figures for your own annual report.</p>
                        <p>Current partners include Safaricom Foundation, Equity Group, Mastercard Foundation, UNICEF
                            Kenya, the Segal Family Trust and four county governments. Our average corporate partnership
                            has now run for 4.2 years.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Partnership tiers -->
        <section class="urf-section urf-bg-soft pt-0">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-8"><div class="section-tittle text-center mb-60">
                        <span class="urf-eyebrow-dark">Ways to partner</span>
                        <h2>Four ways to partner with us</h2>
                    </div></div>
                </div>
                <div class="row">
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-tier">
                            <h4>Programme co-funding</h4>
                            <span class="urf-tier-price">From KES 5M / year</span>
                            <ul class="urf-ticks">
                                <li>Fund a named programme in a named county</li>
                                <li>Quarterly indicator reporting</li>
                                <li>Two field visits a year</li>
                                <li>Audited figures for your annual report</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-tier urf-tier-featured">
                            <h4>Payroll giving &amp; matching</h4>
                            <span class="urf-tier-price">No minimum</span>
                            <ul class="urf-ticks">
                                <li>Staff give monthly from pre-tax salary</li>
                                <li>You match pound for pound, or not</li>
                                <li>We handle enrolment and comms</li>
                                <li>Live dashboard of collective impact</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-tier">
                            <h4>Skills-based volunteering</h4>
                            <span class="urf-tier-price">In-kind</span>
                            <ul class="urf-ticks">
                                <li>Teams of 5-20 on defined projects</li>
                                <li>Finance, legal, engineering, digital</li>
                                <li>Scoped by our country leads</li>
                                <li>Safeguarding training included</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <div class="urf-tier">
                            <h4>Grant makers &amp; trusts</h4>
                            <span class="urf-tier-price">Restricted or core</span>
                            <ul class="urf-ticks">
                                <li>Full logframes and MEL framework</li>
                                <li>Due diligence pack on request</li>
                                <li>Core funding gratefully accepted</li>
                                <li>Independent evaluation co-funded</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Partnership tiers end -->

        <!-- Enquiry -->
        <section class="urf-section">
            <div class="container">
                <div class="row">
                    <div class="col-lg-7">
                        <div class="urf-form-card">
                            <h2>Talk to our partnerships team</h2>
                            <p>Tell us a little about your organisation and what you are trying to achieve. Our Director
                                of Partnerships replies personally within three working days.</p>
                            <form class="form-contact" action="contact_process.php" method="post" id="partnerForm">
                                <input type="hidden" name="subject" value="Corporate partnership enquiry">
                                <div class="row">
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="p-name">Your name</label>
                                            <input type="text" id="p-name" name="name" placeholder="Full name" required>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="p-role">Job title</label>
                                            <input type="text" id="p-role" name="role" placeholder="e.g. Head of Sustainability">
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="p-org">Organisation</label>
                                            <input type="text" id="p-org" name="organisation" placeholder="Company or trust name" required>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="p-email">Work email</label>
                                            <input type="email" id="p-email" name="email" placeholder="you@company.com" required>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="p-type">Partnership type</label>
                                            <select id="p-type" name="type" class="urf-select">
                                                <option>Programme co-funding</option>
                                                <option>Payroll giving &amp; matching</option>
                                                <option>Skills-based volunteering</option>
                                                <option>Grant or trust funding</option>
                                                <option>Gift in kind</option>
                                                <option>Not sure yet</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="urf-field">
                                            <label for="p-budget">Indicative annual budget</label>
                                            <select id="p-budget" name="budget" class="urf-select">
                                                <option>Under KES 1M</option>
                                                <option>KES 1M-5M</option>
                                                <option>KES 5M-20M</option>
                                                <option>Over KES 20M</option>
                                                <option>In-kind only</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="urf-field">
                                            <label for="p-message">What are you hoping to achieve?</label>
                                            <textarea id="p-message" name="message" rows="6"
                                                placeholder="Your CSR priorities, reporting requirements, timelines."></textarea>
                                        </div>
                                    </div>
                                </div>
                                <div class="urf-btn-row">
                                    <button type="submit" class="btn urf-btn-solid">Send enquiry <i class="ti-arrow-right"></i></button>
                                    <a href="{wa_link_partner}" target="_blank" rel="noopener" class="urf-btn-wa"><i class="fab fa-whatsapp"></i> Message us directly</a>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="col-lg-5">
                        <div class="urf-side-card">
                            <h3>Partnerships contact</h3>
                            <div class="media contact-info">
                                <span class="contact-info__icon"><i class="ti-user"></i></span>
                                <div class="media-body">
                                    <h3>Khalid Hassan</h3>
                                    <p>Director of Partnerships</p>
                                </div>
                            </div>
                            <div class="media contact-info">
                                <span class="contact-info__icon"><i class="ti-email"></i></span>
                                <div class="media-body">
                                    <h3><a href="mailto:{partnerships_email}">{partnerships_email}</a></h3>
                                    <p>Replies within three working days</p>
                                </div>
                            </div>
                            <div class="media contact-info">
                                <span class="contact-info__icon"><i class="ti-comment-alt"></i></span>
                                <div class="media-body">
                                    <h3><a href="{wa_link_partner}" target="_blank" rel="noopener">Chat on WhatsApp</a></h3>
                                    <p>Mon-Fri, 8.30am-5pm EAT</p>
                                </div>
                            </div>
                        </div>
                        <div class="urf-side-card urf-side-card-dark">
                            <h3>Due diligence pack</h3>
                            <p>Constitution, NGO Board certificate, audited accounts, safeguarding and anti-fraud
                                policies, MEL framework and two referee contacts, sent on request, same day.</p>
                            <a href="impact.html" class="btn urf-btn-solid">See our published accounts <i class="ti-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Enquiry end -->

""" + PARTNERS_STRIP


# ---------------------------------------------------------------------------
# Blog
# ---------------------------------------------------------------------------

POSTS = [
    ("single_blog_1.jpg", "18", "Sep", "Health",
     "How eleven mobile clinics reached 9,700 people",
     "Our community health teams ran eleven fixed monthly routes last quarter, lifting immunisation coverage from 51% "
     "to 88% in the villages they serve. The decisive factor was not the clinical offer but the reliability of the "
     "schedule."),
    ("single_blog_2.jpg", "02", "Sep", "Climate",
     "What we learned from planting 60,000 seedlings",
     "Our first youth climate cohort achieved only 34 per cent seedling survival. After changing the species mix, "
     "moving planting into the long rains and funding two years of aftercare, survival now stands at 71 per cent."),
    ("single_blog_3.jpg", "21", "Aug", "Education",
     "Returning 400 girls to school after the drought",
     "When the 2024 rains failed in Kakamega, families withdrew daughters from school first. After six months of "
     "household visits by Beatrice Ayuma and her team, 381 of the 400 girls are back in class."),
    ("single_blog_4.jpg", "09", "Aug", "Water",
     "Why every borehole now includes three years of maintenance",
     "Our first borehole in Siaya failed within nine months because no one owned the repairs. That single lesson "
     "reshaped the design of the entire water programme."),
    ("single_blog_5.jpg", "27", "Jul", "Livelihoods",
     "How 190 savings groups saved KES 61 million",
     "Members have saved four times what we have invested. We look at how those funds are used, and why the group "
     "loan book matters more than the start-up grant."),
]


def blog_article(p):
    img, day, mon, cat, title, excerpt = p
    return f"""                            <article class="blog_item">
                                <div class="blog_item_img">
                                    <img class="card-img rounded-0" src="assets/img/blog/{img}" alt="{title}">
                                    <a href="blog_details.html" class="blog_item_date">
                                        <h3>{day}</h3>
                                        <p>{mon}</p>
                                    </a>
                                </div>
                                <div class="blog_details">
                                    <a class="d-inline-block" href="blog_details.html">
                                        <h2 class="blog-head">{title}</h2>
                                    </a>
                                    <p>{excerpt}</p>
                                    <ul class="blog-info-link">
                                        <li><a href="#"><i class="fa fa-user"></i> Ubuntu Rising</a></li>
                                        <li><a href="#"><i class="fa fa-bookmark"></i> {cat}</a></li>
                                    </ul>
                                </div>
                            </article>
"""


SIDEBAR = """                        <div class="blog_right_sidebar">
                            <aside class="single_sidebar_widget search_widget">
                                <form action="#">
                                    <div class="form-group">
                                        <div class="input-group mb-3">
                                            <input type="text" class="form-control" placeholder="Search stories" aria-label="Search stories">
                                            <div class="input-group-append">
                                                <button class="btns" type="button"><i class="ti-search"></i></button>
                                            </div>
                                        </div>
                                    </div>
                                    <button class="button rounded-0 primary-bg text-white w-100 btn_1 boxed-btn" type="submit">Search</button>
                                </form>
                            </aside>
                            <aside class="single_sidebar_widget post_category_widget">
                                <h4 class="widget_title">Categories</h4>
                                <ul class="list cat-list">
                                    <li><a href="#" class="d-flex"><p>Education</p><p>(24)</p></a></li>
                                    <li><a href="#" class="d-flex"><p>Clean water</p><p>(18)</p></a></li>
                                    <li><a href="#" class="d-flex"><p>Women&rsquo;s livelihoods</p><p>(15)</p></a></li>
                                    <li><a href="#" class="d-flex"><p>Community health</p><p>(11)</p></a></li>
                                    <li><a href="#" class="d-flex"><p>Youth climate action</p><p>(09)</p></a></li>
                                    <li><a href="#" class="d-flex"><p>Transparency notes</p><p>(07)</p></a></li>
                                </ul>
                            </aside>
                            <aside class="single_sidebar_widget popular_post_widget">
                                <h3 class="widget_title">Recent stories</h3>
                                <div class="media post_item">
                                    <img src="assets/img/post/post_1.jpg" alt="Classroom in Kakamega">
                                    <div class="media-body">
                                        <a href="blog_details.html"><h3>400 girls back in class</h3></a>
                                        <p>21 August 2026</p>
                                    </div>
                                </div>
                                <div class="media post_item">
                                    <img src="assets/img/post/post_2.jpg" alt="Water from a borehole">
                                    <div class="media-body">
                                        <a href="blog_details.html"><h3>Three years of maintenance, budgeted</h3></a>
                                        <p>09 August 2026</p>
                                    </div>
                                </div>
                                <div class="media post_item">
                                    <img src="assets/img/post/post_3.jpg" alt="A woman trader">
                                    <div class="media-body">
                                        <a href="blog_details.html"><h3>KES 61M saved by members</h3></a>
                                        <p>27 July 2026</p>
                                    </div>
                                </div>
                                <div class="media post_item">
                                    <img src="assets/img/post/post_4.jpg" alt="Mobile health clinic">
                                    <div class="media-body">
                                        <a href="blog_details.html"><h3>Eleven clinics, 9,700 people</h3></a>
                                        <p>18 September 2026</p>
                                    </div>
                                </div>
                            </aside>
                            <aside class="single_sidebar_widget tag_cloud_widget">
                                <h4 class="widget_title">Tags</h4>
                                <ul class="list">
                                    <li><a href="#">Kenya</a></li>
                                    <li><a href="#">Uganda</a></li>
                                    <li><a href="#">Tanzania</a></li>
                                    <li><a href="#">Rwanda</a></li>
                                    <li><a href="#">Scholarships</a></li>
                                    <li><a href="#">Boreholes</a></li>
                                    <li><a href="#">Savings groups</a></li>
                                    <li><a href="#">Volunteers</a></li>
                                    <li><a href="#">Accountability</a></li>
                                </ul>
                            </aside>
                            <aside class="single_sidebar_widget urf-sidebar-cta">
                                <h4 class="widget_title">Support this work</h4>
                                <p>KES 2,500 keeps a girl in school for a full term.</p>
                                <a href="donate.html" class="btn urf-btn-solid">Donate now <i class="ti-arrow-right"></i></a>
                                <a href="{wa_link_donate}" target="_blank" rel="noopener" class="urf-btn-wa mt-10"><i class="fab fa-whatsapp"></i> Give via WhatsApp</a>
                            </aside>
                        </div>
"""


BLOG = bradcam("News &amp; Stories", "News", "bradcam2") + """
        <section class="blog_area section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 mb-5 mb-lg-0">
                        <div class="blog_left_sidebar">
""" + "".join(blog_article(p) for p in POSTS) + """
                            <nav class="blog-pagination justify-content-center d-flex">
                                <ul class="pagination">
                                    <li class="page-item"><a href="#" class="page-link" aria-label="Previous"><i class="ti-angle-left"></i></a></li>
                                    <li class="page-item active"><a href="#" class="page-link">1</a></li>
                                    <li class="page-item"><a href="#" class="page-link">2</a></li>
                                    <li class="page-item"><a href="#" class="page-link" aria-label="Next"><i class="ti-angle-right"></i></a></li>
                                </ul>
                            </nav>
                        </div>
                    </div>
                    <div class="col-lg-4">
""" + SIDEBAR + """                    </div>
                </div>
            </div>
        </section>

""" + NEWSLETTER


BLOG_DETAILS = bradcam("Story", "News", "bradcam2") + """
        <section class="blog_area single-post-area section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 posts-list">
                        <div class="single-post">
                            <div class="feature-img">
                                <img class="img-fluid" src="assets/img/blog/single_blog_1.jpg"
                                     alt="Community health volunteers running a mobile clinic">
                            </div>
                            <div class="blog_details">
                                <h2>How eleven mobile clinics reached 9,700 people</h2>
                                <ul class="blog-info-link mt-3 mb-4">
                                    <li><a href="#"><i class="fa fa-user"></i> Dr. Faith Chebet, Health Programme Lead</a></li>
                                    <li><a href="#"><i class="fa fa-calendar"></i> 18 September 2026</a></li>
                                    <li><a href="#"><i class="fa fa-bookmark"></i> Community Health</a></li>
                                </ul>
                                <p class="excert">When we costed our first mobile clinic in 2021, we budgeted carefully
                                    for drugs, fuel, a clinical officer and a cold chain. What we underestimated was the
                                    factor that mattered most, and which appears on no invoice: arriving on the same day
                                    of the month, every month, without exception.</p>
                                <p>In the first six months, attendance on our Mwanza route averaged nineteen people a
                                    day. These villages had seen short-lived outreach programmes before, and few
                                    households were willing to rearrange a planting day around a vehicle that might not
                                    return.</p>
                                <p>By month fourteen the same route was seeing one hundred and forty people a day, and
                                    community health volunteers were being asked to arrive earlier. The clinical offer
                                    had not changed. What had changed was that the vehicle had arrived fourteen times.</p>
                                <blockquote class="blockquote">
                                    <p class="mb-0">Reliability, not ambition, is what builds trust in a community
                                        health service, and it is the hardest thing to sustain.</p>
                                    <footer class="blockquote-footer">Dr. Faith Chebet</footer>
                                </blockquote>
                                <p>Across the eleven routes we now run in Kenya, Tanzania and Uganda, we saw 9,700
                                    people last quarter. Immunisation coverage in the villages served monthly has risen
                                    from 51 per cent to 88 per cent, and antenatal attendance has roughly doubled. These
                                    are the outcomes of a routine service delivered consistently.</p>
                                <h3>What it costs</h3>
                                <p>One clinic day, serving around 140 people, costs KES 68,000: fuel, drugs, the clinical
                                    officer&rsquo;s day rate, consumables and the stipends of six community health
                                    volunteers. Training and equipping one of those volunteers costs KES 24,000 and they
                                    typically stay with us for four years.</p>
                                <p>The commitment is the expensive part. A route cannot be funded for six months and
                                    then reviewed, so we will not open one unless two years of funding is secured. That
                                    is why our Mwanza expansion appeal covers three routes rather than eight.</p>
                                <h3>What we are still improving</h3>
                                <p>Referral follow-up remains weak. Of the patients we refer to district hospitals,
                                    we only confirm arrival for about 60 per cent. We are piloting a phone follow-up
                                    protocol in two routes this quarter and will publish the result either way.</p>
                                <p>If you would like to fund a route, or you are a clinician able to give two days a
                                    month, we would be glad to hear from you.</p>
                            </div>
                        </div>

                        <div class="navigation-top">
                            <div class="d-sm-flex justify-content-between text-center">
                                <p class="like-info"><span class="align-middle"><i class="fa fa-heart"></i></span> 284 people liked this</p>
                                <div class="col-sm-4 text-center my-2 my-sm-0"></div>
                                <ul class="social-icons">
                                    <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
                                    <li><a href="#"><i class="fab fa-twitter"></i></a></li>
                                    <li><a href="#"><i class="fab fa-linkedin-in"></i></a></li>
                                </ul>
                            </div>
                            <div class="navigation-area">
                                <div class="row">
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-12 nav-left flex-row d-flex justify-content-start align-items-center">
                                        <div class="thumb"><a href="blog_details.html"><img class="img-fluid" src="assets/img/post/preview.png" alt=""></a></div>
                                        <div class="arrow"><a href="blog_details.html"><span class="lnr text-white ti-arrow-left"></span></a></div>
                                        <div class="detials"><p>Prev post</p><a href="blog_details.html"><h4>What we learned from planting 60,000 seedlings</h4></a></div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-6 col-12 nav-right flex-row d-flex justify-content-end align-items-center">
                                        <div class="detials"><p>Next post</p><a href="blog_details.html"><h4>Returning 400 girls to school after the drought</h4></a></div>
                                        <div class="arrow"><a href="blog_details.html"><span class="lnr text-white ti-arrow-right"></span></a></div>
                                        <div class="thumb"><a href="blog_details.html"><img class="img-fluid" src="assets/img/post/next.png" alt=""></a></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="urf-post-cta">
                            <h3>Fund a mobile clinic route</h3>
                            <p>KES 68,000 covers one clinic day serving around 140 people.</p>
                            <div class="urf-btn-row">
                                <a href="donate.html" class="btn urf-btn-solid">Donate now <i class="ti-arrow-right"></i></a>
                                <a href="{wa_link_donate}" target="_blank" rel="noopener" class="urf-btn-wa"><i class="fab fa-whatsapp"></i> Give via WhatsApp</a>
                            </div>
                        </div>

                        <div class="comments-area">
                            <h4>3 Comments</h4>
                            <div class="comment-list">
                                <div class="single-comment justify-content-between d-flex">
                                    <div class="user justify-content-between d-flex">
                                        <div class="thumb"><img src="assets/img/post/post_5.jpg" alt=""></div>
                                        <div class="desc">
                                            <p class="comment">This is the first NGO report I have read that mentions a
                                                60 per cent referral confirmation rate instead of burying it. Thank you.</p>
                                            <div class="d-flex justify-content-between">
                                                <div class="d-flex align-items-center">
                                                    <h5><a href="#">Wanjiru Kamau</a></h5>
                                                    <p class="date">19 September 2026</p>
                                                </div>
                                                <div class="reply-btn"><a href="#" class="btn-reply">Reply</a></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="single-comment justify-content-between d-flex">
                                    <div class="user justify-content-between d-flex">
                                        <div class="thumb"><img src="assets/img/post/post_6.jpg" alt=""></div>
                                        <div class="desc">
                                            <p class="comment">I am a clinical officer in Kisumu and would like to give
                                                two days a month. Who do I write to?</p>
                                            <div class="d-flex justify-content-between">
                                                <div class="d-flex align-items-center">
                                                    <h5><a href="#">Peter Omondi</a></h5>
                                                    <p class="date">19 September 2026</p>
                                                </div>
                                                <div class="reply-btn"><a href="volunteer.html" class="btn-reply">Reply</a></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="single-comment justify-content-between d-flex">
                                    <div class="user justify-content-between d-flex">
                                        <div class="thumb"><img src="assets/img/post/post_7.jpg" alt=""></div>
                                        <div class="desc">
                                            <p class="comment">Our company funds one route in Shinyanga. The quarterly
                                                reporting is genuinely usable. It goes straight into our board pack.</p>
                                            <div class="d-flex justify-content-between">
                                                <div class="d-flex align-items-center">
                                                    <h5><a href="#">Aisha Rahman</a></h5>
                                                    <p class="date">22 September 2026</p>
                                                </div>
                                                <div class="reply-btn"><a href="#" class="btn-reply">Reply</a></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="comment-form">
                            <h4>Leave a comment</h4>
                            <form class="form-contact comment_form" action="contact_process.php" method="post" id="commentForm">
                                <div class="row">
                                    <div class="col-12">
                                        <div class="form-group">
                                            <textarea class="form-control w-100" name="message" id="comment" cols="30" rows="9" placeholder="Write your comment"></textarea>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="form-group">
                                            <input class="form-control" name="name" id="c-name" type="text" placeholder="Your name">
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="form-group">
                                            <input class="form-control" name="email" id="c-email" type="email" placeholder="Your email">
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="form-group">
                                            <input class="form-control" name="subject" id="c-subject" type="text" placeholder="Subject">
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <button type="submit" class="button button-contactForm btn_4 boxed-btn">Post comment</button>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="col-lg-4">
""" + SIDEBAR + """                    </div>
                </div>
            </div>
        </section>

""" + CTA_BAND


# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------

CONTACT = bradcam("Contact Us", "Contact", "bradcam3") + """
        <section class="contact-section urf-section">
            <div class="container">
                <div class="row mb-5">
                    <div class="col-12">
                        <div class="urf-map">
                            <iframe title="Ubuntu Rising Foundation, Riverside Drive, Westlands, Nairobi"
                                src="https://www.openstreetmap.org/export/embed.html?bbox=36.7960%2C-1.2760%2C36.8200%2C-1.2560&amp;layer=mapnik&amp;marker=-1.2660%2C36.8080"
                                loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-8">
                        <h2 class="contact-title">Get in touch</h2>
                        <p class="mb-40">For media, general questions or anything that does not fit a form below.
                            Corporate partners should use the <a href="partners.html">partnerships form</a>, and
                            volunteers the <a href="volunteer.html">volunteer form</a>, it reaches the right
                            person faster.</p>
                        <form class="form-contact contact_form" action="contact_process.php" method="post" id="contactForm" novalidate="novalidate">
                            <div class="row">
                                <div class="col-12">
                                    <div class="form-group">
                                        <textarea class="form-control w-100" name="message" id="message" cols="30" rows="9"
                                            placeholder="Enter your message"></textarea>
                                    </div>
                                </div>
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control valid" name="name" id="name" type="text" placeholder="Enter your name">
                                    </div>
                                </div>
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <input class="form-control valid" name="email" id="email" type="email" placeholder="Enter email address">
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="form-group">
                                        <input class="form-control" name="subject" id="subject" type="text" placeholder="Enter subject">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group mt-3">
                                <button type="submit" class="btn urf-btn-solid">Send message <i class="ti-arrow-right"></i></button>
                            </div>
                        </form>
                    </div>
                    <div class="col-lg-3 offset-lg-1">
                        <div class="media contact-info">
                            <span class="contact-info__icon"><i class="ti-home"></i></span>
                            <div class="media-body">
                                <h3>Ubuntu House, Westlands</h3>
                                <p>4th Floor, Riverside Drive<br>Nairobi, Kenya<br>{po}</p>
                            </div>
                        </div>
                        <div class="media contact-info">
                            <span class="contact-info__icon"><i class="ti-comment-alt"></i></span>
                            <div class="media-body">
                                <h3><a href="{wa_link}" target="_blank" rel="noopener">Chat on WhatsApp</a></h3>
                                <p>Fastest reply, Mon to Fri 8.30am-5pm EAT</p>
                            </div>
                        </div>
                        <div class="media contact-info">
                            <span class="contact-info__icon"><i class="ti-email"></i></span>
                            <div class="media-body">
                                <h3><a href="mailto:{email}">{email}</a></h3>
                                <p>We reply within two working days</p>
                            </div>
                        </div>
                        <div class="media contact-info">
                            <span class="contact-info__icon"><i class="ti-briefcase"></i></span>
                            <div class="media-body">
                                <h3><a href="mailto:{partnerships_email}">{partnerships_email}</a></h3>
                                <p>Corporate &amp; grant enquiries</p>
                            </div>
                        </div>
                        <div class="media contact-info">
                            <span class="contact-info__icon"><i class="ti-shield"></i></span>
                            <div class="media-body">
                                <h3>Safeguarding concerns</h3>
                                <p>safeguarding@ubunturising.org<br>Reviewed by a trustee, not by staff.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

""" + CTA_BAND


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

PAGES = [
    ("index.html", "Ubuntu Rising Foundation | Community-led change across East Africa",
     "Ubuntu Rising Foundation is a Nairobi-based NGO working with 42 communities across Kenya, Uganda, Tanzania and "
     "Rwanda on education, clean water, women's livelihoods, health and climate action. Donate, volunteer or partner with us.",
     "index.html", HOME),
    ("about.html", "About Us | Ubuntu Rising Foundation",
     "Founded in Nairobi in 2013, Ubuntu Rising Foundation funds what communities ask for and stays long enough for it "
     "to work. Meet our team, our values and our thirteen-year story.",
     "about.html", ABOUT),
    ("programmes.html", "Our Programmes | Ubuntu Rising Foundation",
     "Education and scholarships, clean water and sanitation, women's economic empowerment, community health and youth "
     "climate action across East Africa, with published unit costs.",
     "programmes.html", PROGRAMMES),
    ("projects.html", "Current Projects | Ubuntu Rising Foundation",
     "Six open appeals in Kenya, Uganda, Tanzania and Rwanda, each with a published budget, a named field lead and a "
     "community committee resolution behind it.",
     "projects.html", PROJECTS),
    ("impact.html", "Impact & Transparency | Ubuntu Rising Foundation",
     "Audited accounts, unit costs, spend breakdown and an honest list of what did not work. 87% of income reaches "
     "the field.",
     "impact.html", IMPACT),
    ("donate.html", "Donate | Ubuntu Rising Foundation",
     "Give once or monthly by M-PESA, card, bank transfer or PayPal. KES 2,500 keeps a girl in school for a term; "
     "KES 1.8M builds a solar borehole.",
     "donate.html", DONATE),
    ("volunteer.html", "Volunteer | Ubuntu Rising Foundation",
     "1,150 people volunteer with Ubuntu Rising, most of them remotely, four hours a month. See open roles and "
     "sign up.",
     "volunteer.html", VOLUNTEER),
    ("partners.html", "Corporate Partnerships | Ubuntu Rising Foundation",
     "Programme co-funding, payroll giving, skills-based volunteering and grant funding. Three-year partnerships with "
     "quarterly reporting and audited figures.",
     "partners.html", PARTNERS),
    ("blog.html", "News & Stories | Ubuntu Rising Foundation",
     "Reporting from our teams in Kenya, Uganda, Tanzania and Rwanda, including the projects that did not go "
     "to plan.",
     "blog.html", BLOG),
    ("blog_details.html", "What eleven mobile clinics taught us about trust | Ubuntu Rising Foundation",
     "Our community health teams reached 9,700 people last quarter. The hardest part was never the medicine.",
     "blog_details.html", BLOG_DETAILS),
    ("contact.html", "Contact Us | Ubuntu Rising Foundation",
     "Ubuntu House, Riverside Drive, Westlands, Nairobi. Phone, email and safeguarding contacts for Ubuntu Rising "
     "Foundation.",
     "contact.html", CONTACT),
]

TOKENS = dict(SITE)


def main():
    # concatenate the stylesheets/scripts first so the cache-busting token in
    # every page's <link>/<script> matches the bundles we just wrote
    build_site.ASSET_V = build_site.build_bundles(build_site.ROOT)
    for path, title, desc, active, body in PAGES:
        for key, value in TOKENS.items():
            body = body.replace("{" + key + "}", value)
        write(path, title, desc, active, body)


if __name__ == "__main__":
    main()
