from Medical_RAG.rag import RAG

if __name__ == "__main__":
    rag = RAG()

    while True:
        query = input("Put your query for medical bot: ")

        if query.lower() == "quit":
            print("Thank you for chatting :)")
            break

        print(f"Query: {query}")
        response = rag.main(query)
        print(f"Response: {response}")
        print("-" * 80)