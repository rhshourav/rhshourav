import datetime

def generate_readme():
    content = f"![](https://komarev.com/ghpvc/?username=rhshourav&color=03fca9)"
    content += f""" \n\n<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=rhshourav&size_weight=0.0010&count_weight=0.6&theme=dracula&border_color=03fca9&langs_count=10&card_width=320&layout=pie">"""
    content +=  f"\n\n[![GitHub Streak](https://streak-stats.demolab.com?user=rhshourav&theme=nordfox&hide_border=true&border_radius=4.6&exclude_days=Fri&card_width=320)](https://git.io/streak-stats)"
    content += f"\n \n  ![TryHackMe](https://tryhackme.com/badge/533634)"
    content += f"\n\nLast updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    with open("README.md", "w") as readme_file:
        readme_file.write(content)

if __name__ == "__main__":
    generate_readme()
