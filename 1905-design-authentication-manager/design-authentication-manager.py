class AuthenticationManager:

    def __init__(self, timeToLive: int):
        #init time to live
        self.timeToLive = timeToLive
        #init dict
        self.Auth_dict = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        #add new token to the dict where tokenid is key and val is currtime
        self.Auth_dict[tokenId] =  currentTime

        

    def renew(self, tokenId: str, currentTime: int) -> None:
        #checks if the token with key = tokenId is unexpired (tokentime+ttl)>currenttime
       if tokenId in self.Auth_dict :
           if self.Auth_dict[tokenId] + self.timeToLive > currentTime:
               #update tokenid dict's value to the current time
               self.Auth_dict[tokenId] = currentTime
        
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        #go through the dict and check if time+ttl >current time and su them
        unexpired_sum = sum ( 1 for tokenId,creation_time in self.Auth_dict.items()  if creation_time + self.timeToLive > currentTime)
        return unexpired_sum

        #delete expired tokens

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)