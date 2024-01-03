from llama_cpp import Llama

LLAMA_MODEL_PATH = "llama/models/llama-2-7b-chat.Q4_K_M.gguf"


class LlamaModel:
    def __init__(self):
        self.LLM = Llama(model_path=LLAMA_MODEL_PATH, chat_format="llama-2")

    def generate_response(self, question: str):
        prompt = f"Q: {question} A:"
        response = self.LLM(
            prompt,
            max_tokens=32,
            stop=["Q:", "\n"],
            echo=False,
        )
        return response["choices"][0]["text"]

    def generate_response_with_context(self, question: str, context: str):
        response = self.LLM.create_chat_completion(
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": question},
            ]
        )
        return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    llama_model = LlamaModel()
    print(
        llama_model.generate_response_with_context(
            "Can I delete this email because it's unimportant?:\nHey Abdu, click on this link to receive a discount for your next purchase",
            "I want to delete unimportant emails, this includes activation emails, emails to reset passwords or with one time passwords, any newsletters or commercial emails. Also any automatically sent emails that are expired and I no longer need",
        )
    )
