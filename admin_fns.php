<?php
// This file contains functions used by the admin interface

function display_category_form($category = '') {
// This displays the category form.
// This form can be used for inserting or editing categories.
// To insert, don't pass any parameters.  This will set $edit
// to false, and the form will go to insert_category.php.
// To update, pass an array containing a category.  The
// form will contain the old data and point to update_category.php.
// It will also add a "Delete category" button.

  // if passed an existing category, proceed in "edit mode"
  $edit = is_array($category);

  // most of the form is in plain HTML with some
  // optional PHP bits throughout
?>
  <form method="post"
      action="<?php echo $edit ? 'edit_category.php' : 'insert_category.php'; ?>">
  <table border="0">
  <tr>
    <td>Category Name:</td>
    <td><input type="text" name="catname" size="40" maxlength="40"
          value="<?php echo $edit ? $category['catname'] : ''; ?>" /></td>
   </tr>
  <tr>
    <td <?php if (!$edit) { echo "colspan=2";} ?> align="center">
      <?php
         if ($edit) {
            echo "<input type=\"hidden\" name=\"catid\" value=\"".$category['catid']."\" />";
         }
      ?>
      <input type="submit"
       value="<?php echo $edit ? 'Update' : 'Add'; ?> Category" /></form>
     </td>
     <?php
        if ($edit) {
          //allow deletion of existing categories
          echo "<td>
                <form method=\"post\" action=\"delete_category.php\">
                <input type=\"hidden\" name=\"catid\" value=\"".$category['catid']."\" />
                <input type=\"submit\" value=\"Delete category\" />
                </form></td>";
       }
     ?>
  </tr>
  </table>
<?php
}

function display_movie_form($movie = '') {
// This displays the movie form.
// It is very similar to the category form.
// This form can be used for inserting or editing movies.
// To insert, don't pass any parameters.  This will set $edit
// to false, and the form will go to insert_movie.php.
// To update, pass an array containing a movie.  The
// form will be displayed with the old data and point to update_movie.php.
// It will also add a "Delete movie" button.


  // if passed an existing movie, proceed in "edit mode"
  $edit = is_array($movie);

  // most of the form is in plain HTML with some
  // optional PHP bits throughout
?>
  <form method="post"
        action="<?php echo $edit ? 'edit_movie.php' : 'insert_movie.php';?>">
  <table border="0">
  <tr>
    <td>movieid:</td>
    <td><input type="text" name="movieid"
         value="<?php echo $edit ? $movie['movieid'] : ''; ?>" /></td>
  </tr>
  <tr>
    <td>movie Title:</td>
    <td><input type="text" name="title"
         value="<?php echo $edit ? $movie['title'] : ''; ?>" /></td>
  </tr>
  <tr>
    <td>movie director:</td>
    <td><input type="text" name="director"
         value="<?php echo $edit ? $movie['director'] : ''; ?>" /></td>
   </tr>
   <tr>
      <td>Category:</td>
      <td><select name="catid">
      <?php
          // list of possible categories comes from database
          $cat_array=get_categories();
          foreach ($cat_array as $thiscat) {
               echo "<option value=\"".$thiscat['catid']."\"";
               // if existing movie, put in current catgory
               if (($edit) && ($thiscat['catid'] == $movie['catid'])) {
                   echo " selected";
               }
               echo ">".$thiscat['catname']."</option>";
          }
          ?>
          </select>
        </td>
   </tr>
   <tr>
    <td>Price:</td>
    <td><input type="text" name="price"
               value="<?php echo $edit ? $movie['price'] : ''; ?>" /></td>
   </tr>
   <tr>
     <td>Description:</td>
     <td><textarea rows="3" cols="50"
          name="description"><?php echo $edit ? $movie['description'] : ''; ?></textarea></td>
    </tr>
    <tr>
      <td <?php if (!$edit) { echo "colspan=2"; }?> align="center">
         <?php
            if ($edit)
             // we need the old movieid to find movie in database
             // if the movieid is being updated
             echo "<input type=\"hidden\" name=\"oldisbn\"
                    value=\"".$movie['movieid']."\" />";
         ?>
        <input type="submit"
               value="<?php echo $edit ? 'Update' : 'Add'; ?> movie" />
        </form></td>
        <?php
           if ($edit) {
             echo "<td>
                   <form method=\"post\" action=\"delete_movie.php\">
                   <input type=\"hidden\" name=\"movieid\"
                    value=\"".$movie['movieid']."\" />
                   <input type=\"submit\" value=\"Delete movie\"/>
                   </form></td>";
            }
          ?>
         </td>
      </tr>
  </table>
  </form>
<?php
}

function display_password_form() {
// displays html change password form
?>
   <br />
   <form action="change_password.php" method="post">
   <table width="250" cellpadding="2" cellspacing="0" bgcolor="#cccccc">
   <tr><td>Old password:</td>
       <td><input type="password" name="old_passwd" size="16" maxlength="16" /></td>
   </tr>
   <tr><td>New password:</td>
       <td><input type="password" name="new_passwd" size="16" maxlength="16" /></td>
   </tr>
   <tr><td>Repeat new password:</td>
       <td><input type="password" name="new_passwd2" size="16" maxlength="16" /></td>
   </tr>
   <tr><td colspan=2 align="center"><input type="submit" value="Change password">
   </td></tr>
   </table>
   <br />
<?php
}

function insert_category($catname) {
// inserts a new category into the database

   $conn = db_connect();

   // check category does not already exist
   $query = "select *
             from categories
             where catname='".$catname."'";
   $result = $conn->query($query);
   if ((!$result) || ($result->num_rows!=0)) {
     return false;
   }

   // insert new category
   $query = "insert into categories values
            ('', '".$catname."')";
   $result = $conn->query($query);
   if (!$result) {
     return false;
   } else {
     return true;
   }
}

function insert_movie($movieid, $title, $director, $catid, $price, $description) {
// insert a new movie into the database

   $conn = db_connect();

   // check movie does not already exist
   $query = "select *
             from movies
             where movieid='".$movieid."'";

   $result = $conn->query($query);
   if ((!$result) || ($result->num_rows!=0)) {
     return false;
   }

   // insert new movie
   $query = "insert into movies values
            ('".$movieid."', '".$director."', '".$title."',
             '".$catid."', '".$price."', '".$description."')";

   $result = $conn->query($query);
   if (!$result) {
     return false;
   } else {
     return true;
   }
}

function update_category($catid, $catname) {
// change the name of category with catid in the database

   $conn = db_connect();

   $query = "update categories
             set catname='".$catname."'
             where catid='".$catid."'";
   $result = @$conn->query($query);
   if (!$result) {
     return false;
   } else {
     return true;
   }
}

function update_movie($oldisbn, $movieid, $title, $director, $catid,
                     $price, $description) {
// change details of movie stored under $oldisbn in
// the database to new details in arguments

   $conn = db_connect();

   $query = "update movies
             set movieid= '".$movieid."',
             title = '".$title."',
             director = '".$director."',
             catid = '".$catid."',
             price = '".$price."',
             description = '".$description."'
             where movieid = '".$oldisbn."'";

   $result = @$conn->query($query);
   if (!$result) {
     return false;
   } else {
     return true;
   }
}

function delete_category($catid) {
// Remove the category identified by catid from the db
// If there are movies in the category, it will not
// be removed and the function will return false.

   $conn = db_connect();

   // check if there are any movies in category
   // to avoid deletion anomalies
   $query = "select *
             from movies
             where catid='".$catid."'";

   $result = @$conn->query($query);
   if ((!$result) || (@$result->num_rows > 0)) {
     return false;
   }

   $query = "delete from categories
             where catid='".$catid."'";
   $result = @$conn->query($query);
   if (!$result) {
     return false;
   } else {
     return true;
   }
}


function delete_movie($movieid) {
// Deletes the movie identified by $movieid from the database.

   $conn = db_connect();

   $query = "delete from movies
             where movieid='".$movieid."'";
   $result = @$conn->query($query);
   if (!$result) {
     return false;
   } else {
     return true;
   }
}

?>
