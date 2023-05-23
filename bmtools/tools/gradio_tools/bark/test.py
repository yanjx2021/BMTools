from bmtools.agent.singletool import load_single_tools, STQuestionAnswerer
# Langchain
tool_name, tool_url = 'bark',  "http://127.0.0.1:8079/tools/bark/"

tool_name, tool_config = load_single_tools(tool_name, tool_url)

print(tool_name, tool_config)
stqa =  STQuestionAnswerer()

agent = stqa.load_tools(tool_name, tool_config)
agent("Please create a jingle for a spanish company called 'Chipi Chups' that makes lollipops. The jingle should be catchy and playful and meant to appeal to all ages.")