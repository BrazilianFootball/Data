# Brazilian Soccer Data

In Brazil, soccer is a national passion. On 1959, was founded the first Brazillian Championship, named as "Taça Brasil". Since then, we had a lot of name and formats but, after 2001, we have a round-robin system. In 2001 and 2002, we have a playoff with the best 8 clubs of round robin and, in 2003, a full round-robin system was introducted. Furthermore, because the previously systems, between 2001 and 2005 the championship was changing the number os clubs in the competition. In 2006 the championship had 20 clubs, number that didn't change until now.

With technology, CBF (Confederação Brasileira de Futebol, or Brazilian Football Confederation), began to register the games in eletronic dockets, as could be see [here](https://conteudo.cbf.com.br/sumulas/2013/424172se.pdf). Thinking from a perspective of a data sciencist, would be very nice if we had this data avaliable for analysis and to construct models. Them, here we are.

This repository is organized in three main folders:
 - ```auxiliary```: with a `log` file and two `json` with exceptions (manually treated) and number of games for season
 - ```results```: with all data we scraped
 - ```scripts```: with all code we use to scrape this data.

### Know problems

#### We'll fix:
 - We need to add the number of games in file ``number_of_games.json`` to begin extract the data. The idea is remove this file and make the code extract all data without this info (possible generating this info!)
 - Sometimes dockets show wrong data and this fact crash the program. We'll look for this program and will generate an exception, saving the docket and the problem on a info log.

#### Won't fix:
 - Despite saving the docket and the problem on a info log, we won't fix that information.
