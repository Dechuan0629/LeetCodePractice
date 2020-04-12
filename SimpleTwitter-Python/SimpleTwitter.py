import time
class Twitter:
    def __init__(self):
        self.user = {}   #利用字典对用户进行存储，键userId ：( 值['post']键保存推文:[发送的时间戳，推文ID]，值['follow']键保存关注人列表:[]）

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user.keys():
            self.user.update({userId:{'post':[[int(round(time.time() * 1000000)),tweetId]],'follow':[]}})
        else:
            self.user[userId]['post'].append([int(round(time.time() * 1000000)),tweetId])

    def getNewsFeed(self, userId: int) -> list:
        temp = []
        if userId not in self.user.keys():
            self.user.update({userId: {'post': [], 'follow': []}})
            return temp
        for line in self.user[userId]['post']:
            if line in temp:
                continue
            temp.append(line)
        for key in self.user[userId]['follow']:
            for line in self.user[key]['post']:
                if line in temp:
                    continue
                temp.append(line)
        temp.sort(reverse=True)   #按时间顺序排列推文，取10条以内的推文出来
        count = 0
        result = []
        for line in temp:
            if count == 10:
                break
            result.append(line[1])
            count+=1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user.keys():
            self.user.update({followerId: {'post': [], 'follow': []}})
        if followeeId not in self.user.keys():
            self.user.update({followeeId: {'post': [], 'follow': []}})
        self.user[followerId]['follow'].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user.keys():
            self.user.update({followerId: {'post': [], 'follow': []}})
        if followeeId not in self.user.keys():
            self.user.update({followeeId: {'post': [], 'follow': []}})
        try:
            self.user[followerId]['follow'].remove(followeeId)
        except ValueError:
            return -1

def main():
    test = Twitter()
    test.postTweet(1,5)
    print(test.getNewsFeed(1))
    test.follow(1,2)
    test.postTweet(2,6)
    print(test.getNewsFeed(1))
    test.unfollow(1,2)
    print(test.getNewsFeed(1))


if __name__ == '__main__':
    main()