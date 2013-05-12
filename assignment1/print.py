#-------------------------------------------------------------------------------
# Name:        problem 0
# Purpose:
#
# Author:      sadavoya
#
# Created:     10/05/2013
# Copyright:   (c) sadavoya 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
import urllib
import json


qry_format = "http://search.twitter.com/search.json?q={0}&page={1}"
#tweets keys
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

def print_useful_keys(tweets):
    """Print the keys used in the dictionary returned by twitter."""
    print "Tweets Keys"
    print_keys(tweets)
    print
    print "Result Keys"
    result_keys = {}
    for tweet in tweets[TweetKeys.results]:
        for key in tweet.keys():
            if key not in result_keys.keys():
                result_keys[key] = None
    print_keys(result_keys)
    print

def print_keys(d):
    """Given a dictionary of tweets, prints the keys of that dictionary"""
    keys = d.keys()
    keys.sort()
    for key in keys:
        print str(key) + ' = "' + str(key) + '"'

def get_tweets(url):
    response = urllib.urlopen(url)
    return json.load(response)

def qry(qry, lang=None, pages=1):
    for page in range(0, pages):
        url = qry_format.format(qry, page + 1)
        print url
        print "Retrieving...",
        tweets = get_tweets(url)
        print "Done."
        print "Page " + str(tweets[TweetKeys.page])
        for result in tweets[TweetKeys.results]:
            if  lang == None \
                or result[ResultKeys.iso_language_code] == "en":
                    print result[ResultKeys.text].encode('utf-8')
        print

def main(query=None, language=None, pages=1):
    if query == None:
        query = "microsoft"
    qry(query, language, pages)

if __name__ == '__main__':
    error = False
    try:
        query = language = None
        pages = 1
        args = sys.argv
        if len(args) > 1:
            query = str(sys.argv[1])
            print query
            if ["\?", "-?", "-h", "/h"].__contains__(query):
                raise Exception("Help")
        if len(args) > 2:
            language = str(sys.argv[2])
        if len(args) > 3:
            pages = int(sys.argv[3])
        if len(args) > 4:
            error = True
            raise Exceptions("Argument Error")
        main(query, language, pages)
    except Exception as e:
        print e
        error = True
    if error:
        lines = ["Usage: python.exe print.py { /? | -? | /h | -h }",
            " or ",
            "python.exe print.py [query] [language] [pages]",
            "",
            "   /?, -?, /h, -h: Print this usage message",
            "",
            "   query: (optional) The query to send to twitter (default 'microsoft')",
            "   language: (optional) The language of the results to print (default None)",
            "   pages: (optional) The number of results pages to print (default 1)"]
        for line in lines:
            print line
    print_useful_keys(get_tweets(qry_format.format("microsoft", 1)))
