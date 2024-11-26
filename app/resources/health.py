"""Routes for User listing and control."""

from fastapi import APIRouter, Depends, Request, status

from app.managers.auth import can_edit_user, is_admin, oauth2_schema

router = APIRouter(tags=["health"])


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
)
async def health():
    """Return a health status  message."""

    return {"message": "server is healthy"}
