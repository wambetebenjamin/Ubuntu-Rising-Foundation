/* Ubuntu Rising Foundation — small front-end behaviours
   (donation form interactions and impact counters). */
(function ($) {
    'use strict';

    /* Impact counters are initialised by the template's main.js (.counter). */

    /* ---- Scroll reveal --------------------------------------------------
       Progressive enhancement: without IntersectionObserver (or with reduced
       motion preferred) everything simply stays visible. */
    var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var targets = document.querySelectorAll(
        '.urf-door, .single-cat, .single-cases, .urf-stat, .urf-quote, .urf-tl-item, ' +
        '.urf-person, .urf-role, .urf-tier, .urf-learn-card, .urf-region, ' +
        '.urf-programme-text, .urf-programme-img, .home-blog-single, .urf-spend-row'
    );

    if (!reduced && 'IntersectionObserver' in window && targets.length) {
        Array.prototype.forEach.call(targets, function (el) { el.classList.add('urf-animate'); });

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) { return; }
                var el = entry.target;
                // Stagger siblings so a row of cards cascades rather than snapping in.
                var siblings = el.parentNode.parentNode
                    ? el.parentNode.parentNode.children : [];
                var index = Array.prototype.indexOf.call(siblings, el.parentNode);
                el.style.transitionDelay = Math.max(0, Math.min(index, 4)) * 90 + 'ms';
                el.classList.add('is-visible');
                observer.unobserve(el);
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

        Array.prototype.forEach.call(targets, function (el) { observer.observe(el); });
    }

    /* ---- Donation form -------------------------------------------------- */
    var $form = $('#donateForm');
    if (!$form.length) { return; }

    // Rough indicative conversions from KES so the suggested amounts stay
    // sensible when a donor switches currency.
    var RATES = { KES: 1, USD: 1 / 129, GBP: 1 / 164, EUR: 1 / 140 };
    var SYMBOLS = { KES: 'KES', USD: '$', GBP: '\u00A3', EUR: '\u20AC' };

    function round(value, currency) {
        if (currency === 'KES') { return Math.round(value / 100) * 100; }
        if (value < 50) { return Math.max(1, Math.round(value)); }
        return Math.round(value / 5) * 5;
    }

    function format(value) {
        return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    }

    function currency() { return $('#currency').val() || 'KES'; }

    function refresh() {
        var cur = currency();
        $('.urf-cur, .urf-cur-prefix').html(SYMBOLS[cur]);

        $('.urf-amount').each(function () {
            var $btn = $(this);
            if (!$btn.data('base')) { $btn.data('base', parseInt($btn.attr('data-amount'), 10)); }
            var converted = round($btn.data('base') * RATES[cur], cur);
            $btn.data('value', converted);
            $btn.find('strong').html('<span class="urf-cur">' + SYMBOLS[cur] + '</span> ' + format(converted));
        });

        var custom = parseFloat($('#customAmount').val());
        var chosen = !isNaN(custom) && custom > 0
            ? custom
            : $('.urf-amount.active').data('value') || 0;

        $('#summaryAmount').text(format(chosen));
    }

    $('#currency').on('change', refresh);

    $('.urf-amount').on('click', function () {
        $('.urf-amount').removeClass('active');
        $(this).addClass('active');
        $('#customAmount').val('');
        refresh();
    });

    $('#customAmount').on('input', function () {
        if ($(this).val() !== '') { $('.urf-amount').removeClass('active'); }
        refresh();
    });

    $('.urf-toggle-btn').on('click', function () {
        $('.urf-toggle-btn').removeClass('active');
        $(this).addClass('active');
        $('#summaryFreq').text($(this).data('freq') === 'monthly' ? 'a month' : '');
    });

    $form.on('submit', function (event) {
        event.preventDefault();
        var cur = currency();
        var amount = $('#summaryAmount').text();
        var freq = $('.urf-toggle-btn.active').data('freq') === 'monthly' ? ' every month' : '';
        window.alert(
            'Thank you! This demo site is not connected to a payment provider yet.\n\n' +
            'Your gift of ' + SYMBOLS[cur] + ' ' + amount + freq +
            ' would now go to the secure checkout.'
        );
    });

    refresh();
})(jQuery);
