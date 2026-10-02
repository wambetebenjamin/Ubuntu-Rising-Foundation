/* Ubuntu Rising Foundation - small UI behaviours */
(function ($) {
    'use strict';
    $(function () {
        // impact counters
        if ($.fn.counterUp) { $('.counter').counterUp({ delay: 12, time: 1400 }); }

        // donation form: amount + frequency selection
        var $amount = $('#amount'), $freq = $('#frequency'), $sum = $('#give-summary');

        function fmt(n) { return 'KES ' + Number(n || 0).toLocaleString('en-KE'); }
        function refresh() {
            if (!$sum.length) { return; }
            var label = $freq.val() === 'monthly' ? ' a month' : ' once';
            $sum.text(fmt($amount.val()) + label);
        }

        $('.amount-option').on('click', function () {
            $('.amount-option').removeClass('active');
            $(this).addClass('active');
            $amount.val($(this).data('amount'));
            refresh();
        });
        $amount.on('input', function () { $('.amount-option').removeClass('active'); refresh(); });
        $('.give-tab').on('click', function () {
            $('.give-tab').removeClass('active');
            $(this).addClass('active');
            $freq.val($(this).data('freq'));
            refresh();
        });
        refresh();
    });
})(jQuery);
