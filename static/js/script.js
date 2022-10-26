// Changes formatting of the date in events schedule if expanded
$(document).ready(function () {
  // Datatable styles
  $('#booking-table').DataTable();
  $('#user-table').DataTable();
  $('#user-table tr:even').css("background-color", "#F4F4F8");
  $('#user-table tr:odd').css("background-color", "#FFFFFF");
  // Adding bootstrap styles to generated fields in forms
  $('#id_event').attr('rows', 5);
  $('#id_description').attr('rows', 5);

  $('#id_event').addClass('form-select').addClass('form-select-lg');
  $('#id_post').addClass('form-select').addClass('form-select-lg');
});