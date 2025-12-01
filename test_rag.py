# lets write a test whether vectorstore is loading or not 
from Medical_RAG.rag import RAG

# keep function names to be test_*
def test_app():
    rag = RAG()
    response = rag.main(query="Hey How are you?", mock=True)
    assert response == "You are working correctly!"