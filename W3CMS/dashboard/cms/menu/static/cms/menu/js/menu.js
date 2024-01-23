$(document).ready(function(){

jQuery(document).on('click', '.RemoveItem', function(event) {
    var itemId 		=  jQuery(this).attr('rel');
    var item_name 	=  jQuery(this).attr('item-name');



    if(itemId != ""){


    Swal.fire({
        title: 'Are you sure?',
        text: "Are you sure you want to delete item "+item_name+"?",
        type: "warning",
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: "Yes, delete it !!",
        confirmButtonText: 'Delete',
        confirmButtonColor: "#DD6B55"
    }).then((result) => {
        if (result.value) {
        jQuery.ajax({
            headers: {
                'X-CSRF-TOKEN': CSRF_TOKEN
            },
            url: menu_item_delete_url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken:CSRF_TOKEN,
                'item_id': itemId,
            },
            success:function(res){
                if (res.success){
                    var child = jQuery('.xLi_'+itemId+' ol').children().first();
                    jQuery('.xLi_'+itemId).before(child);
                    jQuery('.xLi_'+itemId).fadeOut('slow', function(){
                    jQuery(this).remove();	
                    });
                }
                if (res.error){




                    Swal.fire({
                        type: 'info',
                        title: "Not Allow",
                        text: res.error,
                        confirmButtonColor: "var(--primary)"
                    });



                                 
                }
            },
        });


    }else if (result.dismiss === Swal.DismissReason.cancel) {
        event.preventDefault();
    }

    });



    }









  
   


   
});	

////////////////////////////////End MenuItem Remove>>>>>>>>>>>>>>>>>>>>>>>>>

jQuery(document).on('keyup', '.itemLabel', function() {
    var label = jQuery(this).val();	
    var rel = jQuery(this).attr('rel');	
    jQuery('.showLabel_'+rel).text(label);				  
});


/////////////////////////StartSaveMenu>>>>>>>>>>>>>>>>>>>>>>>>>>>>


jQuery(document).on('click', '.SaveMenu', function() {
    var menu_id = jQuery(this).attr('rel');
    form_data = $("#MenuItem"+menu_id+"Form").serializeArray();
    formData = JSON.stringify(form_data);

    var menu_name = $('#MenuNameEdit').val();

    let menu_data = {
        "menu_id": menu_id,
        "menu_name": menu_name
      };
    menu_data = JSON.stringify(menu_data)
    var data = $('.dd').nestable('toArray');
    // var data = $('.dd').nestable('serialize');
    // var data = $('.dd').nestable('asNestedSet');
    

    dd_data = JSON.stringify(data);

    if(dd_data != ""){
        jQuery.ajax({
            headers: {
                'X-CSRF-TOKEN': CSRF_TOKEN
            },
            url: menu_structure_save_url,
            type: 'POST',
            dataType:'json',
            data: {
                csrfmiddlewaretoken:CSRF_TOKEN,
                'dd_data': dd_data,
                'menu_data':menu_data,
                'form_data':formData
            },
            success:function(res){
                if(res.success){
                    $('.MenuSelectDiv .nice-select .current').text(menu_name);
                    $('.MenuSelectDiv .nice-select .list .selected').text(menu_name)
                    // alert(res.success);
                    Swal.fire({
                        type: 'success',
                        title: 'Save Successfully',
                        text: 'All Menu Item Save Successfully',
                        confirmButtonColor: "var(--primary)"
                    });
                }
                if(res.error){

                    Swal.fire({
                        type: 'warning',
                        title: 'Not Allow',
                        text: res.error,
                        confirmButtonColor: "var(--primary)"
                    })
                    
                }
            },
        });
    }
});
////////////////////////////////EndSaveMenu>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

jQuery(document).on('click', '.MenuSelectbtn', function() {
    var id =  $("#MenuSelect option:selected").val();
    if(id != ""){window.location.href = "/dashboard/menus/setup/"+id+"/";}
});

//////


jQuery(document).on('click', '.CreateNewMenu', function() {


html_data=` 
<div class="row">
   <div class"col-md-12">
      <form action="" method="post">
         <input type="hidden" name="csrfmiddlewaretoken" value="${CSRF_TOKEN}">
         <div class="card">
            <div class="card-header bg-primary flex-wrap" >
               <p class="text-white h4">Menu Name</p>
               <div class="menuinput">
                  <input type="text" name="menu_create" class="form-control w-auto mb-1">
               </div>
               <div class='actions'>
                  <button type="submit" class="btn btn-secondary mb-1 disabled">Create Menu</button>
               </div>
            </div>
            <div class="card-body">
               <div class="nestable">
                  <div class="dd" id="nestable">
                  <p>Give your menu a name, then click Create Menu.</p>
                  </div>
               </div>
            </div>
            <div class="card-footer d-sm-flex justify-content-between align-items-center">
               <div class='actions'>
                  <button type="submit" class="btn btn-primary disabled">Create Menu</button>
               </div>
            </div>
         </div>
      </form>
   </div>
</div>
`
$("#MenuTypeDiv").addClass("disable_menu");
$('#MenuAndMenuItem').replaceWith(html_data);

$('.MenuSelectDiv .nice-select .current').text('Select Menu')
$('.MenuSelectDiv .nice-select .selected').removeClass('selected')

$('.MenuSelectDiv .nice-select').addClass('disabled')


$('.menuinput input').on('keyup', function() {
    let empty = false;
    $('.menuinput input').each(function() {
      empty = $(this).val().length == 0;
    });

    if (empty){ $('.actions button').addClass('disabled');} 
    else{ $('.actions button').removeClass('disabled');}
  });
});


///////////////////////////////////////////////


jQuery(".DeleteMenu").click(function(event){
    var id = jQuery(this).attr('rel');
    var menu_name 	=  jQuery(this).attr('menu-name');
  

 if(id!=''){  
    
   
        Swal.fire({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            type: "warning",
      
            showCancelButton: true,
            confirmButtonText: "Yes, delete it !!",
            confirmButtonText: 'Delete',
            confirmButtonColor: "#DD6B55"
        }).then((result) => {
            if (result.value) {
                jQuery.ajax({
                    headers: {
                        'X-CSRF-TOKEN': CSRF_TOKEN
                    },
                    url: menu_delete_url,
                    type: 'POST',
                    dataType:'json',
                    data: {
                    csrfmiddlewaretoken:CSRF_TOKEN,
                    'menu_id':id
                    },
                    success:function(res){
                        if (res.success){ window.location.href = res.success;}
                        if (res.error){


                            Swal.fire({
                                type: 'info',
                                title: "Not Allow",
                                text: res.error,
                                confirmButtonColor: "var(--primary)"
                            });

                        
                        
                        }
                    },
                });
                
            } else if (result.dismiss === Swal.DismissReason.cancel) {
                event.preventDefault();
            }
        })
    }
});

///////////////////////////////


setScreenOption();
allowBlock();
SearchForMenu();
selectAll();
cancelMenuObject();
AddToMenu();
LinksAddToMenu();
checkboxUtility();

////End
}); 


function selectAll()
{
	jQuery('.SelectAllItems').click(function(){
		jQuery(this).parents('.ItemsCheckboxSec').find('input[type="checkbox"]').prop( "checked", true );		
	});
	jQuery('.DeSelectAllItems').click(function(){
		jQuery(this).parents('.ItemsCheckboxSec').find('input[type="checkbox"]').prop( "checked", false );		
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
function allowBlock()
{
	jQuery(document).on('click', '.allowField', function() {
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

		var date = new Date();
		//date.setTime(date.getTime()+(minute*60*1000)); 	FOR MINUTE
		date.setDate(date.getDate() + 30); 					//FOR DAYS
		
		document.cookie = "isCheck_"+result+"="+isCheck+"; expires="+date.toGMTString()+"path=/";
	});
}

function cancelMenuObject()
{

    jQuery(document).on('click', '.CancelItem', function(){
        var $this = jQuery(this).parents('.accordion .accordion-item');
        $this.find('.accordion-button').addClass('collapsed');
        $this.find('.accordion-collapse').removeClass('show');
    });
	
}


function checkboxUtility()
{
    jQuery(document).on('click', '.checkboxUtility', function(){

        jQuery(this).parents('.default-tab').find('input[type="checkbox"]').prop( "checked", false );
							
	});
}

////////////////////////////////////////////////AddMenu/////////////////////////////



function AddToMenu(){
    jQuery(document).on('click', '.AddToMenu', function() {
        var olSize 		= jQuery('.dd ol').length;
		var $this 		= jQuery(this);
		var MenuType	= $this.attr('menu-type');
		var MenuId 		= $this.attr('menu-id');
		var error 		= 1;
		MenuId 	   		= parseInt(MenuId, 10);
        console.log("MenuId:"+MenuId);
        console.log("olsize:"+olSize);

        formData 	= jQuery(this).closest("form").serialize()+"&menu_type="+MenuType;

	    actionUrl 	= jQuery(this).closest("form").attr('action');

        jQuery.ajax({
            headers: {
                'X-CSRF-TOKEN': CSRF_TOKEN
            },
            type: 'POST',
            url: actionUrl,
            data:formData,
            success : function(res)
            {



                if(res.success){
                    if(olSize != 0){
						var result = '<ol class="dd-list setMenu"></ol>';
                        $(".dd-empty").remove();
                        $("#setMenu").append( res.success ); 
					}
                }
                if (res.error){


                    Swal.fire({
                        type: 'warning',
                        title: 'Not Allow',
                        text: res.error,
                        confirmButtonColor: "var(--primary)"
                    });

                }
               

            },
           
        });

    });
}



function LinksAddToMenu(){
    jQuery(document).on('click', '.LinksAddToMenu', function() {
     
		var olSize = jQuery('.dd ol').length;
		var LinkMenuId = jQuery('.LinkMenu').val();

		var MenuLinkUrl = jQuery('.MenuLinkUrl').val();
		var MenuLinkTitle = jQuery('.MenuLinkTitle').val();
        var error = '';


        console.log(LinkMenuId);
        console.log(MenuLinkUrl);
        console.log(MenuLinkTitle);
        console.log(typeof MenuLinkTitle);

        if((jQuery.trim(MenuLinkUrl) == "") || (MenuLinkTitle == "")) 
		{ 
			error = 'Please fill these fields.';
		}
		else if((jQuery.trim(LinkMenuId) == "")) 
		{ 
			error = 'Please fill these fields.'; 
		}
       
		
		if(error == ''){

            formData = jQuery(this).closest("form").serialize();
			actionUrl = jQuery(this).closest("form").attr('action');


            jQuery.ajax({
                headers: {
                    'X-CSRF-TOKEN': CSRF_TOKEN
                },
                type: 'POST',
                url: actionUrl,
                data:formData,
                success : function(res)
                {
                    if (res.success){
                        if(olSize != 0)
                        {
                            var result = '<ol class="dd-list setMenu"></ol>';
                            
                            $(".dd-empty").remove();
                            $("#setMenu").append( res.success ); 
                        }

                    }
                    if (res.error){
                        Swal.fire({
                            type: 'warning',
                            title: 'Not Allow',
                            text: res.error,
                            confirmButtonColor: "var(--primary)"
                        });
                    }
                   
                },
              
            });


        }else{
            alert(error);
        }





    });
}


function SearchForMenu(){	
	
	jQuery(document).on('keyup', '.SearchForMenu', function() {
		
		var keyValue 			= jQuery(this).val();
		var searchType 			= jQuery(this).parent().children('.search_type').val();
		var searchContentDiv 	= jQuery(this).closest('.tab-pane').children('.searchContentDiv');




        console.log(keyValue)
        console.log(searchType)
        console.log(searchContentDiv)



		//console.log(searchContentDiv); return false;
		if(jQuery.trim(keyValue) != "" && jQuery.trim(searchType) != "" && typeof search_menus_url !== 'undefined')
		{
			jQuery.ajax({
				headers: {
					'X-CSRF-TOKEN': CSRF_TOKEN
				},
				type: 'POST',
				url: search_menus_url,
				data: {
                    csrfmiddlewaretoken: CSRF_TOKEN,
                    'page_key': keyValue,
                    'search_type': searchType,
                },
				success : function(data)
				{
					searchContentDiv.html(data.success);
				},
				error : function(data)
				{
					//alert(data+" Error ");
				}
			});
		}
		else
		{
			var data = ''; 
			searchContentDiv.html(data);
		}

	});	
}



$('.sweet-delete-menu-cancel').on('click', function (event) {
    event.preventDefault();
    const url = $(this).attr('href');

    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        type: "warning",
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: "Yes, delete it !!",
        confirmButtonText: 'Delete',
        confirmButtonColor: "#DD6B55"
        
    }).then((result) => {
        if (result.value) {
            window.location.href = url;
        } else if (result.dismiss === Swal.DismissReason.cancel) {
            event.preventDefault();
        }
    })
});
