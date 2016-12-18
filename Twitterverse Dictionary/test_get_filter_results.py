import unittest
import twitterverse_functions as tf


class TestGetFilterResults(unittest.TestCase):
    '''Your unittests here'''
    def test_empty_element_parameters (self):
        """ Test get_filter_results with all empty parameters \
        (twitterverse_dict, usernames, and filter_spec_dict)."""
        
        expected_list = []
        obtained_list = tf.get_filter_results({}, [], {})
        self.assertEqual (expected_list, obtained_list)
        
    def test_no_filter_value (self):
        """ Test get_filter_results with multiple twitterverse_dict and \
        usernames entries, but empty filter_spec_dict."""
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a', 'b', 'c']
        obtained_list = tf.get_filter_results(twitter_data, usernames, {})
        self.assertEqual (expected_list, obtained_list) 
    
    def test_empty_usernames (self):
        """ Test get_filter_results with entries in the twitterverse_dict and \
        the filter_spec_dict but no usernames entry."""
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = []
        expected_list = []
        filter_spec_dict = {"follower":"a", "following":"b"}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)
        self.assertEqual (expected_list, obtained_list)  
    
    def test_lower_single_char_name_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "name-includes" filter with a single \
        character value that can only be a lowercase letter."""  
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"name-includes":'z'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)
        self.assertEqual (expected_list, obtained_list) 
    
    def test_upper_single_char_name_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "name-includes" filter with a single \
        character value that can only be an uppercase letter."""         
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"name-includes":'Z'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)
        self.assertEqual (expected_list, obtained_list) 
        
        
    def test_lower_multiple_char_name_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "name-includes" filter with a multiple \
        character value that has only lowercase letters."""      
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"name-includes":'zed'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict) 
        self.assertEqual (expected_list, obtained_list) 
    
    def test_capital_multiple_char_name_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "name-includes" filter with a multiple \
        character value that has only uppercase letters."""          
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"name-includes":'ZED'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)  
        self.assertEqual (expected_list, obtained_list) 
    
    def test_mix_multiple_char_name_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "name-includes" filter with a multiple \
        character value that has both uppercase and lowercase letters."""           
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"name-includes":'zED'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)  
        self.assertEqual (expected_list, obtained_list) 
        
    def test_non_existent_char_name_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "name-includes" filter with a multiple \
        character value that does not exist."""          
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = []
        filter_spec_dict = {"name-includes":'zedd'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)
        self.assertEqual (expected_list, obtained_list) 
    
    def test_lower_single_char_location_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "location-includes" filter with a single \
        character value that can only be a lowercase letter."""  
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"location-includes":'u'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)
        
    def test_upper_single_char_location_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "location-includes" filter with a single \
        character value that can only be an uppercase letter."""         
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"location-includes":'U'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)        
        self.assertEqual (expected_list, obtained_list)     
        
    def test_lower_multiple_char_location_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "location-includes" filter with a multiple \
        character value that has only lowercase letters."""          
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"location-includes":'usa'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict) 
        self.assertEqual (expected_list, obtained_list) 
    
    def test_capital_multiple_char_location_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "location-includes" filter with a multiple \
        character value that has only uppercase letters."""  
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"location-includes":'USA'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict) 
        self.assertEqual (expected_list, obtained_list) 
    
    def test_mix_multiple_char_location_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "location-includes" filter with a multiple \
        character value that has both uppercase and lowercase letters."""  
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"location-includes":'uSa'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)  
        self.assertEqual (expected_list, obtained_list) 
        
    def test_non_existent_char_location_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "location-includes" filter with a multiple \
        character value that does not exist."""        
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':[]}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':[]}}    
        usernames = ['a', 'b', 'c']
        expected_list = []
        filter_spec_dict = {"location-includes":'usAa'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                              filter_spec_dict)    
        self.assertEqual (expected_list, obtained_list) 
    
    def test_following_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "following" filter with a single username \
        value."""  
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':['b']}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':['c']}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':['a']}}          
        usernames = ['a', 'b', 'c']
        expected_list = ['a'] 
        filter_spec_dict = {"following":'b'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                             filter_spec_dict) 
        self.assertEqual (expected_list, obtained_list) 
    
    def test_non_existent_following_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "following" filter with a username that does \
        not exist."""         
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':['c']}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':['a']}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':['b']}}          
        usernames = ['a', 'b', 'c']
        expected_list = [] 
        filter_spec_dict = {"following":'d'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                             filter_spec_dict)
        self.assertEqual (expected_list, obtained_list) 
    
    def test_follower_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "follower" filter with a single username \
        value."""         
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':['c']}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':['a']}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':['b']}}  
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"follower":'b'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                                     filter_spec_dict) 
        self.assertEqual (expected_list, obtained_list) 
    
    def test_non_existent_follower_value (self):
        """ Test get_filter_results with entries for the twitterverse_dict and \
        usernames, but only a "follower" filter with a username that does not \
        exist."""         
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':['c']}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':['a']}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':['b']}}  
        usernames = ['a', 'b', 'c']
        expected_list = []
        filter_spec_dict = {"follower":'d'}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                                     filter_spec_dict) 
        self.assertEqual (expected_list, obtained_list)              
    
    def test_multiple_usernames_multiple_filter_values (self):
        """ Test get_filter_results with multiple entries for the \
        twitterverse_dict and usernames, and the filter_spec_dict."""          
        
        twitter_data = {\
            'a':{'name':'Zed', 'location':'usa', 'web':'', 'bio':'', \
                 'following':['c']}, 
            'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', \
                 'following':['a']}, 
            'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', \
                 'following':['b', 'a']}}  
        usernames = ['a', 'b', 'c']
        expected_list = ['a']
        filter_spec_dict = {"following":'c', "follower":"b", \
                            "name-includes":"e"}
        obtained_list = tf.get_filter_results(twitter_data, usernames, \
                                                     filter_spec_dict) 
        self.assertEqual (expected_list, obtained_list)                
    


if __name__ == '__main__':
    unittest.main(exit=False)
