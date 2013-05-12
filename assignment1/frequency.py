#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sadavoya
#
# Created:     11/05/2013
# Copyright:   (c) sadavoya 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
import json

class TweetKeys:
    next_page = "next_page"
    completed_in = "completed_in"
    max_id_str = "max_id_str"
    since_id_str = "since_id_str"
    refresh_url = "refresh_url"
    results = "results"
    since_id = "since_id"
    results_per_page = "results_per_page"
    query = "query"
    max_id = "max_id"
    page = "page"

# result keys
class ResultKeys:
    iso_language_code = "iso_language_code"
    to_user_name = "to_user_name"
    from_user_id_str = "from_user_id_str"
    text = "text"
    from_user_name = "from_user_name"
    in_reply_to_status_id = "in_reply_to_status_id"
    profile_image_url = "profile_image_url"
    id = "id"
    created_at = "created_at"
    source = "source"
    in_reply_to_status_id_str = "in_reply_to_status_id_str"
    to_user = "to_user"
    id_str = "id_str"
    to_user_id = "to_user_id"
    from_user = "from_user"
    from_user_id = "from_user_id"
    to_user_id_str = "to_user_id_str"
    geo = "geo"
    profile_image_url_https = "profile_image_url_https"
    metadata = "metadata"


#print scores.items() # Print every (term, score) pair in the dictionary

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def file_stats(file_name):
    file = open(file_name)
    lines(file)
    file.close()

def print_file_stats(filenames):
    hw()
    for filename in filenames:
        file_stats(filename)

def get_argv(arg, default):
    returnVal = default
    if len(sys.argv) > arg:
        returnVal = sys.argv[arg]
    return returnVal

def get_tweets_from_file(tweet_file_name):
    tweet_file = open(tweet_file_name)
    tweets = []
    line = tweet_file.readline().strip()
    atEOF = line == ""
    while not atEOF:
        try:
            tweets.append(json.loads(line))
        except Exception as e:
            print e
        line = tweet_file.readline().strip()
        atEOF = line == ""
    tweet_file.close()
    return tweets

def get_hist(tweet_file_name):
    tweets = get_tweets_from_file(tweet_file_name)
    hist = {}
    for tweet in tweets:
        if ResultKeys.text not in tweet.keys():
            continue
        text = tweet[ResultKeys.text]
        words = text.split()
        for word in words:
            if word not in hist.keys():
                hist[word] = 0
            hist[word] += 1
    return hist

def calculate_frequency(hist):
    returnVal = {}
    total_occurences = 0
    for key in hist.keys():
        total_occurences += hist[key]
    total_occurences = float(total_occurences)
    for key in hist.keys():
        returnVal[key] = float(hist[key]) / total_occurences
    return returnVal

def main():
    tweet_file_name = get_argv(1, "tweets.txt")
    #print_file_stats([tweet_file_name])

    hist = get_hist(tweet_file_name)

    freq = calculate_frequency(hist)
    for key in freq.keys():
        print key.encode('utf-8'), freq[key]

if __name__ == '__main__':
    main()
