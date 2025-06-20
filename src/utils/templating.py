from typing import Any, Mapping

from fastapi import Request
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

import constants as main_constants


templates = Jinja2Templates(directory=main_constants.TEMPLATES_DIRECTORY)


def get_template(
        request: Request,
        name: str,
        context: dict[str, Any] | None = None,
        status_code: int = 200,
        headers: Mapping[str, str] | None = None,
        media_type: str | None = None,
        ) -> _TemplateResponse:
    if context is None:
        context = dict()
    return templates.TemplateResponse(
        request=request,
        name=name,
        context=context,
        status_code=status_code,
        headers=headers,
        media_type=media_type)
