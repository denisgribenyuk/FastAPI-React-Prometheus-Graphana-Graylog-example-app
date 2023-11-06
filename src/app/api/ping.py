from fastapi import APIRouter

router = APIRouter()


@router.get("/ding")
async def ding():
    return {"ding": "dong!"}
