"use strict"

var themeOptionArr = {
			typography: '',
			version: '',
			layout: '',
			primary: '',
			secondary: '',
			headerBg: '',
			navheaderBg: '',
			sidebarBg: '',
			sidebarStyle: '',
			sidebarPosition: '',
			headerPosition: '',
			containerLayout: '',
			demoActive: '',
			//direction: '',
		};
		
		


 	

(function($) {
	
	"use strict"
	
	//var direction =  getUrlParams('dir');
	var theme =  getUrlParams('theme');
	
	/* Dz Theme Demo Settings  */
	
	var dlabThemeSet0 = { /* Default Theme */
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_1",
		secondary: "color_1",
		headerBg: "color_1",
		navheaderBg: "color_1",
		sidebarBg: "color_1",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		demoActive:0,
	};
	
	var dlabThemeSet1 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_7",
		headerBg: "color_1",
		secondary: "color_10",
		navheaderBg: "color_7",
		sidebarBg: "color_7",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		demoActive:1,
	};
	
	var dlabThemeSet2 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_5",
		secondary: "color_4",
		headerBg: "color_1",
		navheaderBg: "color_5",
		sidebarBg: "color_5",
		sidebarStyle: "mini",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		demoActive:2,
	};
	
	
	var dlabThemeSet3 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_11",
		secondary: "color_10",
		headerBg: "color_1",
		navheaderBg: "color_11",
		sidebarBg: "color_1",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		demoActive:3,
	};
	
	var dlabThemeSet4 = {
		typography: "poppins",
		version: "light",
		layout: "horizontal",
		primary: "color_9",
		secondary: "color_8",
		headerBg: "color_1",
		navheaderBg: "color_1",
		sidebarBg: "color_9",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		demoActive:4,
	};
	
	var dlabThemeSet5 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_6",
		secondary: "color_5",
		headerBg: "color_6",
		navheaderBg: "color_6",
		sidebarBg: "color_1",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		demoActive:5,
	};
	var dlabThemeSet6 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_11",
		secondary: "color_10",
		headerBg: "color_1",
		navheaderBg: "color_11",
		sidebarBg: "color_11",
		sidebarStyle: "morden",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		demoActive:6,
	};
	var dlabThemeSet7 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_12",
		secondary: "color_9",
		headerBg: "color_1",
		navheaderBg: "color_12",
		sidebarBg: "color_12",
		sidebarStyle: "morden",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		demoActive:7,
	};
	var dlabThemeSet8 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_10",
		secondary: "color_6",
		headerBg: "color_1",
		navheaderBg: "color_1",
		sidebarBg: "color_1",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		demoActive:8,
	};
	
		
	function themeChange(theme){
		var themeSettings = {};
		themeSettings = eval('dlabThemeSet'+theme);
		dlabSettingsOptions = themeSettings; /* For Screen Resize */
		new dlabSettings(themeSettings);
		setThemeInCookie(themeSettings);
		console.log(themeSettings);
	}
	
	function setThemeInCookie(themeSettings)
	{
		console.log(themeSettings);
		jQuery.each(themeSettings, function(optionKey, optionValue) {
			setCookie(optionKey,optionValue);
		});
	}
	
	function setThemeLogo() {
		var logo = getCookie('logo_src');
		
		var logo2 = getCookie('logo_src2');
		
		if(logo != ''){
			jQuery('.nav-header .logo-abbr').attr("src", logo);
		}
		
		if(logo2 != ''){
			jQuery('.nav-header .logo-compact, .nav-header .brand-title').attr("src", logo2);
		}
	}
	
	function setThemeOptionOnPage()
	{
		if(getCookie('version') != '')
		{
			jQuery.each(themeOptionArr, function(optionKey, optionValue) {
				
				var optionData = getCookie(optionKey);
				
				/*for  demo btn ac*/
				if(optionKey == "demoActive"){
					
					var themeBtns = document.querySelectorAll('.dlab_theme_demo');
					themeBtns.forEach(setDemoActive);
					function setDemoActive(item, index) {
						if($(item).data('theme') == optionData){
							$(item).parents('.dlab-demo-bx').addClass('demo-active');
						}else{
							$(item).parents('.dlab-demo-bx').removeClass('demo-active');
						}
					}
				}
				
				themeOptionArr[optionKey] = (optionData != '')?optionData:dlabSettingsOptions[optionKey];
				
				
				
			});
			dlabSettingsOptions = themeOptionArr;
			new dlabSettings(dlabSettingsOptions);
			
			setThemeLogo();
		}
	}
	
	jQuery(document).on('click', '.dlab_theme_demo', function(){
		var demoTheme = jQuery(this).data('theme');
		themeChange(demoTheme, 'ltr');
		
	});


	jQuery(document).on('click', '.dlab_theme_demo_rtl', function(){
		var demoTheme = jQuery(this).data('theme');
		themeChange(demoTheme, 'rtl');
	});
	
	
	jQuery(window).on('load', function(){
		//direction = (direction != undefined)?direction:'ltr';
		if(theme != undefined){
			themeChange(theme);
		}else if(getCookie('version') == ''){	
				themeChange(0);
			
		}
		
		/* Set Theme On Page From Cookie */
		setThemeOptionOnPage();
	});
	

})(jQuery);