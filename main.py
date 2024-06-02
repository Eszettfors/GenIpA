from importlib import reload
import utils
reload(utils)
from utils import create_retrieve_index
import os
from llama_index.core import VectorStoreIndex
import warnings
warnings.filterwarnings('ignore')


#Locating and handling relevant files
DOCS_DIR = "data_rag/"
PERSIST_DIR = "index/"
print(f"Current dir: {os.getcwd()}")
if not os.path.exists(DOCS_DIR):
  os.mkdir(DOCS_DIR)
docs = os.listdir(DOCS_DIR)
docs = [d for d in docs]
docs.sort()
print(f"Files in {DOCS_DIR}")
for doc in docs:
    print(doc)

#utils.recreate_directory(PERSIST_DIR)

#Initializes vector store indexes and creates the query engine
VECTORINDEXDIR = PERSIST_DIR + 'VectorStoreIndex'
vectorstoreindex = create_retrieve_index(VECTORINDEXDIR, DOCS_DIR, VectorStoreIndex, 'sv.txt')
query_engine = utils.get_query_engine(vectorstoreindex)

rag_supported_languages =["Swedish"] 

#Application logic for running the application
def main():
  while True:
      check = input("Do you want to get a transcription? (y/n)")
      if check == "y":
        rag_y_n = input("Do you want to use RAG? (y/n)")
        if rag_y_n == "y":
          lang = input(f"what language do you want to use?: (Available languages: {[lang for lang in rag_supported_languages]})")
          if lang not in rag_supported_languages:
            print('not a supported language, non rag_supported transcription will be used')
            transcription = utils.get_ipa_openai(text)
            print(f"openai: {transcription}")
          else:
            text = input("enter the text you want to have transcribed: ")
            transcription_1 = utils.get_ipa_rag(query_engine, text)
            print(f"rag: {transcription}")
        elif rag_y_n == "n":
          text = input("enter the text you want to have transcribed: ")
          transcription = utils.get_ipa_openai(text)
          print(f"openai: {transcription}")
        else:
          print('not a valid answer...')
      elif check == 'n':
            print('closing application...')
            break
      else:
            print('not a valid answer')
            
            
if __name__ == "__main__":
    main()


