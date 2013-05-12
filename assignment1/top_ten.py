import sys
import json

class Tweet:
    class Keys:
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
    class Result:
        class Keys:
            contributors = "contributors"
            coordinates = "coordinates"
            created_at = "created_at"
            delete = "delete"
            entities = "entities"
            favorite_count = "favorite_count"
            favorited = "favorited"
            filter_level = "filter_level"
            geo = "geo"
            id = "id"
            id_str = "id_str"
            in_reply_to_screen_name = "in_reply_to_screen_name"
            in_reply_to_status_id = "in_reply_to_status_id"
            in_reply_to_status_id_str = "in_reply_to_status_id_str"
            in_reply_to_user_id = "in_reply_to_user_id"
            in_reply_to_user_id_str = "in_reply_to_user_id_str"
            lang = "lang"
            place = "place"
            possibly_sensitive = "possibly_sensitive"
            retweet_count = "retweet_count"
            retweeted = "retweeted"
            retweeted_status = "retweeted_status"
            source = "source"
            text = "text"
            truncated = "truncated"
            user = "user"
        class Coordinates:
            coordinates = "coordinates"
            type = "type"
        class Entities:
            class Keys:
                hashtags = "hashtags"
            class HashTag:
                class Keys:
                    indices = "indices"
                    text = "text"

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

def get_at_key(d, key):
    if key in d.keys():
        return d[key]

def get_maxes(d):
    maxes = []
    maxkeys = []
    for i in range(10):
        max = None
        for key in d.keys():
            if key in maxkeys:
                continue
            if max == None or d[key] > d[max]:
                max = key
        maxes.append((max, d[max]))
        maxkeys.append(max)
    return maxes

def main():
    tweet_file_name = get_argv(1, "tweets_1000.txt")
    tweets = get_tweets_from_file(tweet_file_name)
    tags = {}
    for tweet in tweets:
        entities = get_at_key(tweet, Tweet.Result.Keys.entities)
        if entities <> None:
            hashtags = get_at_key(entities, Tweet.Result.Entities.Keys.hashtags)
            if hashtags <> None:
                #print hashtags
                for hashtag in hashtags:
                    if Tweet.Result.Entities.HashTag.Keys.text in hashtag.keys():
                        text = hashtag[Tweet.Result.Entities.HashTag.Keys.text]
                        if text not in tags.keys():
                            tags[text] = float(0)
                        tags[text] += float(1)
    tags = get_maxes(tags)
    i = 1
    for (key, count) in tags:
        print key, count
        i += 1

if __name__ == '__main__':
    main()
