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





def build_scores(sent_file_name):
    sent_file = open(sent_file_name)
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    sent_file.close()
    return scores

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

def score_tweets(tweets, scores):
    """(str, dict of {str:int}) -> list of int
    Opens the specified tweet_file_name and uses the scores dictionary
    to build a score for each tweet. Returns a list containing the score
    for each tweet, in the order they appeared in the tweet file.
    """
    returnVal = []
    for tweet in tweets:
        returnVal.append(score_tweet(tweet, scores))
    return returnVal

def score_tweet(tweet, scores):
    """(dict, dict of (int, dict of (str, int)) -> int
    Given a tweet and a dict of word scores, determine the
    score for the tweet as a sum of all scores for the terms in that tweet.
    """
    if ResultKeys.text not in tweet.keys():
        return (tweet, 0)
    text = tweet[ResultKeys.text]
    words = text.split()
    score = 0
    # First check the singletons
    for word in words:
        if word in scores[1]:
            score += scores[1][word]
    # Next check for multiples
    for i in scores.keys():
        if i == 1:
            continue
        for key in scores[i].keys():
            if key in text:
                score += scores[i][key]
    return (tweet, score)

def split_scores(scores):
    """(dict of (str, int)) -> dict of (int, dict of (str, int))
    Given a score dict, builds a new dict where each key is a positive int x, and
    each value is a dict of scores all of whose keys have exactly x words.
    """
    returnVal = {}
    for key in scores.keys():
        key_len = len(str(key).split())
        if key_len not in returnVal.keys():
            returnVal[key_len] = {}
        returnVal[key_len][key] = scores[key]
    return returnVal

count = "count"
sum = "avg"
avg_score = "score"
def score_terms(tweet_scores):
    score_calcs = {}
    for (tweet, score) in tweet_scores:
        if ResultKeys.text not in tweet.keys():
            continue
        terms = tweet[ResultKeys.text]
        terms = terms.split()
        for term in terms:
            if term not in score_calcs.keys():
                score_calcs[term] = {count:0.0, sum:0.0, avg_score:0.0}
            score_calcs[term][count] += 1.0
            score_calcs[term][sum] += float(score)
            score_calcs[term][avg_score] = score_calcs[term][sum] / score_calcs[term][count]
    just_scores = {}
    for term in score_calcs.keys():
        just_scores[term] = score_calcs[term][avg_score]
    return just_scores



def main():
    sent_file_name = get_argv(1, "AFINN-111.txt")
    tweet_file_name = get_argv(2, "tweets.txt")
    scores = build_scores(sent_file_name)
    scores = split_scores(scores)

    tweets = get_tweets_from_file(tweet_file_name)

    tweet_scores = score_tweets(tweets, scores)
    term_scores = score_terms(tweet_scores)
    sorted_terms = sorted(term_scores, reverse=True, key=term_scores.get)
    #for term in sorted_terms:
        #print term, term_scores[term]




if __name__ == '__main__':
    main()
