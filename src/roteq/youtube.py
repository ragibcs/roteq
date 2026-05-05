import re

from IPython.display import HTML, display

from roteq.custom_exception import InvalidURLException
from roteq.logger import logger


def render_youtube_video(url: str, width: int = 560, height: int = 315):
    try:
        regex = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
        match = re.search(regex, url)

        if not match:
            raise InvalidURLException(f"Invalid YouTube URL :{url}")

        video_id = match.group(1)
        embed_url = f"https://www.youtube-nocookie.com/embed/{video_id}"

        iframe = f"""
        <iframe width="{width}" height="{height}"
        src="{embed_url}"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
        </iframe>
        """

        display(HTML(iframe))
        logger.info(f"Successfully render Youtube video for url : {url}")
        return "success"

    except Exception as e:
        return e
