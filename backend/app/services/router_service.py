import logging
import httpx
from typing import List, Dict, Any, AsyncGenerator, Optional
from ..config import settings

logger = logging.getLogger(__name__)

class RouterService:
    """Service untuk berkomunikasi dengan 9Router AI Gateway (OpenAI-compatible).
    9Router menangani failover otomatis, load balancing provider, dan token compression.
    """

    def __init__(self):
        self.base_url = settings.NINE_ROUTER_BASE_URL.rstrip("/")
        self.api_key = settings.NINE_ROUTER_API_KEY
        self.default_model = settings.NINE_ROUTER_DEFAULT_MODEL
        self.fallback_model = settings.NINE_ROUTER_FALLBACK_MODEL

    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 2000
    ) -> Dict[str, Any]:
        """Mengirim request chat completion non-streaming ke 9Router"""
        target_model = model or self.default_model
        payload = {
            "model": target_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    json=payload,
                    headers=headers
                )
                response.raise_for_status()
                data = response.json()
                return {
                    "content": data["choices"][0]["message"]["content"],
                    "model_used": data.get("model", target_model)
                }
            except Exception as e:
                logger.error("Gagal memanggil 9Router (%s): %s", self.base_url, e)
                # Fallback jika model utama gagal
                if target_model != self.fallback_model and self.fallback_model:
                    logger.info("Mencoba fallback model ke: %s", self.fallback_model)
                    payload["model"] = self.fallback_model
                    try:
                        fallback_resp = await client.post(
                            f"{self.base_url}/chat/completions",
                            json=payload,
                            headers=headers
                        )
                        fallback_resp.raise_for_status()
                        fb_data = fallback_resp.json()
                        return {
                            "content": fb_data["choices"][0]["message"]["content"],
                            "model_used": fb_data.get("model", self.fallback_model)
                        }
                    except Exception as fb_err:
                        logger.error("Fallback 9Router juga gagal: %s", fb_err)
                raise e

    async def chat_completion_stream(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.2
    ) -> AsyncGenerator[str, None]:
        """Streaming response token demi token melalui Server-Sent Events dari 9Router"""
        target_model = model or self.default_model
        payload = {
            "model": target_model,
            "messages": messages,
            "temperature": temperature,
            "stream": True
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream(
                "POST",
                f"{self.base_url}/chat/completions",
                json=payload,
                headers=headers
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if not line:
                        continue
                    if line.startswith("data: "):
                        data_str = line[6:]
                        if data_str == "[DONE]":
                            break
                        yield data_str

router_service = RouterService()
