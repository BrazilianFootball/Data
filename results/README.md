# Game Data

In this repository we have the extracted data Brazillian championship's dockets. The championships we have considered are:

 - [Brazil Cup](https://en.wikipedia.org/wiki/Copa_do_Brasil) (Copa do Brasil) as CdB;
 - [Brazillian Serie A](https://en.wikipedia.org/wiki/Campeonato_Brasileiro_Série_A) (Campeonato Brasileiro Série A) as Serie_A;
 - [Brazillian Serie B](https://en.wikipedia.org/wiki/Campeonato_Brasileiro_Série_B) (Campeonato Brasileiro Série B) as Serie_B;
 - [Brazillian Serie C](https://en.wikipedia.org/wiki/Campeonato_Brasileiro_Série_C) (Campeonato Brasileiro Série C) as Serie_C and;
 - [Brazillian Serie D](https://en.wikipedia.org/wiki/Campeonato_Brasileiro_Série_D) (Campeonato Brasileiro Série D) as Serie_D.

## Directory organization

As comented previously, all data was scraped from CBF's [page](https://www.cbf.com.br/) and saved, in raw format, as PDF and CSV. In addition to the raw data, there are three files for each championship season. This directory is organized as below
```bash
./
└── Championship/
    └── Year/
        ├── CSVs/
        ├── PDFs/
        ├── games.json
        ├── squads.json
        └── summary.csv
```

As the name inform, the CSVs folder have all dockets in `csv` format, besides PDFs folder have the same data, but in `pdf` format. The `summary.csv` file have informations about game code, home and away team. The game code is a numeric code with three digits and represents the filename where that game can be found on CSVs and PDFs folders (the data for the game with code COD will be on `COD.csv` and `COD.pdf` files).

In other hand, the `json` files have a processed data. First, `games.json` have all general info about all games, as show below
```json
{
  "Home": "Remo / PA",
  "Away": "Flamengo / RJ",
  "Result": "0 x 1",
  "Players": [
    ["1Fabiano Bo ... Fabiano Bolla Lora T(g)P132800", "Remo / PA"],
    ["2Carlinho Carlinho Rech TP184862", "Remo / PA"],
    ["3Rico Henrique Silvestre T ... TP156279", "Remo / PA"],
    ["4Toninho José Antonio Horacio ... TP329561", "Remo / PA"],
    ...
  ],
  "Goals": [
    "09:00 2T 11 NR Rafael Lima Pereira Flamengo/RJ"
  ],
  "Changes": [
    "29:00 1TFlamengo/RJ 15 - Carlos Renato de Abreu 2 - Leonardo da Silva Moura",
    "12:00 2TRemo/PA 15 - Jhonnatan Guimaraes Sarai ... 8 - Geronimo dos Santos Olive ...",
    "31:00 2TRemo/PA 17 - Jose Clebson de Lima 10 - Petter Barros de Almeida",
    "32:00 2TFlamengo/RJ 16 - Cleber Santana Loureiro 10 - Rodolfo de Almeida Guimar ...",
    ...
  ],
  "Yellow cards": [
    "28:00 2T 3Renato dos Santos Flamengo/RJ",
    "32:00 2T 10Rodolfo de Almeida Guimaraes Flamengo/RJ",
    "07:00 2T 4José Antonio Horacio de Lima Remo/PA",
    "18:00 2T 11Valdenir Barretos Remo/PA"
  ],
  "Red cards": [

  ]
}
```

Finally, the `squads.json` file breaks this data in subgames. Every time that occur a change, it's defined a new subgame. So, the first 22 players on field begin the first subgame from a game. When the first change of players occur, that subgame ends and the second begins. Independently the parcial result of the game, the second subgame begins with a 0 x 0 score. In this sense, every game was broken in some subgames, having the eleven player's id for each club, the time that subgame lasted and the score of thta subgame. As example
```json
{"0": {
  "Home": {
    "Squad": ["132800", "184862", "156279", "329561", "173645", "166749", "173921", "175741", "340020", "182842", "171968"],
    "Cards": [

    ],
    "Goals": [

    ]
  },
  "Away": {
    "Squad": ["141698", "137644", "164070", "166649", "189046", "155855", "335611", "159607", "186467", "308733", "302196"],
    "Cards": [

    ],
    "Goals": [

    ]
  },
  "Time": 29
},
"1": {
  "Home": {
    "Squad": ["132800", "184862", "156279", "329561", "173645", "166749", "173921", "175741", "340020", "182842", "171968"],
    "Cards": [
      [23, "329561"]
    ],
    "Goals": [

    ]
  },
  "Away": {
    "Squad": ["141698", "164070", "166649", "189046", "155855", "335611", "159607", "186467", "308733", "302196", "133769"],
    "Cards": [

    ],
    "Goals": [
      [25, "302196"]
    ]
  },
  "Time": 28
},
...
}
```

Where the player `132800` is Fabiano Bolla Lora, from Remo, as we can se on the first `json`.