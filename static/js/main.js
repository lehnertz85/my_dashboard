/**
 * Created by william on 12/4/2016.
 */

// Submit post on submit
// $('#post-form').on('submit', function(event){
//     event.preventDefault();
//     console.log("form submitted!");  // sanity check
//
//     $.ajax({
//             type: $('#post-form').attr('method'),
//             url: $('#post-form').attr('action'),
//             data: $('#post-form').serialize(),
//             // csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]'),
//
//             success: function(data) {
//                 $("#form_div").html(data);
//             },
//
//             error: function(data) {
//                 $("#form_div").html(data);
//             }
//         });
// });


// Call the SideNav
$('.button-collapse').sideNav({
    menuWidth: 200, // Default is 240
    edge: 'right', // Choose the horizontal origin
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
    draggable: true // Choose whether you can drag to open on touch screens
});


// Call the modals
$('#settings-modal').modal();
$('#help-modal').modal();
$('#drives-modal').modal();


// Keep track of the Caracter count for each input
$('input.validate').characterCounter();
