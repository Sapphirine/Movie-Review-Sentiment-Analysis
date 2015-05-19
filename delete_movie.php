<?php

// include function files for this application
require_once('movie_sc_fns.php');
session_start();

do_html_header("Deleting movie");
if (check_admin_user()) {
  if (isset($_POST['movieid'])) {
    $movieid = $_POST['movieid'];
    if(delete_movie($movieid)) {
      echo "<p>movie ".$movieid." was deleted.</p>";
    } else {
      echo "<p>movie ".$movieid." could not be deleted.</p>";
    }
  } else {
    echo "<p>We need an movieid to delete a movie.  Please try again.</p>";
  }
  do_html_url("admin.php", "Back to administration menu");
} else {
  echo "<p>You are not authorised to view this page.</p>";
}

do_html_footer();

?>
