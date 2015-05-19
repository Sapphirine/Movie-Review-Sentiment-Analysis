<?php

// include function files for this application
require_once('movie_sc_fns.php');
session_start();

do_html_header("Updating movie");
if (check_admin_user()) {
  if (filled_out($_POST)) {
    $oldisbn = $_POST['oldisbn'];
    $movieid = $_POST['movieid'];
    $title = $_POST['title'];
    $director = $_POST['director'];
    $catid = $_POST['catid'];
    $price = $_POST['price'];
    $description = $_POST['description'];

    if(update_movie($oldisbn, $movieid, $title, $director, $catid, $price, $description)) {
      echo "<p>movie was updated.</p>";
    } else {
      echo "<p>movie could not be updated.</p>";
    }
  } else {
    echo "<p>You have not filled out the form.  Please try again.</p>";
  }
  do_html_url("admin.php", "Back to administration menu");
} else {
  echo "<p>You are not authorised to view this page.</p>";
}

do_html_footer();

?>
