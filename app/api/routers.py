# app/api/routers.py

from fastapi import APIRouter

from app.api.endpoints import (
    donation_router, google_router, project_router, user_router)


main_router = APIRouter()
main_router.include_router(
    project_router, prefix='/charity_project', tags=['Charity projects']
)
main_router.include_router(
    donation_router, prefix='/donation', tags=['Donations']
)
main_router.include_router(
    google_router, prefix='/google', tags=['Google']
)
main_router.include_router(user_router)
