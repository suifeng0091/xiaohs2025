from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from xhs_scraper import search_xiaohongshu

app = FastAPI()

# 允许跨域（用于 Coze 或飞书等前端请求）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/xhs/search")
def xhs_search(q: str = Query(..., description="搜索关键词")):
    try:
        results = search_xiaohongshu(q)
        return {"results": results}
    except Exception as e:
        return {"error": str(e)}
