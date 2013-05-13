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
        class Place:
            attributes = "attributes"
            bounding_box = "bounding_box"
            country = "country"
            country_code = "country_code"
            full_name = "full_name"
            id = "id"
            name = "name"
            place_type = "place_type"
            url = "url"
        class User:
            contributors_enabled = "contributors_enabled"
            created_at = "created_at"
            default_profile = "default_profile"
            default_profile_image = "default_profile_image"
            description = "description"
            favourites_count = "favourites_count"
            follow_request_sent = "follow_request_sent"
            followers_count = "followers_count"
            following = "following"
            friends_count = "friends_count"
            geo_enabled = "geo_enabled"
            id = "id"
            id_str = "id_str"
            is_translator = "is_translator"
            lang = "lang"
            listed_count = "listed_count"
            location = "location"
            name = "name"
            notifications = "notifications"
            profile_background_color = "profile_background_color"
            profile_background_image_url = "profile_background_image_url"
            profile_background_image_url_https = "profile_background_image_url_https"
            profile_background_tile = "profile_background_tile"
            profile_banner_url = "profile_banner_url"
            profile_image_url = "profile_image_url"
            profile_image_url_https = "profile_image_url_https"
            profile_link_color = "profile_link_color"
            profile_sidebar_border_color = "profile_sidebar_border_color"
            profile_sidebar_fill_color = "profile_sidebar_fill_color"
            profile_text_color = "profile_text_color"
            profile_use_background_image = "profile_use_background_image"
            protected = "protected"
            screen_name = "screen_name"
            statuses_count = "statuses_count"
            time_zone = "time_zone"
            url = "url"
            utc_offset = "utc_offset"
            verified = "verified"

states = {}
def init_states():
    states["AK"] = (-152.2683,61.385)
    states["AL"] = (-86.8073,32.799)
    states["AR"] = (-92.3809,34.9513)
    states["AS"] = (-170.7197,14.2417)
    states["AZ"] = (-111.3877,33.7712)
    states["CA"] = (-119.7462,36.17)
    states["CO"] = (-105.3272,39.0646)
    states["CT"] = (-72.7622,41.5834)
    states["DC"] = (-77.0262,38.8964)
    states["DE"] = (-75.5148,39.3498)
    states["FL"] = (-81.717,27.8333)
    states["GA"] = (-83.6487,32.9866)
    states["HI"] = (-157.5311,21.1098)
    states["IA"] = (-93.214,42.0046)
    states["ID"] = (-114.5103,44.2394)
    states["IL"] = (-89.0022,40.3363)
    states["IN"] = (-86.2604,39.8647)
    states["KS"] = (-96.8005,38.5111)
    states["KY"] = (-84.6514,37.669)
    states["LA"] = (-91.8749,31.1801)
    states["MA"] = (-71.5314,42.2373)
    states["MD"] = (-76.7902,39.0724)
    states["ME"] = (-69.3977,44.6074)
    states["MI"] = (-84.5603,43.3504)
    states["MN"] = (-93.9196,45.7326)
    states["MO"] = (-92.302,38.4623)
    states["MP"] = (145.5505,14.8058)
    states["MS"] = (-89.6812,32.7673)
    states["MT"] = (-110.3261,46.9048)
    states["NC"] = (-79.8431,35.6411)
    states["ND"] = (-99.793,47.5362)
    states["NE"] = (-98.2883,41.1289)
    states["NH"] = (-71.5653,43.4108)
    states["NJ"] = (-74.5089,40.314)
    states["NM"] = (-106.2371,34.8375)
    states["NV"] = (-117.1219,38.4199)
    states["NY"] = (-74.9384,42.1497)
    states["OH"] = (-82.7755,40.3736)
    states["OK"] = (-96.9247,35.5376)
    states["OR"] = (-122.1269,44.5672)
    states["PA"] = (-77.264,40.5773)
    states["PR"] = (-66.335,18.2766)
    states["RI"] = (-71.5101,41.6772)
    states["SC"] = (-80.9066,33.8191)
    states["SD"] = (-99.4632,44.2853)
    states["TN"] = (-86.7489,35.7449)
    states["TX"] = (-97.6475,31.106)
    states["UT"] = (-111.8535,40.1135)
    states["VA"] = (-78.2057,37.768)
    states["VI"] = (-64.8199,18.0001)
    states["VT"] = (-72.7093,44.0407)
    states["WA"] = (-121.5708,47.3917)
    states["WI"] = (-89.6385,44.2563)
    states["WV"] = (-80.9696,38.468)
    states["WY"] = (-107.2085,42.7475)
init_states()

def get_keys(d):
    return d.keys()

def get_keys_of(dicts, f=get_keys):
    result_keys = {}
    for d in dicts:
        for key in f(d):
            if key not in result_keys:
                result_keys[key] = None
    result_keys = result_keys.keys()
    result_keys.sort()
    return result_keys

def print_useful_keys(tweets):
    """Print the keys used in the dictionary returned by twitter."""
    print "Tweets Keys"
    print_keys(tweets)
    print
    results = tweets[Tweet.Keys.results]
    print "Result Keys"
    result_keys = get_keys_of(results)
    print_keys_l(result_keys)
    print
    def get_key_func(key_name):
        def f(tweet):
            if key_name in tweet.keys():
                if type(tweet[key_name]) == type({}):
                    return tweet[key_name].keys()
                elif tweet[key_name] <> None:
                    pass #print "VALUE:", tweet[key_name]
            return []
        return f
    print "Coordinates keys"
    result_keys = get_keys_of(results, get_key_func(Tweet.Result.Keys.coordinates))
    print_keys_l(result_keys)
    print
    print "Place keys"
    result_keys = get_keys_of(results, get_key_func(Tweet.Result.Keys.place))
    print_keys_l(result_keys)
    print
    print "User keys"
    result_keys = get_keys_of(results, get_key_func(Tweet.Result.Keys.user))
    print_keys_l(result_keys)
    print
    users = []
    for result in results:
        if Tweet.Result.Keys.user in result \
            and result[Tweet.Result.Keys.user] <> None:
                users.append(result[Tweet.Result.Keys.user])
    print "Location keys"
    result_keys = get_keys_of(users, get_key_func(Tweet.Result.User.location))
    print_keys_l(result_keys)
    print

def print_keys(d):
    """Given a dictionary of tweets, prints the keys of that dictionary"""
    keys = d.keys()
    keys.sort()
    for key in keys:
        print str(key) + ' = "' + str(key) + '"'

def print_keys_l(l):
    l.sort()
    for key in l:
        print str(key) + ' = "' + str(key) + '"'


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
    tweet_scores = []
    for tweet in tweets:
        tweet_scores.append((tweet, score_tweet(tweet, scores)))
    return tweet_scores

def score_tweet(tweet, scores):
    if Tweet.Result.Keys.text not in tweet:
        return 0
    text = tweet[Tweet.Result.Keys.text]
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
    return score

def split_scores(scores):
    returnVal = {}
    for key in scores.keys():
        key_len = len(str(key).split())
        if key_len not in returnVal:
            returnVal[key_len] = {}
        returnVal[key_len][key] = scores[key]
    return returnVal



def get_happiest_state(tweet_scores):
    pass

def get_at_key(d, key):
    if key in d:
        return d[key]

def main():
    sent_file_name = get_argv(1, "AFINN-111.txt")
    tweet_file_name = get_argv(2, "tweets_5000.txt")
    scores = build_scores(sent_file_name)
    scores = split_scores(scores)


    tweets = get_tweets_from_file(tweet_file_name)
    tweet_scores = score_tweets(tweets, scores)
    #print_useful_keys(tweets)
    usable_tweets = []
    for (tweet, score) in tweet_scores:
        #coordinates = get_at_key(tweet, Tweet.Result.Keys.coordinates)
        place = get_at_key(tweet, Tweet.Result.Keys.place)
        #user = get_at_key(tweet, Tweet.Result.Keys.user)
        #user_location = None
        #if user <> None:
        #    user_location = get_at_key(user, Tweet.Result.User.location)
        #if coordinates <> None or place <> None or user_location <> None:
        if place <> None and place[Tweet.Result.Place.country_code].upper() == "US":
            #usable_tweets.append((tweet, coordinates, place, user_location))
            usable_tweets.append((tweet, place, score))
    #print len(usable_tweets)
    us_places = []
    happy_states = {}
    for (tweet, place, score) in usable_tweets:
        if Tweet.Result.Place.full_name in place and place[Tweet.Result.Place.full_name] <> None:
            state = place[Tweet.Result.Place.full_name][-2:]
            if state in states:
                if state not in happy_states:
                    happy_states[state] = 0
                happy_states[state] += score
    sortstates = sorted(happy_states, reverse=True, key=happy_states.get)
    #for state in sortstates:
    #    print state, happy_states[state]
    state = sortstates[0]
    print state, happy_states[state]

    #for (tweet, coordinates, place, user_location) in usable_tweets:
    #    if place <> None:
    #        if place[Tweet.Result.Place.country_code] == "US":
    #            us_places.append((tweet, coordinates, place, user_location))
    #            print place
    #print len(us_places)
    #us_places = []
    #for (tweet, coordinates, place, user_location) in usable_tweets:
    #    if place <> None:
    #        if place[Tweet.Result.Place.country_code] == "US":
    #            us_places.append((tweet, coordinates, place, user_location))
    #            print place
    #print len(us_places)


if __name__ == '__main__':
    main()
