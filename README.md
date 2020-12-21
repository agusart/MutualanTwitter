# Edit your ceredential details 

```
vim .env
```

If you dont have twitter Tokens try this [Tutorials](https://gist.github.com/jimkang/34d16247b40097d8cace/) below:



# Get Twitter Tokens

1. Sign up for a new Twitter account. They'll ask for a phone number, and unfortunately, as of 5/12/2015, I think you have to provide one to get API keys.
![Add phone number](https://cloud.githubusercontent.com/assets/324298/7590996/3f5ee072-f899-11e4-9509-86e34f06f642.png)

2. Go to https://apps.twitter.com to create a new app.
![Create new app](https://cloud.githubusercontent.com/assets/324298/7591017/5cb356bc-f899-11e4-80b8-9c3cd7129a89.png)

3. Fill out the form for creating a new app.
![App form](https://cloud.githubusercontent.com/assets/324298/7591022/60aa8a4c-f899-11e4-8b70-079aec54bcee.png)

4. Go to the Keys and Access Tokens tab, which will have your consumer key and secret. Copy them somewhere so that you can use them in your app. Hit Create My Access Token.
![Keys and Access Tokens tab](https://cloud.githubusercontent.com/assets/324298/7591025/6515aff8-f899-11e4-829c-438f0e6770ca.png)

5. Copy the access token key and secret for your app.
![Access token](https://cloud.githubusercontent.com/assets/324298/7591026/69d028c0-f899-11e4-9bd8-3ca932eb7b92.png)

6. After that, you probably want to go back to your Twitter settings and delete your phone from it.

![Twitter settings](https://cloud.githubusercontent.com/assets/324298/7591030/6de76bee-f899-11e4-96b7-0911ba0dfbfd.png)


[@_hartsick](https://twitter.com/_hartsick) pointed out that you can also just create one app and have [multiple bots share it](http://dghubble.com/blog/posts/twitter-app-write-access-and-bots/)!


## Build docker images
```
docker build --tag agusart/mutualfess .
```

## Run a container
```
docker run --name agusart -v /home/agus/MutualanTwitter:/code -d agusart/mutualfess:latest
```
