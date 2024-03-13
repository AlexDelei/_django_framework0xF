from api import get_instagram_info

username = '_dele.ali'
insta_info = get_instagram_info(username)
if insta_info:
    insta_photos, user, name, bio, profile_pic = insta_info
    print("Instagram User:", user)
    print("Full Name", name)
    print("Bio:", bio)
    print("Profile Pic URL:", profile_pic)
    print("Instagram Photo", insta_photos)