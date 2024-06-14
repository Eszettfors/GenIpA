import os
import openai

os.environ["OPENAI_API_KEY"] = "sk-proj-ati0Co2Vt8anHxAf9emxT3BlbkFJzBBqjuNyNos5W71ryVtc"
openai.api_key = os.environ["OPENAI_API_KEY"]

import shutil

import warnings
warnings.filterwarnings('ignore')


## Llamaindex readers
from llama_index.core import SimpleDirectoryReader


## LlamaIndex Context Managers
from llama_index.core import StorageContext
from llama_index.core import load_index_from_storage
from llama_index.core.response_synthesizers import get_response_synthesizer


from llama_index.core.node_parser import SentenceSplitter
splitter = SentenceSplitter(chunk_size=2048)

response_synthesizer = get_response_synthesizer(
    response_mode="tree_summarize", use_async=True
)


def create_retrieve_index(index_path, docs_path, index_type, file_name):
    if not os.path.exists(index_path):
        print(f"Creating Directory {index_path}")
        os.mkdir(index_path)
    if os.listdir(index_path) == []:
        print("Loading Documents...")
        documents = SimpleDirectoryReader(input_files=[f"{docs_path}{file_name}"]).load_data()
        print("Creating Index...")
        index = index_type.from_documents(documents,
                                          transformations=[splitter],
                                          #response_synthesizer=response_synthesizer,
                                          show_progress=True,
                                          )
        print("Persisting Index...")
        index.storage_context.persist(persist_dir=index_path)
        print("Done!")
    else:
        print("Reading from Index...")
        index = load_index_from_storage(storage_context=StorageContext.from_defaults(persist_dir=index_path))
        print("Done!")
    return index


def recreate_directory(PERSIST_DIR):
    check = input("Are you sure you want to reacreate the directory? (y/n), all indexes will be deleted")
    if check == "y":
        if os.path.exists(PERSIST_DIR):
            shutil.rmtree(PERSIST_DIR)
            os.mkdir(PERSIST_DIR)
            print(f"recreated Directory {PERSIST_DIR}")
        else:
            print(f"Directory {PERSIST_DIR} does not exist")
    else:
        print("Aborting...")


def get_query_engine(vectorstoreindex):
    query_engine = vectorstoreindex.as_query_engine(retriever_mode="embedding",
                                                response_mode="compact",
                                                verbose=True)
    return query_engine

def get_ipa_rag(query_engine, text):
    response = query_engine.query("please transcribe this text to IPA using the vectorstore indexes: " + text)
    return response


def get_ipa_openai(prompt, model="gpt-3.5-turbo", temperature=0, lang = None):
    if lang != None:
        messages = [
            {"role": "system", "content": "You provide IPA translations of text in " + lang + " using only your own knowledge, nothing else."},
            {"role": "user", "content": prompt},
            ]
    else:
        messages = [
            {"role": "system", "content": "You provide IPA translations of text using only your own knowledge, nothing else."},
            {"role": "user", "content": prompt},
            ]
    response = openai.chat.completions.create(model=model,
                                              messages=messages,
                                              temperature=temperature
                                              )
    return response.choices[0].message.content


def edit_distance(str1, str2):
    """
    Calculates the edit distance between two strings
    """
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],    
                                   dp[i - 1][j],    
                                   dp[i - 1][j - 1]) 
    return dp[m][n]

def normalized_edit_distance(str1, str2):
    """
    Calculates the normalized edit distance between two strings using the average lenght of the strings
    """
    return edit_distance(str1, str2) / ((len(str1)+ len(str2))/2)

