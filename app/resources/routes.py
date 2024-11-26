"""Include all the other routes into one router."""

from fastapi import APIRouter

from app.resources import auth, health, home, img2vid, user

api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(auth.router)
api_router.include_router(home.router)
api_router.include_router(img2vid.router)
api_router.include_router(health.router)
