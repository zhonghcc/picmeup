/**
 * Home
 */
$(function(){
    var $container = $('.grid');
    $container.masonry({
        itemSelector: '.grid-item',
        gutter: 20,
        isAnimated: true,
    });
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

    $container.infinitescroll({
            navSelector  : '#page-nav',    //指定page-nav
            nextSelector : '#page-nav a',  // page-nav下一页的链接
            itemSelector : '.grid-item-a',     // 要获取追加的页面元素
            loading: {
                finishedMsg: '已经到底啦',
                img: 'http://i.imgur.com/6RMhx.gif'
            }
        },
        // pathParse: ["/billstudy/bill/question/all/null/", ""],
        // trigger Masonry as a callback
        function( newElements ) {
            // hide new items while they are loading
            var $newElems = $( newElements ).css({ opacity: 0 });
            $container.masonry('appended', $newElems, true);
            $newElems.imagesLoaded(function(){
                // show elems now they're ready
                $newElems.animate({ opacity: 1 });
                $container.masonry();
                readedpage++;//当前页滚动完后，定位到下一页
                if(readedpage>totalpage){//如果滚动到超过最后一页，置成不要再滚动。
                    $("#page-nav").remove();
                    $container.infinitescroll({state:{isDone:true}});
                }else{
                    //'#page-nav a置成下一页的值
                    $("#page-nav a").attr("href","/page/"+readedpage);
                }
            });
        }
    );
});



