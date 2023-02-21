from instabot import Bot
bot = Bot()
bot.login(username = "amityadav1214" , password = "*************")    #Your Username and passsword should be correct
bot.follow("wscubetechindia")    #Follows the User as mentioned
followers = get_user_followers("amityadav1214")    #Gets the list of followers of the mentioned User
for foler in followers:
    print(bot.get_user_info(foler))
following = get_user_following("amityadav1214")    #Gets the list of following by the mentioned User
for foling in following:
    print(bot.get_user_info(foling))
