# views.py
import time
import requests
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FetchPostsAPIView(APIView):
    """
    Fetch posts from external API with Redis caching.
    """

    CACHE_KEY = "posts_data"
    TTL = 120  # seconds

    def get(self, request):

        start_time = time.time()

        # Try Redis first
        data = cache.get(self.CACHE_KEY)

        if data:
            source = "redis"
        else:
            try:
                response = requests.get(
                    "https://jsonplaceholder.typicode.com/posts",
                    timeout=5
                )
                response.raise_for_status()
                data = response.json()

                # Store in Redis
                cache.set(self.CACHE_KEY, data, timeout=self.TTL)
                source = "external_api"

            except requests.RequestException as e:
                return Response(
                    {"error": "Failed to fetch external API"},
                    status=status.HTTP_502_BAD_GATEWAY
                )

        end_time = time.time()
        time_taken_ms = round((end_time - start_time) * 1000, 2)

        return Response({
            "source": source,
            "count": len(data),
            "time_taken": f"{time_taken_ms} ms",
            "data": data
        })