# Project proposal / README

This project was created as a captstone project for the course GenAI for Humanists in S2024 at the univeristy of Vienna. The aim of the project ist to create a pipline to translate documents
into phonetic writing using the international phonetic alphabet (IPA) and emerging techniques from the of area generative AI and large language models. 

The main objectives is to achieve a reliable conversion from orthography to pronounciation for large texts in a select amount of languages that is able to handle abiguity (homographs) - which many available text to pronounciation tools struggle with - as well as handle unconventional spelling and errors. An example could be that the modell should be able to discern that "read" in the sentences:

1. "I will read the book now" and 2. "yesterday I read the book " are pronounced differently. In the first case it is [ri:d] and in the other case it is [rɛd]. 

To showcase the need for a tool like this, entering google search, both the top hits "https://tophonetics.com/" and "http://www.photransedit.com/" fails to capture this difference, providing the following transcriptions: "jestədi ˈaɪ riːd ðə bʊk" and "jɛstədeɪ aɪ riːd ðə bʊk" - both being wrong. As these are rulebased approaches, an AI approach that can take context into account will hopefull fare better.

Being able to deploy such a model on large amounts of data would be usefull in the area typological and contrastive lingistic, particularly with regard to automatic similarity of language judgement, as it would allow for large scale calulations of phonological distance measurements between languages. It could also be usefull for anyone looking to learn a language, requiring an easy way to find the correct pronounciation.

To achieve this, a large language modell will either be fined tuned to the task of text to IPA conversion using the data of monolingual wordlists with pronounciation information
made availble through the ipa-dict project: https://github.com/open-dict-data/ipa-dict, or it will utilize RAG with the same data. Both approaches could be explored and compared. 

Once basic functionality has been implemented for english, the hope is to be able to expand it to work for as many languages as possible, and perhaps even finalize a pipline that takes in translations of the same text in multiple languages, and measures phonological distance between them. 
