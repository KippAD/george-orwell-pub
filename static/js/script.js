// Changes formatting of the date in events schedule if expanded
$(document).ready(function () {
  // Datatable styles
  $('#booking-table').DataTable();
  $('#user-table').DataTable();
  $('#user-table tr:even').css("background-color", "#F4F4F8");
  $('#user-table tr:odd').css("background-color", "#FFFFFF");
});