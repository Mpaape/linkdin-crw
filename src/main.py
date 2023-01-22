import json 

from crawler import LinkBot	
from people import Profile
	
# bot instance
mr_bot = LinkBot()
#login
mr_bot.profile_auth()
 

profile_list = [
	"https://www.linkedin.com/in/dianechiang/",
	"https://www.linkedin.com/in/carlos-fernandes91/",
	"https://www.linkedin.com/in/luizhammes/"
]
url = profile_list[2]

#Profile Class init
profile = Profile(url)
profile.soup = mr_bot.get_soup(url)
profile.get_all_profile()
dictionary = profile.to_dict()
json_object = json.dumps(dictionary) 




with open("..\\data/profile.json", "w" ,encoding='utf8') as outfile:
    json.dump(dictionary, outfile,indent=4,ensure_ascii=False)
