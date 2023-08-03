from multiprocessing import Process
from copy import deepcopy
from functions import *
from glob import glob
from time import time
import warnings
import requests
import json
import csv
import os

from PyPDF2 import *

warnings.filterwarnings('ignore')

def make_directories(competitions, min_year, max_year):
    '''
    Creates directories for storing PDF and CSV files for each competition and year.
    
    Args:
        competitions (list): A list of competition names and codes in the format [(name, code)].
        min_year (int): The minimum year.
        max_year (int): The maximum year.
    '''

    if 'processed' not in os.listdir(): os.mkdir('processed')
    if 'raw' not in os.listdir(): os.mkdir('raw')
    os.chdir('raw')
    for competition in competitions:
        name = competition[0]
        if name not in os.listdir(): os.mkdir(name)
        os.chdir(name)
        for year in range(min_year, max_year + 1):
            year = str(year)
            if year not in os.listdir(): os.mkdir(year)
            os.chdir(year)
            if 'PDFs' not in os.listdir(): os.mkdir('PDFs')
            if 'CSVs' not in os.listdir(): os.mkdir('CSVs')
            os.chdir('..')
        
        os.chdir('..')
    os.chdir('..')

def extract_games(competition, cod, year, files):
    '''
    Extracts games data from PDF files and saves them as PDF and CSV files.
    
    Args:
        competition (str): The name of the competition.
        cod (str): The code of the competition.
        year (int): The year of the games.
        files (list): A list of existing file paths.
    '''

    count_end = 0
    game = 0
    while True:
        game += 1
        if count_end == 10: break
        try:
            name = f'./raw/{competition}/{year}/PDFs/{str(game).zfill(3)}.pdf'
            if name.replace('PDFs', 'CSVs').replace('pdf', 'csv') in files:
                count_end = 0
                continue
            
            pdf = get_pdf(f'https://conteudo.cbf.com.br/sumulas/{year}/{cod}{game}se.pdf')
            if b'File or directory not found' in pdf:
                count_end += 1
                continue
            
            with open(name, 'wb') as f:
                f.write(pdf)
                count_end = 0
                
            reader = PdfReader(name)
            doc = []
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                doc += page.extract_text().split('\n')
                
            for i in range(len(doc)): doc[i] = [doc[i]]
            name = name.replace('PDFs', 'CSVs')
            name = name.replace('pdf', 'csv')
            with open(name, 'w') as f:
                write = csv.writer(f)
                write.writerows(doc)
                
        except: pass

def get_pdf(url):
    '''
    Retrieves the content of a PDF file from the specified URL.
    
    Args:
        url (str): The URL of the PDF file.
    
    Returns:
        bytes: The content of the PDF file.
    '''

    return requests.get(url, verify = False).content

def scrape(competitions, min_year, max_year, files, max_time = 600, cleaning = True):
    '''
    Scrapes games data from websites and saves them as PDF and CSV files.
    
    Args:
        competitions (list): A list of competition names and codes in the format [(name, code)].
        min_year (int): The minimum year.
        max_year (int): The maximum year.
        files (list): A list of existing file paths.
        max_time (int): The maximum time (in seconds) to wait for each scraping process. Defaults to 600 seconds.
        cleaning (bool): Flag indicating whether to clear the console output before scraping. Defaults to True.
    '''

    for competition in competitions:
        competition, cod = competition
        for year in range(min_year, max_year + 1):
            if cleaning: clear()
            print(f'Beggining scrape of {competition.replace("_", " ")} {year}')
            start_scrape = time()
            year = str(year)
            p = Process(target = extract_games, args = (competition, cod, year, files))
            p.start()
            p.join(max_time)
            p.terminate()
            
            end_scrape = time()
            if end_scrape - start_scrape > max_time: print('Finished due timeout')

def extract(competitions, min_year, max_year, cleaning = True):
    '''
    Extracts game data from CSV files and generates summary files for each competition and year.
    
    Args:
        competitions (list): A list of competition names and codes in the format [(name, code)].
        min_year (int): The minimum year.
        max_year (int): The maximum year.
        cleaning (bool): Flag indicating whether to clear the console output before extracting. Defaults to True.
    
    Returns:
        int: The total number of extraction failures.
    '''

    with open('../auxiliary/exceptions.json', 'r') as f: exceptions = json.load(f)

    errors = list()
    cont_fail = 0
    for competition in competitions:
        competition = competition[0]
        for year in range(min_year, max_year + 1):
            if cleaning: clear()
            year = str(year)
            print(f'Beggining extract of {competition.replace("_", " ")} {year}')
            games = {}
            count_end = 0
            if f'{competition}_{year}_games.json' in os.listdir(f'./processed/'):
                files = glob(f'./raw/{competition}/{year}/CSVs/*.csv')
                latest_file = max(files, key = os.path.getmtime)
                mod_time = os.path.getmtime(latest_file)
                if mod_time < os.path.getmtime(f'./processed/{competition}_{year}_games.json'): continue
            
            summary = [['Game', 'Home', 'Away']]
            game = 0
            while True:
                game += 1
                if str(game).zfill(3) in exceptions[competition][year]:
                    if exceptions[competition][year][str(game).zfill(3)] != {}:
                        games[str(game).zfill(3)] = exceptions[competition][year][str(game).zfill(3)]
                        summary.append([str(game).zfill(3), games[str(game).zfill(3)]['Home'], games[str(game).zfill(3)]['Away']])
                        
                    continue
                
                if count_end == 10: break
                f_club, f_result, f_players, f_goals, f_changes = False, False, False, False, False
                try:
                    with open(f'./raw/{competition}/{year}/CSVs/{str(game).zfill(3)}.csv', 'r') as f: text = ''.join(f.readlines())

                    clubs = catch_teams(text)
                    assert len(clubs) == 1
                    f_club = True
                
                    result = final_result(text)
                    assert len(result) == 1
                    result = result[0]
                    f_result = True
                
                    players = catch_players(text)
                    assert len(players) >= 28
                    f_players = True
                
                    goals = catch_goals(text)
                    aux = result.upper().split('X')
                    assert len(goals) == int(aux[0].strip()) + int(aux[-1].strip())
                    f_goals = True
                
                    changes = find_changes(text)
                    assert len(changes) <= 10
                    f_changes = True

                    yellow_cards = catch_yellow_cards(text)
                    red_cards = catch_red_cards(text)
                
                    games[str(game).zfill(3)] = {'Home'         : clubs[0][0],
                                                 'Away'         : clubs[0][1],
                                                 'Result'       : result,
                                                 'Players'      : players,
                                                 'Goals'        : goals,
                                                 'Changes'      : changes,
                                                 'Yellow cards' : yellow_cards,
                                                 'Red cards'    : red_cards}

                    count_end = 0
                    summary.append([str(game).zfill(3), clubs[0][0], clubs[0][1]])
                    
                except FileNotFoundError: count_end += 1
                except AssertionError:
                    cont_fail += 1
                    if not f_club: errors.append(f'Error during extracting clubs from game {game} of {year}\'s {competition}.')
                    elif not f_result: errors.append(f'Error during extracting result from game {game} of {year}\'s {competition}.')
                    elif not f_players: errors.append(f'Error during extracting players from game {game} of {year}\'s {competition}.')
                    elif not f_goals: errors.append(f'Error during extracting goals from game {game} of {year}\'s {competition}.')
                    elif not f_changes: errors.append(f'Error during extracting changes from game {game} of {year}\'s {competition}.')
                    else: errors.append(f'Error in game {game} of {year}\'s {competition}.')

            with open(f'./processed/{competition}_{year}_games.json', 'w') as f: json.dump(games, f)
            with open(f'./raw/{competition}/{year}/summary.csv', 'w') as f:
                writer = csv.writer(f)
                for row in summary: writer.writerow(row)
    
    if len(errors) > 0:
        with open('./infos_errors_extract.csv', 'w') as f:
            writer = csv.writer(f)
            for error in errors: writer.writerow([error])
    
    return cont_fail

def catch_squads(competitions, min_year, max_year, cleaning = True):
    '''
    Updates the lineups data for each game in the specified competitions and years.
    
    Args:
        competitions (list): A list of competition names and codes in the format [(name, code)].
        min_year (int): The minimum year.
        max_year (int): The maximum year.
        cleaning (bool): Flag indicating whether to clear the console output before updating lineups. Defaults to True.
    '''

    errors = list()
    model = {'Home' : {'Squad' : [], 'Cards' : [], 'Goals': []},
             'Away' : {'Squad' : [], 'Cards' : [], 'Goals': []},
             'Time' : 0}

    for competition in competitions:
        competition = competition[0]
        for year in range(min_year, max_year + 1):
            year = str(year)
            if cleaning: clear()
            print(f'Beggining lineups update of {competition.replace("_", " ")} {year}')
            if f'{competition}_{year}_squads.json' in os.listdir(f'processed/'):
                files = glob(f'./raw/{competition}/{year}/CSVs/*.csv')
                latest_file = max(files, key = os.path.getmtime)
                mod_time = os.path.getmtime(latest_file)
                if mod_time < os.path.getmtime(f'./processed/{competition}_{year}_squads.json'): continue

            squads = {}
            with open(f'./processed/{competition}_{year}_games.json') as f: games = json.load(f)
            
            for game in games:
                if games[game] == {}: continue

                home = games[game]['Home']
                away = games[game]['Away']
                players = games[game]['Players']
                if players[0][1] == players[-1][1]: continue
                
                game_players = treat_game_players(players, home, away)
                changes = treat_game_changes(games[game]['Changes'], home, away)
                try:
                    goals = treat_game_events(games[game]['Goals'], home, away)
                except Exception as e:
                    errors.append(f'Treating goals: {e}')

                try:
                    red_cards = treat_game_events(games[game]['Red cards'], home, away)
                except Exception as e:
                    errors.append(f'Treating red cards: {e}')
                
                try:
                    yellow_cards = treat_game_events(games[game]['Yellow cards'], home, away)
                except Exception as e:
                    errors.append(f'Treating yellow cards: {e}')
                
                if len(red_cards) > 0:
                    for i, red_card in enumerate(red_cards):
                        red_card = list(red_card)
                        club = red_card.pop()
                        red_card.insert(0, club)
                        red_card.insert(2, '')
                        red_cards[i] = tuple(red_card)

                changes += red_cards
                changes = sorted(changes, key = lambda x : x[1])
                squads[game] = {}
                squads[game][0] = deepcopy(model)
                for player in players:
                    if player[1] == home: game_club = 'Home'
                    else: game_club = 'Away'
                    if len(squads[game][0][game_club]['Squad']) == 11: continue
                    cod = re.findall('\d{6}', player[0])[0]
                    squads[game][0][game_club]['Squad'].append(cod)
                    
                actual_minute = 0
                changes_breaks = 0
                for i, change in enumerate(changes):
                    club, time, player_in, player_out = change
                    try: player_in = game_players[club][player_in] if player_in != '' else ''
                    except: errors.append(f'Can\'t find player {player_in} of {club} in {game} of {year}\'s {competition}')
                    try: player_out = game_players[club][player_out]
                    except: errors.append(f'Can\'t find player {player_out} of {club} in {game} of {year}\'s {competition}')
                    if time != actual_minute:
                        changes_breaks += 1
                        squads[game][changes_breaks] = deepcopy(squads[game][changes_breaks - 1])
                        if club == home:
                            if player_in != '':
                                try:
                                    squads[game][changes_breaks]['Home']['Squad'].remove(player_out)
                                    squads[game][changes_breaks]['Home']['Squad'].append(player_in)
                                except:
                                    errors.append(f'Can\'t change player {player_out} because he\'s already out of game {game} of {year}\'s {competition}')
                            elif player_out in squads[game][changes_breaks]['Home']['Squad']:
                                try:
                                    squads[game][changes_breaks]['Home']['Squad'].remove(player_out)
                                except:
                                    errors.append(f'Can\'t change player {player_out} because he\'s already out of game {game} of {year}\'s {competition}')
                        else:
                            if player_in != '':
                                try:
                                    squads[game][changes_breaks]['Away']['Squad'].remove(player_out)
                                    squads[game][changes_breaks]['Away']['Squad'].append(player_in)
                                except:
                                    errors.append(f'Can\'t change player {player_out} because he\'s already out of game {game} of {year}\'s {competition}')
                            elif player_out in squads[game][changes_breaks]['Away']['Squad']:
                                try:
                                    squads[game][changes_breaks]['Away']['Squad'].remove(player_out)
                                except:
                                    errors.append(f'Can\'t change player {player_out} because he\'s already out of game {game} of {year}\'s {competition}')
                        
                        squads[game][changes_breaks - 1]['Time'] = time - actual_minute
                        squads[game][changes_breaks]['Home']['Cards'] = list()
                        squads[game][changes_breaks]['Home']['Goals'] = list()
                        squads[game][changes_breaks]['Away']['Cards'] = list()
                        squads[game][changes_breaks]['Away']['Goals'] = list()
                        for goal in goals:
                            minute, player, team = goal
                            if minute > actual_minute and minute <= time:
                                if player == '':
                                    errors.append(f'Not found player whom score goal at {minute}\' on game between {home} and {away} in {year}\'s {competition}')
                                else:
                                    try: player = game_players[team][player]
                                    except KeyError: errors.append(f'Not found player {player} from {team} on game {game} of {year}\'s {competition}')

                                if team == home: squads[game][changes_breaks - 1]['Home']['Goals'].append((minute - actual_minute, player))
                                else: squads[game][changes_breaks - 1]['Away']['Goals'].append((minute - actual_minute, player))

                        for card in yellow_cards:
                            minute, player, team = card
                            if minute > actual_minute and minute <= time:
                                try: player = game_players[team][player]
                                except KeyError: errors.append(f'Not found player {player} from {team} on game {game} of {year}\'s {competition}')
                                
                                if team == home: squads[game][changes_breaks - 1]['Home']['Cards'].append((minute - actual_minute, player))
                                else: squads[game][changes_breaks - 1]['Away']['Cards'].append((minute - actual_minute, player))
                                
                        if i == len(changes) - 1:
                            squads[game][changes_breaks]['Time'] = 90 - time
                            for goal in goals:
                                minute, player, team = goal
                                if minute > time:
                                    try: player = game_players[team][player]
                                    except KeyError: errors.append(f'Not found player {player} from {team} on game {game} of {year}\'s {competition}')
                                    
                                    if team == home: squads[game][changes_breaks]['Home']['Goals'].append((90 - time, player))
                                    else: squads[game][changes_breaks]['Away']['Goals'].append((90 - time, player))

                            for card in yellow_cards:
                                minute, player, team = card
                                if minute > time:
                                    try: player = game_players[team][player]
                                    except KeyError: errors.append(f'Not found player {player} from {team} on game {game} of {year}\'s {competition}')
                                    
                                    if team == home: squads[game][changes_breaks]['Home']['Cards'].append((90 - time, player))
                                    else: squads[game][changes_breaks]['Away']['Cards'].append((90 - time, player))
                                
                    else:
                        if club == home:
                            if player_in != '':
                                try:
                                    squads[game][changes_breaks]['Home']['Squad'].remove(player_out)
                                    squads[game][changes_breaks]['Home']['Squad'].append(player_in)
                                except:
                                    errors.append(f'Can\'t change player {player_out} because he\'s already out of game {game} of {year}\'s {competition}')
                            elif player_out in squads[game][changes_breaks]['Home']['Squad']:
                                try:
                                    squads[game][changes_breaks]['Home']['Squad'].remove(player_out)
                                except:
                                    errors.append(f'Can\'t change player {player_out} because he\'s already out of game {game} of {year}\'s {competition}')
                        else:
                            if player_in != '':
                                try:
                                    squads[game][changes_breaks]['Away']['Squad'].remove(player_out)
                                    squads[game][changes_breaks]['Away']['Squad'].append(player_in)
                                except:
                                    errors.append(f'Can\'t change player {player_out} because he\'s already out of game {game} of {year}\'s {competition}')
                            elif player_out in squads[game][changes_breaks]['Away']['Squad']:
                                try:
                                    squads[game][changes_breaks]['Away']['Squad'].remove(player_out)
                                except:
                                    errors.append(f'Can\'t change player {player_out} because he\'s already out of game {game} of {year}\'s {competition}')
                        
                        if i == len(changes) - 1: squads[game][changes_breaks]['Time'] = 90 - time
                            
                    actual_minute = time
            
            with open(f'./processed/{competition}_{year}_squads.json', 'w') as f: json.dump(squads, f)

    if len(errors) > 0:
        with open('./infos_errors_catch.csv', 'w') as f:
            writer = csv.writer(f)
            for error in errors: writer.writerow([error])
