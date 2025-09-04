from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=1.3)
result=model.invoke("give me indian boy name ")
print(result.content)