#GLOBAL
import asyncio
from agents import Agent, Runner, AsyncOpenAI,OpenAIChatCompletionsModel, set_default_openai_client, set_tracing_disabled, set_default_openai_api
from openai.types.responses import ResponseTextDeltaEvent

gemini_api_key = "AIzaSyDEHmqYAkafo511WLKVDQfn9LaZCWpD9F4"
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

set_default_openai_client(external_client)

agent: Agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant", 
    model=model)

async def main():
    try:
        result = Runner.run_streamed(agent, "Tell 3 myth of the world.")
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)
    except Exception as e:
        print(f"\n❌ Error: {e}")

asyncio.run(main())