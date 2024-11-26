"""Routes for User listing and control."""

from fastapi import APIRouter, Depends, Request, status

from app.managers.auth import can_edit_user, is_admin, oauth2_schema

router = APIRouter(tags=["VideoGenerate"], prefix="/generate")


@router.get(
    "/video",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(oauth2_schema), Depends(is_admin)],
)
async def say_hello():
    """Return a greeting message."""

    return {"message": "Hello generate video"}
