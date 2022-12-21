import json

file_followers = "followers.json"
file_following = "following.json"

data_followers = open(file_followers)
data_following = open(file_following)

following = json.load(data_following)
followers = json.load(data_followers)


following_list = set()
follower_list = set()

#parse through following.json to get following username
for relationships_following in following['relationships_following']:
    for data in relationships_following['string_list_data']:
         following_username = data['value']
         following_list.add(following_username)


#parse through following.json to get followers username
for relationships_followers in followers['relationships_followers']:
    for data2 in relationships_followers['string_list_data']:
        follower_username = data2['value']
        follower_list.add(follower_username)

length = len(following_list.difference(follower_list))
print(f'The number of users that do not follow you back: {length}')
print(*following_list.difference(follower_list), sep = '\n')

data_followers.close()
data_following.close()




