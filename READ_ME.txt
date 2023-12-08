/textbf{READ ME Sanctions Data}

This folder contains all notebooks and files for the retrieval, cleaning and production of the Sanctions Dataset for the INSA project.

the INSA project aims at tracking all individual designations by the EU, US and the UK for entities such as persons, vessels, enterprises and companies.
The temporal scope of the project is from 1995 to 2023 for thge USA and from 2005 to 2023 for the EU/ UK listings.

The following data sources have been used to retrieve the original data from the country lists:

/textbf{USA:}
- OFAC SDN list (Office for Foreign Asset Control: Specially Designated Nationals)
Source URL: https://ofac.treasury.gov/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists
name query Opensanctions: us_ofac_sdn

BIS denied Persons List
Source URL: https://www.bis.doc.gov/dpl/dpl.txt
name query Opensanctions: us_bis_denied

- Designated Foreign Terrorist Organizations Terror List (Listing of Indiviiduals connected to Terrorist Organizations)
Source URL:https://www.state.gov/executive-order-13224/#state
name query Opensanctions: --

/textbf{EU:}
- CFS (Consolidated Financial Sanctions)
Source URL: https://data.europa.eu/data/datasets/consolidated-list-of-persons-groups-and-entities-subject-to-eu-financial-sanctions?locale=en
name query Opensantions:eu_fsf

- EU Sanctions Map (all EU Sanction Regimes and Targeted Measures)
Source URL: https://data.europa.eu/data/datasets/consolidated-list-of-persons-groups-and-entities-subject-to-eu-financial-sanctions?locale=en
name query Opensantions: eu_sanctions_map

- EC list of persons, groups and entities involved in terrorist acts and subject to restrictive measures
Source URL: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32009E0468&qid=1412596355797&from=EN
name query Opensantions:--

/textbf{UK:}
- UK Financial & Consolidated Sanctions list
Source URL: https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets/consolidated-list-of-targets
name query Opensantions:gb_hwt_sanctions

- Non-consolidated Sanctions List
Source URL:https://www.gov.uk/government/publications/the-uk-sanctions-list
name query Opensantions: --