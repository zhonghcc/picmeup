function fmt() {
    var args = arguments;
    return args[0].replace(/%\{(.*?)}/g, function (match, prop) {
        return function (obj, props) {
            var prop = /\d+/.test(props[0]) ? parseInt(props[0]) : props[0];
            if (props.length > 1) {
                return arguments.callee(obj[prop], props.slice(1));
            } else {
                return obj[prop] || '';
            }
        }(typeof args[1] === 'object' ? args[1] : args, prop.split(/\.|\[|\]\[|\]\./));
    });
}

$(function () {
    $('.flash').fadeIn(1000);
    window.setTimeout(
        function () {
            $(".flash").fadeOut(1000);
        }
        , 6000);
});

function gridView(){
    $(".grid-item").hover(function(){
        $(this).find(".grid-relative").fadeIn(800);
        //alert($(item).find(".grid-relative").html());
    },function(){
        $(this).find(".grid-relative").fadeOut(800);

    });
    $(".grid-img[state=false]").each(function(index,obj){
        $(obj).attr("src",$(obj).attr("v"));
        $(obj).attr("state",true);
    });
}

function infinateFlow(){
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
                    msgText: "加载中...",
                    finishedMsg: '已经到底啦',
                    //img: 'http://img.lanrentuku.com/img/allimg/1212/5-121204193Q9.gif',
                    selector: '.grid-loading'
                }
            },
            // pathParse: ["/billstudy/bill/question/all/null/", ""],
            // trigger Masonry as a callback
            function( newElements ) {
                // hide new items while they are loading
                var $newElems = $( newElements ).css({ display:0 });
                $container.masonry('appended', $newElems, true);
                $newElems.imagesLoaded(function(){
                    // show elems now they're ready
                    $newElems.css({display:1});
                    $newElems.animate({ opacity: 1 });
                    $container.masonry();
                    gridView();
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

        gridView();
    });
}