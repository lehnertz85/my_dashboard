/**
 * Created by william on 12/4/2016.
 */

// Call the SideNav
$('.button-collapse').sideNav({
    menuWidth: 200, // Default is 240
    edge: 'right', // Choose the horizontal origin
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
    draggable: true // Choose whether you can drag to open on touch screens
});

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Call the modals
$('#settings-modal').modal();
$('#help-modal').modal();
$('#drives-modal').modal({
    dismissible: false
});

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Keep track of the Caracter count for each input
$('input.validate').characterCounter();

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/* My attempt at ajax. Doesn't work. I suspect is has to do with modals */


$('.ajax-form').on('submit', function(e) {

    e.preventDefault();

    var form = $(this);

    $.ajax({
        type: "post",
        data: form.serialize(),
        dataType: 'json',
        success: function(errors) {
            console.log(JSON.stringify(errors));

            $.each(errors, function (key, value) {
                if(key == 'success')
                {
                    Materialize.toast(value, 6000, 'orange center black-text');

                    // if($('#drives-modal').is(':visible'))
                    // {
                    //     $('#drives-modal').modal('close')
                    // }
                    // else if($('#settings-modal').is(':visible'))
                    // {
                    //     $('#settings-modal').modal('close');
                    // }
                }
                else
                {
                    Materialize.toast(value, 15000, 'red center black-text');
                }
            });
        },
        error: function(errors) {
            Materialize.toast('There was a server error. Not sure what happened.', 4000, 'red center black-text');
        }
    });
});
