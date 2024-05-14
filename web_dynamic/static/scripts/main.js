$(document).ready(() => {

    $(".pull_right .search_icon").click(() => {
        if ($(".search_area").css("display") === "none") {
            $(".search_area").css("display", "block");
            $(".pull_right .search_icon").css("display", "none");
            $(".authentication").removeClass("active");
            $(".create_options").removeClass("active");
        } else {
            $(".search_area").css("display", "none");
        }
    });

    $(".search_area .remove_search_area").click(() => {
        $(".search_area").css("display", "none");
        $(".pull_right .search_icon").css("display", "inline-block");
    });

    $(".menu_icon").click(() => {
        $(".navbar").toggleClass("active");
        $("main").toggleClass("active");
    });

    $(".flash_message i").click(() => {
        $(".flash_message").css({"display": "none"})
    });

    $(".menu_icon").click(() => {
        $(".menu_icon i").toggleClass("bi-x");
    });

    const list = $(".navbar li").toArray();
    const activeLink = (event) => {
        list.forEach(element => {
            $(element).removeClass("hovered");
        });
        $(event.currentTarget).addClass("hovered");
    };

    list.forEach(item => $(item).click(activeLink));

    $(".pull_right .user_icon").click(function() {
        $(".authentication").toggleClass("active");
        $(".create_options").removeClass("active");
        if (window.innerWidth <= 800) {
            $(".search_area").css("display", "none");
            $(".pull_right .search_icon").css("display", "inline-block");
        }
    });

    $(".pull_right .create_icon").click(function() {
        $(".authentication").removeClass("active");
        $(".create_options").toggleClass("active");
        if (window.innerWidth <= 800) {
            $(".search_area").css("display", "none");
            $(".pull_right .search_icon").css("display", "inline-block");
        }
    });
});
