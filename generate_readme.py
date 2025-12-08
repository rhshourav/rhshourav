import datetime
import pytz
from config import PROFILE

def generate_readme():
    tz = pytz.timezone(PROFILE["timezone"])
    now = datetime.datetime.now(tz)

    roles = " | ".join(PROFILE["roles"])
    focus = "\n".join([f"- ✅ {x}" for x in PROFILE["focus_areas"]])
    tools = "\n".join([f"- {x}" for x in PROFILE["tools"]])
    platforms = ", ".join(PROFILE["platforms"])
    os_list = " · ".join(PROFILE["operating_systems"])

    content = f"""
<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=6000&pause=900&color=FF4C69&center=true&width=700&lines=Hey+There!+I'm+{PROFILE['name']}+aka+{PROFILE['username']};{roles.replace(' ', '+')};Always+Learning+🚀" />
</p>

## 🧠 About Me
- {roles}
- 🎯 Goal: Job-driven learning & professional growth
- 🌍 Based in {PROFILE['country']}

## 🔐 Cybersecurity Focus
{focus}

**Platforms:** {platforms}

## 🧰 Tech Stack
**Operating Systems:** {os_list}

**Tools**
{tools}

## 📊 GitHub Activity
![](http://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={PROFILE['username']}&theme=transparent)

## 🏆 TryHackMe
![](https://tryhackme-badges.s3.amazonaws.com/deshoha.png)

## 🌐 Contact
- Discord: {PROFILE['contacts']['Discord']}
- Telegram: {PROFILE['contacts']['Telegram']}

⏱️ Last updated: {now.strftime('%B %d, %Y %I:%M:%S %p')}
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_readme()
