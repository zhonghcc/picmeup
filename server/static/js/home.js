/**
 * Home
 */
$(function(){
    var $container = $('.grid');
    $container.imagesLoaded(function() {
        $container.masonry({
            itemSelector: '.grid-item',
            gutter: 20,
            isAnimated: true,
        });
    });
    //$('.grid').masonry({
    //    // options
    //    itemSelector: '.grid-item',
    //    columnWidth: 200
    //});
});



