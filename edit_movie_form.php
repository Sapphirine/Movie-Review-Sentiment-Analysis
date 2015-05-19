<?php

// include function files for this application
require_once('movie_sc_fns.php');
session_start();

do_html_header("Edit movie details");
if (check_admin_user()) {
  if ($movie = get_movie_details($_GET['movieid'])) {
    display_movie_form($movie);
  } else {
    echo "<p>Could not retrieve movie details.</p>";
  }
  do_html_url("admin.php", "Back to administration menu");
} else {
  echo "<p>You are not authorized to enter the administration area.</p>";
}
do_html_footer();

?>
