$(document).ready(() => {

    $(".pull_right .search_icon").click(() => {
        if ($(".search_area").css("display") === "none") {
            $(".search_area").css("display", "block");
            $(".pull_right .search_icon").css("display", "none");
            $(".authentication").removeClass("active");
            $(".create_options").removeClass("active");
            $(".navbar").removeClass("active");
            if ($(".menu_icon i").hasClass("bi-x")) {
                $(".menu_icon i").toggleClass("bi-x");
            }

        } else {
            $(".search_area").css("display", "none");
        }
    });

    $(".search_area .remove_search_area").click(() => {
        $(".search_area").css("display", "none");
        $(".pull_right .search_icon").css("display", "inline-block");
    });

    $(".flash_message i").click(() => {
        $(".flash_message").css({"display": "none"})
    });

    

    const list = $("nav li").toArray();
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
        $(".navbar").removeClass("active");
        if ($(".menu_icon i").hasClass("bi-x")) {
            $(".menu_icon i").toggleClass("bi-x");
        }
        if (window.innerWidth <= 800) {
            $(".search_area").css("display", "none");
            $(".pull_right .search_icon").css("display", "inline-block");
        }
    });

    $(".pull_right .create_icon").click(function() {
        $(".authentication").removeClass("active");
        $(".create_options").toggleClass("active");
        $(".navbar").removeClass("active");
        if ($(".menu_icon i").hasClass("bi-x")) {
            $(".menu_icon i").toggleClass("bi-x");
        }
        if (window.innerWidth <= 800) {
            $(".search_area").css("display", "none");
            $(".pull_right .search_icon").css("display", "inline-block");
        }
    });

    let lastScrollTop = 0;
    let header = document.querySelector("header");
    let currentWidth = window.innerWidth;

    // Function to initialize or reinitialize your JavaScript logic
    const initialize = () => {
        // Check if the window width is less than or equal to 695 pixels
        if (currentWidth <= 600) {
            // Remove existing scroll event listeners
            window.removeEventListener('scroll', handleScroll);

            // Add new scroll event listener
            window.addEventListener('scroll', handleScroll);
        } else {
            // Remove scroll event listener if the window width is greater than 695 pixels
            window.removeEventListener('scroll', handleScroll);
            header.classList.remove('hidden');
        }
    };

    // Function to handle scroll events
    const handleScroll = () => {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        if (header) { // Ensure header is defined
            if (currentScroll > lastScrollTop) {
                // Scroll down
                header.classList.add('hidden');
            } else {
                // Scroll up
                header.classList.remove('hidden');
            }
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
    };

    // Function to reload JavaScript on width change
    window.addEventListener('resize', () => {
        const newWidth = window.innerWidth;

        if (newWidth !== currentWidth) {
            currentWidth = newWidth;
            initialize();
        }
    });

    // Initial load
    initialize();

});
