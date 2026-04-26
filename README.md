## 🚀 Overview

**MCP Browser Agent** is an intelligent conversational AI agent that can autonomously control web browsers, navigate websites, take screenshots, and extract structured data - all through natural language commands. Built on the Model Context Protocol (MCP) with LangChain integration, it creates a seamless bridge between LLMs and browser automation.

## ✨ Key Features

- 🗣️ **Natural Language Control**: Tell the AI what you want to do on the web, and it executes
- 🧠 **Conversational Memory**: Maintains context across multiple interactions
- 🌐 **Full Browser Automation**: Click, type, navigate, screenshot, and scrape data
- 🔧 **MCP Integration**: Industry-standard protocol for LLM-tool interaction
- 🚄 **Fast LLM Backend**: Powered by Groq's ultra-fast inference
- 📸 **Visual Feedback**: Automatic screenshot capture of browser state
- 💾 **Session Persistence**: Maintains browser state across conversations

## 📋 Prerequisites

- Python 3.9+
- Groq API key

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Anas436/Multi-Agents-Using-MCP.git
cd Multi-Agents-Using-MCP
```

### 2. Install Dependencies with UV
```bash
uv sync
```
### 3. Set Up Environment Variables
Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
```
## 🎮 Usage

### Run the Interactive Chat
```bash
python app.py
```
### Chat Commands
- `exit` / `quit` - End the conversation
- `clear` - Clear conversation history

## 📁 Project Structure

```
Multi-Agents-Using-MCP/
├── app.py                  # Main chat application with memory
├── main.py                 # Core MCP agent implementation
├── browser_mcp.json        # MCP server configuration
├── pyproject.toml         # Project dependencies (UV)
└── README.md              # This file
```

## 💡 Technical Deep Dive

### MCPAgent Memory System
The agent features built-in conversation memory that maintains context across interactions, enabling:
- **Contextual awareness**: Remembers previous commands and results
- **State preservation**: Keeps track of browser state between queries
- **Reduced token usage**: Smart summarization of long conversations

### Performance Optimizations
- Async/await architecture for concurrent operations
- Max 50 steps per task to prevent infinite loops
- Session pooling for resource efficiency
- Automatic cleanup of browser sessions

## 🚦 Error Handling

The agent includes robust error handling for:
- Network failures (automatic retry with backoff)
- Element not found (intelligent waiting and retry)
- API rate limits (exponential backoff)
- Browser crashes (automatic session restart)

## 📊 Performance Metrics

| Operation | Average Time |
|-----------|--------------|
| Simple navigation | 1-2 seconds |
| Screenshot capture | 2-3 seconds |
| Complex workflows | 5-10 seconds |
| Memory retrieval | <100ms |

## 🔒 Security Features

- API keys stored in `.env` (gitignored)
- Session isolation between conversations
- Configurable max steps per operation
- Automatic cleanup on exit

## 🎯 Future Roadmap

- [ ] Multi-browser support (Firefox, WebKit)
- [ ] Voice command integration
- [ ] Custom tool development API
- [ ] Docker containerization
- [ ] WebSocket streaming for real-time feedback
- [ ] Export conversation logs to multiple formats
- [ ] Integration with LangSmith for monitoring

## 🤝 Contributing

Contributions are welcome! Please ensure:
1. Code follows existing patterns (async/await, type hints)
2. Add tests for new features
3. Update documentation
4. Maintain backward compatibility

## 📝 License

MIT License - See LICENSE file for details

## 🌟 Show Your Support

If this project helped you:
- ⭐ Star the repository
- 🔄 Share with others
- 📝 Write a blog post about your use case

## References
1. [mcp-use](https://github.com/mcptutorial/mcp-use)
2. [playwright-mcp](https://github.com/microsoft/playwright-mcp)
3. [mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)
4. [duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mcp-server)
5. [Groq](https://groq.com/)
