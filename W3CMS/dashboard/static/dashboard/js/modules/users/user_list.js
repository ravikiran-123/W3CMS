

$(document).ready(function(){




    jQuery('.clear-user-filter').click(function(){
        window.location.href = "/dashboard/users/";
    });
    




$('#delete_multiple_btn').on('click', function (event) {
    var id = [];
       
    $(':checkbox:checked').each(function(i){
        id[i]=$(this).val();
    });

    var pagedeleteURL = jQuery(this).data('url');

    if(id.length!=0){

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



                $.ajax({
                    url:pagedeleteURL,
                    method:"POST",
                    dataType:'json',
                    data:{
                        id,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(res){
                        if(res.warning){
                            document.getElementById("message").innerHTML += '<div class="alert alert-warning alert-dismissible alert-alt solid fade show">\
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="btn-close">\
                                </button>'+res.warning+'</div>';
    
                        }
                        if(res.success){
    
                            for(var i=0; i < id.length; i++){
                                if(id[i]!=''){
                                    $('tr#'+id[i]+'').css('background-color','#ccc');
                                    // $('tr#'+id[i]+'').fadeOut('slow');
                                     $('tr#'+id[i]+'').remove(); 
                                }
    
                            }
                            document.getElementById("message").innerHTML += '<div class="alert alert-success alert-dismissible alert-alt solid fade show">\
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="btn-close">\
                                </button>'+res.success+'</div>';
    
                        }
                        
                    }
                })


               
            } else if (result.dismiss === Swal.DismissReason.cancel) {
                event.preventDefault();
            }
        });

    
        
    }else{
        Swal.fire({
            type: 'info',
            title: 'Oops...',
            text: 'Please Select Items To Delete',
            confirmButtonColor:"var(--primary)"
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



});






