jQuery(document).ready(function() {
	/* Allow Block */
		allowBlock();
	/* Allow Block */

	/* Screen Option */
		setScreenOption();
	/* Screen Option */

	/* Remove Custom Field */
    remove_CustomField();
	/* Remove Custom Field */
	readURL();

});


jQuery('#ContentTitle').slug({hide:false});//In jQuery(document).ready(function() its not working


function readURL(input) {
 
	if (input.files && input.files[0]) {
		  var reader = new FileReader();
		  reader.onload = function(e) {
			 $('#imagePreview').css('background-image', 'url('+e.target.result +')');
			 $('#imagePreview').hide();
			 $('#imagePreview').fadeIn(650);
		  }
		  reader.readAsDataURL(input.files[0]);
	}
 }
 $("#id_avatar").on('change', function() {
	readURL(this);
 });


window.onload = function() {
    var src = document.getElementById("ContentTitle"),
        dst = document.getElementById("SEOPageTitle");
    src.addEventListener('input', function() {
        dst.value = src.value;
    });
};


/*Add Custom Field*/
const totalNewForms = document.getElementById('id_form-TOTAL_FORMS');

const addMoreBtn = document.getElementById('add-cfield');
addMoreBtn.addEventListener('click',add_new_form);

function add_new_form(event){
  if (event){
	event.preventDefault();
  }

  const currentCF_Forms = document.getElementsByClassName('cfield-form');
  const currentCF_FormCount = currentCF_Forms.length //+ 1

  const formCopyTarget = document.getElementById('cfield-form-list');
  const copyEmptyFormEl = document.getElementById('empty_form').cloneNode(true);
  //remove class hidden
  copyEmptyFormEl.setAttribute('class','cfield-form xrow');
  copyEmptyFormEl.setAttribute('id',`form-${currentCF_FormCount}`);
  const regex = new RegExp('__prefix__','g');
  copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex,currentCF_FormCount);
  totalNewForms.setAttribute('value', currentCF_FormCount +1);
  formCopyTarget.append(copyEmptyFormEl);

 remove_CustomField();
 
}


function remove_CustomField(){
$( ".remove_cfield" ).click(function(event) {
	jQuery(this).closest('.xrow').fadeOut('slow',function(){
	jQuery(this).remove();
	const currentCF_Forms = document.getElementsByClassName('cfield-form')
	const currentCF_FormCount = currentCF_Forms.length
	totalNewForms.setAttribute('value', currentCF_FormCount)                                                                                                   
	});
	
});
}



function allowBlock()
{


	jQuery('.allowField').on('click',function(){  

		var result  = jQuery(this).attr('rel');
		
		if (jQuery(this).prop('checked')==true)
		{
			jQuery('.X'+result).show('slow');
			var isCheck = 1;
		}
		else
		{
			var isCheck = 0;
			jQuery('.X'+result).hide('slow');
		}
		
		document.cookie = "isCheck_"+result+"="+isCheck+"; path=/";


	});


	
}

function setScreenOption() {

    if(typeof screenOptionArray == 'undefined')
    {
        
        return false;
    }
    var screenOption = [];
    var obj = JSON.parse(screenOptionArray);
    jQuery.each(obj, function(outerKey, outerValue) {
        jQuery.each(outerValue, function(innerKey, innerValue) {
            var setOptionValue = getCookie('isCheck_' + outerKey);
            setOptionValue = parseInt(setOptionValue, 10);

            if(setOptionValue == 1)
            {
                jQuery('.X'+outerKey).show('slow');
                jQuery('.Allow'+outerKey).prop( "checked", true );
            }
            else if(setOptionValue == 0)
            {
                jQuery('.X'+outerKey).hide('slow');
                jQuery('.Allow'+outerKey).prop( "checked", false );
            }
            else
            {
                if(outerValue.visibility)
                {
                    jQuery('.X'+outerKey).show('slow');
                    jQuery('.Allow'+outerKey).prop( "checked", true );
                } else {
                    jQuery('.X'+outerKey).hide('slow');
                    jQuery('.Allow'+outerKey).prop( "checked", false );
                }
            }

        });
    });
}

jQuery(document).on('change', '#ContentVisibility', function() {		
	var result = jQuery(this).val();
	if(result == 'PP') { 
		jQuery('#PublicPasswordTextbox').show('slow');
		jQuery( "#ContentPassword" ).focus(); 
	} else { 
		jQuery('#PublicPasswordTextbox').hide('slow'); 
		jQuery('#PublicPasswordTextbox').val(" ");
	}
		
});

