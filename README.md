# fake-news-detector_langgraph


# AI Fake News Detector

An AI-powered fake news detection system built using  **LangGraph, LLMs, Streamlit, and web search tools** .

It analyzes news claims and returns a **verdict (True / False / Uncertain)** with  **confidence scoring and evidence-based reasoning** .

---

##  Features

* 📰 Real-time fake news detection
* 🤖 LLM-powered analysis (Ollama / Llama 3.1)
* 🌐 Web search-based verification
* 📊 Confidence scoring system (0–100%)
* 🧾 Evidence + reasoning output
* 💾 Persistent memory using SQLite
* 📜 History tracking of past analyses
* 🎨 Interactive Streamlit UI

---

## 🏗️ Project Structure

<pre class="overflow-visible! px-0!" data-start="701" data-end="1276"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>fake-news-detector/</span><br/><span>│</span><br/><span>├── app.py                  # Streamlit frontend</span><br/><span>├── graph.py                # LangGraph workflow</span><br/><span>├── state.py                # State schema</span><br/><span>├── config.py               # Environment config</span><br/><span>├── memory.py               # SQLite memory system</span><br/><span>├── db.sqlite               # Auto-generated database</span><br/><span>├── requirements.txt</span><br/><span>├── .env</span><br/><span>│</span><br/><span>└── src/</span><br/><span>    ├── agents/</span><br/><span>    │   └── agents.py      # Analyzer, Verifier, Judge</span><br/><span>    │</span><br/><span>    ├── tools/</span><br/><span>    │   └── tools.py       # Web search tool</span><br/><span>    │</span><br/><span>    └── pipelines/</span><br/><span>        └── pipeline.py    # LangGraph pipeline</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## ⚙️ Installation

### 1. Clone repo

git clone https://github.com/maria2021831011/fake-news-detector_langgraph.git

cd  fake-news-detector 

### 2. Create virtual environment

<pre class="overflow-visible! px-0!" data-start="1456" data-end="1530"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>conda create </span><span class="ͼ12">-n</span><span> fake-news </span><span class="ͼ11">python</span><span class="ͼv">=</span><span class="ͼy">3</span><span>.10</span><br/><span>conda activate fake-news</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### 3. Install dependencies

<pre class="overflow-visible! px-0!" data-start="1560" data-end="1603"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>pip install </span><span class="ͼ12">-r</span><span> requirements.txt</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🔑 Environment Setup

Create a `.env` file:

<pre class="overflow-visible! px-0!" data-start="1658" data-end="1760"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>MODEL_NAME=llama3.1</span><br/><span>OLLAMA_BASE_URL=http://localhost:11434</span><br/><span>TAVILY_API_KEY=your_api_key_here</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## Run Ollama Model

Make sure Ollama is installed and model is pulled:

<pre class="overflow-visible! px-0!" data-start="1843" data-end="1875"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>ollama pull llama3.1</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Run server:

<pre class="overflow-visible! px-0!" data-start="1889" data-end="1913"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>ollama serve</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## ▶️ Run Application

<pre class="overflow-visible! px-0!" data-start="1943" data-end="1975"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>streamlit run app.py</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## Example Inputs

Try these claims:

* 5G causes coronavirus
* Drinking bleach cures diseases
* NASA found alien life on Earth
* Vaccines contain microchips
* Coffee improves focus

---

## 📊 Output Format

* Verdict: TRUE / FALSE / UNCERTAIN
* Confidence Score: 0–100%
* Evidence Summary
* Reasoning Explanation

---

## 🧠 How It Works

1. User enters a news claim
2. LLM analyzes the statement
3. Web search fetches supporting evidence
4. Judge agent evaluates truthfulness
5. Final verdict + confidence generated

---

## ⚠️ Known Issues

* Requires sufficient RAM for large LLM models
* Ollama model must be correctly installed
* API key required for web search tool

---

## 🔮 Future Improvements

* Multi-model voting system
* RAG-based fact database
* Browser extension version
* API backend (FastAPI)
* Multilingual support

---

## Author

Built with ❤️ using AI tools and LangGraph workflow system.

---

## 📌 License

MIT License
