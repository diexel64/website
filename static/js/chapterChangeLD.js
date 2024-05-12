$(document).ready(function() {
    $('#chapterTabs a').on('click', function(event) {
        event.preventDefault();

        var targetPane = $(this).attr('href');
        var embedSrc = $(targetPane).find('embed').attr('src');

        $('.tab-pane').removeClass('show active');
        $('#chapterTabs a').removeClass('active');

        $(targetPane).addClass('show active');
        $(this).addClass('active');

        $(targetPane).find('embed').attr('src', embedSrc);
    });
});