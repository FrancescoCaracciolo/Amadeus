from .extensions import NewelleExtension
from gi.repository import Gtk, WebKit
from .handlers import PromptDescription

DIVERGENCE_PROMPT = """
- You can get the current worldline divergence number using 

```divergence 
current 
```

"""

class DivergenceExtension(NewelleExtension):
    name = "Divergence Meter"
    id="divergence"

    def get_additional_prompts(self) -> list:
        return [
            PromptDescription("divergence", "Divergence", "Get current worldline divergence number", DIVERGENCE_PROMPT)
        ]

    def get_replace_codeblocks_langs(self) -> list:
        return ["divergence"]

    def provides_both_widget_and_answer(self, codeblock: str, lang: str) -> bool:
        return True 

    def get_gtk_widget(self, codeblock: str, lang: str, msg_uuid=None) -> Gtk.Widget | None:
        webview = WebKit.WebView()
        webview.set_size_request(400, 150)
        webview.load_uri("https://divergence.nyarchlinux.moe/lite.html")
        webview.set_sensitive(False)
        return webview

    def get_answer(self, codeblock: str, lang: str) -> str | None:
        import requests
        content = requests.get("https://divergence.nyarchlinux.moe/api/divergence")
        j = content.json()
        result = j["divergence"]
        return result
