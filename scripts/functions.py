import re
import os

def clear():
    os.system('clear')

def treat_time(time_string):
    time = 0
    if '2T' in time_string: time += 45
    if '+' in time_string: time += 45
    else: time += int(time_string[:2])
    
    return time

def treat_club(club):
    club = club.replace('Saf ', '')
    club = club.replace('S.a.f ', '')
    club = club.replace('S.A.F ', '')
    club = club.replace('S.a.f. ', '')
    club = club.replace('S.A.F. ', '')
    club = club.replace('Fc ', '')
    club = club.replace('FC ', '')
    club = club.replace('Futebol Clube ', '')
    club = club.replace('FUTEBOL CLUBE ', '')
    club = club.replace('F. C. ', '')
    club = club.replace('A.c. ', '')
    club = club.replace('Ltda ', '')
    club = club.replace('Associacao Desportiva ', '')
    club = club.replace('Esporte Clube ', '')
    club = club.replace('Sociedade Esportiva ', '')
    club = club.replace('-ap', '')
    club = club.replace('Sport Club ', '')
    club = club.replace('- Vn ', '')
    club = club.replace('- VN ', '')
    club = club.replace('Atletico', 'Atlético')
    club = club.replace('Vitoria', 'Vitória')
    club = club.replace('A.b.c. / RN', 'ABC / RN')
    club = club.replace('Abc / RN', 'ABC / RN')
    club = club.replace('AVAÍ / SC', 'Avaí / SC')
    club = club.replace('A.s.a. / AL', 'ASA / AL')
    club = club.replace('America / MG', 'América / MG')
    club = club.replace('América de Natal / RN', 'América / RN')
    club = club.replace('AMÉRICA / RN', 'América / RN')
    club = club.replace('Atlético / PR', 'Athletico Paranaense / PR')
    club = club.replace('ATLETICO / PR', 'Athletico Paranaense / PR')
    club = club.replace('Atlético / PR', 'Athletico Paranaense / PR')
    club = club.replace('Sobradinho (df) / DF', 'Sobradinho / DF')
    club = club.replace('ÁGUIA NEGRA / MS', 'Águia Negra / MS')
    club = club.replace('Aguia Negra / MS', 'Águia Negra / MS')
    club = club.replace('Aguia / PA', 'Águia de Marabá / PA')
    club = club.replace('Ypiranga Rs / RS', 'Ypiranga / RS')
    club = club.replace('Villa Nova A.c. / MG', 'Villa Nova / MG')
    club = club.replace('Veranopolis / RS', 'Veranópolis / RS')
    club = club.replace('União / MT', 'União de Rondonópolis / MT')
    club = club.replace('Ser Caxias / RS', 'Caxias / RS')
    club = club.replace('Sampaio Correa / MA', 'Sampaio Corrêa / MA')
    club = club.replace('SAMPAIO CORREA / MA', 'Sampaio Corrêa / MA')
    club = club.replace('SANTOS / SP', 'Santos / SP')
    club = club.replace('Bragantino / SP', 'Red Bull Bragantino / SP')
    club = club.replace('MURICI / AL', 'Murici / AL')
    club = club.replace('River / PI', 'Ríver / PI')
    club = club.replace('River A.c. / PI', 'Ríver / PI')
    club = club.replace('RÍVER / PI', 'Ríver / PI')
    club = club.replace('REAL NOROESTE / ES', 'Real Noroeste / ES')
    club = club.replace('Real Noroeste Capixaba / ES', 'Real Noroeste / ES')
    club = club.replace('PONTE PRETA / SP', 'Ponte Preta / SP')
    club = club.replace('PIAUÍ / PI', 'Piauí / PI')
    club = club.replace('Operario / PR', 'Operário / PR')
    club = club.replace('Luziania / DF', 'Luziânia / DF')
    club = club.replace('INDEPENDENTE / PA', 'Independente / PA')
    club = club.replace('Independente Tucuruí / PA', 'Independente / PA')
    club = club.replace('Guarany de Sobral / CE', 'Guarany / CE')
    club = club.replace('Guarani de Juazeiro / CE', 'Guarani / CE')
    club = club.replace('Crb / AL', 'CRB / AL')
    club = club.replace('Criciuma / SC', 'Criciúma / SC')
    club = club.replace('Csa / AL', 'CSA / AL')
    club = club.replace('FIGUEIRENSE / SC', 'Figueirense / SC')
    club = club.replace('FORTALEZA / CE', 'Fortaleza / CE')
    club = club.replace('C. R. B. / AL', 'CRB / AL')
    club = club.replace('C.r.a.c. / GO', 'CRAC / GO')
    club = club.replace('C.r.b. / AL', 'CRB / AL')
    club = club.replace('C.s.a. / AL', 'CSA / AL')
    club = club.replace('CAXIAS / RS', 'Caxias / RS')
    club = club.replace('CORITIBA / PR', 'Coritiba / PR')
    club = club.replace('CRICIÚMA / SC', 'Criciúma / SC')
    club = club.replace('Atlético Cearense / CE', 'Atlético / CE')
    club = club.replace('Atlético Roraima / RR', 'Atlético / RR')
    club = club.replace('BOTAFOGO / PB', 'Botafogo / PB')
    club = club.replace('BOTAFOGO / RJ', 'Botafogo / RJ')
    club = club.replace('Asa / AL', 'ASA / AL')
    club = club.replace('A.s.s.u. / RN', 'ASSU / RN')
    club = club.replace('Xv de Piracicaba / SP', 'XV de Piracicaba / SP')
    club = club.replace('Urt / MG', 'URT / MG')
    club = club.replace('Arapongas Esporte Clube / PR', 'Arapongas / PR')
    club = club.replace('Jacobina Ec / BA', 'Jacobina / BA')
    club = club.replace('Ge Juventus / SC', 'Juventus / SC')
    club = club.replace('TREZE / PB', 'Treze / PB')
    club = club.replace('S.francisco / PA', 'S. Francisco / PA')
    club = club.replace('Pstc / PR', 'PSTC / PR')
    club = club.replace('Prospera / SC', 'Próspera / SC')
    club = club.replace('Marilia / SP', 'Marília / SP')
    club = club.replace('Macae / RJ', 'Macaé / RJ')
    club = club.replace('Macapa / AP', 'Macapá / AP')
    club = club.replace('G.a.s / RR', 'G.A.S. / RR')
    club = club.replace('Cse / AL', 'CSE / AL')
    club = club.replace('Ca Patrocinense / MG', 'Atlético Patrocinense / MG')
    
    return club
    
def treat_round_35_sB(club):
    club = treat_club(club)
    club = club.replace('A.s.a. /  ', 'ASA / AL')
    club = club.replace('Avaí / ', 'Avaí / SC')
    club = club.replace('Boa /  ', 'Boa / MG')
    club = club.replace('Paraná /  ', 'Paraná / PR')
    club = club.replace('Figueirense /  ', 'Figueirense / SC')
    club = club.replace('Guaratinguetá / ', 'Guaratinguetá / SP')
    club = club.replace('Chapecoense / ', 'Chapecoense / SC')
    club = club.replace('América /  ', 'América / RN')
    club = club.replace('Ceará /  ', 'Ceará / CE')
    club = club.replace('Sport / ', 'Sport / PE')
    club = club.replace('A.b.c. / ', 'ABC / RN')
    club = club.replace('Icasa / ', 'Icasa / CE')
    club = club.replace('Palmeiras / ', 'Palmeiras / SP')
    club = club.replace('Joinville /  ', 'Joinville / SC')
    club = club.replace('São Caetano / ', 'São Caetano / SP')
    club = club.replace('América /  ', 'América / MG')
    club = club.replace('Bragantino /  ', 'Red Bull Bragantino / SP')
    club = club.replace('Atlético /  ', 'Atlético / GO')
    club = club.replace('Paysandu /  ', 'Paysandu / PA')
    club = club.replace('Oeste / ', 'Oeste / SP')
    
    return club
    
def catch_teams(text):
    if 'Campeonato: Campeonato Brasileiro - Série B / 2013 Rodada: 35 ' in text: text = treat_round_35_sB(text)
    else: text = treat_club(text)
    return re.findall('Jogo:\s*([a-zA-Z0-9À-ÿ\s\.\-]+\s*\/\s*[A-Z]{2})\s*X\s*([a-zA-Z0-9À-ÿ\s\.\-]+\s*\/\s*[A-Z]{2})', text)

def final_result(text):
    result = re.findall('Resultado\s*Final:\s*(\d+\s*[xX]\s*\d+)', text)
    if len(result) == 0: result = re.findall('Resultado\s*do\s*2º\s*Tempo:\s*(\d+\s*[xX]\s*\d+)', text)
    
    return result

def catch_players(text):
    club_1, club_2 = catch_teams(text)[0]
    club = club_1
    text = text[text.find('Relação de Jogadores'):text.find('Comissão Técnica')]
    goalkeepers = re.findall('CBF\n(\d+\D+[P|A|)|T|R]\s*\d{6})', text)
    for goalkeeper in goalkeepers:
        if 'T(g)' in goalkeeper: continue
        text = text.replace(goalkeeper[-10:], goalkeeper[-10:].replace('TP', 'T(g)P'))
    
    players = re.findall('\n(\d+.+[P|A|)|T|R]\s*\d{6})', text)
    for i in range(len(players)):
        if i > 0 and 'T(g)' in players[i]: club = club_2
        players[i] = [players[i], club]
        
    if players[0][1] == players[-1][1]:
        numbers = []
        changed = False
        for i in range(len(players)):
            number = re.findall('\d+', players[i][0])[0]
            if len(number) == 3:
                if number[1] == '0':
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
    game_players = {home : {}, away : {}}
    for player in players:
        player, club = player
        numbers = re.findall('\d+', player)
        shirt, cod = numbers[0], numbers[-1]
        game_players[club][shirt] = cod
        
    return game_players

def catch_goals(text):
    result = final_result(text)
    text = text[text.find('Gols'):text.find('Cartões Amarelos')]
    if len(result) == 0: return []
    result = result[0].split()
    
    # normal time
    goals  = re.findall('\d{2}:\d{2}\s*\dT\s*\d+\s*NR[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*\d+\s*PN[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*\d+\s*CT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*\d+\s*FT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    
    # without player number
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*NR[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*PN[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*CT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*FT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    
    # extra time
    goals += re.findall('\+\d+\s*\dT\s*\d+\s*NR[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\+\d+\s*\dT\s*\d+\s*PN[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\+\d+\s*\dT\s*\d+\s*CT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\+\d+\s*\dT\s*\d+\s*FT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    
    # without player number
    goals += re.findall('\+\d+\s*\dT\s*NR[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\+\d+\s*\dT\s*PN[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\+\d+\s*\dT\s*CT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    goals += re.findall('\+\d+\s*\dT\s*FT[a-zA-ZÀ-ÿ\-\. 0-9]+\/[A-Z]{2}', text)
    
    if len(goals) == int(result[0]) + int(result[-1]): return goals
    
    # normal time
    goals  = re.findall('\d{2}:\d{2}\s*\dT\s*\d+\s*NR[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*\d+\s*PN[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*\d+\s*CT[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*\d+\s*FT[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    
    # without player number
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*NR[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*PN[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*CT[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\d{2}:\d{2}\s*\dT\s*FT[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    
    # extra time
    goals += re.findall('\+\d+\s*\dT\s*\d+\s*NR[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\+\d+\s*\dT\s*\d+\s*PN[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\+\d+\s*\dT\s*\d+\s*CT[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\+\d+\s*\dT\s*\d+\s*FT[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    
    # without player number
    goals += re.findall('\+\d+\s*\dT\s*NR[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\+\d+\s*\dT\s*PN[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\+\d+\s*\dT\s*CT[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    goals += re.findall('\+\d+\s*\dT\s*FT[a-zA-ZÀ-ÿ\-\. 0-9]+', text)
    
    return goals
    
def treat_goal(goal, home, away):
    if ' / ' not in goal:
        if ' /' in goal: goal = goal.replace(' /', ' / ')
        elif '/ ' in goal: goal = goal.replace('/ ', ' / ')
        elif '/' in goal: goal = goal.replace('/', ' / ')
    
    goal = treat_club(goal)
    if '1T' not in goal and '2T' not in goal:
        if '3T' in goal: goal = goal.replace('3T', '2T')
        elif '0T' in goal: goal = goal.replace('0T', '1T')
    
    time_string = re.findall('\d+:\d+\s*[A-Z0-9]+T|\+\d+\s*\dT', goal)[0]
    time = treat_time(time_string)
    if home in goal and away not in goal: return time, home
    elif home not in goal and away in goal: return time, away
    
    if 'Flamengo / RJ' in [home, away] and 'Flamengo' in goal: return time, 'Flamengo / RJ'
    if 'Vasco da Gama / RJ' in [home, away] and 'Vasco da Gama' in goal: return time, 'Vasco da Gama / RJ'
    if 'Fluminense / RJ' in [home, away] and 'Fluminense' in goal: return time, 'Fluminense / RJ'
    if 'Botafogo / RJ' in [home, away] and 'Botafogo' in goal: return time, 'Botafogo / RJ'
    if 'Madureira / RJ' in [home, away] and 'Madureira' in goal: return time, 'Madureira / RJ'
    if 'Resende / RJ' in [home, away] and 'Resende' in goal: return time, 'Resende / RJ'
    if 'Nova Iguaçu / RJ' in [home, away] and 'Nova Iguaçu' in goal: return time, 'Nova Iguaçu / RJ'
    if 'Macaé / RJ' in [home, away] and 'Macae' in goal: return time, 'Macaé / RJ'
    if 'Duque de Caxias / RJ' in [home, away] and 'Duque de Caxias' in goal: return time, 'Duque de Caxias / RJ'
    if 'Palmeiras / SP' in [home, away] and 'Palmeiras' in goal: return time, 'Palmeiras / SP'
    if 'São Paulo / SP' in [home, away] and 'São Paulo' in goal: return time, 'São Paulo / SP'
    if 'Corinthians / SP' in [home, away] and 'Corinthians' in goal: return time, 'Corinthians / SP'
    if 'Santos / SP' in [home, away] and 'Santos' in goal: return time, 'Santos / SP'
    if 'Red Bull Bragantino / SP' in [home, away] and 'Bragantino' in goal: return time, 'Red Bull Bragantino / SP'
    if 'Sao Bernardo / SP' in [home, away] and 'Sao Bernardo' in goal: return time, 'Sao Bernardo / SP'
    if 'São Bento / SP' in [home, away] and 'São Bento' in goal: return time, 'São Bento / SP'
    if 'Ponte Preta / SP' in [home, away] and 'Ponte Preta' in goal: return time, 'Ponte Preta / SP'
    if 'Portuguesa / SP' in [home, away] and 'Portuguesa' in goal: return time, 'Portuguesa / SP'
    if 'Santo André / SP' in [home, away] and 'Santo André' in goal: return time, 'Santo André / SP'
    if 'São Caetano / SP' in [home, away] and 'São Caetano' in goal: return time, 'São Caetano / SP'
    if 'Penapolense / SP' in [home, away] and 'Penapolense' in goal: return time, 'Penapolense / SP'
    if 'Botafogo / SP' in [home, away] and 'Botafogo' in goal: return time, 'Botafogo / SP'
    if 'Grêmio Barueri / SP' in [home, away] and 'Grêmio Barueri' in goal: return time, 'Grêmio Barueri / SP'
    if 'Mogi Mirim / SP' in [home, away] and 'Mogi Mirim' in goal: return time, 'Mogi Mirim / SP'
    if 'Guarani / SP' in [home, away] and 'Guarani' in goal: return time, 'Guarani / SP'
    if 'Oeste / SP' in [home, away] and 'Oeste' in goal: return time, 'Oeste / SP'
    if 'Guaratinguetá / SP' in [home, away] and 'Guaratinguetá' in goal: return time, 'Guaratinguetá / SP'
    if 'Atlético / MG' in [home, away] and 'Atlético' in goal: return time, 'Atlético / MG'
    if 'América / MG' in [home, away] and 'América' in goal: return time, 'América / MG'
    if 'Cruzeiro / MG' in [home, away] and 'Cruzeiro' in goal: return time, 'Cruzeiro / MG'
    if 'Villa Nova / MG' in [home, away] and 'Villa Nova' in goal: return time, 'Villa Nova / MG'
    if 'Tupi / MG' in [home, away] and 'Tupi' in goal: return time, 'Tupi / MG'
    if 'Araxá / MG' in [home, away] and 'Araxá' in goal: return time, 'Araxá / MG'
    if 'Betim / MG' in [home, away] and 'Betim' in goal: return time, 'Betim / MG'
    if 'Boa / MG' in [home, away] and 'Boa' in goal: return time, 'Boa / MG'
    if 'Aracruz / ES' in [home, away] and 'Aracruz' in goal: return time, 'Aracruz / ES'
    if 'Internacional / RS' in [home, away] and 'Internacional' in goal: return time, 'Internacional / RS'
    if 'Grêmio / RS' in [home, away] and 'Grêmio' in goal: return time, 'Grêmio / RS'
    if 'Juventude / RS' in [home, away] and 'Juventude' in goal: return time, 'Juventude / RS'
    if 'Lajeadense / RS' in [home, away] and 'Lajeadense' in goal: return time, 'Lajeadense / RS'
    if 'Caxias / RS' in [home, away] and 'Caxias' in goal: return time, 'Caxias / RS'
    if 'Athletico Paranaense / PR' in [home, away] and 'Atlético' in goal: return time, 'Athletico Paranaense / PR'
    if 'Coritiba / PR' in [home, away] and 'Coritiba' in goal: return time, 'Coritiba / PR'
    if 'Paraná / PR' in [home, away] and 'Paraná' in goal: return time, 'Paraná / PR'
    if 'Arapongas / PR' in [home, away] and 'Arapongas' in goal: return time, 'Arapongas / PR'
    if 'Londrina / PR' in [home, away] and 'Londrina' in goal: return time, 'Londrina / PR'
    if 'J. Malucelli / PR' in [home, away] and 'J. Malucelli' in goal: return time, 'J. Malucelli / PR'
    if 'Chapecoense / SC' in [home, away] and 'Chapecoense' in goal: return time, 'Chapecoense / SC'
    if 'Figueirense / SC' in [home, away] and 'Figueirense' in goal: return time, 'Figueirense / SC'
    if 'Criciúma / SC' in [home, away] and 'Criciuma' in goal: return time, 'Criciúma / SC'
    if 'Avaí / SC' in [home, away] and 'AVAÍ' in goal: return time, 'Avaí / SC'
    if 'Metropolitano / SC' in [home, away] and 'Metropolitano' in goal: return time, 'Metropolitano / SC'
    if 'Marcílio Dias / SC' in [home, away] and 'Marcílio Dias' in goal: return time, 'Marcílio Dias / SC'
    if 'Avaí / SC' in [home, away] and 'Avaí' in goal: return time, 'Avaí / SC'
    if 'Joinville / SC' in [home, away] and 'Joinville' in goal: return time, 'Joinville / SC'
    if 'Fortaleza / CE' in [home, away] and 'Fortaleza' in goal: return time, 'Fortaleza / CE'
    if 'Ceará / CE' in [home, away] and 'Ceará' in goal: return time, 'Ceará / CE'
    if 'Icasa / CE' in [home, away] and 'Icasa' in goal: return time, 'Icasa / CE'
    if 'Tiradentes / CE' in [home, away] and 'Tiradentes' in goal: return time, 'Tiradentes / CE'
    if 'Guarany / CE' in [home, away] and 'Guarany' in goal: return time, 'Guarany / CE'
    if 'Vitória da Conquista / BA' in [home, away] and 'Vitória da Conquista' in goal: return time, 'Vitória da Conquista / BA'
    if 'Vitória / BA' in [home, away] and 'Vitória' in goal: return time, 'Vitória / BA'
    if 'Bahia / BA' in [home, away] and 'Bahia' in goal: return time, 'Bahia / BA'
    if 'Juazeirense / BA' in [home, away] and 'Juazeirense' in goal: return time, 'Juazeirense / BA'
    if 'ABC / RN' in [home, away] and 'A.b.c.' in goal: return time, 'ABC / RN'
    if 'América / RN' in [home, away] and 'América' in goal: return time, 'América / RN'
    if 'Potiguar / RN' in [home, away] and 'Potiguar' in goal: return time, 'Potiguar / RN'
    if 'Baraúnas / RN' in [home, away] and 'Baraúnas' in goal: return time, 'Baraúnas / RN'
    if 'Salgueiro / PE' in [home, away] and 'Salgueiro' in goal: return time, 'Salgueiro / PE'
    if 'Sport / PE' in [home, away] and 'Sport' in goal: return time, 'Sport / PE'
    if 'Central / PE' in [home, away] and 'Central' in goal: return time, 'Central / PE'
    if 'Santa Cruz / PE' in [home, away] and 'Santa Cruz' in goal: return time, 'Santa Cruz / PE'
    if 'Ypiranga / PE' in [home, away] and 'Ypiranga' in goal: return time, 'Ypiranga / PE'
    if 'Náutico / PE' in [home, away] and 'Náutico' in goal: return time, 'Náutico / PE'
    if 'Confiança / SE' in [home, away] and 'Confiança' in goal: return time, 'Confiança / SE'
    if 'Sergipe / SE' in [home, away] and 'Sergipe' in goal: return time, 'Sergipe / SE'
    if 'ASA / AL' in [home, away] and 'A.s.a.' in goal: return time, 'ASA / AL'
    if 'CSA / AL' in [home, away] and 'C.s.a.' in goal: return time, 'CSA / AL'
    if 'CRB / AL' in [home, away] and 'C.r.b.' in goal: return time, 'CRB / AL'
    if 'Botafogo / PB' in [home, away] and 'Botafogo' in goal: return time, 'Botafogo / PB'
    if 'Treze / PB' in [home, away] and 'Treze' in goal: return time, 'Treze / PB'
    if 'Parnahyba / PI' in [home, away] and 'Parnahyba' in goal: return time, 'Parnahyba / PI'
    if 'Sampaio Corrêa / MA' in [home, away] and 'Sampaio Correa' in goal: return time, 'Sampaio Corrêa / MA'
    if 'Maranhão / MA' in [home, away] and 'Maranhão' in goal: return time, 'Maranhão / MA'
    if 'Cuiabá / MT' in [home, away] and 'Cuiabá' in goal: return time, 'Cuiabá / MT'
    if 'Luverdense / MT' in [home, away] and 'Luverdense' in goal: return time, 'Luverdense / MT'
    if 'Mixto / MT' in [home, away] and 'Mixto' in goal: return time, 'Mixto / MT'
    if 'Naviraiense / MS' in [home, away] and 'Naviraiense' in goal: return time, 'Naviraiense / MS'
    if 'Águia Negra / MS' in [home, away] and 'Aguia Negra' in goal: return time, 'Águia Negra / MS'
    if 'Goiás / GO' in [home, away] and 'Goiás' in goal: return time, 'Goiás / GO'
    if 'Aparecidense / GO' in [home, away] and 'Aparecidense' in goal: return time, 'Aparecidense / GO'
    if 'CRAC / GO' in [home, away] and 'C.r.a.c.' in goal: return time, 'CRAC / GO'
    if 'Goianesia / GO' in [home, away] and 'Goianesia' in goal: return time, 'Goianesia / GO'
    if 'Vila Nova / GO' in [home, away] and 'Vila Nova' in goal: return time, 'Vila Nova / GO'
    if 'Atlético / GO' in [home, away] and 'Atlético' in goal: return time, 'Atlético / GO'
    if 'Brasília / DF' in [home, away] and 'Brasília' in goal: return time, 'Brasília / DF'
    if 'Brasiliense / DF' in [home, away] and 'Brasiliense' in goal: return time, 'Brasiliense / DF'
    if 'Nacional / AM' in [home, away] and 'Nacional' in goal: return time, 'Nacional / AM'
    if 'Ypiranga / AP' in [home, away] and 'Ypiranga' in goal: return time, 'Ypiranga / AP'
    if 'Paysandu / PA' in [home, away] and 'Paysandu' in goal: return time, 'Paysandu / PA'
    if 'Águia de Marabá / PA' in [home, away] and 'Aguia' in goal: return time, 'Águia de Marabá / PA'
    if 'Paragominas / PA' in [home, away] and 'Paragominas' in goal: return time, 'Paragominas / PA'
    if 'Gurupi / TO' in [home, away] and 'Gurupi' in goal: return time, 'Gurupi / TO'
    if 'Plácido de Castro / AC' in [home, away] and 'Plácido de Castro' in goal: return time, 'Plácido de Castro / AC'
    if 'Rio Branco / AC' in [home, away] and 'Rio Branco' in goal: return time, 'Rio Branco / AC'
    if 'Genus / RO' in [home, away] and 'Genus' in goal: return time, 'Genus / RO'
    if 'Nautico / RR' in [home, away] and 'Nautico' in goal: return time, 'Nautico / RR'

    return time, goal
    
def treat_game_goals(goals, home, away):
    for i in range(len(goals)): goals[i] = treat_goal(goals[i], home, away)
    goals = sorted(goals, key = lambda x : x[0])
    
    return goals
    
def find_changes(text):
    text = text[text.find('Substituições'):]
    text = treat_club(text)
    regex  = '\d{2}:\d{2}\s*\dT[a-zA-ZÀ-ÿ\-\.\s]+\/[A-Z]{2}\s*'
    regex += '\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\.\s]+\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\. ]+|'
    regex += '\d{2}:\d{2}\s*[a-zA-ZÀ-ÿ\-\.\s]+\/[A-Z]{2}\s*'
    regex += '\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\.\s]+\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\. ]+|'
    regex += '\d{2}:\d{2}\s*[a-zA-ZÀ-ÿ\-\.\s]+\s*'
    regex += '\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\.\s]+\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\. ]+|'
    regex += '\d{2}:\d{2}\s*\dT\s*[a-zA-ZÀ-ÿ\-\.\s]+\s*'
    regex += '\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\.\s]+\d+\s*\-\s*[a-zA-ZÀ-ÿ\-\. ]+'
    subs = re.findall(regex, text)
    
    return subs
    
def treat_change(change, home, away):
    if ' / ' not in change:
        if ' /' in change: change = change.replace(' /', ' / ')
        elif '/ ' in change: change = change.replace('/ ', ' / ')
        elif '/' in change: change = change.replace('/', ' / ')
            
    if '1T' not in change and '2T' not in change and 'INT' not in change: change = change.replace(':00', ':00 2T')
    change = treat_club(change)
    time_string = re.findall('\d+:\d+\s*[0-9A-Z]+T', change)[0].replace('TT', 'T')
    time = treat_time(time_string)
    subs = re.findall('\d+', change[len(time_string):])
    player_in, player_out = subs
    if home in change: return home, time, player_in, player_out
    elif away in change: return away, time, player_in, player_out
    
    club = re.findall('T([a-zA-ZÀ-ÿ\s\.\-]+)\d', change)[0]
    club = club.replace('.', '').strip()
    if club in home and club not in away: return home, time, player_in, player_out
    elif club not in home and club in away: return away, time, player_in, player_out
    if 'Macaé / RJ' in [home, away] and club == 'Macae': return 'Macaé / RJ', time, player_in, player_out
    if 'Real Noroeste / ES' in [home, away] and club == 'Real Noroeste Capixaba F': return 'Real Noroeste / ES', time, player_in, player_out
    if 'Caxias / RS' in [home, away] and club == 'Caxias': return 'Caxias / RS', time, player_in, player_out
    if 'Athletico Paranaense / PR' in [home, away] and club == 'Atlético': return 'Athletico Paranaense / PR', time, player_in, player_out
    if 'J. Malucelli / PR' in [home, away] and club == 'J Malucelli': return 'J. Malucelli / PR', time, player_in, player_out
    if 'Criciúma / SC' in [home, away] and club == 'Criciuma': return 'Criciúma / SC', time, player_in, player_out
    if 'Avaí / SC' in [home, away] and club == 'AVAÍ': return 'Avaí / SC', time, player_in, player_out
    if 'Hercilio Luz / SC' in [home, away] and club == 'Hercilio Luz Futebol Clube': return 'Hercilio Luz / SC', time, player_in, player_out
    if 'ASA / AL' in [home, away] and club == 'Asa': return 'ASA / AL', time, player_in, player_out
    if 'CRB / AL' in [home, away] and club == 'Crb': return 'CRB / AL', time, player_in, player_out
    if 'CSA / AL' in [home, away] and club == 'Csa': return 'CSA / AL', time, player_in, player_out
    if 'ABC / RN' in [home, away] and club == 'Abc': return 'ABC / RN', time, player_in, player_out
    if 'Águia Negra / MS' in [home, away] and club == 'Aguia Negra': return 'Águia Negra / MS', time, player_in, player_out
    if 'CRAC / GO' in [home, away] and club == 'Crac': return 'CRAC / GO', time, player_in, player_out
    if 'Sampaio Corrêa / MA' in [home, away] and club == 'Sampaio Correa': return 'Sampaio Corrêa / MA', time, player_in, player_out
    if 'Águia de Marabá / PA' in [home, away] and club == 'Aguia': return 'Águia de Marabá / PA', time, player_in, player_out
    if 'Maringá / PR' in [home, away] and club == 'Maringá Sa': return 'Maringá / PR', time, player_in, player_out
    
    return club, time, player_in, player_out
    
def treat_game_changes(changes, home, away):
    for i in range(len(changes)): changes[i] = treat_change(changes[i], home, away)
    changes = sorted(changes, key = lambda x : x[1])    
    return changes
