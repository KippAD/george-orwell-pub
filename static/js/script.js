// Changes formatting of the date in events schedule if expanded
$(document).ready(function () {
  // Datatable styles
  $('#booking-table').DataTable();
  $('#booking-table tr:even').css("background-color", "#F4F4F8");
  $('#booking-table tr:odd').css("background-color", "#FFFFFF");
  
  $('#user-table').DataTable();
  $('#user-table tr:even').css("background-color", "#F4F4F8");
  $('#user-table tr:odd').css("background-color", "#FFFFFF");

  // Sets height of contact form charfield
  $('#id_message').attr("rows", "5");

  // Fades out messages
  $('.alert').delay(3000).fadeOut(400);

  // Fixes responsive error on account page
  $('#account-tab').on('click', function() {
    $('#account-tab-pane').removeClass('d-none');
  })


});