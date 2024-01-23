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

$('.clear-contactus-filter').on('click', function (event) {

    window.location.href = "/dashboard/contact-us/";

});

jQuery(document).on('click', '.contactus-modal', function() {
    var ContentDiv = jQuery('.contact-modal-body');
    var id = jQuery(this).attr('rel');
    console.log(id);
          $.ajax({
              type: 'GET',
              url: "/dashboard/contact-us/view/",
              data:{"id":id},
              success: function (response) {

                    jQuery('#ContactPersonMessage').modal('show');
                    jQuery('#ContactPersonMessage .modal-body').html(response.data);

              },
              error: function (response) {
                  // alert the error if any error occured
                //   alert(respons.error.val);
              }
          })
        
});

