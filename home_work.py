# RUN LEVEL
import asyncio 
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

gemini_api_key = "AIzaSyDEHmqYAkafo511WLKVDQfn9LaZCWpD9F4"

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model= OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client = external_client)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)

agent:Agent = Agent(
    name = "Qur’an Learning Assistant",
    instructions = "Helps users memorize verses from The Quran"
)

async def main():
    result = await Runner.run(agent, "Verse from chapter 2 verse no 2", run_config = config)
    print(result.final_output)

asyncio.run(main())