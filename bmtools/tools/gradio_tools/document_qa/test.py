import pathlib
from bmtools.agent.singletool import load_single_tools, STQuestionAnswerer
# Langchain
tool_name, tool_url = 'document_qa',  "http://127.0.0.1:8079/tools/document_qa/"

tool_name, tool_config = load_single_tools(tool_name, tool_url)

print(tool_name, tool_config)
stqa =  STQuestionAnswerer()

agent = stqa.load_tools(tool_name, tool_config)

IMG_PATH = pathlib.Path(__file__).parent / "florida-drivers-license.jpeg"

agent(f"What is the date of birth the driver in {IMG_PATH}?")
agent("What is the current date?")
agent("Using the current date, what is the age of the driver? Explain your reasoning.")
agent("What is the driver's license number?")