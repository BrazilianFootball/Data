import re
import os


def clear():
    """
    Clears the console screen.
    """

    os.system("clear")


def treat_time(time_string):
    """
    Parses the time string and returns the corresponding time in minutes.

    Args:
        time_string (str): The time string in the format 'HH' or 'HH+T' or '2T'.

    Returns:
        int: The time in minutes.
    """
    time_string = time_string.replace(":00", "")

    time = 0
    if "INT" in time_string:
        return 45
    if "2T" in time_string:
        time += 45
    if "+" in time_string:
        time += 45
    else:
        time += int(time_string[:2])

    return time


def treat_club(club):
    """
    Formats the club name by removing unnecessary words and characters.

    Args:
        club (str): The club name.

    Returns:
        str: The formatted club name.
    """

    # removing
    club = club.replace("Saf ", "")
    club = club.replace("SAF ", "")
    club = club.replace("S.a.f ", "")
    club = club.replace("S.A.F ", "")
    club = club.replace("S.a.f. ", "")
    club = club.replace("S.A.F. ", "")
    club = club.replace("Fc ", "")
    club = club.replace("FC ", "")
    club = club.replace("Futebol Clube ", "")
    club = club.replace("FUTEBOL CLUBE ", "")
    club = club.replace("F. C. ", "")
    club = club.replace("A.c. ", "")
    club = club.replace("Ltda ", "")
    club = club.replace("Associacao Desportiva ", "")
    club = club.replace("Esporte Clube ", "")
    club = club.replace("Sociedade Esportiva ", "")
    club = club.replace("-ap", "")
    club = club.replace("- Me ", "")
    club = club.replace("Acreano ", "")

    # adding special chars
    club = club.replace("Avai", "Avaí")
    club = club.replace("Goias", "Goiás")
    club = club.replace("Cuiaba", "Cuiabá")
    club = club.replace("America", "América")
    club = club.replace("Vitoria", "Vitória")
    club = club.replace("Atletico", "Atlético")
    club = club.replace("Confianca", "Confiança")
    club = club.replace("Sao Paulo", "São Paulo")
    club = club.replace("Sao Raimundo", "São Raimundo")

    # treating club names
    club = club.replace("- Vn ", "- VN ")
    club = club.replace("Sport Club do Recife", "Sport")
    club = club.replace("River Atlético Clube ", "Ríver ")
    club = club.replace("Moto Club de Sao Luis ", "Moto Club ")
    club = club.replace("Parana Clube", "Paraná")
    club = club.replace("Alvorada Club", "Maringá")
    club = club.replace("Clube Esportivo Operario Varzeagrandense", "Operário")
    club = club.replace("Clube de Regatas Brasil", "CRB")
    club = club.replace("CORITIBA FOOT-BALL CLUB", "Coritiba")
    club = club.replace("Clube Nautico Capibaribe", "Náutico")
    club = club.replace("Gremio Foot-ball Porto Alegrense", "Grêmio")
    club = club.replace("Clube Recreativo E Atlético Catalano", "CRAC")
    club = club.replace("Associacao Cultural Baraunas", "Baraúnas")
    club = club.replace("A.b.c. / RN", "ABC / RN")
    club = club.replace("Abc / RN", "ABC / RN")
    club = club.replace("AVAÍ / SC", "Avaí / SC")
    club = club.replace("A.s.a. / AL", "ASA / AL")
    club = club.replace("América de Natal / RN", "América / RN")
    club = club.replace("AMÉRICA / RN", "América / RN")
    club = club.replace("Atlético / MG", "Atlético Mineiro / MG")
    club = club.replace("ATLETICO / PR", "Athletico Paranaense / PR")
    club = club.replace("Atlético / PR", "Athletico Paranaense / PR")
    club = club.replace("Sobradinho (df) / DF", "Sobradinho / DF")
    club = club.replace("ÁGUIA NEGRA / MS", "Águia Negra / MS")
    club = club.replace("Aguia Negra / MS", "Águia Negra / MS")
    club = club.replace("Aguia / PA", "Águia de Marabá / PA")
    club = club.replace("Ypiranga Rs / RS", "Ypiranga / RS")
    club = club.replace("Villa Nova A.c. / MG", "Villa Nova / MG")
    club = club.replace("Veranopolis / RS", "Veranópolis / RS")
    club = club.replace("União / MT", "União de Rondonópolis / MT")
    club = club.replace("Ser Caxias / RS", "Caxias / RS")
    club = club.replace("Sampaio Correa / MA", "Sampaio Corrêa / MA")
    club = club.replace("SAMPAIO CORREA / MA", "Sampaio Corrêa / MA")
    club = club.replace("SANTOS / SP", "Santos / SP")
    club = club.replace("Bragantino / SP", "Red Bull Bragantino / SP")
    club = club.replace("Red Bull Red Bull", "Red Bull")
    club = club.replace("MURICI / AL", "Murici / AL")
    club = club.replace("River / PI", "Ríver / PI")
    club = club.replace("River A.c. / PI", "Ríver / PI")
    club = club.replace("RÍVER / PI", "Ríver / PI")
    club = club.replace("REAL NOROESTE / ES", "Real Noroeste / ES")
    club = club.replace("Real Noroeste Capixaba / ES", "Real Noroeste / ES")
    club = club.replace("PONTE PRETA / SP", "Ponte Preta / SP")
    club = club.replace("PIAUÍ / PI", "Piauí / PI")
    club = club.replace("Operario / PR", "Operário / PR")
    club = club.replace("Luziania / DF", "Luziânia / DF")
    club = club.replace("INDEPENDENTE / PA", "Independente / PA")
    club = club.replace("Independente Tucuruí / PA", "Independente / PA")
    club = club.replace("Guarany de Sobral / CE", "Guarany / CE")
    club = club.replace("Guarani de Juazeiro / CE", "Guarani / CE")
    club = club.replace("Crb / AL", "CRB / AL")
    club = club.replace("Criciuma / SC", "Criciúma / SC")
    club = club.replace("Csa / AL", "CSA / AL")
    club = club.replace("FIGUEIRENSE / SC", "Figueirense / SC")
    club = club.replace("FORTALEZA / CE", "Fortaleza / CE")
    club = club.replace("C. R. B. / AL", "CRB / AL")
    club = club.replace("C.r.a.c. / GO", "CRAC / GO")
    club = club.replace("C.r.b. / AL", "CRB / AL")
    club = club.replace("C.s.a. / AL", "CSA / AL")
    club = club.replace("CAXIAS / RS", "Caxias / RS")
    club = club.replace("CORITIBA / PR", "Coritiba / PR")
    club = club.replace("CRICIÚMA / SC", "Criciúma / SC")
    club = club.replace("Atlético Cearense / CE", "Atlético / CE")
    club = club.replace("Atlético Roraima / RR", "Atlético / RR")
    club = club.replace("BOTAFOGO / PB", "Botafogo / PB")
    club = club.replace("BOTAFOGO / RJ", "Botafogo / RJ")
    club = club.replace("Asa / AL", "ASA / AL")
    club = club.replace("A.s.s.u. / RN", "ASSU / RN")
    club = club.replace("Xv de Piracicaba / SP", "XV de Piracicaba / SP")
    club = club.replace("Urt / MG", "URT / MG")
    club = club.replace("Arapongas Esporte Clube / PR", "Arapongas / PR")
    club = club.replace("Jacobina Ec / BA", "Jacobina / BA")
    club = club.replace("Ge Juventus / SC", "Juventus / SC")
    club = club.replace("TREZE / PB", "Treze / PB")
    club = club.replace("S.francisco / PA", "S. Francisco / PA")
    club = club.replace("Pstc / PR", "PSTC / PR")
    club = club.replace("Prospera / SC", "Próspera / SC")
    club = club.replace("Marilia / SP", "Marília / SP")
    club = club.replace("Macae / RJ", "Macaé / RJ")
    club = club.replace("Macapa / AP", "Macapá / AP")
    club = club.replace("G.a.s / RR", "G.A.S. / RR")
    club = club.replace("Cse / AL", "CSE / AL")
    club = club.replace("Ca Patrocinense / MG", "Atlético Patrocinense / MG")
    club = club.replace("Atlético / GO", "Atlético Goianiense / GO")

    return club


def treat_round_35_sB(club):
    """
    Treats the club name specifically for round 35 of Campeonato Brasileiro - Série B in 2013.

    Args:
        club (str): The club name.

    Returns:
        str: The treated club name.
    """

    club = treat_club(club)
    club = club.replace("A.s.a. /  ", "ASA / AL")
    club = club.replace("Avaí / ", "Avaí / SC")
    club = club.replace("Boa /  ", "Boa / MG")
    club = club.replace("Paraná /  ", "Paraná / PR")
    club = club.replace("Figueirense /  ", "Figueirense / SC")
    club = club.replace("Guaratinguetá / ", "Guaratinguetá / SP")
    club = club.replace("Chapecoense / ", "Chapecoense / SC")
    club = club.replace("Ceará /  ", "Ceará / CE")
    club = club.replace("Sport / ", "Sport / PE")
    club = club.replace("A.b.c. / ", "ABC / RN")
    club = club.replace("Icasa / ", "Icasa / CE")
    club = club.replace("Palmeiras / ", "Palmeiras / SP")
    club = club.replace("Joinville /  ", "Joinville / SC")
    club = club.replace("São Caetano / ", "São Caetano / SP")
    club = club.replace("Bragantino /  ", "Red Bull Bragantino / SP")
    club = club.replace("Atlético /  ", "Atlético / GO")
    club = club.replace("Paysandu /  ", "Paysandu / PA")
    club = club.replace("Oeste / ", "Oeste / SP")

    return club


def catch_game_date(text):
    """
    Extracts the game date from the given text.

    Args:
        text (str): The text containing the game information.

    Returns:
        str: The game date.
    """

    return re.findall(
        r"Data:\s*(\d{2}/\d{2}/\d{4})",
        text,
    )


def catch_game_time(text):
    """
    Extracts the game time from the given text.

    Args:
        text (str): The text containing the game information.

    Returns:
        str: The game time.
    """

    return re.findall(
        r"Horário:\s*(\d{2}:\d{2})",
        text,
    )


def catch_game_stadium(text):
    """
    Extracts the game stadium from the given text.

    Args:
        text (str): The text containing the game information.

    Returns:
        str: The game stadium.
    """

    return re.findall(
        r"Estádio:\s*(.+?)(?=\n|$)",
        text,
    )


def catch_teams(text):
    """
    Extracts the names of the teams from the given text.

    Args:
        text (str): The text containing the game information.

    Returns:
        list: A list of tuples containing the home and away team names.
    """

    if "Campeonato: Campeonato Brasileiro - Série B / 2013 Rodada: 35 " in text:
        text = treat_round_35_sB(text)
    else:
        text = treat_club(text)
    return re.findall(
        "Jogo:\s*([a-zA-Z0-9À-ÿ\s\.\-]+\s*\/\s*[A-Z]{2})\s*X\s*([a-zA-Z0-9À-ÿ\s\.\-]+\s*\/\s*[A-Z]{2})",
        text,
    )


def final_result(text):
    """
    Extracts the final result of the match from the given text.

    Args:
        text (str): The text containing the game information.

    Returns:
        list: A list of strings representing the final result.
    """

    result = re.findall("Resultado\s*Final:\s*(\d+\s*[xX]\s*\d+)", text)
    if len(result) == 0:
        result = re.findall("Resultado\s*do\s*2º\s*Tempo:\s*(\d+\s*[xX]\s*\d+)", text)

    return [r.upper() for r in result]


def catch_players(text):
    """
    Extracts the players' information from the given text.

    Args:
        text (str): The text containing the game information.

    Returns:
        list: A list of tuples containing the player's information and the corresponding club.
    """

    club_1, club_2 = catch_teams(text)[0]
    club = club_1
    text = text[text.find("Relação de Jogadores") : text.find("Comissão Técnica")]
    goalkeepers = re.findall("CBF\n(\d+\D+[P|A|)|T|R]\s*\d{6})", text)
    for goalkeeper in goalkeepers:
        if "T(g)" in goalkeeper:
            continue
        text = text.replace(goalkeeper[-10:], goalkeeper[-10:].replace("TP", "T(g)P"))

    players = re.findall("\n(\d+.+[P|A|)|T|R]\s*\d{6})", text)
    for i in range(len(players)):
        if i > 0 and "T(g)" in players[i]:
            club = club_2
        players[i] = [players[i], club]

    if players[0][1] == players[-1][1]:
        numbers = []
        changed = False
        for i in range(len(players)):
            number = re.findall("\d+", players[i][0])[0]
            if len(number) == 3:
                if number[1] == "0":
                    number = number[2]
                else:
                    number = number[1:]

            if number in numbers and not changed:
                club = club_2
                numbers.append(club)
                changed = True

            numbers.append(number)
            players[i][1] = club

    return players


def treat_game_players(players, home, away):
    """
    Processes the list of players and their clubs to create a dictionary of game players.

    Args:
        players (list): A list of tuples representing players and their clubs.
        home (str): The home team's club name.
        away (str): The away team's club name.

    Returns:
        dict: A dictionary containing the game players, organized by club.
    """

    game_players = {home: {}, away: {}}
    for player in players:
        if player == list():
            continue
        player, club = player
        numbers = re.findall("\d+", player)
        shirt, cod = numbers[0], numbers[-1]
        game_players[club][shirt] = cod

    return game_players


def catch_yellow_cards(text):
    """
    Extracts the yellow cards information from the given text.

    Args:
        text (str): The text containing the game information.

    Returns:
        list: A list of yellow cards strings.
    """
    text = text[text.find("Cartões Amarelos") : text.find("Cartões Vermelhos")]
    text = text.replace("'", "")
    return re.findall(
        "\+*\d+[:\d+]*\s*\dT\s*\d+\s*[a-zA-ZÀ-ÿ\-\. 0-9]+(?:\/[A-Z]{2})?", text
    )


def catch_red_cards(text):
    """
    Extracts the red cards information from the given text.

    Args:
        text (str): The text containing the game information.

    Returns:
        list: A list of red cards strings.
    """
    text = text[text.find("Cartões Vermelhos") : text.find("Ocorrências / Observações")]
    text = text.replace("'", "")
    return re.findall(
        "\+*\d+[:\d+]*\s*\dT\s*\d+\s*[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}", text
    )


def catch_goals(text):
    """
    Extracts the goal information from the given text.

    Args:
        text (str): The text containing the game information.

    Returns:
        list: A list of goal strings.
    """

    result = final_result(text)
    text = text[text.find("Gols") : text.find("Cartões Amarelos")]
    text = text.replace("'", "")
    if len(result) == 0:
        return []
    result = result[0].split()

    goals = re.findall(
        "\+*\d+[:\d+]*\s*\dT\s*[\d+\s*]*NR[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}", text
    )
    goals += re.findall(
        "\+*\d+[:\d+]*\s*\dT\s*[\d+\s*]*PN[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}", text
    )
    goals += re.findall(
        "\+*\d+[:\d+]*\s*\dT\s*[\d+\s*]*CT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}", text
    )
    goals += re.findall(
        "\+*\d+[:\d+]*\s*\dT\s*[\d+\s*]*FT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}", text
    )

    if len(goals) == int(result[0]) + int(result[-1]):
        return goals

    goals = re.findall("\+*\d+[:\d+]*\s*\dT\s*[\d+\s*]*NR[a-zA-ZÀ-ÿ\-\. 0-9]+", text)
    goals += re.findall("\+*\d+[:\d+]*\s*\dT\s*[\d+\s*]*PN[a-zA-ZÀ-ÿ\-\. 0-9]+", text)
    goals += re.findall("\+*\d+[:\d+]*\s*\dT\s*[\d+\s*]*CT[a-zA-ZÀ-ÿ\-\. 0-9]+", text)
    goals += re.findall("\+*\d+[:\d+]*\s*\dT\s*[\d+\s*]*FT[a-zA-ZÀ-ÿ\-\. 0-9]+", text)

    return goals


def treat_event(event, home, away):
    """
    Processes a single event string and determines the time and scoring team.

    Args:
        event (str): The event string to be processed.
        home (str): The home team's club name.
        away (str): The away team's club name.

    Returns:
        tuple: A tuple containing the time (str) and scoring team (str).
    """

    if " / " not in event:
        if " /" in event:
            event = event.replace(" /", " / ")
        elif "/ " in event:
            event = event.replace("/ ", " / ")
        elif "/" in event:
            event = event.replace("/", " / ")

    event = treat_club(event)
    if "1T" not in event and "2T" not in event:
        if "3T" in event:
            event = event.replace("3T", "2T")
        elif "0T" in event:
            event = event.replace("0T", "1T")

    time_string = re.findall("\+*\d+:\d+\s*[A-Z0-9]+T|\+*\d+\s*\dT", event)[0]
    time = treat_time(time_string)
    player_number = re.findall(
        "\d+:\d+\s*[A-Z0-9]+T\s*(\d+)|\+\d+\s*\dT\s*(\d+)", event
    )
    player_number = player_number[0] if len(player_number) > 0 else ("", "")
    player_number = player_number[0] if len(player_number[0]) > 0 else player_number[1]
    if home in event and away not in event:
        return time, player_number, home
    elif home not in event and away in event:
        return time, player_number, away

    if "Flamengo / RJ" in [home, away] and "Flamengo" in event:
        return time, player_number, "Flamengo / RJ"
    if "Vasco da Gama / RJ" in [home, away] and "Vasco da Gama" in event:
        return time, player_number, "Vasco da Gama / RJ"
    if "Fluminense / RJ" in [home, away] and "Fluminense" in event:
        return time, player_number, "Fluminense / RJ"
    if "Botafogo / RJ" in [home, away] and "Botafogo" in event:
        return time, player_number, "Botafogo / RJ"
    if "Madureira / RJ" in [home, away] and "Madureira" in event:
        return time, player_number, "Madureira / RJ"
    if "Resende / RJ" in [home, away] and "Resende" in event:
        return time, player_number, "Resende / RJ"
    if "Nova Iguaçu / RJ" in [home, away] and "Nova Iguaçu" in event:
        return time, player_number, "Nova Iguaçu / RJ"
    if "Macaé / RJ" in [home, away] and "Macae" in event:
        return time, player_number, "Macaé / RJ"
    if "Duque de Caxias / RJ" in [home, away] and "Duque de Caxias" in event:
        return time, player_number, "Duque de Caxias / RJ"
    if "Palmeiras / SP" in [home, away] and "Palmeiras" in event:
        return time, player_number, "Palmeiras / SP"
    if "São Paulo / SP" in [home, away] and "São Paulo" in event:
        return time, player_number, "São Paulo / SP"
    if "Corinthians / SP" in [home, away] and "Corinthians" in event:
        return time, player_number, "Corinthians / SP"
    if "Santos / SP" in [home, away] and "Santos" in event:
        return time, player_number, "Santos / SP"
    if "Red Bull Bragantino / SP" in [home, away] and "Bragantino" in event:
        return time, player_number, "Red Bull Bragantino / SP"
    if "Sao Bernardo / SP" in [home, away] and "Sao Bernardo" in event:
        return time, player_number, "Sao Bernardo / SP"
    if "São Bento / SP" in [home, away] and "São Bento" in event:
        return time, player_number, "São Bento / SP"
    if "Ponte Preta / SP" in [home, away] and "Ponte Preta" in event:
        return time, player_number, "Ponte Preta / SP"
    if "Portuguesa / SP" in [home, away] and "Portuguesa" in event:
        return time, player_number, "Portuguesa / SP"
    if "Santo André / SP" in [home, away] and "Santo André" in event:
        return time, player_number, "Santo André / SP"
    if "São Caetano / SP" in [home, away] and "São Caetano" in event:
        return time, player_number, "São Caetano / SP"
    if "Penapolense / SP" in [home, away] and "Penapolense" in event:
        return time, player_number, "Penapolense / SP"
    if "Botafogo / SP" in [home, away] and "Botafogo" in event:
        return time, player_number, "Botafogo / SP"
    if "Grêmio Barueri / SP" in [home, away] and "Grêmio Barueri" in event:
        return time, player_number, "Grêmio Barueri / SP"
    if "Mogi Mirim / SP" in [home, away] and "Mogi Mirim" in event:
        return time, player_number, "Mogi Mirim / SP"
    if "Guarani / SP" in [home, away] and "Guarani" in event:
        return time, player_number, "Guarani / SP"
    if "Oeste / SP" in [home, away] and "Oeste" in event:
        return time, player_number, "Oeste / SP"
    if "Guaratinguetá / SP" in [home, away] and "Guaratinguetá" in event:
        return time, player_number, "Guaratinguetá / SP"
    if "Atlético / MG" in [home, away] and "Atlético" in event:
        return time, player_number, "Atlético Mineiro / MG"
    if "América / MG" in [home, away] and "América" in event:
        return time, player_number, "América / MG"
    if "Cruzeiro / MG" in [home, away] and "Cruzeiro" in event:
        return time, player_number, "Cruzeiro / MG"
    if "Villa Nova / MG" in [home, away] and "Villa Nova" in event:
        return time, player_number, "Villa Nova / MG"
    if "Tupi / MG" in [home, away] and "Tupi" in event:
        return time, player_number, "Tupi / MG"
    if "Araxá / MG" in [home, away] and "Araxá" in event:
        return time, player_number, "Araxá / MG"
    if "Betim / MG" in [home, away] and "Betim" in event:
        return time, player_number, "Betim / MG"
    if "Boa / MG" in [home, away] and "Boa" in event:
        return time, player_number, "Boa / MG"
    if "Aracruz / ES" in [home, away] and "Aracruz" in event:
        return time, player_number, "Aracruz / ES"
    if "Internacional / RS" in [home, away] and "Internacional" in event:
        return time, player_number, "Internacional / RS"
    if "Grêmio / RS" in [home, away] and "Grêmio" in event:
        return time, player_number, "Grêmio / RS"
    if "Juventude / RS" in [home, away] and "Juventude" in event:
        return time, player_number, "Juventude / RS"
    if "Lajeadense / RS" in [home, away] and "Lajeadense" in event:
        return time, player_number, "Lajeadense / RS"
    if "Caxias / RS" in [home, away] and "Caxias" in event:
        return time, player_number, "Caxias / RS"
    if "Athletico Paranaense / PR" in [home, away] and "Atlético" in event:
        return time, player_number, "Athletico Paranaense / PR"
    if "Coritiba / PR" in [home, away] and "Coritiba" in event:
        return time, player_number, "Coritiba / PR"
    if "Paraná / PR" in [home, away] and "Paraná" in event:
        return time, player_number, "Paraná / PR"
    if "Arapongas / PR" in [home, away] and "Arapongas" in event:
        return time, player_number, "Arapongas / PR"
    if "Londrina / PR" in [home, away] and "Londrina" in event:
        return time, player_number, "Londrina / PR"
    if "J. Malucelli / PR" in [home, away] and "J. Malucelli" in event:
        return time, player_number, "J. Malucelli / PR"
    if "Chapecoense / SC" in [home, away] and "Chapecoense" in event:
        return time, player_number, "Chapecoense / SC"
    if "Figueirense / SC" in [home, away] and "Figueirense" in event:
        return time, player_number, "Figueirense / SC"
    if "Criciúma / SC" in [home, away] and "Criciuma" in event:
        return time, player_number, "Criciúma / SC"
    if "Avaí / SC" in [home, away] and "AVAÍ" in event:
        return time, player_number, "Avaí / SC"
    if "Metropolitano / SC" in [home, away] and "Metropolitano" in event:
        return time, player_number, "Metropolitano / SC"
    if "Marcílio Dias / SC" in [home, away] and "Marcílio Dias" in event:
        return time, player_number, "Marcílio Dias / SC"
    if "Avaí / SC" in [home, away] and "Avaí" in event:
        return time, player_number, "Avaí / SC"
    if "Joinville / SC" in [home, away] and "Joinville" in event:
        return time, player_number, "Joinville / SC"
    if "Fortaleza / CE" in [home, away] and "Fortaleza" in event:
        return time, player_number, "Fortaleza / CE"
    if "Ceará / CE" in [home, away] and "Ceará" in event:
        return time, player_number, "Ceará / CE"
    if "Icasa / CE" in [home, away] and "Icasa" in event:
        return time, player_number, "Icasa / CE"
    if "Tiradentes / CE" in [home, away] and "Tiradentes" in event:
        return time, player_number, "Tiradentes / CE"
    if "Guarany / CE" in [home, away] and "Guarany" in event:
        return time, player_number, "Guarany / CE"
    if "Vitória da Conquista / BA" in [home, away] and "Vitória da Conquista" in event:
        return time, player_number, "Vitória da Conquista / BA"
    if "Vitória / BA" in [home, away] and "Vitória" in event:
        return time, player_number, "Vitória / BA"
    if "Bahia / BA" in [home, away] and "Bahia" in event:
        return time, player_number, "Bahia / BA"
    if "Juazeirense / BA" in [home, away] and "Juazeirense" in event:
        return time, player_number, "Juazeirense / BA"
    if "ABC / RN" in [home, away] and "A.b.c." in event:
        return time, player_number, "ABC / RN"
    if "América / RN" in [home, away] and "América" in event:
        return time, player_number, "América / RN"
    if "Potiguar / RN" in [home, away] and "Potiguar" in event:
        return time, player_number, "Potiguar / RN"
    if "Baraúnas / RN" in [home, away] and "Baraúnas" in event:
        return time, player_number, "Baraúnas / RN"
    if "Salgueiro / PE" in [home, away] and "Salgueiro" in event:
        return time, player_number, "Salgueiro / PE"
    if "Sport / PE" in [home, away] and "Sport" in event:
        return time, player_number, "Sport / PE"
    if "Central / PE" in [home, away] and "Central" in event:
        return time, player_number, "Central / PE"
    if "Santa Cruz / PE" in [home, away] and "Santa Cruz" in event:
        return time, player_number, "Santa Cruz / PE"
    if "Ypiranga / PE" in [home, away] and "Ypiranga" in event:
        return time, player_number, "Ypiranga / PE"
    if "Náutico / PE" in [home, away] and "Náutico" in event:
        return time, player_number, "Náutico / PE"
    if "Confiança / SE" in [home, away] and "Confiança" in event:
        return time, player_number, "Confiança / SE"
    if "Sergipe / SE" in [home, away] and "Sergipe" in event:
        return time, player_number, "Sergipe / SE"
    if "ASA / AL" in [home, away] and "A.s.a." in event:
        return time, player_number, "ASA / AL"
    if "CSA / AL" in [home, away] and "C.s.a." in event:
        return time, player_number, "CSA / AL"
    if "CRB / AL" in [home, away] and "C.r.b." in event:
        return time, player_number, "CRB / AL"
    if "Botafogo / PB" in [home, away] and "Botafogo" in event:
        return time, player_number, "Botafogo / PB"
    if "Treze / PB" in [home, away] and "Treze" in event:
        return time, player_number, "Treze / PB"
    if "Parnahyba / PI" in [home, away] and "Parnahyba" in event:
        return time, player_number, "Parnahyba / PI"
    if "Sampaio Corrêa / MA" in [home, away] and "Sampaio Correa" in event:
        return time, player_number, "Sampaio Corrêa / MA"
    if "Maranhão / MA" in [home, away] and "Maranhão" in event:
        return time, player_number, "Maranhão / MA"
    if "Cuiabá / MT" in [home, away] and "Cuiabá" in event:
        return time, player_number, "Cuiabá / MT"
    if "Luverdense / MT" in [home, away] and "Luverdense" in event:
        return time, player_number, "Luverdense / MT"
    if "Mixto / MT" in [home, away] and "Mixto" in event:
        return time, player_number, "Mixto / MT"
    if "Naviraiense / MS" in [home, away] and "Naviraiense" in event:
        return time, player_number, "Naviraiense / MS"
    if "Águia Negra / MS" in [home, away] and "Aguia Negra" in event:
        return time, player_number, "Águia Negra / MS"
    if "Goiás / GO" in [home, away] and "Goiás" in event:
        return time, player_number, "Goiás / GO"
    if "Aparecidense / GO" in [home, away] and "Aparecidense" in event:
        return time, player_number, "Aparecidense / GO"
    if "CRAC / GO" in [home, away] and "C.r.a.c." in event:
        return time, player_number, "CRAC / GO"
    if "Goianesia / GO" in [home, away] and "Goianesia" in event:
        return time, player_number, "Goianesia / GO"
    if "Vila Nova / GO" in [home, away] and "Vila Nova" in event:
        return time, player_number, "Vila Nova / GO"
    if "Atlético / GO" in [home, away] and "Atlético" in event:
        return time, player_number, "Atlético / GO"
    if "Brasília / DF" in [home, away] and "Brasília" in event:
        return time, player_number, "Brasília / DF"
    if "Brasiliense / DF" in [home, away] and "Brasiliense" in event:
        return time, player_number, "Brasiliense / DF"
    if "Nacional / AM" in [home, away] and "Nacional" in event:
        return time, player_number, "Nacional / AM"
    if "Ypiranga / AP" in [home, away] and "Ypiranga" in event:
        return time, player_number, "Ypiranga / AP"
    if "Paysandu / PA" in [home, away] and "Paysandu" in event:
        return time, player_number, "Paysandu / PA"
    if "Águia de Marabá / PA" in [home, away] and "Aguia" in event:
        return time, player_number, "Águia de Marabá / PA"
    if "Paragominas / PA" in [home, away] and "Paragominas" in event:
        return time, player_number, "Paragominas / PA"
    if "Gurupi / TO" in [home, away] and "Gurupi" in event:
        return time, player_number, "Gurupi / TO"
    if "Plácido de Castro / AC" in [home, away] and "Plácido de Castro" in event:
        return time, player_number, "Plácido de Castro / AC"
    if "Rio Branco / AC" in [home, away] and "Rio Branco" in event:
        return time, player_number, "Rio Branco / AC"
    if "Genus / RO" in [home, away] and "Genus" in event:
        return time, player_number, "Genus / RO"
    if "Nautico / RR" in [home, away] and "Nautico" in event:
        return time, player_number, "Nautico / RR"

    raise NotImplementedError(
        f"Couldn't parse event {event} in game between {home} and {away}"
    )


def treat_game_events(events, home, away):
    """
    Treats the game events list by applying the treat_event function to each event.
    Sorts the events list based on the time of each event.

    Args:
        events (list): A list of events in the string format.
        home (str): The name of the home team.
        away (str): The name of the away team.

    Returns:
        list: The treated and sorted events list.
    """

    for i in range(len(events)):
        events[i] = treat_event(events[i], home, away)
    events = sorted(events, key=lambda x: x[0])

    return events


def find_changes(text):
    """
    Finds and extracts the substitutions from the given text.

    Args:
        text (str): The text containing the substitutions.

    Returns:
        list: A list of substitution strings.
    """

    text = text[text.find("Substituições") :]
    text = treat_club(text)
    regex = "\d{2}:\d{2}\s*\dT[a-zA-ZÀ-ÿ\-\.\s]+\/[A-Z]{2}\s*"
    regex += "\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\.\s]+\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\. ]+|"
    regex += "\d{2}:\d{2}\s*[a-zA-ZÀ-ÿ\-\.\s]+\/[A-Z]{2}\s*"
    regex += "\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\.\s]+\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\. ]+|"
    regex += "\d{2}:\d{2}\s*[a-zA-ZÀ-ÿ\-\.\s]+\s*"
    regex += "\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\.\s]+\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\. ]+|"
    regex += "\d{2}:\d{2}\s*\dT\s*[a-zA-ZÀ-ÿ\-\.\s]+\s*"
    regex += "\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\.\s]+\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\. ]+"
    subs = re.findall(regex, text)

    return subs


def treat_change(change, home, away):
    """
    Treats a single substitution change string by extracting relevant information.

    Args:
        change (str): The substitution change string.
        home (str): The name of the home team.
        away (str): The name of the away team.

    Returns:
        tuple: A tuple containing the treated substitution information in the format (club, time, player_in, player_out).
    """

    if " / " not in change:
        if " /" in change:
            change = change.replace(" /", " / ")
        elif "/ " in change:
            change = change.replace("/ ", " / ")
        elif "/" in change:
            change = change.replace("/", " / ")

    if "1T" not in change and "2T" not in change and "INT" not in change:
        change = change.replace(":00", ":00 2T")
    change = treat_club(change)
    time_string = re.findall("\d+:\d+\s*[0-9A-Z]+T", change)[0].replace("TT", "T")
    time = treat_time(time_string)
    subs = re.findall("\d+", change[len(time_string) :])
    player_in, player_out = subs
    if home in change:
        return home, time, player_in, player_out
    elif away in change:
        return away, time, player_in, player_out

    club = re.findall("T([a-zA-ZÀ-ÿ\s\.\-\/]+)\d", change)[0]
    club = club.replace(".", "").strip()
    if club in home and club not in away:
        return home, time, player_in, player_out
    elif club not in home and club in away:
        return away, time, player_in, player_out
    if "Macaé / RJ" in [home, away] and club == "Macae":
        return "Macaé / RJ", time, player_in, player_out
    if "Real Noroeste / ES" in [home, away] and club == "Real Noroeste Capixaba F":
        return "Real Noroeste / ES", time, player_in, player_out
    if "Caxias / RS" in [home, away] and club == "Caxias":
        return "Caxias / RS", time, player_in, player_out
    if "Athletico Paranaense / PR" in [home, away] and club == "Atlético":
        return "Athletico Paranaense / PR", time, player_in, player_out
    if "J. Malucelli / PR" in [home, away] and club == "J Malucelli":
        return "J. Malucelli / PR", time, player_in, player_out
    if "Criciúma / SC" in [home, away] and club == "Criciuma":
        return "Criciúma / SC", time, player_in, player_out
    if "Avaí / SC" in [home, away] and club == "AVAÍ":
        return "Avaí / SC", time, player_in, player_out
    if "Hercilio Luz / SC" in [home, away] and club == "Hercilio Luz Futebol Clube":
        return "Hercilio Luz / SC", time, player_in, player_out
    if "ASA / AL" in [home, away] and club == "Asa":
        return "ASA / AL", time, player_in, player_out
    if "CRB / AL" in [home, away] and club == "Crb":
        return "CRB / AL", time, player_in, player_out
    if "CSA / AL" in [home, away] and club == "Csa":
        return "CSA / AL", time, player_in, player_out
    if "ABC / RN" in [home, away] and club == "Abc":
        return "ABC / RN", time, player_in, player_out
    if "Águia Negra / MS" in [home, away] and club == "Aguia Negra":
        return "Águia Negra / MS", time, player_in, player_out
    if "CRAC / GO" in [home, away] and club == "Crac":
        return "CRAC / GO", time, player_in, player_out
    if "Sampaio Corrêa / MA" in [home, away] and club == "Sampaio Correa":
        return "Sampaio Corrêa / MA", time, player_in, player_out
    if "Águia de Marabá / PA" in [home, away] and club == "Aguia":
        return "Águia de Marabá / PA", time, player_in, player_out
    if "Maringá / PR" in [home, away] and club == "Maringá Sa":
        return "Maringá / PR", time, player_in, player_out

    return club, time, player_in, player_out


def treat_game_changes(changes, home, away):
    """
    Treats the game changes list by applying the treat_change function to each change.
    Sorts the changes list based on the time of each change.

    Args:
        changes (list): A list of substitution changes.
        home (str): The name of the home team.
        away (str): The name of the away team.

    Returns:
        list: The treated and sorted changes list.
    """

    for i in range(len(changes)):
        changes[i] = treat_change(changes[i], home, away)
    changes = sorted(changes, key=lambda x: x[1])
    return changes
