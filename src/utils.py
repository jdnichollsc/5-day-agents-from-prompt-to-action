"""
Helper functions for the AI Agent project
"""

from IPython.core.display import display, HTML
from jupyter_server.serverapp import list_running_servers


def get_adk_proxy_url():
    """
    Gets the proxied URL in the Kaggle Notebooks environment.
    If you are running this outside the Kaggle environment, you don't need to use this function.
    
    Returns:
        str: The URL prefix for the ADK proxy
    """
    PROXY_HOST = "https://kkb-production.jupyter-proxy.kaggle.net"
    ADK_PORT = "8000"

    servers = list(list_running_servers())
    if not servers:
        raise Exception("No running Jupyter servers found.")

    baseURL = servers[0]["base_url"]

    try:
        path_parts = baseURL.split("/")
        kernel = path_parts[2]
        token = path_parts[3]
    except IndexError:
        raise Exception(f"Could not parse kernel/token from base URL: {baseURL}")

    url_prefix = f"/k/{kernel}/{token}/proxy/proxy/{ADK_PORT}"
    url = f"{PROXY_HOST}{url_prefix}"

    styled_html = f"""
    <div style="background-color: #e8f4f8; padding: 15px; border-radius: 5px; border-left: 5px solid #2196F3;">
        <h3 style="margin-top: 0; color: #1976D2;">ADK Proxy URL</h3>
        <p><strong>URL:</strong> <a href="{url}" target="_blank">{url}</a></p>
    </div>
    """

    display(HTML(styled_html))

    return url_prefix


print("✅ Helper functions defined.")
