# Movie-Review-Sentiment-Analysis

This document can help you use the following repository.
https://github.com/Sapphirine/Movie-Review-Sentiment-Analysis

Part A) the folder contains a well-built online movie website.  

    To run this online movie website, you need to get an access to a LAMP server. LAMP stands for Linux, Apache, MySQL, PHP. 

    First, copy the content of this folder to the root of your server, e.g. /var/www/html.
    
    Then, execute movie_sc.sql and populate.sql subsequently to create the MySQL database for the movie website.

    Finally, open a terminal and type in the command “ifconfig” to see the IP address of your server. Find another computer, and type in the above address, you should be able to browse the movie website now.

Part B) the folder Movie_Recommendation_Engine contains a graph database based movie recommendation engine. Detailed discussion could be found in M. A. Rodriguez’s blog, http://markorodriguez.com/2011/09/22/a-graph-based-movie-recommender-engine/. The gremlin_commands.txt contains all the commands that are needed to build a movie recommendation engine. 

    To run this command, you need to read the above blog, and install gremlin-1.3 on your computer. Besides that, you also need to download the MovieLens 1M dataset from the following link http://grouplens.org/datasets/movielens/.

    In addition, we also include a java log file analysis tool that can be used to process your website’s user log file and generate the user preferences for you. 
    
Objective: 
----------
Develop our own online movie shopping website/Implement movie review sentiment analysis to improve user experience. 

Innovations: 
------------
1. Using PHP/HTML language to build a online movie website. 

2. Using MySQL to manage the movie and customer information. 

3. Implementing the review sentiment analysis system with very high accuracy. 

4. Building the movie dataset which contains movie basic information along with associated critics reviews. 

Importance: 
-----------
1. Improve the user experience when they are browsing the movie website, saving their time spending on reading reviews. 

2. Provide a method to implement sentiment analysis with high accuracy, which not only can be performed for movie reviews, but also for other kinds of text processing. 

Dataset:
--------
MovieLens 1M dataset - including 1 million ratings from 6000 users on 4000 movies. 
http://grouplens.org/datasets/movielens/ 

Large Movie Review Dataset v1.0 - including 50,000 reviews along with their associated sentiment labels. http://ai.stanford.edu/~amaas/data/sentiment/ 

Rotten Tomatoes Movie Reviews Dataset - including 15,000 unlabeled reviews from critics for 2000 movies. Built by ourselves. 

Language:
---------
Languages - Python/PHP/MySQL/HTML/. Platforms - Spark/Linux/Apache/MySQL. 

Analytics: 
----------
1. Movie review sentiment analysis. 

2. Natural language processing. 

3. Naive Bayes classifier. 

4. Feature extraction by detecting bigrams.
