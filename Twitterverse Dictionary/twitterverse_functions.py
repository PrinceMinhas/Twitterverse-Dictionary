"""
Type descriptions of Twitterverse and Query dictionaries
(for use in docstrings)

Twitterverse dictionary:  dict of {str: dict of {str: object}}
    - each key is a username (a str)
    - each value is a dict of {str: object} with items as follows:
        - key "name", value represents a user's name (a str)
        - key "location", value represents a user's location (a str)
        - key "web", value represents a user's website (a str)
        - key "bio", value represents a user's bio (a str)
        - key "following", value represents all the usernames of users this 
          user is following (a list of str)
       
Query dictionary: dict of {str: dict of {str: object}}
   - key "search", value represents a search specification dictionary
   - key "filter", value represents a filter specification dictionary
   - key "present", value represents a presentation specification dictionary

Search specification dictionary: dict of {str: object}
   - key "username", value represents the username to begin search at (a str)
   - key "operations", value represents the operations to perform (a list of str)

Filter specification dictionary: dict of {str: str}
   - key "following" might exist, value represents a username (a str)
   - key "follower" might exist, value represents a username (a str)
   - key "name-includes" might exist, value represents a str to match (a case-insensitive match)
   - key "location-includes" might exist, value represents a str to match (a case-insensitive match)

Presentation specification dictionary: dict of {str: str}
   - key "sort-by", value represents how to sort results (a str)
   - key "format", value represents how to format results (a str)
   
"""

# Write your Twitterverse functions here

def process_username (data_file, username, twitterverse_dict):
    """ (file open for reading, str, dict of {str: dict of {str: object}}) -> \
    NoneType
    
    When given the username of the next person in the data_file, add the 
    username and additional information regarding that person to the 
    twitterverse_dict.
    """
    
    twitterverse_dict[username] = {}
    twitterverse_dict[username]["name"] = data_file.readline().strip()
    twitterverse_dict[username]["location"] = data_file.readline().strip()
    twitterverse_dict[username]["web"] = data_file.readline().strip()
    bio = ""
    line = data_file.readline().strip()
    while (line != "ENDBIO"):
        bio = bio + (line + "\n")
        line = data_file.readline().strip()
    twitterverse_dict[username]["bio"] = bio[0:-1]
    twitterverse_dict[username]["following"] = []
    line = data_file.readline().strip()
    while (line != "END"):
        twitterverse_dict[username]["following"].append(line) 
        line = data_file.readline().strip()

def process_data (data_file):
    """ (file open for reading) -> dict of {str: dict of {str: object}}
    
    Return the completed twitterverse dictionary by going through the entire
    data_file and adding all the information associated with each individual 
    one at a time.
    """
    
    twitterverse_dict_complete = {}
    line = data_file.readline().strip()
    while (line != ''):
        process_username (data_file, line, twitterverse_dict_complete)
        line = data_file.readline().strip()
    return (twitterverse_dict_complete)

def process_query (data_file):
    """ (file open for reading) -> dict of {str: dict of {str: object}}
    
    Go through the given query as represented in the data_file and return the
    various specifications of it.
    """
    data_file.readline()
    query_dict = {}
    query_dict["search"] = {}
    query_dict["search"]["username"] = data_file.readline().strip()
    query_dict["search"]["operations"] = []
    operations = data_file.readline().strip()
    while (operations != "FILTER"):
        query_dict["search"]["operations"].append(operations)
        operations = data_file.readline().strip()
    query_dict["filter"] = {}
    filter_by = data_file.readline().strip()
    filter_strings = []
    while (filter_by != "PRESENT"):
        filter_strings = filter_by.split()
        query_dict["filter"][filter_strings[0]] = filter_strings[-1]
        filter_by = data_file.readline().strip()
    query_dict["present"] = {}
    present_strings = data_file.readline().strip().split()
    query_dict["present"][present_strings[0]] = present_strings[-1]
    present_strings = data_file.readline().strip().split()
    query_dict["present"][present_strings[0]] = present_strings[-1]
    return (query_dict)

def all_followers (twitterverse_dict, given_username):
    """ (dict of {str: dict of {str: object}}, str) -> list of str
    
    Determine and then return all the followers of a given_username while given
    the twitterverse_dict as a database.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> all_followers (twitter_data, "b")
    ['a']
    >>> all_followers (twitter_data, "a")
    []
    """
    
    followers = []
    temp_followers = []
    for people in twitterverse_dict:
        temp_followers = twitterverse_dict[people]["following"]
        if (given_username in temp_followers):
            followers.append (people)
    return (followers)

def all_following (twitterverse_dict, given_username):
    """ (dict of {str: dict of {str: object}}, str) -> list of str
    
    Return all the usernames that a given_username is following
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> all_following (twitter_data, "a")
    ['b']
    >>> all_following (twitter_data, "b")
    []
    """
    
    return (twitterverse_dict[given_username]["following"])
    
    
def search_usernames (twitterverse_dict, usernames, operation):
    """ (dict of {str: dict of {str: object}}, list of str, str) \
    -> list of str
    
    Given the usernames perform the specific given operation on all of the 
    usernames based on the data in the twitterverse_dict.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':['c']}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':['c']}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':['b']}}
    >>> search_usernames (twitter_data, ['a', 'b', 'c'], "following")
    ['c', 'c', 'b']
    >>> search_usernames (twitter_data, ['a'], "followers")
    []
    """
    
    modified_list = []
    followers_or_following = []
    if (operation == "following"):
        for names in usernames:
            followers_or_following = all_following (twitterverse_dict, names)
            modified_list.extend (followers_or_following)
    elif (operation == "followers"):
        for names in usernames:
            followers_or_following = all_followers (twitterverse_dict, names)
            modified_list.extend (followers_or_following)
    return (modified_list)

def remove_dups (given_list):
    """ (list of str) -> list of str
    
    Go through all the elements of the given_list and return only single \
    instances of all the elements (disregarding duplicates)
    
    >>> remove_dups (['a', 'b', 'c'])
    ['a', 'b', 'c']
    >>> remove_dups (['a', 'b', 'b'])
    ['a', 'b']
    """
    
    removed_dups = []
    for items in given_list:
        if items not in removed_dups:
            removed_dups.append (items)
    return removed_dups
    
def get_search_results (twitterverse_dict, search_spec_dict):
    """ (dict of {str: dict of {str: object}}, dict of {str: object}) -> \
    list of str
    
    To obtain the initial username and the operations from the search_spec_dict\
    and return the usernames that result from conducting the operations on the \
    initial usernmaes based on the information in the twitterverse_dict.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':['c']}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':['c']}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':['b']}}
    >>> get_search_results (twitter_data, \
    {"username":"a", "operations":["followers", "following"]})
    []
    >>> get_search_results (twitter_data, \
    {"username":"a", "operations":[]})
    ['a']
    """
    
    searched_list = []
    searched_list.append (search_spec_dict["username"])
    operations = search_spec_dict["operations"]
    for ops in operations:
        searched_list = search_usernames (twitterverse_dict, searched_list, ops)
        searched_list = remove_dups (searched_list)
    return (searched_list)
            

def filter_usernames (twitterverse_dict, given_usernames, operation, \
                      filter_spec_dict):
    """ (dict of {str: dict of {str: object}}, list of str, str, \
    dict of {str: str}) -> list of str
    
    Given the value to filter by from the filter_spec_dict and the operation,
    return the given_usernames after filtering them using the data in the
    twitterverse_dict.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> filter_usernames (twitter_data, ['a','b','c'], "name-includes", \
    {"name-includes":"e"})
    ['a', 'b']
    >>> filter_usernames (twitter_data, ['a','b','c'], "following", \
    {"following":"d"})
    []
    """
    
    value = filter_spec_dict[operation]
    changed_list = []
    if (operation == "name-includes"):
        for names in given_usernames:
            if (value.lower() in twitterverse_dict[names]["name"].lower()):
                changed_list.append(names)
    elif (operation == "location-includes"):
        for names in given_usernames:
            if (value.lower() in twitterverse_dict[names]["location"].lower()):
                changed_list.append(names)
    elif (operation == "following"):
        for names in given_usernames:
            if (value in all_following (twitterverse_dict, names)):
                changed_list.append(names)
    elif (operation == "follower"):
        for names in given_usernames:
            if (value in all_followers (twitterverse_dict, names)):
                changed_list.append(names)
    return (changed_list)
    
    
    
def get_filter_results (twitterverse_dict, usernames, filter_spec_dict):
    """ (dict of {str: dict of {str: object}}, list of str, \
    dict of {str: str}) -> list of str
    
    To filter the usernames with respect to the values in the filter_spec_dict,\
    based on the data in the twitterverse_dict.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':['a']}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':['b']}}
    >>> get_filter_results (twitter_data, ['a','b','c'], \
    {"name-includes":"e", "following":"b"})
    ['a']
    >>> get_filter_results (twitter_data, ['a','b','c'], {})
    ['a', 'b', 'c']
    """
    
    all_usernames = usernames[:]
    operation = list(filter_spec_dict.keys())
    for operations in operation:
        all_usernames = filter_usernames (twitterverse_dict, all_usernames, \
                                       operations, filter_spec_dict)
    return (all_usernames)
 
def format_long (twitterverse_dict, username):
    """ (dict of {str: dict of {str: object}}, str) -> str
    
    Retern the specific information that is associated with the given usernamne,
    that can be obtained from the twitterverse_dict.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> format_long (twitter_data, 'a')
    '----------\\na\\nname: Zed\\nlocation: \\nwebsite: \\nbio:\\n\\nfollowing: []\\n'
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'Toronto, Ontario', 'web':'www.Zed.com', \
    'bio':'I love to meet new people!', 'following':[]}}
    >>> format_long (twitter_data, 'a')
    '----------\\na\\nname: Zed\\nlocation: Toronto, Ontario\\nwebsite: www.Zed.com\\nbio:\\nI love to meet new people!\\nfollowing: []\\n'
    """
    
    single_user_info = "----------\n"
    single_user_info = single_user_info + username + "\n"
    single_user_info = single_user_info + "name: " + \
        twitterverse_dict[username]["name"] + "\n"
    single_user_info = single_user_info + "location: " + \
        twitterverse_dict[username]["location"] + "\n"
    single_user_info = single_user_info + "website: " + \
        twitterverse_dict[username]["web"] + "\n"
    single_user_info = single_user_info + "bio:\n"
    single_user_info = single_user_info + twitterverse_dict[username]["bio"] \
        + "\n"
    single_user_info = single_user_info + "following: " + "[" 
    people_following = twitterverse_dict[username]["following"]
    if (len (people_following) != 0):
        for names in people_following:
            if (names == people_following[-1]):
                single_user_info = single_user_info + "\'" + names + "\'" + "]"\
                    + "\n"
            else:
                single_user_info = single_user_info + "\'" + names + "\'" + ", "
    else:
        single_user_info = single_user_info + "]" + "\n"
    return (single_user_info)

def sort_by (twitterverse_dict, usernames, present_spec_dict):
    """ (dict of {str: dict of {str: object}}, list of str, dict of {str: str})\
    -> NoneType
    
    Sort the usernames with respect to the factor represented in the 
    present_spec_dict, based on the data in the twitterverse_dict.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> result_list = ['a', 'b', 'c']
    >>> sort_by (twitter_data, result_list, \
    {'sort-by':'username','format':'long'})
    >>> result_list
    ['a', 'b', 'c']
    >>> sort_by (twitter_data, result_list, \
    {'sort-by':'name', 'format':'long'})
    >>> result_list
    ['b', 'a', 'c']
    """
    
    if (present_spec_dict["sort-by"] == "username"):
        tweet_sort (twitterverse_dict, usernames, username_first)
    elif (present_spec_dict["sort-by"] == "name"):
        tweet_sort (twitterverse_dict, usernames, name_first)
    elif (present_spec_dict["sort-by"] == "popularity"):
        tweet_sort (twitterverse_dict, usernames, more_popular)
    

def format_short (usernames):
    formatted_result = '['
    if (len != 0):
        for names in usernames:
            if (names == usernames[-1]):
                formatted_result = formatted_result + "\'" + names + "\'" + "]"
            else:
                formatted_result = formatted_result + "\'" + names + "\'" + ", "            
    else:
        formatted_result = formatted_result + ']'
    return (formatted_result)
        
def get_present_string (twitterverse_dict, usernames, present_spec_dict):
    """ (dict of {str: dict of {str: object}}, list of str, dict of {str: str})\
    -> str
    
    Return the usernames entirely formatted with respect to the contents in the 
    present_spec_dict, based on the data in the twitterverse_dict
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> usernames = ['a']
    >>> get_present_string (twitter_data, [], \
    {'sort-by':'username', 'format':'long'})
    '----------\\n----------'
    >>> get_present_string (twitter_data, usernames, \
    {'sort-by':'username', 'format':'short'})
    ['a']\n
    """
    
    formatted_result = ""
    all_usernames = usernames[:]
    if (len (all_usernames) == 0):
        formatted_result = "----------\n----------"
    else:
        sort_by (twitterverse_dict, all_usernames, present_spec_dict)
        
        if (present_spec_dict["format"] == "short"):
            for names in all_usernames:
                formatted_result = format_short (all_usernames)
        elif (present_spec_dict["format"] == "long"):
            for names in all_usernames:
                formatted_result = formatted_result + \
                format_long (twitterverse_dict, names)
                if (names == all_usernames[-1]):
                    formatted_result = formatted_result + "----------" + "\n"
    return (formatted_result)
    
    
# --- Sorting Helper Functions ---
def tweet_sort(twitter_data, results, cmp):
    """ (Twitterverse dictionary, list of str, function) -> NoneType
    
    Sort the results list using the comparison function cmp and the data in 
    twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> result_list = ['c', 'a', 'b']
    >>> tweet_sort(twitter_data, result_list, username_first)
    >>> result_list
    ['a', 'b', 'c']
    >>> tweet_sort(twitter_data, result_list, name_first)
    >>> result_list
    ['b', 'a', 'c']
    """
    
    # Insertion sort
    for i in range(1, len(results)):
        current = results[i]
        position = i
        while position > 0 and cmp(twitter_data, results[position - 1], current) > 0:
            results[position] = results[position - 1]
            position = position - 1 
        results[position] = current 
            
def more_popular(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return -1 if user a has more followers than user b, 1 if fewer followers, 
    and the result of sorting by username if they have the same, based on the 
    data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> more_popular(twitter_data, 'a', 'b')
    1
    >>> more_popular(twitter_data, 'a', 'c')
    -1
    """
    
    a_popularity = len(all_followers(twitter_data, a)) 
    b_popularity = len(all_followers(twitter_data, b))
    if a_popularity > b_popularity:
        return -1
    if a_popularity < b_popularity:
        return 1
    return username_first(twitter_data, a, b)
    
def username_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return 1 if user a has a username that comes after user b's username 
    alphabetically, -1 if user a's username comes before user b's username, 
    and 0 if a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> username_first(twitter_data, 'c', 'b')
    1
    >>> username_first(twitter_data, 'a', 'b')
    -1
    """
    
    if a < b:
        return -1
    if a > b:
        return 1
    return 0

def name_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
        
    Return 1 if user a's name comes after user b's name alphabetically, 
    -1 if user a's name comes before user b's name, and the ordering of their
    usernames if there is a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> name_first(twitter_data, 'c', 'b')
    1
    >>> name_first(twitter_data, 'b', 'a')
    -1
    """
    
    a_name = twitter_data[a]["name"]
    b_name = twitter_data[b]["name"]
    if a_name < b_name:
        return -1
    if a_name > b_name:
        return 1
    return username_first(twitter_data, a, b)       

if __name__ == '__main__':
    import doctest
    doctest.testmod()