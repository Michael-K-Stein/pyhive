from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.notification import Notification
from ...models.notification_list_validation_error import NotificationListValidationError
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assignment: Union[Unset, int] = UNSET,
    assignment_exercise: Union[Unset, int] = UNSET,
    assignment_exercise_in: Union[Unset, list[int]] = UNSET,
    from_user_isnull: Union[Unset, bool] = UNSET,
    help_: Union[Unset, int] = UNSET,
    help_in: Union[Unset, list[int]] = UNSET,
    was_read: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["assignment"] = assignment

    params["assignment__exercise"] = assignment_exercise

    json_assignment_exercise_in: Union[Unset, list[int]] = UNSET
    if not isinstance(assignment_exercise_in, Unset):
        json_assignment_exercise_in = assignment_exercise_in

    params["assignment__exercise__in"] = json_assignment_exercise_in

    params["from_user__isnull"] = from_user_isnull

    params["help"] = help_

    json_help_in: Union[Unset, list[int]] = UNSET
    if not isinstance(help_in, Unset):
        json_help_in = help_in

    params["help__in"] = json_help_in

    params["was_read"] = was_read

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/notification/",
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
        Union["NotificationListValidationError", "ParseErrorResponse"],
        list["Notification"],
    ]
]:
    if response.status_code == 400:

        def _parse_response_400(data: object) -> Union["NotificationListValidationError", "ParseErrorResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_notification_list_error_response_400_type_0 = (
                    NotificationListValidationError.from_dict(data)
                )

                return componentsschemas_notification_list_error_response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_notification_list_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_notification_list_error_response_400_type_1

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
            response_200_item = Notification.from_dict(response_200_item_data)

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
        Union["NotificationListValidationError", "ParseErrorResponse"],
        list["Notification"],
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
    assignment: Union[Unset, int] = UNSET,
    assignment_exercise: Union[Unset, int] = UNSET,
    assignment_exercise_in: Union[Unset, list[int]] = UNSET,
    from_user_isnull: Union[Unset, bool] = UNSET,
    help_: Union[Unset, int] = UNSET,
    help_in: Union[Unset, list[int]] = UNSET,
    was_read: Union[Unset, bool] = UNSET,
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["NotificationListValidationError", "ParseErrorResponse"],
        list["Notification"],
    ]
]:
    """Notifications

    Args:
        assignment (Union[Unset, int]):
        assignment_exercise (Union[Unset, int]):
        assignment_exercise_in (Union[Unset, list[int]]):
        from_user_isnull (Union[Unset, bool]):
        help_ (Union[Unset, int]):
        help_in (Union[Unset, list[int]]):
        was_read (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['NotificationListValidationError', 'ParseErrorResponse'], list['Notification']]]
    """

    kwargs = _get_kwargs(
        assignment=assignment,
        assignment_exercise=assignment_exercise,
        assignment_exercise_in=assignment_exercise_in,
        from_user_isnull=from_user_isnull,
        help_=help_,
        help_in=help_in,
        was_read=was_read,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    assignment: Union[Unset, int] = UNSET,
    assignment_exercise: Union[Unset, int] = UNSET,
    assignment_exercise_in: Union[Unset, list[int]] = UNSET,
    from_user_isnull: Union[Unset, bool] = UNSET,
    help_: Union[Unset, int] = UNSET,
    help_in: Union[Unset, list[int]] = UNSET,
    was_read: Union[Unset, bool] = UNSET,
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["NotificationListValidationError", "ParseErrorResponse"],
        list["Notification"],
    ]
]:
    """Notifications

    Args:
        assignment (Union[Unset, int]):
        assignment_exercise (Union[Unset, int]):
        assignment_exercise_in (Union[Unset, list[int]]):
        from_user_isnull (Union[Unset, bool]):
        help_ (Union[Unset, int]):
        help_in (Union[Unset, list[int]]):
        was_read (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['NotificationListValidationError', 'ParseErrorResponse'], list['Notification']]
    """

    return sync_detailed(
        client=client,
        assignment=assignment,
        assignment_exercise=assignment_exercise,
        assignment_exercise_in=assignment_exercise_in,
        from_user_isnull=from_user_isnull,
        help_=help_,
        help_in=help_in,
        was_read=was_read,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    assignment: Union[Unset, int] = UNSET,
    assignment_exercise: Union[Unset, int] = UNSET,
    assignment_exercise_in: Union[Unset, list[int]] = UNSET,
    from_user_isnull: Union[Unset, bool] = UNSET,
    help_: Union[Unset, int] = UNSET,
    help_in: Union[Unset, list[int]] = UNSET,
    was_read: Union[Unset, bool] = UNSET,
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["NotificationListValidationError", "ParseErrorResponse"],
        list["Notification"],
    ]
]:
    """Notifications

    Args:
        assignment (Union[Unset, int]):
        assignment_exercise (Union[Unset, int]):
        assignment_exercise_in (Union[Unset, list[int]]):
        from_user_isnull (Union[Unset, bool]):
        help_ (Union[Unset, int]):
        help_in (Union[Unset, list[int]]):
        was_read (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['NotificationListValidationError', 'ParseErrorResponse'], list['Notification']]]
    """

    kwargs = _get_kwargs(
        assignment=assignment,
        assignment_exercise=assignment_exercise,
        assignment_exercise_in=assignment_exercise_in,
        from_user_isnull=from_user_isnull,
        help_=help_,
        help_in=help_in,
        was_read=was_read,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    assignment: Union[Unset, int] = UNSET,
    assignment_exercise: Union[Unset, int] = UNSET,
    assignment_exercise_in: Union[Unset, list[int]] = UNSET,
    from_user_isnull: Union[Unset, bool] = UNSET,
    help_: Union[Unset, int] = UNSET,
    help_in: Union[Unset, list[int]] = UNSET,
    was_read: Union[Unset, bool] = UNSET,
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["NotificationListValidationError", "ParseErrorResponse"],
        list["Notification"],
    ]
]:
    """Notifications

    Args:
        assignment (Union[Unset, int]):
        assignment_exercise (Union[Unset, int]):
        assignment_exercise_in (Union[Unset, list[int]]):
        from_user_isnull (Union[Unset, bool]):
        help_ (Union[Unset, int]):
        help_in (Union[Unset, list[int]]):
        was_read (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['NotificationListValidationError', 'ParseErrorResponse'], list['Notification']]
    """

    return (
        await asyncio_detailed(
            client=client,
            assignment=assignment,
            assignment_exercise=assignment_exercise,
            assignment_exercise_in=assignment_exercise_in,
            from_user_isnull=from_user_isnull,
            help_=help_,
            help_in=help_in,
            was_read=was_read,
        )
    ).parsed
