from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled
from openai import AsyncOpenAI

gemini_api_key = "Api key"

client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model= OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client = client)
config = RunConfig(model=model, model_provider=client,tracing_disabled=True)

agent:Agent = Agent(
    name ="Assistant", 
    instructions="You're a heplful Assistant", 
)
# output = Runner.run_sync(starting_agent=agent, input="Hello, How can I")

result = Runner.run_sync(
    starting_agent = agent,
    input = "Write program that sum two nuumbers and numbers are 10 and 5",
    run_config = config
)

print(result.final_output)
