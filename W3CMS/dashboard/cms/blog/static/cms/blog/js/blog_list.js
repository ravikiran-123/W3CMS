

jQuery('.clear-blog-filter').click(function(){
    window.location.href = "/dashboard/blogs/";
});

$(document).ready(function(){

    $('#delete_multiple_items').on('click', function (event) {
        var ids = [];
        $(':checkbox:checked').each(function(i){
            ids[i]=$(this).val();
        });

        var blogdeleteURL = jQuery(this).data('url');
             
        if(ids.length!=0){


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
                  

  
                    $.ajax({
                        url:blogdeleteURL,
                        method:"POST",
                        dataType:'json',
                        data:{
                            ids,
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                        },
                        success:function(res){
                            if(res.warning){
                                document.getElementById("message").innerHTML += '<div class="alert alert-warning alert-dismissible alert-alt solid fade show">\
                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="btn-close">\
                                    </button>'+res.warning+'</div>';
                            }
                            if(res.success){
        
                                for(var i=0; i < ids.length; i++){
                                    if (ids[i] != ''){
                                        $('tr#'+ids[i]+'').css('background-color','#ccc');
                                        $('tr#'+ids[i]+'').remove(); 
    
                                    }
                                    
                                }
                                document.getElementById("message").innerHTML += '<div class="alert alert-success alert-dismissible alert-alt solid fade show">\
                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="btn-close">\
                                    </button>'+res.success+'</div>';
                            }
                            
                        }
                    });


                } else if (result.dismiss === Swal.DismissReason.cancel) {
                    event.preventDefault();
                }
            });

        }else{
            Swal.fire({
                type: 'info',
                title: 'Oops...',
                text: 'Please Select Items To Delete',
                confirmButtonColor: 'var(--primary)'
            });
        }


    
    });




    $('.sweet-success-cancel').on('click', function (event) {
        event.preventDefault();
        const url = $(this).attr('href');

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
                window.location.href = url;
            } else if (result.dismiss === Swal.DismissReason.cancel) {
                event.preventDefault();
            }
        })
    });




});



jQuery(document).on('click', '.copyToClip', function(event) {
    
     var $temp = $("<input>");
        $("body").append($temp);
        $temp.val($(this).find('.site_url').text()).select();
        document.execCommand("copy");
        $('.copyToClip i').removeClass('text-success');
        $(this).find('i').addClass('text-success')
        $temp.remove();
    
    });
    