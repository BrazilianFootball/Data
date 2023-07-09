from datetime import datetime
from time import time
from scrape import *
import sys
import os

if __name__ == '__main__':
    now = datetime.now()
    os.chdir('../results')
    if now.strftime('%d') == '01':
        for file in glob('../results/*/*/*.json'): os.remove(file)
        min_year = 2013
    
    else: min_year = int(now.strftime('%Y'))
    max_year = int(now.strftime('%Y'))
    competitions = [('CdB',     '424', 180),
                    ('Serie_A', '142', 380),
                    ('Serie_B', '242', 380),
                    ('Serie_C', '342', 214),
                    ('Serie_D', '542', 518)]
    
    if '--c' in sys.argv: cleaning = True
    else: cleaning = False
    
    if '--s' in sys.argv or len(sys.argv) == 1:
        make_directories(competitions, min_year, max_year)
        with open('../auxiliary/scrape.log', 'a') as f:
            f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Scraping] - Beginning docket scraping.\n')
        
        start_scrape = time()
        n = len(glob('../*/*/*/CSVs/*.csv'))
        max_time = 60
        added = 0
        it = 1
        k = 0
        while n != k:
            files = glob('../*/*/*/CSVs/*.csv')
            k = len(files)
            if it == 1: scrape(competitions, min_year, max_year, files, max_time, cleaning = cleaning)
            else: scrape(competitions, min_year, max_year, files, max_time / 2, cleaning = cleaning)
            n = len(glob('../*/*/*/CSVs/*.csv'))
            added += n - k
            it += 1
        
        end_scrape = time()
        with open('../auxiliary/scrape.log', 'a') as f:
            f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Scraping] - Docket scraping complete.\n')
            if added == 0: f.write('                                   [INFO] Already up to date.\n')
            elif added == 1: f.write('                                   [INFO] 1 docket added.\n')
            else: f.write(f'                                   [INFO] {added} dockets addeds.\n')
            
        if added > 0 or '--t' in sys.argv:
            start_extract = time()
            with open('../auxiliary/scrape.log', 'a') as f:
                f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Extract]  - Beginning info extract.\n')
            
            cont_fail = extract(competitions, min_year, max_year, cleaning = cleaning)
            with open('../auxiliary/scrape.log', 'a') as f:
                f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Extract]  - Info extract complete.\n')
                if cont_fail == 1: f.write('                                   [INFO] 1 game failed.\n')
                elif cont_fail > 0: f.write(f'                                   [INFO] {cont_fail} games failed.\n')
                else: f.write('                                   [INFO] Sucess!\n')
                    
                f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Lineups]  - Beginning lineups treatment.\n')
            
            catch_squads(competitions, min_year, max_year, cleaning = cleaning)
            with open('../auxiliary/scrape.log', 'a') as f: f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Lineups]  - Lineups complete.\n')
            
            end_extract = time()
            if cleaning: clear()
            print(f'Scrape complete in {end_scrape - start_scrape:.2f} seconds!',
                  f'Extract complete in {end_extract - start_extract:.2f} seconds!',
                  f'{added} games added.',
                  f'{cont_fail} games failed.',
                  '-' * 58,
                  f'Total time: {end_extract - start_scrape:.2f} seconds.',
                  sep = '\n')
        else:
            if cleaning: clear()
            print(f'Scrape complete in {end_scrape - start_scrape:.2f} seconds!',
                  'Nothing to add.',
                  sep = '\n')
    
    elif '--t' in sys.argv:
        start_extract = time()
        with open('../auxiliary/scrape.log', 'a') as f:
            f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Extract]  - Beginning info extract.\n')
        
        cont_fail = extract(competitions, min_year, max_year, cleaning = cleaning)
        with open('../auxiliary/scrape.log', 'a') as f:
            f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Extract]  - Info extract complete.\n')
            if cont_fail == 1: f.write('                                   [INFO] 1 game failed.\n')
            elif cont_fail > 0: f.write(f'                                   [INFO] {cont_fail} games failed.\n')
            else: f.write('                                   [INFO] Sucess!\n')
                
            f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Lineups]  - Beginning lineups treatment.\n')
        
        catch_squads(competitions, min_year, max_year, cleaning = cleaning)
        with open('../auxiliary/scrape.log', 'a') as f: f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} [Lineups]  - Lineups complete.\n')
            
        end_extract = time()
        if cleaning: clear()
        print(f'Extract complete in {end_extract - start_extract:.2f} seconds!',
              f'{cont_fail} games failed.',
              sep = '\n')
              
    with open('../auxiliary/scrape.log', 'a') as f:
        f.write('\n')
        f.write('-' * 85 + '\n')
        f.write('\n')
