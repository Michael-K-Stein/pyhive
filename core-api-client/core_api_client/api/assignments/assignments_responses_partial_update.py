from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assignment_response import AssignmentResponse
from ...models.assignments_responses_partial_update_validation_error import (
    AssignmentsResponsesPartialUpdateValidationError,
)
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_404 import ErrorResponse404
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.parse_error_response import ParseErrorResponse
from ...models.patched_assignment_response_request import PatchedAssignmentResponseRequest
from ...types import Response


def _get_kwargs(
    parent_id: int,
    id: int,
    *,
    body: Union[
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/core/assignments/{parent_id}/responses/{id}/",
    }

    if isinstance(body, PatchedAssignmentResponseRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedAssignmentResponseRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedAssignmentResponseRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        AssignmentResponse,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsResponsesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    if response.status_code == 400:

        def _parse_response_400(
            data: object,
        ) -> Union["AssignmentsResponsesPartialUpdateValidationError", "ParseErrorResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_responses_partial_update_error_response_400_type_0 = (
                    AssignmentsResponsesPartialUpdateValidationError.from_dict(data)
                )

                return componentsschemas_assignments_responses_partial_update_error_response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_assignments_responses_partial_update_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_assignments_responses_partial_update_error_response_400_type_1

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
        response_200 = AssignmentResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        AssignmentResponse,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsResponsesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    parent_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
    ],
) -> Response[
    Union[
        AssignmentResponse,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsResponsesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Assignment Response

    Args:
        parent_id (int):
        id (int):
        body (PatchedAssignmentResponseRequest):
        body (PatchedAssignmentResponseRequest):
        body (PatchedAssignmentResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignmentResponse, ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsResponsesPartialUpdateValidationError', 'ParseErrorResponse']]]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    parent_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
    ],
) -> Optional[
    Union[
        AssignmentResponse,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsResponsesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Assignment Response

    Args:
        parent_id (int):
        id (int):
        body (PatchedAssignmentResponseRequest):
        body (PatchedAssignmentResponseRequest):
        body (PatchedAssignmentResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignmentResponse, ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsResponsesPartialUpdateValidationError', 'ParseErrorResponse']]
    """

    return sync_detailed(
        parent_id=parent_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    parent_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
    ],
) -> Response[
    Union[
        AssignmentResponse,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsResponsesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Assignment Response

    Args:
        parent_id (int):
        id (int):
        body (PatchedAssignmentResponseRequest):
        body (PatchedAssignmentResponseRequest):
        body (PatchedAssignmentResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignmentResponse, ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsResponsesPartialUpdateValidationError', 'ParseErrorResponse']]]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    parent_id: int,
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
        PatchedAssignmentResponseRequest,
    ],
) -> Optional[
    Union[
        AssignmentResponse,
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse404,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsResponsesPartialUpdateValidationError", "ParseErrorResponse"],
    ]
]:
    """Assignment Response

    Args:
        parent_id (int):
        id (int):
        body (PatchedAssignmentResponseRequest):
        body (PatchedAssignmentResponseRequest):
        body (PatchedAssignmentResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignmentResponse, ErrorResponse401, ErrorResponse403, ErrorResponse404, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsResponsesPartialUpdateValidationError', 'ParseErrorResponse']]
    """

    return (
        await asyncio_detailed(
            parent_id=parent_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
