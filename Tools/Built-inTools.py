from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()        #Perform web search and retrieve top results.
result = search_tool.run("Who is Albert Einstein?")
print(result)


from langchain.tools import ShellTool

shell_tool = ShellTool()
output = shell_tool.run("cd   #Execute shell commands")  
print(output)