# Project proposal / README

This project was created as a capstone project for the course GenAI for Humanists in S2024 at the univeristy of Vienna. The aim of the project ist to create a pipeline to transcribe documents
into phonetic writing using the international phonetic alphabet (IPA) and emerging techniques from the of area generative AI and large language models. 

The main objectives is to achieve a reliable conversion from orthography to pronounciation for large texts in a select amount of languages that is able to handle abiguity (homographs) - which many available text to pronounciation tools struggle with - as well as handle unconventional spelling and errors. An example could be that the modell should be able to discern that "read" in the sentences:

1. "I will read the book now" and 2. "Yesterday I read the book " are pronounced differently. In the first case it is [ri:d] and in the second case it is [rɛd]. 

To showcase the need for a tool like this, entering "text to IPA" into google search, both the top hits "https://tophonetics.com/" and "http://www.photransedit.com/" fails to capture this difference, providing the following transcriptions: "jestədi ˈaɪ riːd ðə bʊk" and "jɛstədeɪ aɪ riːd ðə bʊk" - both being wrong. As these are rule based approaches, an AI approach that can take context into account will hopefull fare better.

Being able to deploy such a model on large amounts of data would be usefull in the area typological and contrastive lingistic, particularly with regard to automatic similarity of language judgement, as it would allow for large scale calulations of phonological distance measurements between languages. It could also be usefull for anyone looking to learn a language, requiring an easy way to find the correct pronounciation.

The file openAI_+_rag.py can be run to interact with the transcriber and select if you want it to be enhanced by RAG. For a quick showcase of the application, there is a notebook: Showcase_of_app.ipynb and for an example of usage in research, please see the notebook: phon_dist.

Please feel free to use the resources presented through this project, note that the supplying of an openAI API key in utils.py is necessary, however.
