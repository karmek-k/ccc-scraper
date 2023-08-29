from models.toc import Chapter, Part


content = [
    Chapter('Konstytucja Apostolska "Fidei depositum"'),  # rkkkap.htm
    Chapter('Wstęp', article_range=(1, 25)),

    Part('WYZNANIE WIARY', [
        Chapter('Wprowadzenie', article_range=(26, )),
        Chapter('CZŁOWIEK JEST "OTWARTY" NA BOGA', article_range=(27, 49)),
        Chapter('BÓG WYCHODZI NAPRZECIW CZŁOWIEKOWI', article_range=(50, 141)),
        Chapter('CZŁOWIEK ODPOWIADA BOGU', article_range=(142, 184)),

        Chapter('Symbole wiary', article_range=(185, 197)),  # wprowadzenie
        Chapter('WIERZĘ W BOGA OJCA', article_range=(198, 421)),
        Chapter('WIERZĘ W JEZUSA CHRYSTUSA, SYNA BOŻEGO JEDNORODZONEGO', article_range=(422, 682)),
        Chapter('WIERZĘ W DUCHA ŚWIĘTEGO', article_range=(683, 1065)),
    ]),

    Part('CELEBRACJA MISTERIUM CHRZEŚCIJAŃSKIEGO', [
        Chapter('Dlaczego liturgia? - Co znaczy pojęcie "liturgia"? - Liturgia jako źródło Życia - Modlitwa i liturgia - Katecheza i liturgia', article_range=(1066, 1075)),

        Chapter('Wprowadzenie', article_range=(1076, )),
        Chapter('MISTERIUM PASCHALNE W CZASIE KOŚCIOŁA', article_range=(1077, 1134)),
        Chapter('CELEBRACJA SAKRAMENTALNA MISTERIUM PASCHALNEGO', article_range=(1135, 1209)),

        Chapter('Wprowadzenie', article_range=(1210, 1211)),
        Chapter('SAKRAMENTY WTAJEMNICZENIA CHRZEŚCIJAŃSKIEGO', article_range=(1212, 1419)),
        Chapter('SAKRAMENTY UZDROWIENIA', article_range=(1420, 1532)),
        Chapter('SAKRAMENTY W SŁUŻBIE KOMUNII', article_range=(1533, 1666)),
        Chapter('INNE CELEBRACJE LITURGICZNE', article_range=(1667, 1690)),
    ]),

    Part('ŻYCIE W CHRYSTUSIE', [
        Chapter('Wprowadzenie', article_range=(1691, 1698)),

        Chapter('Wprowadzenie', article_range=(1699, )),
        Chapter('GODNOŚĆ OSOBY LUDZKIEJ', article_range=(1700, 1876)),
        Chapter('WSPÓLNOTA LUDZKA', article_range=(1877, 1948)),
        Chapter('ZBAWIENIE BOŻE: PRAWO I ŁASKA', article_range=(1949, 2051)),

        Chapter('Wprowadzenie', article_range=(2052, 2082)),
        Chapter('"BĘDZIESZ MIŁOWAŁ PANA BOGA SWEGO CAŁYM SWOIM SERCEM, CAŁĄ SWOJĄ DUSZĄ I CAŁYM SWOIM UMYSŁEM"', article_range=(2083, 2195)),
        Chapter('"BĘDZIESZ MIŁOWAŁ SWEGO BLIŹNIEGO JAK SIEBIE SAMEGO"', article_range=(2196, 2557)),
    ]),

    Part('MODLITWA CHRZEŚCIJAŃSKA', [
        Chapter('Wprowadzenie', article_range=(2558, )),
        Chapter('Czym jest modlitwa?', article_range=(2559, 2565)),
        Chapter('OBJAWIENIE MODLITWY. POWSZECHNE POWOŁANIE DO MODLITWY', article_range=(2566, 2649)),
        Chapter('TRADYCJA MODLITWY', article_range=(2650, 2696)),
        Chapter('ŻYCIE MODLITWY', article_range=(2697, 2758)),

        Chapter('MODLITWA PAŃSKA "OJCZE NASZ"', article_range=(2759, 2865)),
    ]),
]