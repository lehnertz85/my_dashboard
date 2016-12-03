/**
 * Created by william on 11/5/2016.
 */
(function($){
  $(function(){
    $('.button-collapse').sideNav({
          menuWidth: 200, // Default is 240
          edge: 'right', // Choose the horizontal origin
          closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
          draggable: true // Choose whether you can drag to open on touch screens
        });
  }); // end of document ready
})(jQuery); // end of jQuery name space