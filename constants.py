class Variables:

    
    pre_treatment_covariates_to_include = ['total_twenty_seventeen_group_0_crimes_250m',
                                            'month_neg_twelve_group_0_crimes_250m',
                                            'month_neg_six_group_0_crimes_250m',
                                            'med_hhinc2016',
                                            'poor_share2010',
                                            'popdensity2010',
                                            'share_white2010',
                                            'non_payment',
                                             ]
    
    outcomes = [f"group_{group}_crimes_{range}m" for group in range(7) for range in [250, 300, '250_to_300', '250_to_350', '250_to_400']]
    
    variable_display_names_dict = \
    {
        "total_twenty_seventeen_group_0_crimes_250m": "All Crime Reports, 2017",
        "month_neg_twelve_group_0_crimes_250m": "All Crime Reports, Month -12",
        "month_neg_six_group_0_crimes_250m": "All Crime Reports, Month -6",
    
        "total_twenty_seventeen_group_2_crimes_250m": "Drug Crime Reports, 2017",
        "month_neg_twelve_group_2_crimes_250m": "Drug Crime Reports, Month -12",
        "month_neg_six_group_2_crimes_250m": "Drug Crime Reports, Month -6",
            
        "total_twenty_seventeen_group_1_crimes_250m": "Larceny Reports, 2017",
        "month_neg_twelve_group_1_crimes_250m": "Larceny Reports, Month -12",
        "month_neg_six_group_1_crimes_250m": "Larceny Reports, Month -6",
    
        "total_twenty_seventeen_group_3_crimes_250m": "Vandalism Reports, 2017",
        "month_neg_twelve_group_3_crimes_250m": "Vandalism Reports, Month -12",
        "month_neg_six_group_3_crimes_250m": "Vandalism Reports, Month -6",
    
    
        "total_twenty_seventeen_group_4_crimes_250m": "Assault Reports, 2017",
        "month_neg_twelve_group_4_crimes_250m": "Assault Reports, Month -12",
        "month_neg_six_group_4_crimes_250m": "Assault Reports, Month -6",
    
    
        "total_twenty_seventeen_group_5_crimes_250m": "Auto Theft Reports, 2017",
        "month_neg_twelve_group_5_crimes_250m": "Auto Theft Reports, Month -12",
        "month_neg_six_group_5_crimes_250m": "Auto Theft Reports, Month -6",
            
    
        "med_hhinc2016": "Median household income, 2016",
        "poor_share2010": "Poverty rate, 2010",
        "popdensity2010": "Population density, 2010",
        "share_white2010": "Share white, 2010",
    
        "non_payment": "Filing for nonpayment",
        "hasAttyD": "Defendant has attorney",
        "hasAttyP": "Plaintiff has attorney",
        "isEntityP": "Plaintiff is entity",
        "case_duration": "Case duration",
        "defaulted": "Judgment by default",
        "dismissed": "Case dismissed",
        "heard": "Case heard",
        "judgment": "Money judgment",
    }


class Analysis:
    MAIN_RESULTS_RADIUS = 250
    ROBUSTNESS_RADII = ["250_to_300", "250_to_350", "250_to_400"]
    MINIMUM_PRE_PERIOD = -12
    MAXIMUM_POST_PERIOD = 24

    months = ['2015-06',
              '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12',
              '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06',
              '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12',
              '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06',
              '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
              '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06',
              '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12',
              '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06',
              '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12',
              '2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06',
              '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12',
              '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06',
              '2021-07', '2021-08', '2021-09', '2021-10', '2021-11', '2021-12',
              '2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06',
              '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12',
              '2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06',
              '2023-07']
    
    larceny = [633, 623, 632, 622, 612, 631, 621, 611,
               613, 617, 627, 637, 614, 624, 634, 619,
               615, 625, 635, 629, 639, 649]

    drugs = [1843, 1844, 1845, 1846, 1870, 1874,
             1842, 1841, 1849, 1847, 1848, 1850,
             2631, 1805, 1806, 1807, 1825, 1815,
             1832, 1831, 2609, 1810, 1830, 1870,
             2609, 1874, 1842, 1841, 1849, 1848,
             1858, 1855, 1864, 1863, 1866, 1868,
             1843, 3023, 3021, 1875, 3022, 1847, 
             1840, 1873, 1843, 1844, 1845, 1846]
    
    
    vandalism = [1402, 1415]
    
    

    assault = [801, 802, 803, 423, 413, 401, 402, 403, 404, 411, 412, 413, 421,
               422, 423,424, 431, 432, 433, 3301, 2647]


    auto_theft = [701, 702, 704, 711, 712, 713, 714, 715, 706,  724,
                  727, 706, 723, 724, 727, 735, 770, 780, 790]
    
    assault_auto_theft_vandalism_larceny = assault + auto_theft + vandalism + larceny


class Colors:
    P1 = "#29B6A4"
    P2 = "#FAA523"
    P3 = "#003A4F"
    P4 = "#7F4892"
    P5 = "#A4CE4E"
    P6 = "#2B8F43"
    P7 = "#0073A2"
    P8 = "#E54060"
    P9 = "#FFD400"
    P10 = "#6BBD45"

    SUMMARY_STATISTICS_COLOR = 'black'
    LABELING_COLOR = 'grey'
    TREATMENT_COLOR = 'red'
    CONTROL_COLOR = 'blue'


class Text:
    DEFAULT_DECIMAL_PLACES = 3
