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

});