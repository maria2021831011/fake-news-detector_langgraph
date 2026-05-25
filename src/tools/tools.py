from config import TAVILY_API_KEY

_client = None


def _get_client():
    global _client

    if _client is None:

        if not TAVILY_API_KEY:
            raise RuntimeError("TAVILY_API_KEY is required.")

        try:
            from tavily import TavilyClient
        except ImportError as exc:
            raise RuntimeError("pip install tavily-python") from exc

        _client = TavilyClient(api_key=TAVILY_API_KEY)

    return _client


def web_search(query: str):
    client = _get_client()

    results = client.search(query=query, max_results=3)

    if not results.get("results"):
        return "No relevant web results found."

    context = ""

    for r in results.get("results", []):
        title = r.get("title", "")
        content = r.get("content", "")[:200]
        url = r.get("url", "")

        context += f"{title} - {content} - {url}\n"

    return context.strip()