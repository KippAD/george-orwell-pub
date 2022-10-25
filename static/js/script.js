// Changes formatting of the date in events schedule if expanded
$(document).ready(function () {
  $('#user-table').DataTable();
  $('#user-table tr:even').css("background-color", "#F4F4F8");
  $('#user-table tr:odd').css("background-color", "#FFFFFF");
  // Message tab in admin
  $('#v-pills-tab button:first').addClass('active');
});