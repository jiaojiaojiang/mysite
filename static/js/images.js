
        let $box = $("#box");
        let $imgList = $("#imgList");
        let $leftBtn = $("#leftBtn");
        let $rightBtn = $("#rightBtn");
        let $cirList = $("#cirList li");


        let idx = 0;
        let width = $box.width();
        let time = 2000;
        let imgCount = $imgList.children().length - 1;

        // 避免动画执行过程中 再次触发动画 设置lock
        let lock = true;


        /* 点击右按钮 */
        $rightBtn.click(function () {
            // 上锁
            if (!lock) {
                return;
            }
            lock = false;

            idx++;
            // 图片切换
            $imgList.animate({ left: -width * idx }, time, function () {
                if (idx >= imgCount) {
                    $imgList.css("left", 0);
                    idx = 0;
                }

               // console.log(idx, this);
                lock = true; // 开锁
            })
            // 底部圆点改变
            cirChange.call($cirList[idx >= imgCount ? 0 : idx]);
        })


        /* 点击左按钮 */
        $leftBtn.click(function () {
            // 上锁
            if (!lock) {
                return;
            }
            lock = false;

            idx--;
            if (idx < 0) {
                $imgList.css("left", -width * imgCount);
                idx = imgCount - 1;
            }
            // 图片切换
            $imgList.animate({ left: -width * idx }, time, function () {
                //console.log(idx, this);
                lock = true; // 开锁
            })
            // 底部圆点改变
            cirChange.call($cirList[idx]);
        })

        /* 点击小圆点 */
        $cirList.click(function () {
            // 上锁
            if (!lock) {
                return;
            }
            lock = false;

            // .call()传参改变函数的this
            cirChange.call(this);
            // 改变idx
            idx = $(this).index();
            // 图片切换
            $imgList.animate({ left: -width * idx }, time, function () {
                console.log(idx, this);
                lock = true; // 开锁
            })
        })


        /* 底部圆点改变 函数 */
        function cirChange() {
            $(this).addClass("change").siblings().removeClass("change");
        }


        /* 自动轮播 */
        let autotimer = setInterval(function () {
            $rightBtn.click();
        }, 2000)


        /* 鼠标滑入 自动轮播停止 */
        $box.mouseover(function () {
            clearInterval(autotimer);
        })
        $box.mouseleave(function () {
            autotimer = setInterval(function () {
                $rightBtn.click();
            }, time * 2)
        })