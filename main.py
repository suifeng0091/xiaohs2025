# main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from xhs_search import search_xiaohongshu

app = FastAPI(title="小红书搜索API")

# 允许跨域访问（Coze 可用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/xhs/search")
def search_xhs(q: str = Query(..., description="搜索关键词")):
    results = search_xiaohongshu(q)
    return {"results": results}
