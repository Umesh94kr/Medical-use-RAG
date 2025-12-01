from Medical_RAG.vectorstore_data import get_vectorstore
import ollama


class RAG:
    def __init__(self, mock=False):
        if mock:
            pass
        self.vectorstore = get_vectorstore()
        self.history = []

    # Retrieve relevant docs
    def get_relevant_docs(self, query, k=3, mock=False):
        if mock:
            return "This is a mock Context."
        docs = self.vectorstore.similarity_search(query, k=k)
        context = "\n\n".join([f"[Doc {i+1}]\n{d.page_content}" for i, d in enumerate(docs)])
        return context

    # Build messages for the model
    def build_messages(self, query, context):
        system_prompt = (
            "You are a helpful medical assistant. "
            "Use only the provided context to answer the query. "
            "If context does not contain enough information, say so. "
            "Keep responses short and medically safe."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "system", "content": f"Retrieved context:\n{context}"}
        ]

        # Add full chat history
        messages.extend(self.history)

        # Add current query
        messages.append({"role": "user", "content": query})

        return messages

    # LLM call
    def call_llm(self, messages, mock=False):
        if mock:
            return "You are working correctly!"
        response = ollama.chat(
            model='llama3.2',
            messages=messages
        )
        return response["message"]["content"]

    # Main RAG process
    def main(self, query, mock=False):
        context = self.get_relevant_docs(query, mock=mock)
        messages = self.build_messages(query, context)

        response = self.call_llm(messages, mock=mock)

        # Update history
        self.history.append({"role": "user", "content": query})
        self.history.append({"role": "assistant", "content": response})

        return response


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
