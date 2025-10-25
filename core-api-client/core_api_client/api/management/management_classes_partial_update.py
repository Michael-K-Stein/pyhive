from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.class_ import Class
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_404 import ErrorResponse404
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.management_classes_partial_update_validation_error import ManagementClassesPartialUpdateValidationError
from ...models.parse_error_response import ParseErrorResponse
from ...models.patched_class_request import PatchedClassRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedClassRequest,
        PatchedClassRequest,
        PatchedClassRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/core/management/classes/{id}/",
    }

    if isinstance(body, PatchedClassRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedClassRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedClassRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Class,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ManagementClassesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    if response.status_code == 400:

        def _parse_response_400(
            data: object,
        ) -> Union["ManagementClassesPartialUpdateValidationError", "ParseErrorResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_classes_partial_update_error_response_400_type_0 = (
                    ManagementClassesPartialUpdateValidationError.from_dict(data)
                )

                return componentsschemas_management_classes_partial_update_error_response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_management_classes_partial_update_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_management_classes_partial_update_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = ErrorResponse405.from_dict(response.json())

        return response_405
    if response.status_code == 406:
        response_406 = ErrorResponse406.from_dict(response.json())

        return response_406
    if response.status_code == 415:
        response_415 = ErrorResponse415.from_dict(response.json())

        return response_415
    if response.status_code == 500:
        response_500 = ErrorResponse500.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = Class.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Class,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ManagementClassesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedClassRequest,
        PatchedClassRequest,
        PatchedClassRequest,
    ],
) -> Response[
    Union[
        Class,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ManagementClassesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Classes

    Args:
        id (int):
        body (PatchedClassRequest):
        body (PatchedClassRequest):
        body (PatchedClassRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Class, ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ManagementClassesPartialUpdateValidationError', 'ParseErrorResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedClassRequest,
        PatchedClassRequest,
        PatchedClassRequest,
    ],
) -> Optional[
    Union[
        Class,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ManagementClassesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Classes

    Args:
        id (int):
        body (PatchedClassRequest):
        body (PatchedClassRequest):
        body (PatchedClassRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Class, ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ManagementClassesPartialUpdateValidationError', 'ParseErrorResponse']]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedClassRequest,
        PatchedClassRequest,
        PatchedClassRequest,
    ],
) -> Response[
    Union[
        Class,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ManagementClassesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Classes

    Args:
        id (int):
        body (PatchedClassRequest):
        body (PatchedClassRequest):
        body (PatchedClassRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Class, ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ManagementClassesPartialUpdateValidationError', 'ParseErrorResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedClassRequest,
        PatchedClassRequest,
        PatchedClassRequest,
    ],
) -> Optional[
    Union[
        Class,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ManagementClassesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Classes

    Args:
        id (int):
        body (PatchedClassRequest):
        body (PatchedClassRequest):
        body (PatchedClassRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Class, ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ManagementClassesPartialUpdateValidationError', 'ParseErrorResponse']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
