from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assignment_notification import AssignmentNotification
from ...models.assignments_latest_list_validation_error import AssignmentsLatestListValidationError
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    exercise_parent_module_parent_subject_id: Union[Unset, int] = UNSET,
    user_classes_id: Union[Unset, int] = UNSET,
    user_id_in: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["exercise__parent_module__parent_subject__id"] = exercise_parent_module_parent_subject_id

    params["user__classes__id"] = user_classes_id

    json_user_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(user_id_in, Unset):
        json_user_id_in = user_id_in

    params["user__id__in"] = json_user_id_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/assignments/latest/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestListValidationError", "ParseErrorResponse"],
        list["AssignmentNotification"],
    ]
]:
    if response.status_code == 400:

        def _parse_response_400(data: object) -> Union["AssignmentsLatestListValidationError", "ParseErrorResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_latest_list_error_response_400_type_0 = (
                    AssignmentsLatestListValidationError.from_dict(data)
                )

                return componentsschemas_assignments_latest_list_error_response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_assignments_latest_list_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_assignments_latest_list_error_response_400_type_1

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
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AssignmentNotification.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestListValidationError", "ParseErrorResponse"],
        list["AssignmentNotification"],
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
    exercise_parent_module_parent_subject_id: Union[Unset, int] = UNSET,
    user_classes_id: Union[Unset, int] = UNSET,
    user_id_in: Union[Unset, list[int]] = UNSET,
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestListValidationError", "ParseErrorResponse"],
        list["AssignmentNotification"],
    ]
]:
    """Assignment Notifications

    Args:
        exercise_parent_module_parent_subject_id (Union[Unset, int]):
        user_classes_id (Union[Unset, int]):
        user_id_in (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsLatestListValidationError', 'ParseErrorResponse'], list['AssignmentNotification']]]
    """

    kwargs = _get_kwargs(
        exercise_parent_module_parent_subject_id=exercise_parent_module_parent_subject_id,
        user_classes_id=user_classes_id,
        user_id_in=user_id_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    exercise_parent_module_parent_subject_id: Union[Unset, int] = UNSET,
    user_classes_id: Union[Unset, int] = UNSET,
    user_id_in: Union[Unset, list[int]] = UNSET,
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestListValidationError", "ParseErrorResponse"],
        list["AssignmentNotification"],
    ]
]:
    """Assignment Notifications

    Args:
        exercise_parent_module_parent_subject_id (Union[Unset, int]):
        user_classes_id (Union[Unset, int]):
        user_id_in (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsLatestListValidationError', 'ParseErrorResponse'], list['AssignmentNotification']]
    """

    return sync_detailed(
        client=client,
        exercise_parent_module_parent_subject_id=exercise_parent_module_parent_subject_id,
        user_classes_id=user_classes_id,
        user_id_in=user_id_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    exercise_parent_module_parent_subject_id: Union[Unset, int] = UNSET,
    user_classes_id: Union[Unset, int] = UNSET,
    user_id_in: Union[Unset, list[int]] = UNSET,
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestListValidationError", "ParseErrorResponse"],
        list["AssignmentNotification"],
    ]
]:
    """Assignment Notifications

    Args:
        exercise_parent_module_parent_subject_id (Union[Unset, int]):
        user_classes_id (Union[Unset, int]):
        user_id_in (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsLatestListValidationError', 'ParseErrorResponse'], list['AssignmentNotification']]]
    """

    kwargs = _get_kwargs(
        exercise_parent_module_parent_subject_id=exercise_parent_module_parent_subject_id,
        user_classes_id=user_classes_id,
        user_id_in=user_id_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    exercise_parent_module_parent_subject_id: Union[Unset, int] = UNSET,
    user_classes_id: Union[Unset, int] = UNSET,
    user_id_in: Union[Unset, list[int]] = UNSET,
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["AssignmentsLatestListValidationError", "ParseErrorResponse"],
        list["AssignmentNotification"],
    ]
]:
    """Assignment Notifications

    Args:
        exercise_parent_module_parent_subject_id (Union[Unset, int]):
        user_classes_id (Union[Unset, int]):
        user_id_in (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['AssignmentsLatestListValidationError', 'ParseErrorResponse'], list['AssignmentNotification']]
    """

    return (
        await asyncio_detailed(
            client=client,
            exercise_parent_module_parent_subject_id=exercise_parent_module_parent_subject_id,
            user_classes_id=user_classes_id,
            user_id_in=user_id_in,
        )
    ).parsed
