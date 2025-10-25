from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assignment_notification import AssignmentNotification
from ...models.assignments_latest_create_validation_error import AssignmentsLatestCreateValidationError
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.parse_error_response import ParseErrorResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/assignments/latest/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        AssignmentNotification,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestCreateValidationError", "ParseErrorResponse"],
    ]
]:
    if response.status_code == 400:

        def _parse_response_400(data: object) -> Union["AssignmentsLatestCreateValidationError", "ParseErrorResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_latest_create_error_response_400_type_0 = (
                    AssignmentsLatestCreateValidationError.from_dict(data)
                )

                return componentsschemas_assignments_latest_create_error_response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_assignments_latest_create_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_assignments_latest_create_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse403.from_dict(response.json())

        return response_403
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
    if response.status_code == 201:
        response_201 = AssignmentNotification.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        AssignmentNotification,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestCreateValidationError", "ParseErrorResponse"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        AssignmentNotification,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestCreateValidationError", "ParseErrorResponse"],
    ]
]:
    """Assignment Notifications

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignmentNotification, ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsLatestCreateValidationError', 'ParseErrorResponse']]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        AssignmentNotification,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestCreateValidationError", "ParseErrorResponse"],
    ]
]:
    """Assignment Notifications

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignmentNotification, ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsLatestCreateValidationError', 'ParseErrorResponse']]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        AssignmentNotification,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestCreateValidationError", "ParseErrorResponse"],
    ]
]:
    """Assignment Notifications

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignmentNotification, ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsLatestCreateValidationError', 'ParseErrorResponse']]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        AssignmentNotification,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestCreateValidationError", "ParseErrorResponse"],
    ]
]:
    """Assignment Notifications

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignmentNotification, ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsLatestCreateValidationError', 'ParseErrorResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
