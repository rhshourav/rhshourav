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
    tracker_url = f"https://github-profile-tracker.rhshourav02.workers.dev/?v={int(now.timestamp())}"
    content = f""" ![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&duration=6000&pause=1000&color=FF4C69&center=true&random=true&width=435&lines=Hey%2C+There+it's++Shourav+.+.+.+)"""
    content += f"""

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
![]({tracker_url})
![](http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username={PROFILE['username']}&theme=transparent)

## 🏆 TryHackMe
![](https://tryhackme-badges.s3.amazonaws.com/deshoha.png)

## 🌐 Contact
- Discord: {PROFILE['contacts']['Discord']}
- Telegram: {PROFILE['contacts']['Telegram']}

[![Auto Regenerate README](https://github.com/rhshourav/rhshourav/actions/workflows/regenerate.yml/badge.svg)](https://github.com/rhshourav/rhshourav/actions/workflows/regenerate.yml)
⏱️ Last updated: {now.strftime('%B %d, %Y %I:%M:%S %p')}
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_readme()
