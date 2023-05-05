from bmtools.agent.singletool import load_single_tools, STQuestionAnswerer
# Langchain
tool_name, tool_url = 'stable_diffusion',  "http://127.0.0.1:8079/tools/stable_diffusion/"

tool_name, tool_config = load_single_tools(tool_name, tool_url)

print(tool_name, tool_config)
stqa =  STQuestionAnswerer()

agent = stqa.load_tools(tool_name, tool_config)
agent("Please create a photo of a dog riding a skateboard ")