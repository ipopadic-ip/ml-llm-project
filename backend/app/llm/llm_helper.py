import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_password_advice(password: str, strength: int) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",  # free llm
        "messages": [
            {"role": "system", "content": "You are a helpful cybersecurity assistant."},
            {
                "role": "user",
                "content": f"""
                The password is: '{password}'.
                It has been rated with strength score: {strength} (0=weak, 1=medium, 2=strong).
                Its length is {len(password)} characters.

                Do NOT assume anything beyond this info (e.g. do not guess symbol presence unless it's visible in the string).

                Briefly evaluate the password's quality.

                If it's not strong, suggest 2–3 improvements.

                If it is already strong, explain why and say no changes are needed.

                Respond in 2 to 3 full sentences, no bullet points or lists.
                """
            }
        #    {
        #         "role": "user",
        #         "content": f"""
        #             Analyze the strength of this password: '{password}'.
        #             First, evaluate its overall security in 1–2 sentences.
        #             Then, if the password is not already strong, suggest 2–3 specific improvements.
        #             If the password is already strong, explain why and say that no improvements are needed.
        #             Be specific but concise.
        #             """
        #     }
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"LLM error: {response.status_code} - {response.text}"
