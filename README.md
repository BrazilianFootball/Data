# Brazilian Soccer Data

[![DOI](https://zenodo.org/badge/646611229.svg)](https://doi.org/10.5281/zenodo.15207727)

In Brazil, soccer is a national passion. On 1959, was founded the first Brazillian Championship, named as "Taça Brasil". Since then, we had a lot of name and formats but, after 2001, we have a round-robin system. In 2001 and 2002, we have a playoff with the best 8 clubs of round robin and, in 2003, a full round-robin system was introducted. Furthermore, because the previously systems, between 2001 and 2005 the championship was changing the number os clubs in the competition. In 2006 the championship had 20 clubs, number that didn't change until now.

With technology, CBF (Confederação Brasileira de Futebol, or Brazilian Football Confederation), began to register the games in eletronic dockets, as could be see [here](https://conteudo.cbf.com.br/sumulas/2013/424172se.pdf). Thinking from a perspective of a data sciencist, would be very nice if we had this data avaliable for analysis and to construct models. Them, here we are.

This repository is organized in three main folders:
 - ```auxiliary```: with a `log` file and a `json` file with exceptions manually treated
 - ```results```: with all data we scraped
 - ```scripts```: with all code we use to scrape this data.

## Total games

|   Competition   |Total games|Scraped games|
|-----------------|-----------|-------------|
|Brazil Cup (2024)|    122    |     122     |
|Brazil Cup (2025)|    107    |     107     |
|  Serie A (2024) |    380    |     380     |
|  Serie A (2025) |    200    |     187     |
|  Serie B (2024) |    380    |     379     |
|  Serie B (2025) |    220    |     214     |
|  Serie C (2024) |    216    |     216     |
|  Serie C (2025) |    170    |     168     |
|  Serie D (2024) |    510    |     508     |
|  Serie D (2025) |    488    |     484     |
|Brazil Cup (2023)|    122    |     122     |
|Brazil Cup (2024)|    122    |     122     |
|Brazil Cup (2025)|    107    |     107     |
|  Serie A (2013) |    380    |     380     |
|  Serie A (2014) |    380    |     380     |
|  Serie A (2015) |    380    |     380     |
|  Serie A (2016) |    380    |     379     |
|  Serie A (2017) |    380    |     380     |
|  Serie A (2018) |    380    |     380     |
|  Serie A (2019) |    380    |     380     |
|  Serie A (2020) |    380    |     380     |
|  Serie A (2021) |    380    |     380     |
|  Serie A (2022) |    380    |     380     |
|  Serie A (2023) |    380    |     380     |
|  Serie A (2024) |    380    |     375     |
|  Serie A (2025) |    200    |     185     |
|  Serie B (2013) |    380    |     380     |
|  Serie B (2014) |    380    |     379     |
|  Serie B (2015) |    380    |     380     |
|  Serie B (2016) |    380    |     380     |
|  Serie B (2017) |    380    |     380     |
|  Serie B (2018) |    380    |     380     |
|  Serie B (2019) |    380    |     379     |
|  Serie B (2020) |    380    |     379     |
|  Serie B (2021) |    380    |     380     |
|  Serie B (2022) |    380    |     380     |
|  Serie B (2023) |    380    |     380     |
|  Serie B (2024) |    380    |     379     |
|  Serie B (2025) |    220    |     214     |
|  Serie C (2013) |    220    |     213     |
|  Serie C (2014) |    194    |     194     |
|  Serie C (2015) |    194    |     194     |
|  Serie C (2016) |    194    |     194     |
|  Serie C (2017) |    194    |     193     |
|  Serie C (2018) |    194    |     194     |
|  Serie C (2019) |    194    |     194     |
|  Serie C (2020) |    206    |     206     |
|  Serie C (2021) |    206    |     206     |
|  Serie C (2022) |    216    |     216     |
|  Serie C (2023) |    216    |     216     |
|  Serie C (2024) |    216    |     216     |
|  Serie C (2025) |    170    |     168     |
|  Serie D (2013) |    190    |     190     |
|  Serie D (2014) |    200    |     195     |
|  Serie D (2015) |    190    |     190     |
|  Serie D (2016) |    266    |     266     |
|  Serie D (2017) |    266    |     266     |
|  Serie D (2018) |    266    |     266     |
|  Serie D (2019) |    266    |     266     |
|  Serie D (2020) |    518    |     516     |
|  Serie D (2021) |    518    |     518     |
|  Serie D (2022) |    510    |     510     |
|  Serie D (2023) |    510    |     510     |
|  Serie D (2024) |    510    |     508     |
|  Serie D (2025) |    488    |     484     |

Follow these steps to configure the pre-commit hook via command line:

1. Clone the repository and navigate to the directory:

   ```bash
   git clone <repository-url> && cd <repository-directory>
   ```

2. Run the setup script:

    ```
    cp _locally/scripts/pre-commit.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
    ```

This script copies the pre-commit script to .git/hooks/ and sets execution permissions.

3. The pre-commit hook is now configured in your local repository.

After setup, the pre-commit hook will run automatically before each commit. If any issues are found, the commit process will halt, allowing you to fix them before proceeding.

If you encounter any issues or have questions, please refer to the documentation or contact the repository maintainers for assistance.

## Know problems

### Won't fix:
 - The added time info of each game isn't catch. All events occurred in added time are considered as occurred in the last minute of correspondent game half.
 - Despite saving the docket and the problem on a info log, we won't fix that information.
