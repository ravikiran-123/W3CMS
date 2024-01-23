$(document).ready(function() {



/* Allow Block */
allowBlock();
/* Allow Block */

/* Screen Option */
setScreenOption();
/* Screen Option */



addNewBlogCategory();

remove_CustomField();
readURL();
});



if(typeof blogCategoryIds != 'undefined')
{
categoryTreeSelected(blogCategoryIds);
}



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



$(document).ready(function() {
    $(window).keydown(function(event){
      if(event.keyCode == 13) {
        event.preventDefault();
        return false;
      }
    });
  });


window.onload = function() {
    src = document.getElementById("BlogTitle"),
    dst = document.getElementById("SEOBlogTitle");

    src.addEventListener('input', function() {
        dst.value = src.value;
    });
   
   
};




jQuery('#BlogTitle').slug({hide:false});


const totalNewForms = document.getElementById('id_form-TOTAL_FORMS');
const form_id_count = document.getElementById('form-id-count');
form_id_count.setAttribute('value', totalNewForms.value);
console.log('Total New Forms: '+totalNewForms.value);

const addMoreBtn = document.getElementById('add-cfield');
addMoreBtn.addEventListener('click',add_new_form);

function add_new_form(event){
  if (event){
	event.preventDefault();
  }

  const currentCF_Forms = document.getElementsByClassName('cfield-form');
  console.log(currentCF_Forms.length);
  const currentCF_FormCount = currentCF_Forms.length ;//+ 1
  const formCopyTarget = document.getElementById('cfield-form-list');
  const copyEmptyFormEl = document.getElementById('empty_form').cloneNode(true);

  const form_id_count = document.getElementById('form-id-count');
  console.log("ID COUNTER: "+form_id_count.value);
//   form_id_count.setAttribute('value', totalNewForms.value)



  copyEmptyFormEl.setAttribute('class','cfield-form xrow');
  copyEmptyFormEl.setAttribute('id',`form-${form_id_count.value}`);
  const regex = new RegExp('__prefix__','g');
  copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex,currentCF_FormCount);
  totalNewForms.setAttribute('value', currentCF_FormCount +1);
  //now add new empty form element to our html form
  formCopyTarget.append(copyEmptyFormEl);
  form_id_count.setAttribute('value', parseInt(form_id_count.value) + 1);
;
  remove_CustomField();
}


function remove_CustomField(){
    $(".remove_cfield").click(function(event) {
        if (event){
            event.preventDefault()
        }
        jQuery(this).closest('.xrow').fadeOut('slow',function(){
        jQuery(this).remove();
        const currentCF_Forms = document.getElementsByClassName('cfield-form')
        const currentCF_FormCount = currentCF_Forms.length
        totalNewForms.setAttribute('value', currentCF_FormCount)                                                                                                   
        });
    
    
    
    });
}
    


function allowBlock() {
    jQuery('.allowField').click(function() {

        //var isCheck = jQuery(this).val();
        var result = jQuery(this).attr('rel');

        //var p = getCookie('screenOption'+result);

        if (jQuery(this).prop('checked') == true) {
            jQuery('.X' + result).show('slow');
            var isCheck = 1;
        } else {
            var isCheck = 0;
            jQuery('.X' + result).hide('slow');
        }
         var date = new Date();
        //date.setTime(date.getTime()+(minute*60*1000));    FOR MINUTE
        date.setDate(date.getDate() + 30);                  //FOR DAYS
        
         document.cookie = "isCheck_"+result+"="+isCheck+"; expires="+date.toGMTString()+"path=/";
 
    });
}

function getScreenOptionValue(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(',');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1);
        if (c.indexOf(name) != -1) return c.substring(name.length, c.length);
    }
    return "";
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

function categoryTreeSelected(blogCategoryIds) {

    if (jQuery.trim(blogCategoryIds) != '') {
        var obj = JSON.parse(blogCategoryIds);

        jQuery.each(obj, function(outerKey, outerValue) {
            jQuery('.blog_categories').each(function() {

                if (jQuery(this).val() == outerValue) {
                    jQuery(this).prop("checked", true);
                }

            });
        });

    }
}

function addNewBlogCategory() {

    jQuery('.newCategoryDiv').hide();
    jQuery('.addNewBlogCategorylink').click(function() {
        jQuery('.newCategoryDiv').toggle('slow');
    });

    jQuery('.addNewBlogCategoryBtn').click(function() {
        var name       = jQuery('.newCategoryTitle').val();
        var parent_id   = jQuery('.CategoryParentId').val();
        
        var blogcatURL = jQuery(this).data('url');

        if (name != ""){
            $.ajax({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                },
                url: blogcatURL,
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    'name':name,
                    'parent': parent_id
                },
                dataType: 'html',
                success: function(res) {
                    data = JSON.parse(res);

                    if (data.success){
                        if(jQuery('.BlogCategory'+parent_id).length > 0){
                            jQuery('.BlogCategory'+parent_id).after().append(data.success.html_data);
                        }
                        else{
                            jQuery('#categories_checkbox ul:first').append(data.success.html_data)
                        }
                        // $('#id_parent option[value=val2]')
                        // if(parent_id){
                        //     jQuery(`#id_parent option[value=${parent_id}]`).after().append(data.success.select_option_html)
                        // }

                        // $('.newCategoryTitle').removeAttr('value');
                        $(".newCategoryTitle").val(null);
                        $(".CategoryParentId").val(null);
                        // $('.newCategoryTitle').removeAttr('value');
                        
                    }
                    if(data.warning){
                        alert('Category Already Exists !')
                        $(".newCategoryTitle").val(null);
                        $(".CategoryParentId").val(null);
                    }


                }
            });
        }
        else{
            alert('Category Title is Empty!')
        }
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



