import datetime
import pytz

def generate_readme():
    # Define the timezone for Bangladesh
    bd_timezone = pytz.timezone('Asia/Dhaka')

    # Get the current time in Bangladesh time
    bd_time = datetime.datetime.now(bd_timezone)
    content = f""" ![](http://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=rhshourav&theme=transparent)
![](http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=rhshourav&theme=transparent) ![](http://github-profile-summary-cards.vercel.app/api/cards/stats?username=rhshourav&theme=transparent) 
![](http://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=rhshourav&theme=transparent&utcOffset=6) [![GitHub Streak](https://streak-stats.demolab.com?user=rhshourav&theme=transparent&hide_border=true&border_radius=4.6&card_width=320)](https://git.io/streak-stats)"""
    content += f"""![](https://tryhackme-badges.s3.amazonaws.com/deshoha.png) ![](https://komarev.com/ghpvc/?username=rhshourav&color=03fca9)"""
    content += f"\nLast updated: {bd_time.strftime('%B %d, %Y')} at {bd_time.strftime('%I:%M:%S %p')} \n"
    
    with open("README.md", "w") as readme_file:
        readme_file.write(content)

if __name__ == "__main__":
    generate_readme()
