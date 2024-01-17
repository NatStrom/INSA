/textbf{READ ME Sanctions Data}

This folder contains all notebooks and files for the retrieval, cleaning and production of the Sanctions Dataset for the INSA project.

the INSA project aims at designinmg and implementing a dataset that contains all individual listings of sanctioned persons, entities and/ or vessels made by the EU, USA and the UK as well as their date of designation, information on the sanctioning authority and further identifying information. As the date on which such individual sanctions where first authorized differs between the authorities, the temporal span of the data is different as well – for the USA all months between 1994 and 2023, for the EU 2004 to 2023 and the UK 2020 to 2023.

For each sanctioning authority, the updated most recent lists are available for download and the script to clean and process the data is prepared. In an additional step, the data dating back to July 2021 is extracted from the OpenSanctions API to retrieve a dataset that has a temporal span of at least the last 2 ½ years. In order to provide data reaching further back, more inquiry into the availability and structure of the respective lists is needed. 
The US SDN list is available as a pdf released yearly and including all additions, revisions, de-listings and new additions branded with specific dates. The pdf files span from 1994 to 2022.
The UK consolidated list is available as HTML for all instances of changes in 2022 and 2023. The instances have to be queried/ accessed via the URL individually (341 in total) or a function extracting them has to be written. The old version of the list dating back until 2020 is not accessible as of now. 
The EU list does not seem to be archived. The only files available are the FSF files spanning from 2015 onward. Only one file per year could be obtained via the FISMA, omitting all other potential changes to the list.

Technical note:
All scripts, raw data files and code is stored in the INSA GitHub repository. All initial coding is done in Python, while the Text Analysis will be based on R. To contribute to the code, please clone the main branch and work in your own branch that is merged back, when the task is finished. All organizational documents as well as written Data Analysis is found in Sharepoint under INSA/ Documents/ Data. For large data queries or computationally heavy tasks please contact Tillmann from the GIGA IT Service to book and access the server.
IMPORTANT: Please do not open any of the datafiles in excel. Use a tool like VS Code or Libre Office instead.


The following time plan specifies the actions taken to retrieve, clean and analyse the data in the coming months. Variables needed and additional data sources are provided further below.
 
EU
EU Sanctions Data.docx
-	Get data up to 2021 fom Opensantions
-	Get list and EU sanctions map – lates version cleaned up
-	Need to get archived consolidated lists
Data sources: 
-	CFS (Consolidated Financial Sanctions)
o	Source URL: https://data.europa.eu/data/datasets/consolidated-list-of-persons-groups-and-entities-subject-to-eu-financial-sanctions?locale=en
o	name query Opensantions:eu_fsf

-	EU Sanctions Map (all EU Sanction Regimes and Targeted Measures)
o	Source URL: https://data.europa.eu/data/datasets/consolidated-list-of-persons-groups-and-entities-subject-to-eu-financial-sanctions?locale=en
o	name query Opensantions: eu_sanctions_map

-	Archived Sanctions List
o	Source URL: ?

-	EC list of persons, groups and entities involved in terrorist acts and subject to restrictive measures
o	Source URL: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32009E0468&qid=1412596355797&from=EN
o	name query Opensantions:--

Proceedings:
1.	
 
USA
US Sanctions Data.docx
-	Get data up to 2021 fom Opensantions
-	Get OFAC SDN – latest version cleaned up
-	Need to get archived SDN lists

Data Sources:
-	 OFAC SDN list (Office for Foreign Asset Control: Specially Designated Nationals)
o	Source URL: https://ofac.treasury.gov/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists
o	name query Opensanctions: us_ofac_sdn

-	Archived SDN lists:
o	Archive of Changes to the SDN List | Office of Foreign Assets Control (treasury.gov) 


-	BIS denied Persons List
o	Source URL: https://www.bis.doc.gov/dpl/dpl.txt
o	name query Opensanctions: us_bis_denied

-	Designated Foreign Terrorist Organizations Terror List (Listing of Indiviiduals connected to Terrorist Organizations)
o	Source URL:https://www.state.gov/executive-order-13224/#state
o	name query Opensanctions: --

Proceeding:
The historic files are not structured but in the format of press releases that have a date assigned. One step could be to load each date and its assigned conent as a nested Json/ list. Another possible solution or the next step is, to use regular expression functions to match ans search for context that can then be assigned as a value to a specific key. I have yet no experience on how to automate that or to ensure, that the lines are not split but the information belonging to one entity is connected to each other. Furthermore, most updates do not provide an Entity ID. I can work on it, but its gonna take some time   
UK
UK Sanctions Data.docx
-	Get data up to 2021 fom Opensantions
-	Get list and EU sanctions map – lates version cleaned up
-	Need to get archived consolidated lists

Data Sources:
- UK Financial & Consolidated Sanctions list
Source URL: https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets/consolidated-list-of-targets
name query Opensantions:gb_hwt_sanctions

-	Archived files of UK Consolidated Sanctions list:

- Non-consolidated Sanctions List
Source URL:https://www.gov.uk/government/publications/the-uk-sanctions-list
name query Opensantions: --

Proceedings:

 
General requirements for the dataset:

Technical notes:
-	The month variable needs to be transformed and to make it comparable across all authorizing organizations needs to be assigned a base month aka follow the USA pattern with the January 1994 being assigned as month 1 and continuous count from there. In total the USA will cover 29 years, meaning 348 months.
-	An own unique case id has to be assigned so all entities matching across sanctioning authority have the same id in the dataset
-	It has to be ensured that all Aliases are deduplicated
