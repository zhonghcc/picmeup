/**
 * 用户登陆，注册，资料修改等功能
 */

function Check()  // 验证表单数据有效性
{
    if (document.send.username.value == "") {
        window.alert('请输入用户名!');
        return false;
    }
    if (document.send.username.value.length < 3) {
        window.alert('用户名长度必须大于3!');
        return false;
    }
    if (document.send.password.value == "") {
        alert('请输入密码!');
        return false;
    }
    if (document.send.password.value.length < 6) {
        alert('密码长度必须大于6!');
        return false;
    }
    if (document.send.password.value != document.send.chkpwd.value) {
        alert('确认密码与密码不一致!');
        return false;
    }
    if (document.send.email.value == "") {
        alert('请输入Email!');
        return false;
    }
    if (document.send.email.value.indexOf("@") == -1) {
        alert('请输入有效的email地址!');
        return false;
    }
    return true;
}
$(function () {
    var $container = $('.grid');
    $container.imagesLoaded(function () {
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
            navSelector: '#page-nav',    //指定page-nav
            nextSelector: '#page-nav a',  // page-nav下一页的链接
            itemSelector: '.grid-item-a',     // 要获取追加的页面元素
            loading: {
                finishedMsg: '已经到底啦',
                img: 'http://i.imgur.com/6RMhx.gif'
            }
        },
        // pathParse: ["/billstudy/bill/question/all/null/", ""],
        // trigger Masonry as a callback
        function (newElements) {
            // hide new items while they are loading
            var $newElems = $(newElements).css({opacity: 0});
            // ensure that images load before adding to masonry layout
            $newElems.imagesLoaded(function () {
                // show elems now they're ready
                $newElems.animate({opacity: 1});
                $container.masonry('appended', $newElems, true);
                readedpage++;//当前页滚动完后，定位到下一页
                if (readedpage > totalpage) {//如果滚动到超过最后一页，置成不要再滚动。
                    $("#page-nav").remove();
                    $container.infinitescroll({state: {isDone: true}});
                } else {
                    //'#page-nav a置成下一页的值
                    $("#page-nav a").attr("href", "/billstudy/bill/question/all/null/" + readedpage);
                }
            });
        }
    );
});