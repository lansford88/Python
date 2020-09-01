#This would be to login into a special part of the website that would only be available to
#higher ranking guild members such as inventory and roster manipulations

class main_User:
    name = "Bob"
    email = "rp@gmail.com"
    password = "1234abc"

    def grabinfo(self):
        user_name =input("Enter your name please: ")
        user_email = input("Enter your email please: ")
        user_password = input("Enter your password please: ")
        if (user_email == self.email and user_password == self.password):
            print("Hey there, {}! Welcome back!".format(user_name))
        else:
            print("Are you sure you entered that right? Go ahead, try again")
                  
class guildee_probee(main_User):
    guild_title = "Probee"
    time_served = "3 Months or less"
    rank_Number = "9"

    def grabinfo(self):
        user_name =input("Enter your name please: ")
        user_password = input("Enter your password please: ")
        rank_Number = input("Please enter your Rank")
        if (user_name == self.name and rank_Number >= self.rank_Number):
            print("Hey man, welcome back to the fold!")
        else:
            print("We both know this is WAY over your paygrade!")

class guild_Master(main_User):
    guild_title = "GM"
    time_served = "Creator"
    special_code = "only one highlander"

    def grabinfo(self):
        user_name = input ("Enter your name please: ")
        user_password = input("Enter your password please: ")
        key_phrase = "only one highlander"
        if (user_name == self.name and user_password == self.password and key_phrase == self.special_code):
            print("Welcome back, the files are open!")
        else:
            print("Your in an area where you do not belong, this has been logged!")
        
if __name__ == "__main__":
    main_login = main_User()
    main_login.grabinfo()

    probee = guildee_probee()
    probee.grabinfo()

    leader = guild_Master()
    leader.grabinfo()
