import json
import asyncio
import aiohttp
from typing import List


class MultipleQuestionsHandler:
    """
    Class that handles multiple questions and generates responses using the Anthropic API.

    Args:
        api_key (str): The API key for accessing the Anthropic API.
        model (str, optional): The model to use for generating responses. Defaults to "claude-3-opus-20240229".

    Attributes:
        api_key (str): The API key for accessing the Anthropic API.
        model (str): The model to use for generating responses.
        url (str): The URL for the Anthropic API.

    Methods:
        generate_response: Generates a response for a single question using the Anthropic API.
        form_responses: Forms the final response by joining multiple responses.
        ask: Handles the process of asking multiple questions and generating responses.

    """

    def __init__(self, api_key: str, model: str = "claude-3-opus-20240229") -> None:
        self.api_key = api_key
        self.model = model
        self.url = "https://api.anthropic.com/v1/messages"

    async def generate_response(
        self, session: aiohttp.ClientSession, question: str
    ) -> str:
        """
        Generates a response for a single question using the Anthropic API.

        Args:
            session (aiohttp.ClientSession): The aiohttp client session.
            question (str): The question to generate a response for.

        Returns:
            str: The generated response.

        Raises:
            aiohttp.ClientResponseError: If there is an error in the client response.
            Exception: If there is an unhandled exception.

        """

        headers = {
            "x-api-key": self.api_key,
            "content-type": "application/json",
            "anthropic-version": "2023-06-01",
        }
        data = {
            "model": self.model,
            "max_tokens": 100,
            "messages": [{"role": "user", "content": question}],
        }
        try:
            async with session.post(self.url, headers=headers, json=data) as response:
                response.raise_for_status()
                data = await response.json()
                return data["content"][0]["text"]
        except aiohttp.ClientResponseError as e:
            return f"[ERROR] {type(e).__name__} : {str(e)}"
        except Exception as e:
            return f"[ERROR] {type(e).__name__} : {str(e)}"

    async def form_responses(self, responses: List[str]) -> str:
        """
        Forms the final response by joining multiple responses.

        Args:
            responses (List[str]): A list of responses.

        Returns:
            str: The final response.

        """

        return "\n\n".join(responses)

    async def ask(self, questions: List[str]) -> str:
        """
        Handles the process of asking multiple questions and generating responses.

        Args:
            questions (List[str]): The input string of questions.

        Returns:
            str: The final response.

        """

        async with aiohttp.ClientSession() as session:
            responses = await asyncio.gather(
                *[self.generate_response(session, question) for question in questions]
            )
            return await self.form_responses(responses)


async def main(api_key: str, questions: List[str]):
    handler = MultipleQuestionsHandler(api_key=api_key)
    result = await handler.ask(questions)
    print(result)


if __name__ == "__main__":
    with open("./config.json", "r") as file:
        data = json.load(file)
    api_key = data["api-key"]
    questions = data["questions"]
    asyncio.run(main(api_key=api_key, questions=questions))
