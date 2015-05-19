<?php

// include function files for this application
require_once('movie_sc_fns.php');
session_start();

do_html_header("Adding a movie");
if (check_admin_user()) {
  if (filled_out($_POST)) {
    $movieid = $_POST['movieid'];
    $title = $_POST['title'];
    $director = $_POST['director'];
    $catid = $_POST['catid'];
    $price = $_POST['price'];
    $description = $_POST['description'];

    if(insert_movie($movieid, $title, $director, $catid, $price, $description)) {
      echo "<p>movie <em>".stripslashes($title)."</em> was added to the database.</p>";
    } else {
      echo "<p>movie <em>".stripslashes($title)."</em> could not be added to the database.</p>";
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
