#Static Folder Name
foldername_d = "dashboard" 


dz_array = {
    "public": {
        "favicon": f"{foldername_d}/images/favicon.png",
        "description": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
        "og_title": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
        "og_description": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
        "og_image": "https://w3cms.dexignzone.com/django/social-image.png",
        "title": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
    },
    "global": {
        "css": [
            f"{foldername_d}/vendor/jquery-nice-select/css/nice-select.css",
            f"{foldername_d}/css/style.css",
        ],
        "js": {
            "top": [
                f"{foldername_d}/vendor/global/global.min.js",
                f"{foldername_d}/vendor/jquery-nice-select/js/jquery.nice-select.min.js",
            ],
            "bottom": [
                f"{foldername_d}/js/utils.js",
                f"{foldername_d}/js/custom.js",
                f"{foldername_d}/js/dlabnav-init.js",
                f"{foldername_d}/js/demo.js",
                f"{foldername_d}/js/styleSwitcher.js",
            ],
        },
    },
    "pagelevel": {
            "frontend": {
                "public": {
                    "description": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
                    "og_title": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
                    "og_description": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
                    "og_image": "https://w3cms.dexignzone.com/django/social-image.png",
                    "title": "W3CMS  : Django CMS With Dashboard & FrontEnd Template",
                },
                "global": {
                    "css": {
                        "theme1": {
                            f"theme1/vendor/aos/aos.css",
                            f"theme1/vendor/lightgallery/css/lightgallery.min.css",
                            f"theme1/vendor/magnific-popup/magnific-popup.min.css",
                            f"theme1/vendor/swiper/swiper-bundle.min.css",
                            f"theme1/css/style.css",
                        },
                        "theme2": {
                            f"theme2/vendor/bootstrap-select/bootstrap-select.min.css",
                            f"theme2/vendor/owl-carousel/owl.carousel.css",
                            f"theme2/vendor/lightgallery/css/lightgallery.min.css",
                            f"theme2/vendor/animate/animate.css",
                            f"theme2/css/style.css",
                            f"theme2/css/skin/skin-1.css",
                            f"theme2/vendor/switcher/switcher.css",
                            f"theme2/vendor/rangeslider/rangeslider.css",
                            f"theme2/vendor/swiper/css/swiper.min.css",
                        },
                        "theme3": [
                            "theme3/css/style.css",
                            "theme3/vendor/animate/animate.css",
                            "theme3/vendor/magnific-popup/magnific-popup.css",
                            "theme3/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                        ],
                        "theme4": [
                            "theme4/css/plugins.css",
                            "theme4/css/style.css",
                            "theme4/css/templete.css",
                            "theme4/css/skin/skin-1.css",
                            "theme4/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                        ],
                        "theme5": [
                            "theme5/css/plugins.css",
                            "theme5/css/style.css",
                            "theme5/css/templete.css",
                            "theme5/css/skin/skin-1.css",
                        ],
                        "theme6": [
                            "theme6/css/plugins.css",
                            "theme6/css/style.css",
                            "theme6/css/templete.css",
                            "theme6/css/skin/blue-white-dark.css",
                        ],
                        "theme7": [
                            "theme7/vendor/animate/animate.css",
                            "theme7/vendor/magnific-popup/magnific-popup.min.css",
                            "theme7/vendor/swiper/swiper-bundle.min.css",
                            "theme7/vendor/rangeslider/rangeslider.css",
                            "theme7/css/style.css",
                            "theme7/css/skin/skin-1.css",
                        ],
                        "theme8": [
                            "theme8/css/plugins.css",
                            "theme8/css/style.css",
                            "theme8/css/templete.css",
                            "theme8/css/food.css",
                            "theme8/css/skin/red-white-light.css",
                        ],
                        "theme9": [
                            "theme9/css/plugins.css",
                            "theme9/css/style.css",
                            "theme9/css/templete.css",
                            "theme9/vendor/swiper/css/swiper.min.css",
                            "theme9/css/skin/black-blue-default.css",
                        ],
                        "theme10": [
                            "theme10/css/plugins.css",
                            "theme10/css/style.css",
                            "theme10/css/templete.css",
                            "theme10/css/skin/black-blue-default.css",
                        ],
                    },
                    "js": {
                        "theme1": {
                            "top": {
                                f"theme1/js/jquery.min.js",
                                f"theme1/vendor/bootstrap/js/bootstrap.bundle.min.js",
                            },
                            "bottom": {
                                f"theme1/vendor/magnific-popup/magnific-popup.js",
                                f"theme1/vendor/lightgallery/js/lightgallery-all.min.js",
                                f"theme1/vendor/counter/waypoints-min.js",
                                f"theme1/vendor/counter/counterup.min.js",
                                f"theme1/vendor/swiper/swiper-bundle.min.js",
                                f"theme1/vendor/aos/aos.js",
                                f"theme1/js/dz.carousel.js",
                                f"theme1/js/dz.ajax.js",
                                f"theme1/vendor/rangeslider/rangeslider.js",
                                f"theme1/vendor/switcher/switcher.js",
                                f"theme1/js/custom.js",
                            },
                        },
                        "theme2": {
                            "top": {
                                f"theme2/js/jquery.min.js",
                                
                            },
                            "bottom": {
                                f"theme2/vendor/bootstrap/js/bootstrap.bundle.min.js",
                                f"theme2/vendor/rangeslider/rangeslider.js",
                                f"theme2/vendor/wow/wow.js",
                                f"theme2/vendor/bootstrap/js/popper.min.js",
                                f"theme2/vendor/owl-carousel/owl.carousel.js",
                                f"theme2/vendor/magnific-popup/magnific-popup.js",
                                f"theme2/vendor/counter/waypoints-min.js",
                                f"theme2/vendor/counter/counterup.min.js",
                                f"theme2/vendor/masonry/masonry-4.2.2.js",
                                f"theme2/vendor/lightgallery/js/lightgallery-all.min.js",
                                f"theme2/vendor/bootstrap-select/bootstrap-select.min.js",
                                f"theme2/vendor/imagesloaded/imagesloaded.js",
                                f"theme2/vendor/masonry/isotope.pkgd.min.js",
                                f"theme2/js/dz.carousel.js",
                                f"theme2/js/dz.ajax.js",
                                f"theme2/js/custom.js",

                            },
                        },
                        "theme3": {
                            "top": [
                                "theme3/js/jquery.min.js",
                               
                            ],
                            "bottom": [
                                "theme3/vendor/bootstrap/js/bootstrap.bundle.min.js",
                                "theme3/vendor/bootstrap-select/dist/js/bootstrap-select.min.js",
                                "theme3/vendor/wow/wow.js",
                                "theme3/js/custom.js",
                            ],
                        },
                        "theme4": {
                            "top": [
                                "theme4/js/jquery.min.js",
                               
                            ],
                            "bottom": [
                                "theme4/vendor/bootstrap/js/popper.min.js",
                                "theme4/vendor/bootstrap/js/bootstrap.bundle.min.js",
                                "theme4/vendor/bootstrap-select/bootstrap-select.min.js",
                                "theme4/vendor/bootstrap-touchspin/jquery.bootstrap-touchspin.js",
                                "theme4/vendor/magnific-popup/magnific-popup.js",
                                "theme4/vendor/counter/waypoints-min.js",
                                "theme4/vendor/counter/counterup.min.js",
                                "theme4/vendor/imagesloaded/imagesloaded.js",
                                "theme4/vendor/masonry/masonry-3.1.4.js",
                                "theme4/vendor/masonry/masonry.filter.js",
                                "theme4/vendor/owl-carousel/owl.carousel.js",
                                "theme4/js/dz.carousel.js",
                                "theme4/js/dz.ajax.js",
                                "theme4/js/custom.js",
                            ],
                        },
                        "theme5": {
                            "top": [
                                "theme5/js/jquery.min.js",
                               
                            ],
                            "bottom": [
                                "theme5/vendor/bootstrap/js/popper.min.js",
                                "theme5/vendor/bootstrap/js/bootstrap.min.js",
                                "theme5/vendor/bootstrap-select/bootstrap-select.min.js",
                                "theme5/vendor/bootstrap-touchspin/jquery.bootstrap-touchspin.js",
                                "theme5/vendor/magnific-popup/magnific-popup.js",
                                "theme5/vendor/counter/waypoints-min.js",
                                "theme5/vendor/counter/counterup.min.js",
                                "theme5/vendor/imagesloaded/imagesloaded.js",
                                "theme5/vendor/masonry/masonry-3.1.4.js",
                                "theme5/vendor/masonry/masonry.filter.js",
                                "theme5/vendor/owl-carousel/owl.carousel.js",
                                "theme5/js/dz.carousel.js",
                                "theme5/js/dz.ajax.js",
                                "theme5/js/custom.js",
                            ],
                        },
                        "theme6": {
                            "top": [
                                "theme6/js/jquery.min.js",
                               
                            ],
                            "bottom": [
                                "theme6/vendor/wow/wow.js",
                                "theme6/vendor/bootstrap/js/popper.min.js",
                                "theme6/vendor/bootstrap/js/bootstrap.min.js",
                                "theme6/vendor/bootstrap-select/bootstrap-select.min.js",
                                "theme6/vendor/bootstrap-touchspin/jquery.bootstrap-touchspin.js",
                                "theme6/vendor/magnific-popup/magnific-popup.js",
                                "theme6/vendor/counter/waypoints-min.js",
                                "theme6/vendor/counter/counterup.min.js",
                                "theme6/vendor/imagesloaded/imagesloaded.js",
                                "theme6/vendor/masonry/masonry-3.1.4.js",
                                "theme6/vendor/masonry/masonry.filter.js",
                                "theme6/vendor/owl-carousel/owl.carousel.js",
                                "theme6/vendor/scroll/scrollbar.min.js",
                                "theme6/vendor/lightgallery/js/lightgallery-all.min.js",
                                "theme6/vendor/rangeslider/rangeslider.js",
                                "theme6/vendor/loading/anime.js",
                                "theme6/vendor/loading/anime-app3.js",
                                "theme6/js/dz.ajax.js",
                                "theme6/js/dz.carousel.js",
                                "theme6/js/custom.js",
                            ],
                        },
                        "theme7": {
                            "top": [
                                "theme7/js/jquery.min.js",
                               
                            ],
                            "bottom": [
                                "theme7/vendor/wow/wow.js",
                                "theme7/vendor/bootstrap/js/bootstrap.bundle.min.js",
                                "theme7/vendor/magnific-popup/magnific-popup.js",
                                "theme7/vendor/counter/waypoints-min.js",
                                "theme7/vendor/counter/counterup.min.js",
                                "theme7/vendor/counter/waypoints-min.js",
                                "theme7/vendor/swiper/swiper-bundle.min.js",
                                "theme7/vendor/rangeslider/rangeslider.js",
                                "theme7/js/dz.ajax.js",
                                "theme7/vendor/anm/anm.js",
                                "theme7/js/dz.carousel.js",
                                "theme7/js/custom.js",
                            ],
                        },
                        "theme8": {
                            "top": [
                                "theme8/js/jquery.min.js",
                               
                            ],
                            "bottom": [
                                "theme8/vendor/wow/wow.js",
                                "theme8/vendor/bootstrap/js/popper.min.js",
                                "theme8/vendor/bootstrap/js/bootstrap.min.js",
                                "theme8/vendor/bootstrap-select/bootstrap-select.min.js",
                                "theme8/vendor/bootstrap-touchspin/jquery.bootstrap-touchspin.js",
                                "theme8/vendor/magnific-popup/magnific-popup.js",
                                "theme8/vendor/counter/waypoints-min.js",
                                "theme8/vendor/counter/counterup.min.js",
                                "theme8/vendor/imagesloaded/imagesloaded.js",
                                "theme8/vendor/masonry/masonry-3.1.4.js",
                                "theme8/vendor/masonry/masonry.filter.js",
                                "theme8/vendor/owl-carousel/owl.carousel.js",
                                "theme8/vendor/scroll/scrollbar.min.js",
                                "theme8/vendor/lightgallery/js/lightgallery-all.min.js",
                                "theme8/vendor/rangeslider/rangeslider.js",
                                "theme8/vendor/loading/anime.js",
                                "theme8/vendor/loading/anime-app3.js",
                                "theme8/js/dz.carousel.js",
                                "theme8/js/dz.ajax.js",
                                "theme8/js/custom.js",
                            ],
                        },
                        "theme9": {
                            "top": [
                                "theme9/js/jquery.min.js",
                               
                            ],
                            "bottom": [
                                "theme9/vendor/wow/wow.js",
                                "theme9/vendor/bootstrap/js/popper.min.js",
                                "theme9/vendor/bootstrap/js/bootstrap.min.js",
                                "theme9/vendor/bootstrap-select/bootstrap-select.min.js",
                                "theme9/vendor/bootstrap-touchspin/jquery.bootstrap-touchspin.js",
                                "theme9/vendor/magnific-popup/magnific-popup.js",
                                "theme9/vendor/counter/waypoints-min.js",
                                "theme9/vendor/counter/counterup.min.js",
                                "theme9/vendor/imagesloaded/imagesloaded.js",
                                "theme9/vendor/masonry/masonry-3.1.4.js",
                                "theme9/vendor/masonry/masonry.filter.js",
                                "theme9/vendor/owl-carousel/owl.carousel.js",
                                "theme9/vendor/scroll/scrollbar.min.js",
                                "theme9/vendor/lightgallery/js/lightgallery-all.min.js",
                                "theme9/vendor/rangeslider/rangeslider.js",
                                "theme9/vendor/swiper/js/swiper.min.js",
                                "theme9/vendor/loading/anime.js",
                                "theme9/vendor/loading/anime-app3.js",
                                "theme9/js/dz.carousel.js",
                                "theme9/js/dz.ajax.js",
                                "theme9/js/custom.js",
                            ],
                        },
                        "theme10": {
                            "top": [
                                "theme10/js/jquery.min.js",
                               
                            ],
                            "bottom": [
                                "theme10/vendor/wow/wow.js",
                                "theme10/vendor/bootstrap/js/popper.min.js",
                                "theme10/vendor/bootstrap/js/bootstrap.min.js",
                                "theme10/vendor/bootstrap-select/bootstrap-select.min.js",
                                "theme10/vendor/bootstrap-touchspin/jquery.bootstrap-touchspin.js",
                                "theme10/vendor/magnific-popup/magnific-popup.js",
                                "theme10/vendor/counter/waypoints-min.js",
                                "theme10/vendor/counter/counterup.min.js",
                                "theme10/vendor/imagesloaded/imagesloaded.js",
                                "theme10/vendor/masonry/masonry-3.1.4.js",
                                "theme10/vendor/masonry/masonry.filter.js",
                                "theme10/vendor/owl-carousel/owl.carousel.js",
                                "theme10/vendor/scroll/scrollbar.min.js",
                                "theme10/vendor/lightgallery/js/lightgallery-all.min.js",
                                "theme10/vendor/rangeslider/rangeslider.js",
                                "theme10/vendor/loading/anime.js",
                                "theme10/vendor/loading/anime-app3.js",
                                "theme10/js/dz.carousel.js",
                                "theme10/js/dz.ajax.js",
                                "theme10/js/custom.js",
                            ],
                        },
                    },
                },
            },
    
            "dashboard": {
                # AppName
                "dashboard_views": {
                    "css": {
                        "index": [
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css"
                        ],
                        "index2": [
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css"
                        ],
                        "schedule": [
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css",
                            f"{foldername_d}/vendor/fullcalendar/css/main.min.css",
                        ],
                        "instructors": [],
                        "message": [],
                        "activity": [],
                        "profile": [],
                        "permissions": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        ],
                        "users": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        ],
                        "add_user": [
                            f"{foldername_d}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                            f"{foldername_d}/vendor/select2/css/select2.min.css",
                        ],
                        "edit_user": [
                            f"{foldername_d}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                            f"{foldername_d}/vendor/select2/css/select2.min.css",
                        ],
                        "groups_list": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        ],
                        "assign_permissions_to_user": [
                            f"{foldername_d}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                        ],
                        "group_add": [
                            f"{foldername_d}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                        ],
                        "group_edit": [
                            f"{foldername_d}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/prettify.min.css",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/src/bootstrap-duallistbox.css",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/dist/bootstrap-duallistbox.css",
                        ],
                        "cms_page_list": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        ],
                        "cms_page_create": [],
                        "cms_page_edit": [],
                        "cms_blog_list": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        ],
                        "cms_comment_list": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        ],
                        "cms_blog_create": [
                            f"{foldername_d}/vendor/select2/css/select2.min.css",
                            "cms/blog/css/bootstrap-tagsinput.css",
                        ],
                        "cms_blog_edit": [
                            f"{foldername_d}/vendor/select2/css/select2.min.css",
                            "cms/blog/css/bootstrap-tagsinput.css",
                            "cms/blog/css/content-styles.css",
                        ],
                        "blogCategory": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css"
                        ],
                        "blogCategoryEdit": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css"
                        ],
                        "blogTag": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css"
                        ],
                        "blogTagEdit": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css"
                        ],
                        "cms_menu_setup": [
                            f"{foldername_d}/vendor/nestable2/css/jquery.nestable.min.css",
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                            "cms/menu/css/menu.css",
                        ],
                        "all_config": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        },
                        "subscribe": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        },
                        "edit_subscribe": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        },
                        "contact_us": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        },
                        "edit_contact_us": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        },
                        "courses": [f"{foldername_d}/vendor/swiper/css/swiper-bundle.min.css"],
                        "course_details_1": [
                            f"{foldername_d}/vendor/magnific-popup/magnific-popup.min.css",
                        ],
                        "course_details_2": [
                            f"{foldername_d}/vendor/magnific-popup/magnific-popup.min.css",
                        ],
                        "instructor_dashboard": [
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css",
                        ],
                        "instructor_courses": [
                            f"{foldername_d}/vendor/owl-carousel/owl.carousel.css",
                        ],
                        "instructor_schedule": [
                            f"{foldername_d}/vendor/fullcalendar/css/main.min.css",
                        ],
                        "instructor_students": [
                            f"{foldername_d}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "instructor_resources": [],
                        "instructor_transactions": [
                            f"{foldername_d}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "instructor_liveclass": [],
                        "app_profile": [
                            f"{foldername_d}/vendor/lightgallery/css/lightgallery.min.css",
                            f"{foldername_d}/vendor/magnific-popup/magnific-popup.css",
                        ],
                        "post_details": [
                            f"{foldername_d}/vendor/lightgallery/css/lightgallery.min.css",
                            f"{foldername_d}/vendor/magnific-popup/magnific-popup.css",
                        ],
                        "email_compose": [
                            f"{foldername_d}/vendor/dropzone/dist/dropzone.css",
                        ],
                        "email_inbox": [],
                        "email_read": [],
                        "app_calender": [
                            f"{foldername_d}/vendor/fullcalendar/css/main.min.css",
                        ],
                        "ecom_product_grid": [],
                        "ecom_product_list": [
                            f"{foldername_d}/vendor/star-rating/star-rating-svg.css",
                        ],
                        "ecom_product_detail": [
                            f"{foldername_d}/vendor/star-rating/star-rating-svg.css",
                        ],
                        "ecom_product_order": [],
                        "ecom_checkout": [],
                        "ecom_invoice": [
                            f"{foldername_d}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                        ],
                        "ecom_customers": [],
                        "chart_float": [],
                        "chart_morris": [],
                        "chart_chartjs": [],
                        "chart_chartist": [
                            f"{foldername_d}/vendor/chartist/css/chartist.min.css"
                        ],
                        "chart_sparkline": [],
                        "chart_peity": [],
                        "uc_select2": [
                            f"{foldername_d}/vendor/select2/css/select2.min.css",
                        ],
                        "uc_nestable": [
                            f"{foldername_d}/vendor/nestable2/css/jquery.nestable.min.css"
                        ],
                        "uc_noui_slider": [
                            f"{foldername_d}/vendor/nouislider/nouislider.min.css"
                        ],
                        "uc_sweetalert": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.css"
                        ],
                        "uc_toastr": [f"{foldername_d}/vendor/toastr/css/toastr.min.css"],
                        "map_jqvmap": [f"{foldername_d}/vendor/jqvmap/css/jqvmap.min.css"],
                        "uc_lightgallery": [
                            f"{foldername_d}/vendor/lightgallery/css/lightgallery.min.css"
                        ],
                        "widget_basic": [
                            f"{foldername_d}/vendor/chartist/css/chartist.min.css",
                            f"{foldername_d}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                        ],
                        "form_element": [],
                        "form_wizard": [
                            f"{foldername_d}/vendor/jquery-smartwizard/dist/css/smart_wizard.min.css"
                        ],
                        "form_ckeditor": [],
                        "form_pickers": [
                            f"{foldername_d}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                            f"{foldername_d}/vendor/clockpicker/css/bootstrap-clockpicker.min.css",
                            f"{foldername_d}/vendor/jquery-asColorPicker/css/asColorPicker.min.css",
                            f"{foldername_d}/vendor/bootstrap-material-datetimepicker/css/bootstrap-material-datetimepicker.css",
                            f"{foldername_d}/vendor/pickadate/themes/default.css",
                            f"{foldername_d}/vendor/pickadate/themes/default.date.css",
                        ],
                        "form_validation": [],
                        "table_bootstrap_basic": [],
                        "table_datatable_basic": [
                            f"{foldername_d}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "page_login": [],
                        "page_register": [],
                        "page_forgot_password": [],
                        "page_lock_screen": [],
                        "page_error_400": [],
                        "page_error_403": [],
                        "page_error_404": [],
                        "page_error_500": [],
                        "page_error_503": [],
                        "empty_page": [],
                    },
                    "js": {
                        "index": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/js/moment.js",
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/js/bootstrap-datetimepicker.min.js",
                            f"{foldername_d}/js/dashboard/dashboard-1.js",
                        ],
                        "index2": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/js/moment.js",
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/js/bootstrap-datetimepicker.min.js",
                            f"{foldername_d}/js/dashboard/dashboard-1.js",
                        ],
                        "schedule": [
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/js/moment.js",
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/js/bootstrap-datetimepicker.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/moment/moment.min.js",
                            f"{foldername_d}/vendor/fullcalendar/js/main.min.js",
                            f"{foldername_d}/js/plugins-init/fullcalendar-init.js",
                            f"{foldername_d}/js/dashboard/schedule.js",
                        ],
                        "instructors": [],
                        "message": [],
                        "activity": [],
                        "profile": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/peity/jquery.peity.min.js",
                            f"{foldername_d}/js/dashboard/my-profile.js",
                        ],
                        "permissions": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                        ],
                        "users": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            f"{foldername_d}/js/modules/users/user_list.js",
                        ],
                        "add_user": [
                            f"{foldername_d}/vendor/moment/moment.min.js",
                            f"{foldername_d}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                            f"{foldername_d}/vendor/select2/js/select2.full.min.js",
                            f"{foldername_d}/js/plugins-init/select2-init.js",
                        ],
                        "edit_user": [
                            f"{foldername_d}/vendor/moment/moment.min.js",
                            f"{foldername_d}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                            f"{foldername_d}/vendor/select2/js/select2.full.min.js",
                            f"{foldername_d}/js/plugins-init/select2-init.js",
                        ],
                        "groups_list": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                        ],
                        "assign_permissions_to_user": [
                            f"{foldername_d}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                        ],
                        "group_add": [
                            f"{foldername_d}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                        ],
                        "group_edit": [
                            f"{foldername_d}/vendor/bootstrap-duallistbox/ajax/libs/popper.js/1.12.9/umd/popper.min.js",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/ajax/libs/prettify/r298/run_prettify.js",
                            f"{foldername_d}/vendor/bootstrap-duallistbox/dist/jquery.bootstrap-duallistbox.js",
                        ],
                        "cms_page_list": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/page/js/page_list.js",
                        ],
                        "cms_page_create": [
                            "ckeditor/ckeditor/config.js",
                            "cms/page/js/jquery.slug.js",
                            "cms/page/js/pages.js",
                        ],
                        "cms_page_edit": [
                            "ckeditor/ckeditor/config.js",
                            "cms/page/js/jquery.slug.js",
                            "cms/page/js/pages.js",
                        ],
                        "cms_blog_list": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/blog/js/blog_list.js",
                        ],
                        "cms_comment_list": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/comment/js/comment_list.js",
                        ],
                        "cms_blog_create": [
                            f"{foldername_d}/vendor/select2/js/select2.full.min.js",
                            f"{foldername_d}/js/plugins-init/select2-init.js",
                            "ckeditor/ckeditor/config.js",
                            "cms/blog/js/bootstrap-tagsinput.js",
                            "cms/blog/js/jquery.slug.js",
                            "cms/blog/js/cookie.js",
                            "cms/blog/js/blogs.js",
                        ],
                        "cms_blog_edit": [
                            f"{foldername_d}/vendor/select2/js/select2.full.min.js",
                            f"{foldername_d}/js/plugins-init/select2-init.js",
                            "ckeditor/ckeditor/config.js",
                            "cms/blog/js/bootstrap-tagsinput.js",
                            "cms/blog/js/jquery.slug.js",
                            "cms/blog/js/cookie.js",
                            "cms/blog/js/blogs.js",
                        ],
                        "blogCategory": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/blog/js/category.js",
                        ],
                        "blogCategoryEdit": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/blog/js/category.js",
                        ],
                        "blogTag": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/blog/js/tag.js",
                        ],
                        "blogTagEdit": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/blog/js/tag.js",
                        ],
                        "cms_menu_setup": [
                            f"{foldername_d}/vendor/nestable2/js/jquery.nestable.min.js",
                            f"{foldername_d}/js/plugins-init/nestable-init.js",
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            # f"{foldername_d}/js/plugins-init/sweetalert.init.js",
                            f"cms/menu/js/menu.js"
                            # f"cms/menu/js/jquery.nestable.min.js"
                        ],
                        "all_config": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                        },
                        "subscribe": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/subscribe/subscribe.js",
                        },
                        "edit_subscribe": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/subscribe/subscribe.js",
                        },
                        "contact_us": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/contactus/contact-us.js",
                        },
                        "edit_contact_us": {
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            "cms/contactus/contact-us.js",
                        },
                        "courses": [
                            f"{foldername_d}/vendor/swiper/js/swiper-bundle.min.js",
                            f"{foldername_d}/js/dlab.carousel.js",
                        ],
                        "course_details_1": [
                            f"{foldername_d}/vendor/magnific-popup/magnific-popup.js"
                        ],
                        "course_details_2": [
                            f"{foldername_d}/vendor/magnific-popup/magnific-popup.js"
                        ],
                        "instructor_dashboard": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/js/moment.js",
                            f"{foldername_d}/vendor/bootstrap-datetimepicker/js/bootstrap-datetimepicker.min.js",
                            f"{foldername_d}/vendor/day-fullcalendar/main.min.js",
                            f"{foldername_d}/vendor/peity/jquery.peity.min.js",
                            f"{foldername_d}/js/dashboard/instructor-dashboard.js",
                        ],
                        "instructor_courses": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/peity/jquery.peity.min.js",
                            f"{foldername_d}/vendor/owl-carousel/owl.carousel.js",
                            f"{foldername_d}/js/dashboard/instructor-courses.js",
                            f"{foldername_d}/js/dlab.carousel.js",
                        ],
                        "instructor_schedule": [
                            f"{foldername_d}/vendor/moment/moment.min.js",
                            f"{foldername_d}/vendor/fullcalendar/js/main.min.js",
                            f"{foldername_d}/js/plugins-init/fullcalendar-init.js",
                        ],
                        "instructor_students": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{foldername_d}/js/plugins-init/datatables.init.js",
                            f"{foldername_d}/vendor/owl-carousel/owl.carousel.js",
                            f"{foldername_d}/js/dashboard/instructor-student.js",
                        ],
                        "instructor_resources": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                        ],
                        "instructor_transactions": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{foldername_d}/js/plugins-init/datatables.init.js",
                            f"{foldername_d}/js/dashboard/instructor-transactions.js",
                        ],
                        "instructor_liveclass": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                        ],
                        "app_profile": [
                            f"{foldername_d}/vendor/lightgallery/js/lightgallery-all.min.js",
                            f"{foldername_d}/vendor/magnific-popup/magnific-popup.js",
                        ],
                        "post_details": [
                            f"{foldername_d}/vendor/lightgallery/js/lightgallery-all.min.js",
                            f"{foldername_d}/vendor/magnific-popup/magnific-popup.js",
                        ],
                        "email_compose": [
                            f"{foldername_d}/vendor/dropzone/dist/dropzone.js",
                        ],
                        "email_inbox": [],
                        "email_read": [],
                        "app_calender": [
                            f"{foldername_d}/vendor/moment/moment.min.js",
                            f"{foldername_d}/vendor/fullcalendar/js/main.min.js",
                            f"{foldername_d}/js/plugins-init/fullcalendar-init.js",
                        ],
                        "ecom_product_grid": [],
                        "ecom_product_list": [
                            f"{foldername_d}/vendor/star-rating/jquery.star-rating-svg.js",
                        ],
                        "ecom_product_detail": [
                            f"{foldername_d}/vendor/star-rating/jquery.star-rating-svg.js",
                        ],
                        "ecom_product_order": [],
                        "ecom_checkout": [],
                        "ecom_invoice": [],
                        "ecom_customers": [],
                        "chart_flot": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/flot/jquery.flot.js",
                            f"{foldername_d}/vendor/flot/jquery.flot.pie.js",
                            f"{foldername_d}/vendor/flot/jquery.flot.resize.js",
                            f"{foldername_d}/vendor/flot-spline/jquery.flot.spline.min.js",
                            f"{foldername_d}/js/plugins-init/flot-init.js",
                        ],
                        "chart_morris": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/raphael/raphael.min.js",
                            f"{foldername_d}/vendor/morris/morris.min.js",
                            f"{foldername_d}/js/plugins-init/morris-init.js",
                        ],
                        "chart_chartjs": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/js/plugins-init/chartjs-init.js",
                        ],
                        "chart_chartist": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/chartist/js/chartist.min.js",
                            f"{foldername_d}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                            f"{foldername_d}/js/plugins-init/chartist-init.js",
                        ],
                        "chart_sparkline": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                            f"{foldername_d}/js/plugins-init/sparkline-init.js",
                            f"{foldername_d}/vendor/svganimation/vivus.min.js",
                            f"{foldername_d}/vendor/svganimation/svg.animation.js",
                        ],
                        "chart_peity": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/peity/jquery.peity.min.js",
                            f"{foldername_d}/js/plugins-init/piety-init.js",
                        ],
                        "uc_select2": [
                            f"{foldername_d}/vendor/select2/js/select2.full.min.js",
                            f"{foldername_d}/js/plugins-init/select2-init.js",
                        ],
                        "uc_nestable": [
                            f"{foldername_d}/vendor/nestable2/js/jquery.nestable.min.js",
                            f"{foldername_d}/js/plugins-init/nestable-init.js",
                        ],
                        "uc_noui_slider": [
                            f"{foldername_d}/vendor/nouislider/nouislider.min.js",
                            f"{foldername_d}/vendor/wnumb/wNumb.js",
                            f"{foldername_d}/js/plugins-init/nouislider-init.js",
                        ],
                        "uc_sweetalert": [
                            f"{foldername_d}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            f"{foldername_d}/js/plugins-init/sweetalert.init.js",
                        ],
                        "uc_toastr": [
                            f"{foldername_d}/vendor/toastr/js/toastr.min.js",
                            f"{foldername_d}/js/plugins-init/toastr-init.js",
                        ],
                        "map_jqvmap": [
                            f"{foldername_d}/vendor/jqvmap/js/jquery.vmap.min.js",
                            f"{foldername_d}/vendor/jqvmap/js/jquery.vmap.world.js",
                            f"{foldername_d}/vendor/jqvmap/js/jquery.vmap.usa.js",
                            f"{foldername_d}/js/plugins-init/jqvmap-init.js",
                        ],
                        "uc_lightgallery": [
                            f"{foldername_d}/vendor/lightgallery/js/lightgallery-all.min.js"
                        ],
                        "widget_basic": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/chartist/js/chartist.min.js",
                            f"{foldername_d}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                            f"{foldername_d}/vendor/flot/jquery.flot.js",
                            f"{foldername_d}/vendor/flot/jquery.flot.pie.js",
                            f"{foldername_d}/vendor/flot/jquery.flot.resize.js",
                            f"{foldername_d}/vendor/flot-spline/jquery.flot.spline.min.js",
                            f"{foldername_d}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                            f"{foldername_d}/js/plugins-init/sparkline-init.js",
                            f"{foldername_d}/vendor/peity/jquery.peity.min.js",
                            f"{foldername_d}/js/plugins-init/piety-init.js",
                            f"{foldername_d}/js/plugins-init/widgets-script-init.js",
                        ],
                        "form_element": [],
                        "form_wizard": [
                            f"{foldername_d}/vendor/jquery-steps/build/jquery.steps.min.js",
                            f"{foldername_d}/vendor/jquery-validation/jquery.validate.min.js",
                            f"{foldername_d}/js/plugins-init/jquery.validate-init.js",
                            f"{foldername_d}/vendor/jquery-smartwizard/dist/js/jquery.smartWizard.js",
                        ],
                        "form_ckeditor": [f"{foldername_d}/vendor/ckeditor/ckeditor.js"],
                        "form_pickers": [
                            f"{foldername_d}/vendor/bootstrap-select/dist/js/bootstrap-select.min.js",
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/moment/moment.min.js",
                            f"{foldername_d}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                            f"{foldername_d}/vendor/clockpicker/js/bootstrap-clockpicker.min.js",
                            f"{foldername_d}/vendor/jquery-asColor/jquery-asColor.min.js",
                            f"{foldername_d}/vendor/jquery-asGradient/jquery-asGradient.min.js",
                            f"{foldername_d}/vendor/jquery-asColorPicker/js/jquery-asColorPicker.min.js",
                            f"{foldername_d}/vendor/bootstrap-material-datetimepicker/js/bootstrap-material-datetimepicker.js",
                            f"{foldername_d}/vendor/pickadate/picker.js",
                            f"{foldername_d}/vendor/pickadate/picker.time.js",
                            f"{foldername_d}/vendor/pickadate/picker.date.js",
                            f"{foldername_d}/js/plugins-init/bs-daterange-picker-init.js",
                            f"{foldername_d}/js/plugins-init/clock-picker-init.js",
                            f"{foldername_d}/js/plugins-init/jquery-asColorPicker.init.js",
                            f"{foldername_d}/js/plugins-init/material-date-picker-init.js",
                            f"{foldername_d}/js/plugins-init/pickadate-init.js",
                        ],
                        "form_validation": [],
                        "table_bootstrap_basic": [],
                        "table_datatable_basic": [
                            f"{foldername_d}/vendor/chart.js/Chart.bundle.min.js",
                            f"{foldername_d}/vendor/apexchart/apexchart.js",
                            f"{foldername_d}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{foldername_d}/js/plugins-init/datatables.init.js",
                        ],
                        "page_login": [],
                        "page_register": [],
                        "page_forgot_password": [],
                        "page_lock_screen": [],
                        "page_error_400": [],
                        "page_error_403": [],
                        "page_error_404": [],
                        "page_error_500": [],
                        "page_error_503": [],
                        "empty_page": [],
                    },
                }
            },
    },
}
