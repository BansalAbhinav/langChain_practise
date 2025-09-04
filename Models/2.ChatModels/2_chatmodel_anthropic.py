from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3.5-sonnet")
result = model.invoke("what is captial of india")

print(result)