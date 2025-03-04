from scrape import make_directories, scrape, extract, catch_squads
from py_markdown_table.markdown_table import markdown_table
from datetime import datetime
from functions import clear
from time import time
from glob import glob
import json
import sys
import os

if __name__ == "__main__":
    now = datetime.now()
    os.chdir("..")
    if "results" not in os.listdir():
        os.mkdir("results")
    os.chdir("results")
    competitions = [
        ("CdB", "424"),
        ("Serie_A", "142"),
        ("Serie_B", "242"),
        ("Serie_C", "342"),
        ("Serie_D", "542"),
    ]

    if now.strftime("%d") == "04":
        for file in glob("./processed/*.json"):
            os.remove(file)
        min_year = 2013

    else:
        min_year = int(now.strftime("%Y"))
        for year in range(2013, min_year):
            if len(glob(f"./processed/*{year}*.json")) != 2 * len(competitions):
                min_year = year
                sys.argv.append("--t")
                break

    max_year = int(now.strftime("%Y"))
    if "--c" in sys.argv:
        cleaning = True
    else:
        cleaning = False

    if "--s" in sys.argv or len(sys.argv) == 1:
        if min_year != max_year:
            print(f"Scraping years of {min_year} to {max_year}")
        else:
            print(f"Scraping data of {min_year}")
        make_directories(competitions, min_year, max_year)
        with open("../auxiliary/scrape.log", "a") as f:
            f.write(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Scraping] - Beginning docket scraping.\n'
            )

        start_scrape = time()
        max_time = 60
        added = 0
        for competition in competitions:
            n = len(glob(f"./raw/{competition[0]}/*/CSVs/*.csv"))
            it = 1
            k = 0
            while n != k or n == 0:
                files = glob(f"./raw/{competition[0]}/*/CSVs/*.csv")
                k = len(files)
                scrape(
                    [competition],
                    min_year,
                    max_year,
                    files,
                    max_time,
                    cleaning=cleaning,
                )
                n = len(glob(f"./raw/{competition[0]}/*/CSVs/*.csv"))
                added += n - k
                it += 1

        end_scrape = time()
        with open("../auxiliary/scrape.log", "a") as f:
            f.write(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Scraping] - Docket scraping complete.\n'
            )
            if added == 0:
                f.write(
                    "                                   [INFO] Already up to date.\n"
                )
            elif added == 1:
                f.write("                                   [INFO] 1 docket added.\n")
            else:
                f.write(
                    f"                                   [INFO] {added} dockets addeds.\n"
                )

        if added > 0 or "--t" in sys.argv:
            start_extract = time()
            with open("../auxiliary/scrape.log", "a") as f:
                f.write(
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Extract]  - Beginning info extract.\n'
                )

            cont_fail = extract(competitions, min_year, max_year, cleaning=cleaning)
            with open("../auxiliary/scrape.log", "a") as f:
                f.write(
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Extract]  - Info extract complete.\n'
                )
                if cont_fail == 1:
                    f.write(
                        "                                   [INFO] 1 game failed.\n"
                    )
                elif cont_fail > 0:
                    f.write(
                        f"                                   [INFO] {cont_fail} games failed.\n"
                    )
                else:
                    f.write("                                   [INFO] Sucess!\n")

                f.write(
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Lineups]  - Beginning lineups treatment.\n'
                )

            catch_squads(competitions, min_year, max_year, cleaning=cleaning)
            with open("../auxiliary/scrape.log", "a") as f:
                f.write(
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Lineups]  - Lineups complete.\n'
                )

            end_extract = time()
            if cleaning:
                clear()
            print(
                f"Scrape complete in {end_scrape - start_scrape:.2f} seconds!",
                f"Extract complete in {end_extract - start_extract:.2f} seconds!",
                f"{added} games added.",
                f"{cont_fail} games failed.",
                "-" * 58,
                f"Total time: {end_extract - start_scrape:.2f} seconds.",
                sep="\n",
            )
        else:
            if cleaning:
                clear()
            print(
                f"Scrape complete in {end_scrape - start_scrape:.2f} seconds!",
                "Nothing to add.",
                sep="\n",
            )

    elif "--t" in sys.argv:
        start_extract = time()
        with open("../auxiliary/scrape.log", "a") as f:
            f.write(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Extract]  - Beginning info extract.\n'
            )

        cont_fail = extract(competitions, min_year, max_year, cleaning=cleaning)
        with open("../auxiliary/scrape.log", "a") as f:
            f.write(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Extract]  - Info extract complete.\n'
            )
            if cont_fail == 1:
                f.write("                                   [INFO] 1 game failed.\n")
            elif cont_fail > 0:
                f.write(
                    f"                                   [INFO] {cont_fail} games failed.\n"
                )
            else:
                f.write("                                   [INFO] Sucess!\n")

            f.write(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Lineups]  - Beginning lineups treatment.\n'
            )

        catch_squads(competitions, min_year, max_year, cleaning=cleaning)
        with open("../auxiliary/scrape.log", "a") as f:
            f.write(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Lineups]  - Lineups complete.\n'
            )

        end_extract = time()
        if cleaning:
            clear()
        print(
            f"Extract complete in {end_extract - start_extract:.2f} seconds!",
            f"{cont_fail} games failed.",
            sep="\n",
        )

    data = list()
    for file in sorted(glob("./processed/*games.json")):
        competition = (
            file.split("/")[-1]
            .replace("_games.json", "")
            .replace("_", " ")
            .replace("CdB", "Brazil Cup")
        )

        *competition, year = competition.split(" ")
        competition = " ".join(competition) + f" ({year})"
        with open(file) as f:
            games = json.load(f)
        if len(games) == 0:
            continue
        data.append(
            {
                "Competition": competition,
                "Real games": int(sorted(games.keys())[-1]),
                "Scraped games": len(games),
            }
        )

    markdown = markdown_table(data).set_params(row_sep="markdown").get_markdown()
    markdown = markdown.replace("`", "")
    with open("../README.md", "r") as f:
        readme = f.readlines()
    if "## Total games\n" in readme:
        aux = readme.index("## Total games\n")
        markdown = markdown.split("\n")
        for i in range(len(markdown)):
            readme[aux + 2 + i] = markdown[i] + "\n"
    else:
        aux = readme.index("### Know problems\n")
        readme.insert(aux, "## Total games\n\n")
        readme.insert(aux + 1, markdown + "\n\n")

    with open("../README.md", "w") as f:
        f.writelines(readme)

    with open("../auxiliary/scrape.log", "a") as f:
        f.write("\n")
        f.write("-" * 85 + "\n")
        f.write("\n")
