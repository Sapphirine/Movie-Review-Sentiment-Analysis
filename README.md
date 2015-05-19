# Movie-Review-Sentiment-Analysis

This document can help you use the following repository.
https://github.com/Sapphirine/Movie-Review-Sentiment-Analysis

Part A) the folder contains a well-built online movie website.  

    To run this online movie website, you need to get an access to a LAMP server. LAMP stands for Linux, Apache, MySQL, PHP. 

    First, copy the content of this folder to the root of your server, e.g. /var/www/html.
    
    Then, execute movie_sc.sql and populate.sql subsequently to create the MySQL database for the movie website.

    Finally, open a terminal and type in the command “ifconfig” to see the IP address of your server. Find another computer, and type in the above address, you should be able to browse the movie website now.

Part B) the folder contains python files and datasets related to sentiment analysis of reviews. 

    critics.csv 
    
    This is the Rotten Tomatoes reviews dataset. We use this dataset to predict sentiment labels of each review. 
    
    aclImdb
    
    This is the Large Movie Review Dataset v1.0 from http://ai.stanford.edu/~amaas/data/sentiment/, which we use as training dataset and test dataset. There is one well-written README file in the folder describing the dataset.
    
    Sentiment Analysis
    
    Including all the files doing sentiment analysis of reviews. To run the .py files, first you need to install nltk toolkit, scikit-learn toolkit and tabulate package. You can try
    
    $ pip install <package-name>
    
    or install packages from official website.

    build_csv.py

    This is the python script to fetch critics movie reviews from Rotten Tomatoes API into “critics.csv”, which is the dataset for the online movie website. To run this file, first you must have a Rotten Tomatoes API key, please go to http://developer.rottentomatoes.com/member/register to register one. After you get your API key, fill it in “api_key” row to replace ‘YOUR KEY HERE’ in the code. Besides, you need to install python libraries numpy, scikit-learn, json, pandas, matplotlib, requests.

    Then run csvToTxt.py to extract the Rotten Tomatoes reviews data. Notice that you need to change all the file path to your local path. For example:
    
    change dir_name = '/Users/tianhan/Documents/ColumbiaU/Spring15/Adv_Big_Data_Analytics/Project/Reviews'
    
    to dir_name = '/Users/<your-username>/.../Reviews'
    
    Then you can run evaluation.py to see the evaluation results of different algorithms, run classifyUpdateLabelsInDataset.py to update the sentiment labels of reviews in Rotten Tomatoes reviews dataset, or run classifySingleReview.py to classify a single review.
    
    
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
